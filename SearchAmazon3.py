# -*- coding: utf-8 -*-

PLUGIN_NAME = u"Search Amazon for Release"
PLUGIN_AUTHOR = u"Brian Schweitzer"
PLUGIN_DESCRIPTION = "Search Amazon"
PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10","0.11","0.12","0.13","0.14","0.15","0.16"]

from PyQt4 import QtCore
from picard.cluster import Cluster
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_album_action
from picard.ui.itemviews import BaseAction, register_cluster_action

class SearchAmazonCA(BaseAction):
    NAME = "Search Amazon.ca"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.amazon.ca/s/?url=search-alias%3Dpopular&field-keywords="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["artist"])
        url += " "
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        webbrowser2.open(url)
register_cluster_action(SearchAmazonCA())
register_album_action(SearchAmazonCA())

class SearchAmazonCOM(BaseAction):
    NAME = "Search Amazon.com"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.amazon.com/s/?url=search-alias%3Dpopular&field-keywords="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["artist"])
        url += " "
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        webbrowser2.open(url)
register_cluster_action(SearchAmazonCOM())
register_album_action(SearchAmazonCOM())

class SearchAmazonDE(BaseAction):
    NAME = "Search Amazon.de"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.amazon.de/s/?url=search-alias%3Dpopular&field-keywords="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["artist"])
        url += " "
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        webbrowser2.open(url)
register_cluster_action(SearchAmazonDE())
register_album_action(SearchAmazonDE())

class SearchAmazonFR(BaseAction):
    NAME = "Search Amazon.fr"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.amazon.fr/s/?url=search-alias%3Dpopular&field-keywords="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["artist"])
        url += " "
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        webbrowser2.open(url)
register_cluster_action(SearchAmazonFR())
register_album_action(SearchAmazonFR())

class SearchAmazonJP(BaseAction):
    NAME = "Search Amazon.jp"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.amazon.jp/s/?url=search-alias%3Dpopular&field-keywords="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["artist"])
        url += " "
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        webbrowser2.open(url)
register_cluster_action(SearchAmazonJP())
register_album_action(SearchAmazonJP())

class SearchAmazonUK(BaseAction):
    NAME = "Search Amazon.co.uk"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.amazon.co.uk/s/?url=search-alias%3Dpopular&field-keywords="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["artist"])
        url += " "
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        webbrowser2.open(url)
register_cluster_action(SearchAmazonUK())
register_album_action(SearchAmazonUK())

