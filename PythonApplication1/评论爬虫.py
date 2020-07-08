from re import findall,compile
from bs4 import BeautifulSoup
import xlwt
from urllib import request,error
import gzip

def visitUrl(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
             'cookie': '_uuid=AA640CB8-7C2E-BC16-A246-8117C55FB28400863infoc; buvid3=CE09E52F-62FF-41EC-AAE1-5B826F0A6FA6155813infoc; sid=9crz219m; CURRENT_FNVAL=16; rpdid=|(u~u|YYRJlm0J\'ul)kJRY)u|; LIVE_BUVID=AUTO6215823470107838; im_notify_type_363729307=1; LNG=zh-CN; DedeUserID=363729307; DedeUserID__ckMd5=148af2f754052f7c; SESSDATA=10b754a4%2C1600435541%2C474cd*31; bili_jct=a069f160c6f9361a4e0bc08b246a9984; CURRENT_QUALITY=80; bp_t_offset_363729307=408936321730321708; bp_video_offset_363729307=409317216602812283; PVID=2'}
    req=request.Request(url,headers=headers)
    try:
        response=request.urlopen(req)
        html=response.read()
        html=gzip.decompress(html).decode()
        print(html)
    except error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
            return 0
        if hasattr(e,'reason'):
            print(e.reason)
            return 0
    return html


def getData(url):
    datalist=[]
    html=visitUrl(url)
    if html==0:
        print("错误")
        return
    print(html)
    bs=BeautifulSoup(html,'html.parser')
    for item in bs.find_all('div',class_='list-item reply-wrap '):
        data=[]
        item=str(item)
        print(item)
    return datalist

def main():
    url='https://api.bilibili.com/x/v2/reply?callback=jQuery17209236304697103193_1594170405604&jsonp=jsonp&pn=2&type=1&oid=926339470&sort=2&_=1594170418809'
    datalist=getData(url)


if __name__=="__main__":
    main()