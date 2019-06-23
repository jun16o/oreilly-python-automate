#! python3

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('cover-thumb')
    print('そのクラム名を持つ要素 <{}>を見つけた！'.format(elem.tag_name))
except:
    print('そのクラム名を持つ要素は見つからなかった。')