#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/19 上午10:18
# @Author  : 苏玉恒
# @File    : test0.py
# @Software: PyCharm


import requests
from bs4 import BeautifulSoup


def get_file_links():
    # 设置目标URL
    url = 'https://www.zybuluo.com/bintou/note/1697174'

    # 发送GET请求获取页面内容
    response = requests.get(url)

    # 确保请求成功
    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
        return []

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到指定的预览按钮容器
    preview_container = soup.find('li', {
        'class': 'preview-button-full-reader dropdown',
        'id': 'preview-list-button'
    })

    if not preview_container:
        print("未找到指定的预览按钮容器")
        return []

    # 查找所有包含'file-item'类的li元素
    file_items = preview_container.find_all('li', class_='file-item')

    # 提取所有a标签的href属性
    href_list = [item.find('a')['href'] for item in file_items if item.find('a')]
    seen = set()
    href_list = [x for x in href_list if not (x in seen or seen.add(x))]

    return href_list


# 运行并打印结果
if __name__ == "__main__":
    result = get_file_links()
    print("找到的链接列表：")
    for link in result:
        print(link)
    print(len(result))