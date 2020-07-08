from re import *
from bs4 import BeautifulSoup
from urllib.request import *
from urllib.error import *
import xlwt

#得到html
def visitUrl(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
             'cookie': '_uuid=AA640CB8-7C2E-BC16-A246-8117C55FB28400863infoc; buvid3=CE09E52F-62FF-41EC-AAE1-5B826F0A6FA6155813infoc; sid=9crz219m; CURRENT_FNVAL=16; rpdid=|(u~u|YYRJlm0J\'ul)kJRY)u|; LIVE_BUVID=AUTO6215823470107838; im_notify_type_363729307=1; LNG=zh-CN; DedeUserID=363729307; DedeUserID__ckMd5=148af2f754052f7c; SESSDATA=10b754a4%2C1600435541%2C474cd*31; bili_jct=a069f160c6f9361a4e0bc08b246a9984; CURRENT_QUALITY=80; bp_video_offset_363729307=408479955684415224; bp_t_offset_363729307=408936321730321708; PVID=4'}
    req=Request(url,headers=headers)
    try:
        response=urlopen(req)
        html=response.read().decode('utf-8')
    except URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html

findvLink=compile(r'<a href="//(.*?)".*?>')
findiLink=compile(r'<img.*src="//(.*?)"')
findTitle=compile(r'<p class="title" title=".*?">(.*?)</p>')
#获得数据
def getData(url):
    datalist=[]
    html=visitUrl(url)
    bs=BeautifulSoup(html,'html.parser')
    for item in bs.find_all('div',class_='video-card-reco'):
        data=[]
        item=str(item)
        videoLink=findall(findvLink,item)[0]
        data.append(videoLink)
        imgLink=findall(findiLink,item)[0]
        data.append(imgLink)
        title=findall(findTitle,item)[0]
        data.append(title)
        datalist.append(data)
    return datalist

def saveData(savePath,datalist):
    book=xlwt.Workbook('utf-8')
    sheet=book.add_sheet('sheet1')
    col=('视频链接','图片链接','文字')
    for i in range(3):
        sheet.write(0,i,col[i])
    x,y=0,1
    for i in datalist:
        print('正在写入第%d条'%y)
        for j in i:
            sheet.write(y,x,j)
            x+=1
        x=0
        y+=1
    book.save(savePath)

def main():
    url='https://www.bilibili.com'
    #获得html
    #数据分析
    datalist=getData(url)
    #保存数据
    savePath=r'./bilibili.xls'
    saveData(savePath,datalist)

if __name__=='__main__':
    main()
    print("写入成功")