#class student:
#    def __init__(self,name,age):
#        self.__name=name
#        self.__age=age
#    @property
#    def age(self):
#        return self.__age
#    @age.setter
#    def age(self,b):
#        self.__age=b
import cv2
import time
import os
from PIL import Image,ImageFont,ImageDraw
from cv2 import VideoWriter,VideoWriter_fourcc,imread,resize
import re
 
#转换为字符画
class CharFrame:
    ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
 
    # 像素映射到字符
    def pixelToChar(self, luminance):
        return self.ascii_char[int(luminance / 256 * len(self.ascii_char))]
 
    # 将普通帧转为 ASCII 字符帧
    def convert(self, img, limitSize=(),fill=False,wrap=False):
        if limitSize != () and (img.shape[0] > limitSize[1] or img.shape[1] > limitSize[0]):
            #对图像缩放到适合终端的大小
            img = cv2.resize(img, limitSize, interpolation=cv2.INTER_NEAREST)
        ascii_frame = ''
        blank = ''
        if fill:
            blank += ' ' * (limitSize[0] - img.shape[1])
        if wrap:
            blank += '\n'
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                ascii_frame += self.pixelToChar(img[i, j])
            ascii_frame += blank
        return ascii_frame
 
 
class V2Char(CharFrame):
    charVideo = []
 
    def __init__(self, path,size=(120,30)):
        """
        :param path:视频文件路径
        :param size: 所要缩放的大小,(width，height)
        """
        self.path=path
        self.size=size
        self.genCharVideo(path)
 
    def genCharVideo(self, filepath):
        self.charVideo = []
        # 用opencv读取视频，设置相机
        cap = cv2.VideoCapture(filepath)
        #get(5)为视频的帧速率
        self.FPS=cap.get(cv2.CAP_PROP_FPS)#或者用get(5)
        #get(7)为视频的帧数
        nf = int(cap.get(7))
        print('Generate char video, please wait...')
        for i in range(nf):
            # 转换颜色空间，第二个参数是转换类型，cv2.COLOR_BGR2GRAY表示从BGR↔Gray
            #read()读取视频画面，第一个参数表示读取是否成功，第二个即为画面，所以索引用1
            #每read一次读取一个画面
            rawFrame = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
            frame = self.convert(rawFrame,self.size,fill=True)#注意这里的参数输入
            self.charVideo.append(frame)
        #释放相机
        cap.release()
        print('Finished.')
 
 
    #设置最大的单字符长度
    def max_width(self):
        font = ImageFont.truetype(os.path.join("fonts", "arial.ttf"), 18)
        font_size=[]
        for i in self.ascii_char:
            font_size.append(font.getsize(i)[0])
        return max(font_size)
 
 
    #对一行切分为数组的形式，即表示为一个画面
    def str_slice(self,char,row,col):
        slice_char=[]
        for i in range(row):
            slice_char.append(char[i*col:(i+1)*col])
        return slice_char
 
 
    def str2fig(self):
        #很多字符的宽度不一样，需要设置字符最大的宽度
        font = ImageFont.truetype('arial.ttf', 18)
        le_width=self.max_width()
        line_height=font.getsize(self.charVideo[0])[1]
        #上面每3600个字符为一个画面，在列表中为一行,30*120
        col,row=self.size
        #画布参数设置
        img_height=line_height*(row+1)
        img_width=le_width*(col+1)
        #处理过的图片保存位置,以视频的名字命名文件夹
        catalog=self.path.split('.')[0]
        self.mkdir(catalog)
        #绘制图片
        for p_id,char in enumerate(self.charVideo):
            div_char=self.str_slice(char,row,col)
            im = Image.new("RGB", (img_width, img_height), (255, 255, 255))
            dr = ImageDraw.Draw(im)
            for i,str in enumerate(div_char):
                for j in range(len(str)):
                    dr.text((5+j*le_width,5+i*line_height), str[j],
                            font=font, fill="#000000")
            im.save(catalog+r'\pic_{}.jpg'.format(p_id))
 
 
    def mkdir(self,catalog):
        isExists = os.path.exists(catalog)
        if not isExists:
            os.makedirs(catalog)
            return True
        else:
            return False
 
    def jpg2video(self):
        catalog=self.path.split('.')[0]
        #利用os.listdir()读取文件有乱序的问题，需要对其进行排序
        images=os.listdir(catalog)
        images.sort(key=lambda x: int(re.findall(r'\d+', x)[0]))
        im=Image.open(catalog+'\\'+images[0])
        fourcc = VideoWriter_fourcc(*"MJPG")
        vw = VideoWriter('stringvideo' + '.avi', fourcc,self.FPS, im.size)
        for image in images:
            frame=cv2.imread(catalog+'\\'+image)
            vw.write(frame)
        vw.release()
 
    #递归删除目录
    def remove_dir(self,path):
        if os.path.exists(path):
            if os.path.isdir(path):
                dirs = os.listdir(path)
                for d in dirs:
                    if os.path.isdir(path+'/'+d):
                        self.remove_dir(path+'/'+d)
                    elif os.path.isfile(path+'/'+d):
                        os.remove(path+'/'+d)
                os.rmdir(path)
                return
            elif os.path.isfile(path):
                os.remove(path)
            return
 
 
    def gen_video(self):
        self.str2fig()
        print('str2fig Finished')
        print('start generate video.wait...')
        self.jpg2video()
        print('generate video Finished')
        print('start delete catalog.wait...')
        self.remove_dir(self.path.split('.')[0])
        print('delete cache catalog finished')
 
if __name__ == '__main__':
    #修改你索要输入的文件的路径
    v2char = V2Char('1.mp4')
    v2char.gen_video()