# -*- coding: utf-8 -*-

PLUGIN_NAME = u"Search eBay for Release"
PLUGIN_AUTHOR = u"Brian Schweitzer"
PLUGIN_DESCRIPTION = "Search eBay"
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10","0.11","0.12","0.13","0.14","0.15","0.16"]

from PyQt4 import QtCore
from picard.cluster import Cluster
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_album_action, register_cluster_action

urls = {
    'ar' : {
                'name' : u"Argentina (Mercado Libre)",
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
                'name' : u"Brazil (Mercado Livre)",
                'url'  : u"http://lista.mercadolivre.com.br/"},
    'ca1' : {
                'name' : u"Canada (English)",
                'url'  : u"http://www.ebay.ca/sch/i.html?_nkw="},
    'ca2' : {
                'name' : u"Canada (French)",
                'url'  : u"http://www.cafr.ebay.ca/sch/i.html?_nkw="},
    'cl' : {
                'name' : u"Chile (Mercado Libre)",
                'url'  : u"http://listado.mercadolibre.cl/"},
    'co' : {
                'name' : u"Columbia (Mercado Libre)",
                'url'  : u"http://listado.mercadolibre.com.co/"},
    'cr' : {
                'name' : u"Costa Rica (Mercado Libre)",
                'url'  : u"http://listado.mercadolibre.co.cr/"},
    'cz' : {
                'name' : u"Czech Republic",
                'url'  : u"http://search.eim.ebay.cz/?kw="},
    'dk' : {
                'name' : u"Denmark",
                'url'  : u"http://search.eim.ebay.dk/?kw="},
    'do' : {
                'name' : u"Dominican Republic (Mercado Libre)",
                'url'  : u"http://listado.mercadolibre.com.do/"},
    'ec' : {
                'name' : u"Ecuador (Mercado Libre)",
                'url'  : u"http://listado.mercadolibre.com.ec/"},
    'fi' : {
                'name' : u"Finland",
                'url'  : u"http://search.eim.ebay.fi/?kw="},
    'fr' : {
                'name' : u"France",
                'url'  : u"http://shop.ebay.fr/i.html?_nkw="},
    'de' : {
                'name' : u"Germany",
                'url'  : u"http://www.ebay.de/sch/i.html?_nkw="},
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
    'it' : {
                'name' : u"Italy",
                'url'  : u"http://www.ebay.it/sch/i.html?_nkw="},
    'my' : {
                'name' : u"Malaysia",
                'url'  : u"http://www.ebay.com.my/sch/i.html?_nkw="},
    'mx' : {
                'name' : u"México (Mercado Livre)",
                'url'  : u"http://listado.mercadolibre.com.mx/"},
    'nl' : {
                'name' : u"Netherlands",
                'url'  : u"http://www.ebay.nl/sch/i.html?_nkw="},
    'no' : {
                'name' : u"Norway",
                'url'  : u"http://search.eim.ebay.no/?kw="},
    'pa' : {
                'name' : u"Panamá (Mercado Libre)",
                'url'  : u"http://listado.mercadolibre.com.pa/"},
    'pe' : {
                'name' : u"Perú (Mercado Libre)",
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
                'name' : u"Portugal (Mercado Livre)",
                'url'  : u"http://lista.mercadolivre.pt/"},
    'ru' : {
                'name' : u"Russia",
                'url'  : u"http://search.classifieds.ebay.ru/eim/search.ru_RU.html?kw="},
    'sg' : {
                'name' : u"Singapore",
                'url'  : u"http://www.ebay.com.sg/sch/i.html?_nkw="},
    'kr' : {
                'name' : u"South Korea (AUCTION)",
                'url'  : u"http://search.auction.co.kr/search/search.aspx?keyword="},
    'es' : {
                'name' : u"Spain",
                'url'  : u"http://anuncios.ebay.es/anuncios/"},
    'se' : {
                'name' : u"Sweden (Tradera)",
                'url'  : u"http://www.tradera.com/finding.mvc/itemlisting?search="},
    'ch' : {
                'name' : u"Switzerland",
                'url'  : u"http://www.ebay.ch/sch/i.html?_nkw="},
    'tw' : {
                'name' : u"Taiwan (Ruten)",
                'url'  : u"http://search.ruten.com.tw/search/s000.php?k="},
    'th' : {
                'name' : u"Thailand",
                'url'  : u"http://export.ebay.co.th/search/index.php?q="},
    'tr' : {
                'name' : u"Turkey (Gitti Gidiyor)",
                'url'  : u"http://arama.gittigidiyor.com/?aramakelime="},
    'uk' : {
                'name' : u"United Kingdom",
                'url'  : u"http://www.ebay.co.uk/sch/i.html?_nkw="},
    'us' : {
                'name' : u"United States",
                'url'  : u"http://www.ebay.com/sch/i.html?_nkw="},
    'uy' : {
                'name' : u"Uruguay (Mercado Libre)",
                'url'  : u"http://listado.mercadolibre.com.uy/"},
    've' : {
                'name' : u"Venezuela (Mercado Libre)",
                'url'  : u"http://listado.mercadolibre.com.ve/"},
    'vn' : {
                'name' : u"Vietnam",
                'url'  : u"http://chodientu.vn/ebay-browse-keyword-"}
}


for tld in ['ar','au','at','be1','be2','br','ca1','ca2','cl','co','cr','cz','dk','do','ec','fi','fr','de','gr','hk','hu','in','ie','it','my','mx','nl','no','pa','pe','ph','pl','pt1','pt2','ru','sg','kr','es','se','ch','tw','th','tr','uk','us','uy','ve','vn']:
    class SearcheBay(BaseAction):
        NAME = "Search eBay " + urls[tld]['name']
        def callback(self, objs, tld=tld):
            cluster = objs[0]
            url = urls[tld]['url']
            url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
            if tld == 'es':
                url += '.htm'
            if tld == 'vn':
                url += '.html'
            webbrowser2.open(url)
    register_cluster_action(SearcheBay())
    register_album_action(SearcheBay())
