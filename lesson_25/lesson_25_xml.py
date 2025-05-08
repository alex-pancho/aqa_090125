import requests
from lxml.html import fromstring, fragment_fromstring
from lxml import etree
from io import StringIO

broken_html = """<html><head>
<title>test<body><h1>page title</h1>
<a href='mailto:my@mail.com' rel='my@mail.com'>click me</a>
<p class='abc' > some text
<div id="xyz"> text </div>  <p class="">невірний, покоцаний html
""" # невірний покоцаний хтмл



def get_page(url):
    r = requests.get(url)
    return r.content

def get_by_xpath(html_content, x_path):
    tree = fromstring(html_content)
    text = tree.xpath(x_path)
    return text

def get_by_class(html_content, css_class):
    tree = fromstring(html_content)
    text = tree.find_class(css_class)
    return text

def clean_html(broken_html):
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(broken_html), parser)  # перетворюєм в зрозумілу структуру
    result = etree.tostring(tree.getroot(),
                            pretty_print=True,
                            method="html")  # звороне перетворення - обєкт дерева у строку
    print(result.decode("utf-8"))
    with open("index.html", "w", encoding="utf8") as f:
        f.write(str(result, encoding="utf8"))

if __name__ == "__main__":
    url = "https://lxml.de/index.html"
    html_content = get_page(url)
    #print(html_content)

    xpath = '//*[@id="introduction"]/p/text()'
    text_introduction = get_by_xpath(html_content, xpath)
    print(text_introduction)

    css_class = "title"
    text_class = get_by_class(html_content, css_class)
    print(text_class)
    print(text_class[0].attrib, text_class[0].text,  text_class[0].tag)

    clean_html(broken_html)
