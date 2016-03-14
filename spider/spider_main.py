#!/usr/local/bin/python

# coding:utf8
import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()


    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "current %d, url %s" % (count, new_url)
                html_cnt = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parser(new_url, html_cnt)

                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count = count + 1
                if count == 20:
                    break
            except:
                print "craw fail"
        self.outputer.output_html()



if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
