from bs4 import BeautifulSoup
import urllib.request
from urllib import error
##导入需要的模块
novel_url = "http://www.biqukan.com/1_1496/"
base_url = "http://www.biqukan.com"
save_dir = "Novel/"  # 下载小说的存放路径
##定义变量

##新建方法
def save_chapter(txt, path):#定义了一个方法，这个方法需要两个参数txt和path
    try:
        with open(path, "a+") as f:
            f.write(txt.get_text(strip=True))
    except (error.HTTPError, OSError) as reason:
        print(str(reason))
    else:
        print("下载完成：" + path)


# 获得所有章节的url
def get_chapter_url():
    chapter_req = urllib.request.Request(novel_url)  #使用urllib库的request模块的Request方法，传入一个定义好的参数
    '''
    使用urllib库的request模块的Request方法，传入一个定义好的参数
     chapter_req = urllib.request.Request(novel_url)
     chapter_req = urllib.request.Request(http://www.biqukan.com/1_1496/)请求到这个网页
     
    '''
    chapter_resp = urllib.request.urlopen(chapter_req, timeout=20)
    chapter_content = chapter_resp.read()
    chapter_soup = BeautifulSoup(chapter_content, 'html.parser')

    listmain = chapter_soup.find_all(attrs={'class': 'listmain'})
    a_list = []

    for i in listmain:
        if 'a' not in str(i):
            continue
        for d in i.findAll('a'):
            a_list.append(d)

    result_list = a_list[12:]
    return result_list

#下载内容
def get_chapter_content(c):
    chapter_url = base_url + c.attrs.get('href')
    chapter_name = c.string
    chapter_req = urllib.request.Request(chapter_url)
    chapter_resp = urllib.request.urlopen(chapter_req, timeout=20)
    chapter_content = chapter_resp.read()
    chapter_soup = BeautifulSoup(chapter_content, 'html.parser')

    showtxt = chapter_soup.find_all(attrs={'class': 'showtxt'})
    for txt in showtxt:
        save_chapter(txt, save_dir + chapter_name + ".txt")


if __name__ == '__main__':
    novel_list = get_chapter_url()
    ''''''
    for chapter in novel_list:
        get_chapter_content(chapter)