# -*- coding: utf-8 -*-

PLUGIN_NAME = u"Search AMG"
PLUGIN_AUTHOR = u"Brian Schweitzer"
PLUGIN_DESCRIPTION = "Search AMG"
PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10","0.11","0.12","0.13","0.14","0.15","0.16"]

from PyQt4 import QtCore
from picard.cluster import Cluster
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_cluster_action
from picard.ui.itemviews import BaseAction, register_album_action
from picard.ui.itemviews import BaseAction, register_file_action
from picard.metadata import register_track_metadata_processor

class SearchAMGR(BaseAction):
    NAME = "Search AMG for Release"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://wc10.allmusic.com/cg/amg.dll?P=amg&opt1=2&sql="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        webbrowser2.open(url)
register_cluster_action(SearchAMGR())
register_album_action(SearchAMGR())

class SearchAMGA(BaseAction):
    NAME = "Search AMG for Artist"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://wc09.allmusic.com/cg/amg.dll?P=amg&opt1=1&sql="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["artist"])
        webbrowser2.open(url)
register_cluster_action(SearchAMGA())
register_album_action(SearchAMGA())

class SearchAMGT(BaseAction):
    NAME = "Search AMG for Track"
    def callback(self, objs):
        file = objs[0]
        url = "http://wc10.allmusic.com/cg/amg.dll?P=amg&opt1=3&sql="
        url += QtCore.QUrl.toPercentEncoding(file.metadata["title"])
        webbrowser2.open(url)
register_file_action(SearchAMGT())
