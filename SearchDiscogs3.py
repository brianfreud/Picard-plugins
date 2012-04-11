# -*- coding: utf-8 -*-

PLUGIN_NAME = u"Search Discogs for Release"
PLUGIN_AUTHOR = u"Brian Schweitzer"
PLUGIN_DESCRIPTION = "Search Discogs"
PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10","0.11","0.12","0.13","0.14","0.15","0.16"]

from PyQt4 import QtCore
from picard.cluster import Cluster
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_cluster_action
from picard.ui.itemviews import BaseAction, register_album_action

class SearchDiscogs(BaseAction):
    NAME = "Search Discogs"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.discogs.com/search?type=all&q="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["artist"])
        url += "+"
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        url += "&btn=Search"
        webbrowser2.open(url)
register_cluster_action(SearchDiscogs())
register_album_action(SearchDiscogs())
