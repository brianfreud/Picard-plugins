# -*- coding: utf-8 -*-

PLUGIN_NAME = u"Search with Google"
PLUGIN_AUTHOR = u"Brian Schweitzer"
PLUGIN_DESCRIPTION = "Search Google.  Thanks to Lukas Lalinsky for bug-fix!"
PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10","0.11","0.12","0.13","0.14","0.15","0.16"]

from PyQt4 import QtCore
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_cluster_action
from picard.ui.itemviews import BaseAction, register_album_action
from picard.ui.itemviews import BaseAction, register_file_action
from picard.metadata import register_track_metadata_processor

class SearchGoogle(BaseAction):
    NAME = "Search with Google"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.google.com/search?hl=en&q="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["artist"])
        url += " "
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        webbrowser2.open(url)
register_cluster_action(SearchGoogle())
register_album_action(SearchGoogle())

class SearchGoogleTrack(BaseAction):
    NAME = "Search with Google"
    def callback(self, objs):
        file = objs[0]
        url = "http://www.google.com/search?hl=en&q="
        url += QtCore.QUrl.toPercentEncoding(file.metadata["artist"])
        url += " "
        url += QtCore.QUrl.toPercentEncoding(file.metadata["album"])
        url += " "
        url += QtCore.QUrl.toPercentEncoding(file.metadata["title"])
        webbrowser2.open(url)
register_file_action(SearchGoogleTrack())
