# 使用Scrapy爬取斌头博客文章

## 项目概述

在探索网络的过程中，发现了某大学老师（网名：斌头）写在其个人博客“作业部落”上的多篇文章，阅读后深感启发。为了进一步学习和练习Scrapy框架的使用，决定以斌头的博客作为案例进行实践。

用Scrapy采集这个毫无反爬措施的网站，实在是小题大做，单纯只为练习框架，就为了盘醋包的这顿饺子。

## 爬虫目标

- **来源网站**: [斌头的博客](https://www.zybuluo.com/bintou/note/1697174)
- **目标内容**: 提取右侧的文章列表中所有文章链接，并抓取每篇文章的内容。
- **最终输出**: 将HTML格式的文章转换为Markdown格式，并保存至`bintou.md`文件中。

## 技术栈

- **Scrapy**: 用于构建爬虫逻辑，发起请求并解析响应。
- **BeautifulSoup4 (bs4)**: 从HTML或XML文件中提取数据。
- **markdownify**: 将HTML内容转换为Markdown格式，确保文章格式的一致性和可读性。

## 实现步骤

1. **初始化Scrapy项目**
   - 创建一个新的Scrapy项目，配置项目的设置，如USER_AGENT等。
   
2. **定义Start URLs**
   - 使用BeautifulSoup4访问斌头博客页面，解析右侧的文章列表，提取所有文章链接，形成`start_urls`列表。

3. **编写Item Pipeline**
   - 定义一个Item Pipeline来处理每个被爬取的文章，包括调用`markdownify`库将HTML内容转换为Markdown格式。

4. **保存结果**
   - 将所有转换后的Markdown格式文章内容汇总，写入到一个名为`bintou.md`的文件中。

5. **运行爬虫**
   - 执行爬虫，开始抓取过程，等待所有任务完成后检查生成的Markdown文件。

   