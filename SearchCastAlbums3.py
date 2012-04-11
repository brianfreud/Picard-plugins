# -*- coding: utf-8 -*-

PLUGIN_NAME = u"Search CastAlbums.org for Release"
PLUGIN_AUTHOR = u"Brian Schweitzer"
PLUGIN_DESCRIPTION = "Search CastAlbums.org"
PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10","0.11","0.12","0.13","0.14","0.15","0.16"]

from PyQt4 import QtCore
from picard.cluster import Cluster
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_album_action
from picard.ui.itemviews import BaseAction, register_cluster_action


class SearchCastAlbums(BaseAction):
    NAME = "Search with CastAlbums.org"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.castalbums.org/shows/search/"
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        webbrowser2.open(url)
register_cluster_action(SearchCastAlbums())
register_album_action(SearchCastAlbums())
