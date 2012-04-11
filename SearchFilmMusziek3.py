# -*- coding: utf-8 -*-

PLUGIN_NAME = u"Search FilmMuziek.be"
PLUGIN_AUTHOR = u"Brian Schweitzer"
PLUGIN_DESCRIPTION = "Search FilmMuziek.be"
PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10","0.11","0.12","0.13","0.14","0.15","0.16"]

from PyQt4 import QtCore
from picard.cluster import Cluster
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_cluster_action
from picard.ui.itemviews import BaseAction, register_album_action


class SearchFilmMusic(BaseAction):
    NAME = "Search with FilmMuziek.be"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.filmmuziek.be/search.cgi?Match=0&Realm=All&Terms="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        webbrowser2.open(url)
register_cluster_action(SearchFilmMusic())
register_album_action(SearchFilmMusic())
