# -*- coding: utf-8 -*-

PLUGIN_NAME = u"Search the Lortel Archives"
PLUGIN_AUTHOR = u"Brian Schweitzer"
PLUGIN_DESCRIPTION = "Search the Lortel Archives"
PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10","0.11","0.12","0.13","0.14","0.15","0.16"]

from PyQt4 import QtCore
from picard.cluster import Cluster
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_cluster_action
from picard.ui.itemviews import BaseAction, register_album_action


class SearchLortelArchives(BaseAction):
    NAME = "Search the Lortel Archives"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.lortel.org/LLA_archive/index.cfm?keyword="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        url += "&COMMITT=YES&search_by=ALL&Go.x=0&Go.y=0"
        webbrowser2.open(url)
register_cluster_action(SearchLortelArchives())
register_album_action(SearchLortelArchives())
