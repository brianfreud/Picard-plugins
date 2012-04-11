# -*- coding: utf-8 -*-

PLUGIN_NAME = u"Search Game Music Revolution"
PLUGIN_AUTHOR = u"Brian Schweitzer"
PLUGIN_DESCRIPTION = "Search Game Music Revolution"
PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10","0.11","0.12","0.13","0.14","0.15","0.16"]

from PyQt4 import QtCore
from picard.cluster import Cluster
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_cluster_action
from picard.ui.itemviews import BaseAction, register_album_action

class SearchGameMusicRevolution(BaseAction):
    NAME = "Search with Game Music Revolution"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.gmronline.com/results.asp?display=0&go=Go+Find+It&searchType=Title&browseType=Title&results=25&search="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        webbrowser2.open(url)
register_cluster_action(SearchGameMusicRevolution())
register_album_action(SearchGameMusicRevolution())
