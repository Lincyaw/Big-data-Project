# -*- coding: utf-8 -*-

import os
from utils import news_crawler

if __name__ == '__main__':
    project_path = os.path.dirname(os.path.realpath(__file__))  # 获取项目路径
    news_path = os.path.join(project_path, 'news')  # 新闻数据存放目录路径
    if not os.path.exists(news_path):  # 创建news文件夹
        os.mkdir(news_path)
    xinhuanet_news_df = news_crawler.get_latest_news('xinhuanet', top=100, show_content=True)
    news_crawler.save_news(xinhuanet_news_df, os.path.join(news_path, 'xinhuanet_latest_news.txt'))
