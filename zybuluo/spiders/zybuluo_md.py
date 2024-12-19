import datetime

import scrapy
from bs4 import BeautifulSoup
from dateutil import parser
import markdownify

from zybuluo.items import ZybuluoItem
from zybuluo.utils.test0 import get_file_links


class ZybuluoMdSpider(scrapy.Spider):
    name = "zybuluo_md"
    allowed_domains = ["www.zybuluo.com"]
    # start_urls = ["https://www.zybuluo.com"]
    k = get_file_links()
    start_urls = k

    def parse(self, response):
        article = response.text
        soup = BeautifulSoup(response.text, 'html.parser')

        # 获取指定div的内容
        content_div = soup.find('div', id='editor-reader-full')
        if not content_div:
            raise ValueError("未找到指定的div内容")

        content_div1 = soup.find('div', id='reader-full-topInfo')
        if not content_div1:
            raise ValueError("未找到指定的div内容")

        time_pre = content_div1.find(class_='article-updated-date').string
        # print(time_pre)
        # 解析UTC时间字符串
        utc_time = parser.isoparse(time_pre)

        # 转换为北京时间（UTC+8）
        beijing_time = utc_time + datetime.timedelta(hours=8)

        # 格式化时间为指定格式
        formatted_beijing_time = beijing_time.strftime('%Y-%m-%d %H:%M:%S')

        # 更新时间设置
        content_div1.find(class_='article-updated-date').string = formatted_beijing_time

        content_div2 = soup.find('div', id='wmd-preview')
        if not content_div2:
            raise ValueError("未找到指定的div内容")

        # 转换为markdown格式
        content_div2 = markdownify.markdownify(str(content_div2))
        content_div1 = markdownify.markdownify(str(content_div1))

        content_div1 = content_div1.replace('\n\n', '\n').replace('\r\r', '\r')
        markdown_content = content_div1 + content_div2

        item = ZybuluoItem()
        item['text'] = markdown_content
        yield item
        # pass
