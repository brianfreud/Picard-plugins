# -*- coding: utf-8 -*-

PLUGIN_NAME = u"Search eBay for Release"
PLUGIN_AUTHOR = u"Brian Schweitzer"
PLUGIN_DESCRIPTION = "Search eBay"
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10","0.11","0.12","0.13","0.14","0.15","0.16"]

from PyQt4 import QtCore, QtGui
from picard.cluster import Cluster
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_album_action, register_cluster_action, register_add_plugin_submenu

urls = {
    'ar' : {
                'name' : u"Argentina",
                'url'  : u"http://listado.mercadolibre.com.ar/"},
    'au' : {
                'name' : u"Australia",
                'url'  : u"http://www.ebay.com.au/sch/i.html?_nkw="},
    'at' : {
                'name' : u"Austria",
                'url'  : u"http://www.ebay.at/sch/i.html?_nkw="},
    'be1' : {
                'name' : u"Belgium (Dutch)",
                'url'  : u"http://www.benl.ebay.be/sch/i.html?_nkw="},
    'be2' : {
                'name' : u"Belgium (French)",
                'url'  : u"http://www.befr.ebay.be/sch/i.html?_nkw="},
    'br' : {
                'name' : u"Brazil",
                'url'  : u"http://lista.mercadolivre.com.br/"},
    'ca1' : {
                'name' : u"Canada (English)",
                'url'  : u"http://www.ebay.ca/sch/i.html?_nkw="},
    'ca2' : {
                'name' : u"Canada (French)",
                'url'  : u"http://www.cafr.ebay.ca/sch/i.html?_nkw="},
    'cl' : {
                'name' : u"Chile",
                'url'  : u"http://listado.mercadolibre.cl/"},
    'co' : {
                'name' : u"Columbia",
                'url'  : u"http://listado.mercadolibre.com.co/"},
    'cr' : {
                'name' : u"Costa Rica",
                'url'  : u"http://listado.mercadolibre.co.cr/"},
    'cz' : {
                'name' : u"Czech Republic",
                'url'  : u"http://search.eim.ebay.cz/?kw="},
    'dk1' : {
                'name' : u"Denmark",
                'url'  : u"http://search.eim.ebay.dk/?kw="},
    'dk2' : {
                'name' : u"dba.dk (Denmark)",
                'url'  : u"http://www.dba.dk/soeg/?soeg="},
    'do' : {
                'name' : u"Dominican Republic",
                'url'  : u"http://listado.mercadolibre.com.do/"},
    'ec' : {
                'name' : u"Ecuador",
                'url'  : u"http://listado.mercadolibre.com.ec/"},
    'fi' : {
                'name' : u"Finland",
                'url'  : u"http://search.eim.ebay.fi/?kw="},
    'fr' : {
                'name' : u"France",
                'url'  : u"http://shop.ebay.fr/i.html?_nkw="},
    'de1' : {
                'name' : u"Germany (eBay classic)",
                'url'  : u"http://www.ebay.de/sch/i.html?_nkw="},
    'de2' : {
                'name' : u"Germany (eBay kleinanzeigen)",
                'url'  : u"http://kleinanzeigen.ebay.de/anzeigen/s-"},
    'gr' : {
                'name' : u"Greece",
                'url'  : u"http://search.eim.ebay.gr/?kw="},
    'hk' : {
                'name' : u"Hong Kong",
                'url'  : u"http://www.ebay.com.hk/sch/i.html?_nkw="},
    'hu' : {
                'name' : u"Hungary",
                'url'  : u"http://search.eim.ebay.hu/?kw="},
    'in' : {
                'name' : u"India",
                'url'  : u"http://www.ebay.in/sch/i.html?_nkw="},
    'ie' : {
                'name' : u"Ireland",
                'url'  : u"http://www.ebay.ie/sch/i.html?_nkw="},
    'jp' : {
                'name' : u"Sekaimon (Japan)",
                'url'  : u"http://www.sekaimon.com/ItemListReg.do?srch_keyword="},
    'it1' : {
                'name' : u"Italy (eBay classic)",
                'url'  : u"http://www.ebay.it/sch/i.html?_nkw="},
    'it2' : {
                'name' : u"Italy (eBay annunci)",
                'url'  : u"http://annunci.ebay.it/"},
    'my' : {
                'name' : u"Malaysia",
                'url'  : u"http://www.ebay.com.my/sch/i.html?_nkw="},
    'mx' : {
                'name' : u"México",
                'url'  : u"http://listado.mercadolibre.com.mx/"},
    'nl1' : {
                'name' : u"Netherlands",
                'url'  : u"http://www.ebay.nl/sch/i.html?_nkw="},
    'nl2' : {
                'name' : u"Marktplaats.nl (Netherlands)",
                'url'  : u"http://kopen.marktplaats.nl/search.php?q="},
    'no' : {
                'name' : u"Norway",
                'url'  : u"http://search.eim.ebay.no/?kw="},
    'pa' : {
                'name' : u"Panamá",
                'url'  : u"http://listado.mercadolibre.com.pa/"},
    'pe' : {
                'name' : u"Perú",
                'url'  : u"http://listado.mercadolibre.com.pe/"},
    'ph' : {
                'name' : u"Philippines",
                'url'  : u"http://www.ebay.ph/sch/i.html?_nkw="},
    'pl' : {
                'name' : u"Poland",
                'url'  : u"http://www.ebay.pl/sch/i.html?_nkw="},
    'pt1' : {
                'name' : u"Portugal",
                'url'  : u"http://search.eim.ebay.pt/?kw="},
    'pt2' : {
                'name' : u"Portugal",
                'url'  : u"http://lista.mercadolivre.pt/"},
    'ru' : {
                'name' : u"Russia",
                'url'  : u"http://search.classifieds.ebay.ru/eim/search.ru_RU.html?kw="},
    'sg' : {
                'name' : u"Singapore",
                'url'  : u"http://www.ebay.com.sg/sch/i.html?_nkw="},
    'kr' : {
                'name' : u"AUCTION.co.kr (South Korea)",
                'url'  : u"http://search.auction.co.kr/search/search.aspx?keyword="},
    'es1' : {
                'name' : u"Spain (eBay classic)",
                'url'  : u"http://www.ebay.es/sch/i.html?_nkw="},
    'es2' : {
                'name' : u"Spain (eBay anuncios)",
                'url'  : u"http://anuncios.ebay.es/anuncios/"},
    'se' : {
                'name' : u"Tradera (Sweden)",
                'url'  : u"http://www.tradera.com/finding.mvc/itemlisting?search="},
    'ch' : {
                'name' : u"Switzerland",
                'url'  : u"http://www.ebay.ch/sch/i.html?_nkw="},
    'tw' : {
                'name' : u"Ruten (Taiwan)",
                'url'  : u"http://search.ruten.com.tw/search/s000.php?k="},
    'th1' : {
                'name' : u"Thailand",
                'url'  : u"http://export.ebay.co.th/search/index.php?q="},
    'th2' : {
                'name' : u"Sanook (Thailand)",
                'url'  : u"http://shopping.sanook.com/search_list.php?q="},
    'tr' : {
                'name' : u"Gitti Gidiyor (Turkey)",
                'url'  : u"http://arama.gittigidiyor.com/?aramakelime="},
    'uk' : {
                'name' : u"United Kingdom",
                'url'  : u"http://www.ebay.co.uk/sch/i.html?_nkw="},
    'us' : {
                'name' : u"United States",
                'url'  : u"http://www.ebay.com/sch/i.html?_nkw="},
    'uy' : {
                'name' : u"Uruguay",
                'url'  : u"http://listado.mercadolibre.com.uy/"},
    've' : {
                'name' : u"Venezuela",
                'url'  : u"http://listado.mercadolibre.com.ve/"},
    'vn' : {
                'name' : u"Chodientu (Vietnam)",
                'url'  : u"http://chodientu.vn/ebay-browse-keyword-"}
}


def open_page(self, objs, tld):
            cluster = objs[0]
            url = urls[tld]['url']
            url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
            if tld == 'de2':
                url += '/k0'
            if tld == 'es':
                url += '.htm'
            if tld == 'vn':
                url += '.html'
            webbrowser2.open(url)


for tld in ['ar','br','cl','co','cr','do','ec','mx','pa','pe','pt2','uy','ve']:
    class SearchML(BaseAction):
        NAME = urls[tld]['name']
        MENU = "Mercado Libre"

        def callback(self, objs, tld=tld):
            open_page(self, objs, tld)
    register_cluster_action(SearchML())
    register_album_action(SearchML())

for tld in ['au','at','be1','be2','ca1','ca2','cz','dk1','fi','fr','de1','de2','gr','hk','hu','in','ie','it1','it2','my','nl1','no','ph','pl','pt1','ru','sg','es1','es2','ch','th1','uk','us']:
    class SearcheBay(BaseAction):
        NAME = urls[tld]['name']
        MENU = "eBay"

        def callback(self, objs, tld=tld):
            open_page(self, objs, tld)
    register_cluster_action(SearcheBay())
    register_album_action(SearcheBay())

for tld in ['kr','dk2','vn','tr','nl2','tw','jp','se','th2']:
    class SearcheBayAffiliate(BaseAction):
        NAME = urls[tld]['name']
        MENU = "eBay-affiliated"

        def callback(self, objs, tld=tld):
            open_page(self, objs, tld)
    register_cluster_action(SearcheBayAffiliate())
    register_album_action(SearcheBayAffiliate())

register_add_plugin_submenu("Search")
register_add_plugin_submenu("eBay", "Search")
register_add_plugin_submenu("Mercado Libre", "Search")
register_add_plugin_submenu("eBay-affiliated", "Search")