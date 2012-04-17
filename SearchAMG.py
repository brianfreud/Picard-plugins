# -*- coding: utf-8 -*-

PLUGIN_NAME = u"Search AMG"
PLUGIN_AUTHOR = u"Brian Schweitzer"
PLUGIN_DESCRIPTION = "Search AMG"
PLUGIN_VERSION = "0.3"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10","0.11","0.12","0.13","0.14","0.15","0.16"]

from PyQt4 import QtCore, QtGui
from picard.cluster import Cluster
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_cluster_action, register_album_action, register_file_action, BaseTreeView
from picard.metadata import register_track_metadata_processor

class SearchAMGR(BaseAction):
    NAME = "Search AMG for Release"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.allmusic.com/search/album/"
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        webbrowser2.open(url)
register_cluster_action(SearchAMGR())
register_album_action(SearchAMGR())

class SearchAMGA(BaseAction):
    NAME = "Search AMG for Artist"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.allmusic.com/search/artist/"
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["albumartist"])
        webbrowser2.open(url)
register_cluster_action(SearchAMGA())
register_album_action(SearchAMGA())

class SearchAMGTc(BaseAction):
    NAME = "Search AMG (non-classical music) for Track"
    def callback(self, objs):
        file = objs[0]
        url = "http://www.allmusic.com/search/song/"
        url += QtCore.QUrl.toPercentEncoding(file.metadata["title"])
        webbrowser2.open(url)
register_file_action(SearchAMGTc())

class SearchAMGT(BaseAction):
    NAME = "Search AMG (classical music) for Track"
    def callback(self, objs):
        file = objs[0]
        url = "http://www.allmusic.com/search/work/"
        url += QtCore.QUrl.toPercentEncoding(file.metadata["title"])
        webbrowser2.open(url)
register_file_action(SearchAMGT())
