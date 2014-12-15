# coding: utf-8

import urllib2, urllib, re, sys, os, requests,datetime
from bs4 import BeautifulSoup
from string import Template
from HtmlLink import HtmlLink
from HtmlInput import HtmlInput
reload(sys)
sys.setdefaultencoding('utf-8')

# base_url = 'http://www.crummy.com/software/BeautifulSoup/bs4/doc/'
base_url='http://www.slb.com/'
vr = re.compile('[\w\d_]')  # 变量命名规范：字母数字下划线

def get_cookies():
    url = 'https://github.com/176coding/taobaomm/edit/master/mm.py'
    data = {'login_field': '176coding', 'password': 'jyg765081406',
            'return_to': r'	https://github.com/176coding/taobaomm/edit/master/mm.py'}
    post_url = 'https://github.com/session'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
    }
    s = requests.session()
    r = s.post('https://github.com')
    print r.headers
    print r.text
    pass


def get_bs(url, user_name=None, password=None):
    # 根据url，获取html_doc
    # 过程中可能需要重新登录
    req = requests.get(url,timeout=120)
    html_doc = req.text
    bs = BeautifulSoup(html_doc)
    return bs
    pass

def get_htmlinput_list(bs):
    input_list = bs.find_all('input')
    html_input_list=[]
    for hi in input_list:
        ids=hi.get('id')
        name=hi.get('name')
        show_name=ids if ids else name
        htmlinput=HtmlInput(show_name,ids,name)
        print htmlinput.get_private_property()
        print htmlinput.get_public_property()
        html_input_list.append(htmlinput)
        pass
    return html_input_list
    pass

def get_htmllink_list(bs):
    #获取页面中所有的超链
    link_list = bs.find_all('a')
    # print len(link_list)
    html_link_list = []
    for link in link_list:
        link_text = link.get_text()
        temp_link_text = link_text.strip()
        temp_link_text = re.sub(r'\s', '_', temp_link_text)
        temp_link_text = temp_link_text.lower()
        show_name = ''
        for i in temp_link_text:
            if vr.match(i):
                show_name += i

        if show_name == '':  # 用正则匹配之后没有要显示的名称
            continue
        # 获取需要的属性，然后实例化一个HtmlLink实例，加入到html_link_list中
        ids = link.get('id')
        href = link.get('href')  #此处要去掉url的server部分
        text = link_text
        hl = HtmlLink(show_name, ids, text, href)
        # print hl.get_private_property()
        # print hl.get_public_property()
        html_link_list.append(hl)

    return html_link_list
    pass


def test():
    html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" >Elsie</a>
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
"""

    bs = BeautifulSoup(html_doc)
    link = bs.find('a')
    text = link.get('id')

    print text

    pass


def read_template_file_text():
    #读文件
    with open('obj_template.cs', 'r') as f:
        template_file_text = f.read()
    return template_file_text
    pass
def write_template_file_text(file_name,data):
    with open(file_name+'.cs','w') as f:
        f.write(data)
    pass



def replace_template_file():
    bs = get_bs(base_url)
    html_link_list = get_htmllink_list(bs)
    html_input_list=get_htmlinput_list(bs)
    private_property = ''
    public_property = ''
    for link in html_link_list:
        private_property += link.get_private_property()
        public_property += link.get_public_property()
        pass

    for hi in html_input_list:
        private_property += hi.get_private_property()
        public_property += hi.get_public_property()
        pass


    class_name='Template_'+datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    template_file_text=read_template_file_text()
    replace_dict={'class_name':class_name,'private_property':private_property,'public_property':public_property}
    new_template_file_text =Template(template_file_text).substitute(replace_dict)
    write_template_file_text(class_name, new_template_file_text)
    pass


if __name__ == '__main__':
    # print get_dict('a','link_')

    # get_cookies()
    # test()


    # public_property = """
    # public HtmlAnchor ${show_name}
    # {
    #     get
    #     {
    #         ${return_get}
    #     }
    # }
    # """
    # rep = {'show_name': 'asdf', 'return_get': 'qwre'}
    # temp= Template(public_property)
    # print temp.substitute(rep)
    # get_template_file_text()
    replace_template_file()
    # print datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    pass




