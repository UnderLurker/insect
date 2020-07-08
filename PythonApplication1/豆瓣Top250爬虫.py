# coding=utf-8

from urllib.request import *
from urllib.error import *
from bs4 import BeautifulSoup
import re
import xlwt



#访问链接
def visitUrl(baseurl):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    req=Request(baseurl,headers=headers)
    try:
        response=urlopen(req)
        html=response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html

#正则表达式
findLink=re.compile(r'<a href="(.*?)"')
findImg=re.compile(r'<img.*src="(.*?)".*>',re.S)
findName=re.compile(r'<span class="title">(.*)</span>')
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findJudge=re.compile(r'<span>(.*?)人评价</span>')
findInq=re.compile(r'<span class="inq">(.*?)</span>')
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)
#爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(10):
        url=baseurl+str(i*25)
        html=visitUrl(url)
        #解析数据
        bs=BeautifulSoup(html,'html.parser')
        for item in bs.find_all('div',class_='item'):
            data=[]#保存所有信息
            item=str(item)
            link=re.findall(findLink,item)[0]
            data.append(link)
            img=re.findall(findImg,item)[0]
            data.append(img)
            name=re.findall(findName,item)
            if len(name)==2:
                data.append(name[0])
                data.append(name[1].replace('/',''))
            else:
                data.append(name[0])
                data.append(' ')
            rating=re.findall(findRating,item)[0]
            data.append(rating)
            judge=re.findall(findJudge,item)[0]
            data.append(judge)
            inq=re.findall(findInq,item)
            if len(inq)==0:
                data.append(' ')
            else:
                data.append(inq[0].replace('。',''))
            bd=re.findall(findBd,item)[0]
            bd=re.sub(r'<br(\s+)?/>(\s+)?',' ',bd)
            data.append(bd.strip())
            datalist.append(data)
    return datalist


#保存数据
def saveData(savePath,datalist):
    workbook=xlwt.Workbook('utf-8',style_compression=0)
    worksheet=workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    col=("影片链接","图片链接","影片中文名","影片英文名","评分","评价数","概识","相关信息")
    for i in range(len(col)):
        worksheet.write(0,i,col[i])
    x,y=0,1
    for i in datalist:
        print('正在写入%d条'%y)
        for j in i:
            worksheet.write(y,x,j)
            x+=1
        y+=1
        x=0
    workbook.save(savePath)

def main():
    baseurl='https://movie.douban.com/top250?start='
    #流程 1、爬取网页
    datalist=getData(baseurl)
     #3、保存数据
    savePath=r'.\豆瓣电影Top250.xls'
    saveData(savePath,datalist)
    print('写入成功')


if __name__=='__main__':
    main()