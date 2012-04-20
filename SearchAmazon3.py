# -*- coding: utf-8 -*-

PLUGIN_NAME = u"Search Amazon for Release"
PLUGIN_AUTHOR = u"Brian Schweitzer"
PLUGIN_DESCRIPTION = "Search Amazon"
PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10","0.11","0.12","0.13","0.14","0.15","0.16"]

from PyQt4 import QtCore
from picard.cluster import Cluster
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_album_action, register_cluster_action, register_add_plugin_submenu

urls = {
    'ca' : {
        'name' : u"Canada",
        'url'  : u"http://www.amazon.ca/s/?url=search-alias%3Dpopular&field-keywords="},
    'cn' : {
        'name' : u"China",
        'url'  : u"http://www.amazon.cn/s/?url=search-alias%3Dpopular&field-keywords="},
    'fr' : {
        'name' : u"France",
        'url'  : u"http://www.amazon.fr/s/?url=search-alias%3Dpopular&field-keywords="},
    'de' : {
        'name' : u"Germany",
        'url'  : u"http://www.amazon.de/s/?url=search-alias%3Dpopular&field-keywords="},
    'it' : {
        'name' : u"Italy",
        'url'  : u"http://www.amazon.it/s/?url=search-alias%3Dpopular&field-keywords="},
    'jp' : {
        'name' : u"Japan",
        'url'  : u"http://www.amazon.co.jp/s/?url=search-alias%3Dpopular&field-keywords="},
    'es' : {
        'name' : u"Spain",
        'url'  : u"http://www.amazon.es/s/?url=search-alias%3Dpopular&field-keywords="},
    'uk' : {
        'name' : u"United Kingdom",
        'url'  : u"http://www.amazon.co.uk/s/?url=search-alias%3Dpopular&field-keywords="},
    'com' : {
        'name' : u"United States",
        'url'  : u"http://www.amazon.com/s/?url=search-alias%3Dpopular&field-keywords="},
}

def amazon_open_page(objs, tld):
    cluster = objs[0]
    url = []
    url.append(cluster.metadata["artist"])
    url.append(" ")
    url.append(cluster.metadata["album"])
    url = urls[tld]['url'] + QtCore.QUrl.toPercentEncoding(''.join(url))
    webbrowser2.open(url)

for tld in ['ca','cn','fr','de','it','jp','es','uk','com']:
    class search_amazon(BaseAction):
        NAME = urls[tld]['name']
        MENU = "Amazon"

        def callback(self, objs, tld=tld):
            amazon_open_page(objs, tld)

    register_cluster_action(search_amazon())
    register_album_action(search_amazon())

class search_all_amazon(BaseAction):
        NAME = "all Amazon sites"
        MENU = "Amazon"

        def callback(self, objs, tld=tld):
            for tld in ['ca','cn','fr','de','it','jp','es','uk','com']:
                amazon_open_page(objs, tld)

register_cluster_action(search_all_amazon())
register_album_action(search_all_amazon())

register_add_plugin_submenu("Search")
register_add_plugin_submenu("Amazon", "Search")