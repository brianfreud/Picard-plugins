# -*- coding: utf-8 -*-

PLUGIN_NAME = u'Search online'
PLUGIN_AUTHOR = u'Brian Schweitzer'
PLUGIN_DESCRIPTION = 'Using existing metadata, launch a search at various websites.'
PLUGIN_VERSION = '1.1'
PLUGIN_API_VERSIONS = ['0.16']

from PyQt4 import QtCore, QtGui
from picard.album import Album, NatAlbum
from picard.cluster import Cluster, ClusterList, UnmatchedFiles
from picard.file import File
from picard.track import Track, NonAlbumTrack
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_album_action, register_file_action, register_cluster_action, register_add_plugin_submenu
from picard.plugin import ExtensionPoint

register_add_plugin_submenu("Search", (Cluster,Album,File,NonAlbumTrack,Track))
register_add_plugin_submenu('Mercado Libre', (Cluster,Album), "Search")
register_add_plugin_submenu('eBay-affiliated', (Cluster,Album), "Search")
register_add_plugin_submenu('eBay', (Cluster,Album), "Search")
register_add_plugin_submenu('Amazon', (Cluster,Album), "Search")
register_add_plugin_submenu('Universal Publishing Production Music', (Cluster,Album,File,Track,NonAlbumTrack), "Search")

urls = {
    'generic' : [
        ('All Music Guide (album)', set(['album','cluster']), 'album', 'http://www.allmusic.com/search/album/'),
        ('All Music Guide (artist)', set(['album','cluster']), 'artist', 'http://www.allmusic.com/search/artist/'),
        ('All Music Guide (artist)', set(['file']), 'artist', 'http://www.allmusic.com/search/artist/'),
        ('All Music Guide (title, classical music)', set(['file']), 'file', 'http://www.allmusic.com/search/work/'),
        ('All Music Guide (title, non-classical music)', set(['file']), 'file', 'http://www.allmusic.com/search/song/'),
        ('CastAlbums.org', set(['album','cluster']), 'album', 'http://www.castalbums.org/shows/search/'),
        ('Discogs', set(['album','cluster']), 'album_and_artist', 'http://www.discogs.com/search?type=all&q='),
        ('Discogs', set(['file']), 'file', 'http://www.discogs.com/search?type=all&q='),
        ('FilmMuziek.be', set(['album','cluster']), 'album', 'http://www.filmmuziek.be/search.cgi?Match=0&Realm=All&Terms='),
        ('Game Music Revolution', set(['album','cluster']), 'album', 'http://www.gmronline.com/results.asp?display=0&go=Go+Find+It&searchType=Title&browseType=Title&results=25&search='),
        ('Google', set(['album','cluster']), 'album_and_artist', 'http://www.google.com/search?hl=en&q='),
        ('Google', set(['file']), 'file_and_album_and_artist', 'http://www.google.com/search?hl=en&q='),
        ('SoundtrackCollector', set(['album','cluster']), 'album', 'http://www.soundtrackcollector.com/catalog/search.php?searchon=all&searchtext='),
        ('SoundtrackINFO', set(['album','cluster']), 'album', 'http://www.soundtrackinfo.com/search.asp?q='),
        ('The Lortel Archives (IoBDb)', set(['album','cluster']), 'album', 'http://www.lortel.org/LLA_archive/index.cfm?COMMITT=YES&search_by=SHOW+TITLE&Go.x=0&Go.y=0&keyword='),
        ('VGMdb', set(['album','cluster']), 'album', 'http://vgmdb.net/search?q='),
    ],
    'amazon': {
        'ca' : {
            'name' : u'Canada',
            'url'  : u'http://www.amazon.ca/s/?url=search-alias%3Dpopular&field-keywords='},
        'cn' : {
            'name' : u'China',
            'url'  : u'http://www.amazon.cn/s/?url=search-alias%3Dpopular&field-keywords='},
        'fr' : {
            'name' : u'France',
            'url'  : u'http://www.amazon.fr/s/?url=search-alias%3Dpopular&field-keywords='},
        'de' : {
            'name' : u'Germany',
            'url'  : u'http://www.amazon.de/s/?url=search-alias%3Dpopular&field-keywords='},
        'it' : {
            'name' : u'Italy',
            'url'  : u'http://www.amazon.it/s/?url=search-alias%3Dpopular&field-keywords='},
        'jp' : {
            'name' : u'Japan',
            'url'  : u'http://www.amazon.co.jp/s/?url=search-alias%3Dpopular&field-keywords='},
        'es' : {
            'name' : u'Spain',
            'url'  : u'http://www.amazon.es/s/?url=search-alias%3Dpopular&field-keywords='},
        'uk' : {
            'name' : u'United Kingdom',
            'url'  : u'http://www.amazon.co.uk/s/?url=search-alias%3Dpopular&field-keywords='},
        'com' : {
            'name' : u'United States',
            'url'  : u'http://www.amazon.com/s/?url=search-alias%3Dpopular&field-keywords='},
    },
    'ebay': {
        'ar' : {
            'name' : u'Argentina',
            'url'  : u'http://listado.mercadolibre.com.ar/'},
        'au' : {
            'name' : u'Australia',
            'url'  : u'http://www.ebay.com.au/sch/i.html?_nkw='},
        'at' : {
            'name' : u'Austria',
            'url'  : u'http://www.ebay.at/sch/i.html?_nkw='},
        'be1' : {
            'name' : u'Belgium (Dutch)',
            'url'  : u'http://www.benl.ebay.be/sch/i.html?_nkw='},
        'be2' : {
            'name' : u'Belgium (French)',
            'url'  : u'http://www.befr.ebay.be/sch/i.html?_nkw='},
        'br' : {
            'name' : u'Brazil',
            'url'  : u'http://lista.mercadolivre.com.br/'},
        'ca1' : {
            'name' : u'Canada (English)',
            'url'  : u'http://www.ebay.ca/sch/i.html?_nkw='},
        'ca2' : {
            'name' : u'Canada (French)',
            'url'  : u'http://www.cafr.ebay.ca/sch/i.html?_nkw='},
        'cl' : {
            'name' : u'Chile',
            'url'  : u'http://listado.mercadolibre.cl/'},
        'co' : {
            'name' : u'Columbia',
            'url'  : u'http://listado.mercadolibre.com.co/'},
        'cr' : {
            'name' : u'Costa Rica',
            'url'  : u'http://listado.mercadolibre.co.cr/'},
        'cz' : {
            'name' : u'Czech Republic',
            'url'  : u'http://search.eim.ebay.cz/?kw='},
        'dk1' : {
            'name' : u'Denmark',
            'url'  : u'http://search.eim.ebay.dk/?kw='},
        'dk2' : {
            'name' : u'dba.dk (Denmark)',
            'url'  : u'http://www.dba.dk/soeg/?soeg='},
        'do' : {
            'name' : u'Dominican Republic',
            'url'  : u'http://listado.mercadolibre.com.do/'},
        'ec' : {
            'name' : u'Ecuador',
            'url'  : u'http://listado.mercadolibre.com.ec/'},
        'fi' : {
            'name' : u'Finland',
            'url'  : u'http://search.eim.ebay.fi/?kw='},
        'fr' : {
            'name' : u'France',
            'url'  : u'http://shop.ebay.fr/i.html?_nkw='},
        'de1' : {
            'name' : u'Germany (eBay classic)',
            'url'  : u'http://www.ebay.de/sch/i.html?_nkw='},
        'de2' : {
            'name' : u'Germany (eBay kleinanzeigen)',
            'url'  : u'http://kleinanzeigen.ebay.de/anzeigen/s-'},
        'gr' : {
            'name' : u'Greece',
            'url'  : u'http://search.eim.ebay.gr/?kw='},
        'hk' : {
            'name' : u'Hong Kong',
            'url'  : u'http://www.ebay.com.hk/sch/i.html?_nkw='},
        'hu' : {
            'name' : u'Hungary',
            'url'  : u'http://search.eim.ebay.hu/?kw='},
        'in' : {
            'name' : u'India',
            'url'  : u'http://www.ebay.in/sch/i.html?_nkw='},
        'ie' : {
            'name' : u'Ireland',
            'url'  : u'http://www.ebay.ie/sch/i.html?_nkw='},
        'jp' : {
            'name' : u'Sekaimon (Japan)',
            'url'  : u'http://www.sekaimon.com/ItemListReg.do?srch_keyword='},
        'it1' : {
            'name' : u'Italy (eBay classic)',
            'url'  : u'http://www.ebay.it/sch/i.html?_nkw='},
        'it2' : {
            'name' : u'Italy (eBay annunci)',
            'url'  : u'http://annunci.ebay.it/'},
        'my' : {
            'name' : u'Malaysia',
            'url'  : u'http://www.ebay.com.my/sch/i.html?_nkw='},
        'mx' : {
            'name' : u'México',
            'url'  : u'http://listado.mercadolibre.com.mx/'},
        'nl1' : {
            'name' : u'Netherlands',
            'url'  : u'http://www.ebay.nl/sch/i.html?_nkw='},
        'nl2' : {
            'name' : u'Marktplaats.nl (Netherlands)',
            'url'  : u'http://kopen.marktplaats.nl/search.php?q='},
        'no' : {
            'name' : u'Norway',
            'url'  : u'http://search.eim.ebay.no/?kw='},
        'pa' : {
            'name' : u'Panamá',
            'url'  : u'http://listado.mercadolibre.com.pa/'},
        'pe' : {
            'name' : u'Perú',
            'url'  : u'http://listado.mercadolibre.com.pe/'},
        'ph' : {
            'name' : u'Philippines',
            'url'  : u'http://www.ebay.ph/sch/i.html?_nkw='},
        'pl' : {
            'name' : u'Poland',
            'url'  : u'http://www.ebay.pl/sch/i.html?_nkw='},
        'pt1' : {
            'name' : u'Portugal',
            'url'  : u'http://search.eim.ebay.pt/?kw='},
        'pt2' : {
            'name' : u'Portugal',
            'url'  : u'http://lista.mercadolivre.pt/'},
        'ru' : {
            'name' : u'Russia',
            'url'  : u'http://search.classifieds.ebay.ru/eim/search.ru_RU.html?kw='},
        'sg' : {
            'name' : u'Singapore',
            'url'  : u'http://www.ebay.com.sg/sch/i.html?_nkw='},
        'kr' : {
            'name' : u'AUCTION.co.kr (South Korea)',
            'url'  : u'http://search.auction.co.kr/search/search.aspx?keyword='},
        'es1' : {
            'name' : u'Spain (eBay classic)',
            'url'  : u'http://www.ebay.es/sch/i.html?_nkw='},
        'es2' : {
            'name' : u'Spain (eBay anuncios)',
            'url'  : u'http://anuncios.ebay.es/anuncios/'},
        'se' : {
            'name' : u'Tradera (Sweden)',
            'url'  : u'http://www.tradera.com/finding.mvc/itemlisting?search='},
        'ch' : {
            'name' : u'Switzerland',
            'url'  : u'http://www.ebay.ch/sch/i.html?_nkw='},
        'tw' : {
            'name' : u'Ruten (Taiwan)',
            'url'  : u'http://search.ruten.com.tw/search/s000.php?k='},
        'th1' : {
            'name' : u'Thailand',
            'url'  : u'http://export.ebay.co.th/search/index.php?q='},
        'th2' : {
            'name' : u'Sanook (Thailand)',
            'url'  : u'http://shopping.sanook.com/search_list.php?q='},
        'tr' : {
            'name' : u'Gitti Gidiyor (Turkey)',
            'url'  : u'http://arama.gittigidiyor.com/?aramakelime='},
        'uk' : {
            'name' : u'United Kingdom',
            'url'  : u'http://www.ebay.co.uk/sch/i.html?_nkw='},
        'us1' : {
            'name' : u'United States',
            'url'  : u'http://www.ebay.com/sch/i.html?_nkw='},
        'us2' : {
            'name' : u'half.com (United States)',
            'url'  : u'http://search.half.ebay.com/'},
        'uy' : {
            'name' : u'Uruguay',
            'url'  : u'http://listado.mercadolibre.com.uy/'},
        've' : {
            'name' : u'Venezuela',
            'url'  : u'http://listado.mercadolibre.com.ve/'},
        'vn' : {
            'name' : u'Chodientu (Vietnam)',
            'url'  : u'http://chodientu.vn/ebay-browse-keyword-'}
    },
    'unippm': {
        'au' : {
            'name' : u'Australia',
            'url'  : u'http://www.unippm.com.au'},
        'hk' : {
            'name' : u'Asia',
            'url'  : u'http://www.unippm.hk'},
        'cn' : {
            'name' : u'China',
            'url'  : u'http://www.unippm.cn'},
        'de' : {
            'name' : u'Germany',
            'url'  : u'http://www.unippm.de'},
        'fr' : {
            'name' : u'France',
            'url'  : u'http://www.unippm.fr'},
        'global' : {
            'name' : u'Global',
            'url'  : u'http://www.unippmglobal.com'},
        'il' : {
            'name' : u'Israel',
            'url'  : u'http://www.unippm.co.il'},
        'it' : {
            'name' : u'Italy',
            'url'  : u'http://www.unippm.it'},
        'latin' : {
            'name' : u'Latin America',
            'url'  : u'http://www.umpla.com'},
        'pl' : {
            'name' : u'Poland',
            'url'  : u'http://www.unippm.pl'},
        'se' : {
            'name' : u'Scandinavia',
            'url'  : u'http://www.unippm.se'},
        'za' : {
            'name' : u'South Africa',
            'url'  : u'http://www.unippm.co.za'},
        'es' : {
            'name' : u'Spain',
            'url'  : u'http://www.unippm.es'},
        'nl' : {
            'name' : u'The Netherlands',
            'url'  : u'http://www.unippm.nl'},
        'uk' : {
            'name' : u'United Kingdom',
            'url'  : u'http://www.unippm.co.uk'},
        'us1' : {
            'name' : u'United States (Killer Tracks)',
            'url'  : u'http://www.killertracks.com'},
        'us2' : {
            'name' : u'United States (firstcom Music)',
            'url'  : u'http://www.firstcom.com/'},
    }
}

# ebay:
# half.com
# eachnet.com
# alamaula.com
# alamaula.com.br
# alamaula.cl
# alamaula.com.co
# alamaula.co.cr
# alamaula.ec
# alamaula.es
# alamaula.us
# alamaula.com.mx
# alamaula.pe

def get_terms(self, objs, atom):
    print objs
    terms_list = []
    for obj in objs:
        print obj.metadata
        terms_list.append(QtCore.QUrl.toPercentEncoding(obj.metadata[atom]))
    print terms_list
    return terms_list

def open_pages(self, url, obj_list, atom):
    for term in list(set(get_terms(self, obj_list, atom))):
        webbrowser2.open(url + term)

def album_open_page(self, objs, url):
    clusters = [o for o in objs if isinstance(o, Cluster)]
    open_pages(self, url, clusters, 'album')

def artist_open_page(self, objs, url):
    files = [o for o in objs if isinstance(o, File)]
    if (len(files) > 0):
        open_pages(self, url, files, 'artist')
    clusters = [o for o in objs if isinstance(o, Cluster)]
    if (len(clusters) > 0):
        open_pages(self, url, clusters, 'albumartist')

def file_open_page(self, objs, url):
    files = [o for o in objs if isinstance(o, File)]
    open_pages(self, url, files, 'title')

def album_and_artist_open_page(self, objs, tld, amazon = None):
    clusters = [o for o in objs if (isinstance(o, Cluster) or isinstance(o, File))]
    for cluster in clusters:
        url = []
        url.append(cluster.metadata['artist'])
        url.append(' ')
        url.append(cluster.metadata['album'])
        url = QtCore.QUrl.toPercentEncoding(''.join(url))
        if amazon:
            url = urls['amazon'][tld]['url'] + url
        else:
            url = tld + url
        webbrowser2.open(url)

def file_and_album_and_artist_open_page(self, objs, tld):
    clusters = [o for o in objs if (isinstance(o, Cluster) or isinstance(o, File))]
    for cluster in clusters:
        url = []
        url.append(cluster.metadata['artist'])
        url.append(' ')
        url.append(cluster.metadata['album'])
        url.append(' ')
        url.append(cluster.metadata['title'])
        url = QtCore.QUrl.toPercentEncoding(''.join(url))
        url = tld + url
        webbrowser2.open(url)

def ebay_open_page(self, objs, tld):
    clusters = [o for o in objs if isinstance(o, Cluster)]
    album_list = []
    for cluster in clusters:
        album_list.append(QtCore.QUrl.toPercentEncoding(cluster.metadata['album']))
    for album in list(set(album_list)):
        url = urls['ebay'][tld]['url'] + album
        if tld == 'de2':
            url += '/k0'
        if tld == 'es':
            url += '.htm'
        if tld == 'us2':
            url += '._W0QQmZmusicQQsubmitZSearchQQtgZproductsQQ_trksidZp3030'
        if tld == 'vn':
            url += '.html'
        webbrowser2.open(url)


for tld in ['ar','br','cl','co','cr','do','ec','mx','pa','pe','pt2','uy','ve']:
    class SearchML(BaseAction):
        NAME = urls['ebay'][tld]['name']
        MENU = 'Mercado Libre'

        def callback(self, objs, tld=tld):
            ebay_open_page(self, objs, tld)
    register_cluster_action(SearchML())
    register_album_action(SearchML())


for tld in ['au','at','be1','be2','ca1','ca2','cz','dk1','fi','fr','de1','de2','gr','hk','hu','in','ie','it1','it2','my','nl1','no','ph','pl','pt1','ru','sg','es1','es2','ch','th1','uk','us1']:
    class SearcheBay(BaseAction):
        NAME = urls['ebay'][tld]['name']
        MENU = 'eBay'

        def callback(self, objs, tld=tld):
            ebay_open_page(self, objs, tld)
    register_cluster_action(SearcheBay())
    register_album_action(SearcheBay())


for tld in ['kr','vn','dk2','tr','us2','nl2','tw','th2','jp','se']:
    class SearcheBayAffiliate(BaseAction):
        NAME = urls['ebay'][tld]['name']
        MENU = 'eBay-affiliated'

        def callback(self, objs, tld=tld):
            ebay_open_page(self, objs, tld)
    register_cluster_action(SearcheBayAffiliate())
    register_album_action(SearcheBayAffiliate())


for tld in ['ca','cn','fr','de','it','jp','es','uk','com']:
    class Search_amazon(BaseAction):
        NAME = urls['amazon'][tld]['name']
        MENU = 'Amazon'

        def callback(self, objs, tld=tld):
            album_and_artist_open_page(self, objs, tld, True)

    register_cluster_action(Search_amazon())
    register_album_action(Search_amazon())


class Search_all_amazon(BaseAction):
    NAME = 'all Amazon sites'
    MENU = 'Amazon'

    def callback(self, objs, tld=tld):
        for tld in ['ca','cn','fr','de','it','jp','es','uk','com']:
            album_and_artist_open_page(self, objs, tld, True)

register_cluster_action(Search_all_amazon())
register_album_action(Search_all_amazon())


for tld in ['au','hk','cn','de','fr','global','il','it','latin','pl','se','za','es','nl','uk','us2','us1']:
    class Search_unippm_album(BaseAction):
        NAME = urls['unippm'][tld]['name']
        MENU = 'Universal Publishing Production Music'

        def callback(self, objs, tld=tld):
            album_open_page(self, objs, urls['unippm'][tld]['url'] + '/#/en/search-results.aspx?searchtype=quick&isNewSearch=true&mode=CD&keyword=')

    register_cluster_action(Search_unippm_album())
    register_album_action(Search_unippm_album())


for tld in ['au','hk','cn','de','fr','global','il','it','latin','pl','se','za','es','nl','uk','us2','us1']:
    class Search_unippm_file(BaseAction):
        NAME = urls['unippm'][tld]['name']
        MENU = 'Universal Publishing Production Music'

        def callback(self, objs, tld=tld):
            file_open_page(self, objs, urls['unippm'][tld]['url'] + '/#/en/search-results.aspx?searchtype=quick&isNewSearch=true&keyword=')

    register_file_action(Search_unippm_file())

for site in urls['generic']:
    class Search_generic(BaseAction):
        MENU = "Search"
        NAME = site[0]
        def callback(self, objs, site = site):
            cbFunction = globals()[site[2] + '_open_page']
            cbFunction(self, objs, site[3])

    if 'album' in site[1]:
        register_album_action(Search_generic())
    if 'cluster' in site[1]:
        register_cluster_action(Search_generic())
    if 'file' in site[1]:
        register_file_action(Search_generic())
