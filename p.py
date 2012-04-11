# coding=utf-8

# Based on:
# http://www.unicode.org/Public/UNIDATA/Scripts.txt
# http://www.evertype.com/standards/csur/index.html
# http://www.kreativekorp.com/ucsur/

# History
# Version 0.1       2011-01-??:  Initial version
# Version 0.2.1  2011-03-18: First public release
# Version 0.3      2012-04-09: Recovered and rereleased to the public, after the original distribution links broke and I lost the master file. Huge
#                               thanks to kccourier!  Updated to include Unicode 6.1.0 additions to Arabic, Armenian, Coptic, Cyrillic, Georgian, Gujarati, Han, 
#                               Lao, Latin, Meetei Mayek, Sundanese, Tifinagh, and Vedic.  Added support for Amlin, Chakma, Glaitha-A, Glaitha-B, Lhenazi, 
#                               Miao, Sharada, Sora Sompeng, Takri, as well as Picard v. 0.16.  Changed the result for non-script accents and extensions from 
#                               "inherited" to "noscript".

PLUGIN_NAME = '$p'
PLUGIN_AUTHOR = 'Brian Schweitzer'
PLUGIN_DESCRIPTION = 'Identifies the script of a grapheme.  Essentially, this does the inverse of a \p{M} regular expression.'
PLUGIN_VERSION = "0.3"
PLUGIN_API_VERSIONS = ["0.12", "0.13", "0.14", "0.15", "0.16"]

from picard.script import register_script_function
import re

scripts = {
    'scripts' : ["latin","cyrillic","aiha","alzetjan","ammaniar","arabic","armenian","aui","avestan","balinese","bamum","batak","bengali","bopomofo","brahmi","braille","buginese","buhid","canadianaboriginal","carian","cham","cherokee","cirth","coptic","cuneiform","cypriot","deseret","devanagari","egyptianhieroglyphs","engsvanyali","ethiopic","ewellic","ferengi","gargoyle","georgian","glagolitic","gothic","greek","gujarati","gurmukhi","han","hangul","hanunoo","hebrew","hiragana","ilianore","imperialaramaic","noscript","inscriptionalpahlavi","inscriptionalparthian","javanese","kaithi","kannada","katakana","kayahli","kazatakkorou","kazvarad","kelwathi","kharoshthi","khmer","kinya","klingon","lao","lepcha","limbu","linearb","lisu","lycian","lydian","malayalam","mandaic","meeteimayek","mizarian","mongolian","monofon","myanmar","newtailue","niskloz","nko","ogham","olaetyan","olchiki","olditalic","oldpersian","oldsoutharabian","oldturkic","ophidian","oriya","osmanya","phagspa","phoenician","pikto","rejang","rozhxh","runic","rynnan","saklor","samaritan","sarkai","saurashtra","serivelna","seussian","shavian","sinhala","solresol","ssuraki","streich","sundanese","syai","sylotinagri","syriac","tagalog","tagbanwa","taile","taitham","taiviet","tamil","telarasso","telugu","tengwar","thaana","thai","thelwik","tibetan","tifinagh","ugaritic","unifon","vai","verdurian","visiblespeech","xaini","yi","zarkhand","zirinka","amlin","chakma","glaithaa","glaithab","lhenazi","meroitic","miao","sharada","sorasompeng","takri"],
    'aiha' : {
                'name'  : u"Aiha",
                'official' : False,
                'regex' : re.compile(ur"[\uF8A0-\uF8CF]")},
    'alzetjan' : {
                'name'  : u"Alzetjan",
                'official' : False,
                'regex' : re.compile(ur"[\uE550-\uE57F]")},
    'amlin' : {
                'name'  : u"Amlin",
                'official' : False,
                'regex' : re.compile(ur"[\uE6D0-\uE6EF]")},
    'ammaniar' : {
                'name'  : u"Amman-Iar",
                'official' : False,
                'regex' : re.compile(ur"[\uE2A0-\uE2CF]")},
    'arabic' : {
                'name'  : u"Arabic",
                'official' : True,
                'regex' : re.compile(ur"[\u0600-\u0604\u0606-\u0608\u0609-\u060A\u060B\u060D\u060E-\u060F\u0610-\u061A\u061E\u0620-\u063F\u0641-\u064A\u0656-\u065E\u066A-\u066D\u066E-\u066F\u0671-\u06D3\u06D4\u06D5\u06D6-\u06DC\u06DE\u06DF-\u06E4\u06E5-\u06E6\u06E7-\u06E8\u06E9\u06EA-\u06ED\u06EE-\u06EF\u06F0-\u06F9\u06FA-\u06FC\u06FD-\u06FE\u06FF\u0750-\u077F\uFB50-\uFBB1\uFBB2-\uFBC1\uFBD3-\uFD3D\uFD50-\uFD8F\uFD92-\uFDC7\uFDF0-\uFDFB\uFDFC\uFE70-\uFE74\uFE76-\uFEFC\U00010E60-\U00010E7E\u08A0-\u08FF\U0001EE00-\U0001EEFF]")},
    'armenian' : {
                'name'  : u"Armenian",
                'official' : True,
                'regex' : re.compile(ur"[\u0531-\u0556\u0559\u055A-\u055F\u0561-\u0587\u058A\u058F\uFB13-\uFB17]")},
    'aui' : {
                'name'  : u"Aui",
                'official' : False,
                'regex' : re.compile(ur"[\uE280-\uE29F]")},
    'avestan' : {
                'name'  : u"Avestan",
                'official' : True,
                'regex' : re.compile(ur"[\U00010B00-\U00010B35\U00010B39-\U00010B3F]")},
    'balinese' : {
                'name'  : u"Balinese",
                'official' : True,
                'regex' : re.compile(ur"[\u1B00-\u1B03\u1B04\u1B05-\u1B33\u1B34\u1B35\u1B36-\u1B3A\u1B3B\u1B3C\u1B3D-\u1B41\u1B42\u1B43-\u1B44\u1B45-\u1B4B\u1B50-\u1B59\u1B5A-\u1B60\u1B61-\u1B6A\u1B6B-\u1B73\u1B74-\u1B7C]")},
    'bamum' : {
                'name'  : u"Bamum",
                'official' : True,
                'regex' : re.compile(ur"[\uA6A0-\uA6E5\uA6E6-\uA6EF\uA6F0-\uA6F1\uA6F2-\uA6F7\U00016800-\U00016A38]")},
    'batak' : {
                'name'  : u"Batak",
                'official' : True,
                'regex' : re.compile(ur"[\u1BC0-\u1BE5\u1BE6\u1BE7\u1BE8-\u1BE9\u1BEA-\u1BEC\u1BED\u1BEE\u1BEF-\u1BF1\u1BF2-\u1BF3\u1BFC-\u1BFF]")},
    'bengali' : {
                'name'  : u"Bengali",
                'official' : True,
                'regex' : re.compile(ur"[\u0981\u0982-\u0983\u0985-\u098C\u098F-\u0990\u0993-\u09A8\u09AA-\u09B0\u09B2\u09B6-\u09B9\u09BC\u09BD\u09BE-\u09C0\u09C1-\u09C4\u09C7-\u09C8\u09CB-\u09CC\u09CD\u09CE\u09D7\u09DC-\u09DD\u09DF-\u09E1\u09E2-\u09E3\u09E6-\u09EF\u09F0-\u09F1\u09F2-\u09F3\u09F4-\u09F9\u09FA\u09FB]")},
    'bopomofo' : {
                'name'  : u"Bopomofo",
                'official' : True,
                'regex' : re.compile(ur"[\u02EA-\u02EB\u3105-\u312D\u31A0-\u31BA]")},
    'brahmi' : {
                'name'  : u"Brahmi",
                'official' : True,
                'regex' : re.compile(ur"[\U00011000\U00011001\U00011002\U00011003-\U00011037\U00011038-\U00011046\U00011047-\U0001104D\U00011052-\U00011065\U00011066-\U0001106F]")},
    'braille' : {
                'name'  : u"Braille",
                'official' : True,
                'regex' : re.compile(ur"[\u2800-\u28FF]")},
    'buginese' : {
                'name'  : u"Buginese",
                'official' : True,
                'regex' : re.compile(ur"[\u1A00-\u1A16\u1A17-\u1A18\u1A19-\u1A1B\u1A1E-\u1A1F]")},
    'buhid' : {
                'name'  : u"Buhid",
                'official' : True,
                'regex' : re.compile(ur"[\u1740-\u1751\u1752-\u1753]")},
    'canadianaboriginal' : {
                'name'  : u"Canadian Aboriginal",
                'official' : True,
                'regex' : re.compile(ur"[\u1400\u1401-\u166C\u166D-\u166E\u166F-\u167F\u18B0-\u18F5]")},
    'carian' : {
                'name'  : u"Carian",
                'official' : True,
                'regex' : re.compile(ur"[\U000102A0-\U000102D0]")},
    'chakma' : {
                'name'  : u"Chakma",
                'official' : True,
                'regex' : re.compile(ur"[\U00011100-\U0001114F]")},
    'cham' : {
                'name'  : u"Cham",
                'official' : True,
                'regex' : re.compile(ur"[\uAA00-\uAA28\uAA29-\uAA2E\uAA2F-\uAA30\uAA31-\uAA32\uAA33-\uAA34\uAA35-\uAA36\uAA40-\uAA42\uAA43\uAA44-\uAA4B\uAA4C\uAA4D\uAA50-\uAA59\uAA5C-\uAA5F]")},
    'cherokee' : {
                'name'  : u"Cherokee",
                'official' : True,
                'regex' : re.compile(ur"[\u13A0-\u13F4]")},
    'cirth' : {
                'name'  : u"Cirth",
                'official' : False,
                'regex' : re.compile(ur"[\uE080-\uE0FF]")},
    'coptic' : {
                'name'  : u"Coptic",
                'official' : True,
                'regex' : re.compile(ur"[\u03E2-\u03EF\u2C80-\u2CE4\u2CE5-\u2CEA\u2CEB-\u2CEE\u2CEF-\u2CF3\u2CF9-\u2CFC\u2CFD\u2CFE-\u2CFF]")},
    'cuneiform' : {
                'name'  : u"Cuneiform",
                'official' : True,
                'regex' : re.compile(ur"[\U00012000-\U0001236E\U00012400-\U00012462\U00012470-\U00012473]")},
    'cypriot' : {
                'name'  : u"Cypriot",
                'official' : True,
                'regex' : re.compile(ur"[\U00010800-\U00010805\U00010808\U0001080A-\U00010835\U00010837-\U00010838\U0001083C\U0001083F]")},
    'cyrillic' : {
                'name'  : u"Cyrillic",
                'official' : True,
                'regex' : re.compile(ur"[\u0400-\u0484\u0487-\u0489\u048A-\u0527\u1D2B\u1D78\u2DE0-\u2DFF\uA640-\uA66D\uA66E\uA66F\uA670-\uA672\uA673\uA67C-\uA67D\uA67E\uA67F\uA680-\uA697]")},
    'deseret' : {
                'name'  : u"Deseret",
                'official' : True,
                'regex' : re.compile(ur"[\U00010400-\U0001044F]")},
    'devanagari' : {
                'name'  : u"Devanagari",
                'official' : True,
                'regex' : re.compile(ur"[\u0900-\u0939\u093A-\u094F\u0950\u0953-\u0957\u0958-\u0961\u0962-\u0963\u0966-\u096F\u0971\u0972-\u0977\u0979-\u097F\uA8E0-\uA8F1\uA8F2-\uA8F7\uA8F8-\uA8FA\uA8FB]")},
    'egyptianhieroglyphs' : {
                'name'  : u"Egyptian Hieroglyphs",
                'official' : True,
                'regex' : re.compile(ur"[\U00013000-\U0001342E]")},
    'engsvanyali' : {
                'name'  : u"Engsvanyáli",
                'official' : False,
                'regex' : re.compile(ur"[\uE100-\uE14F]")},
    'ethiopic' : {
                'name'  : u"Ethiopic",
                'official' : True,
                'regex' : re.compile(ur"[\u1200-\u1248\u124A-\u124D\u1250-\u1256\u1258\u125A-\u125D\u1260-\u1288\u128A-\u128D\u1290-\u12B0\u12B2-\u12B5\u12B8-\u12BE\u12C0\u12C2-\u12C5\u12C8-\u12D6\u12D8-\u1310\u1312-\u1315\u1318-\u135A\u135D-\u135F\u1360\u1361-\u1368\u1369-\u137C\u1380-\u138F\u1390-\u1399\u2D80-\u2D96\u2DA0-\u2DA6\u2DA8-\u2DAE\u2DB0-\u2DB6\u2DB8-\u2DBE\u2DC0-\u2DC6\u2DC8-\u2DCE\u2DD0-\u2DD6\u2DD8-\u2DDE\uAB01-\uAB06\uAB09-\uAB0E\uAB11-\uAB16\uAB20-\uAB26\uAB28-\uAB2E]")},
    'ewellic' : {
                'name'  : u"Ewellic",
                'official' : False,
                'regex' : re.compile(ur"[\uE680-\uE6CF]")},
    'ferengi' : {
                'name'  : u"Ferengi",
                'official' : False,
                'regex' : re.compile(ur"[\uE600-\uE62F]")},
    'gargoyle' : {
                'name'  : u"Gargoyle",
                'official' : False,
                'regex' : re.compile(ur"[\uE5C0-\uE5DF]")},
    'georgian' : {
                'name'  : u"Georgian",
                'official' : True,
                'regex' : re.compile(ur"[\u10A0-\u10C5\u10C7\u10CD\u10D0-\u10FA\u10FC\u2D00-\u2D25\u10C7\u2D27\u10CD\u2D2D\u10FD-\u10FF]")},
    'glagolitic' : {
                'name'  : u"Glagolitic",
                'official' : True,
                'regex' : re.compile(ur"[\u2C00-\u2C2E\u2C30-\u2C5E]")},
    'glaithaa' : {
                'name'  : u"Glaitha-A",
                'official' : False,
                'regex' : re.compile(ur"[\uE900-\uE97F]")},
    'glaithab' : {
                'name'  : u"Glaitha-B",
                'official' : False,
                'regex' : re.compile(ur"[\uE980-\uE9DF]")},
    'gothic' : {
                'name'  : u"Gothic",
                'official' : True,
                'regex' : re.compile(ur"[\U00010330-\U00010340\U00010341\U00010342-\U00010349\U0001034A]")},
    'greek' : {
                'name'  : u"Greek",
                'official' : True,
                'regex' : re.compile(ur"[\u0370-\u0373\u0375-\u0377\u037A-\u037D\u0384\u0386\u0388-\u038A\u038C\u038E-\u03A1\u03A3-\u03E1\u03F0-\u03F5\u03F6\u03F7-\u03FF\u1D26-\u1D2A\u1D5D-\u1D61\u1D66-\u1D6A\u1DBF\u1F00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC\u1FBD\u1FBE\u1FBF-\u1FC1\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FCD-\u1FCF\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FDD-\u1FDF\u1FE0-\u1FEC\u1FED-\u1FEF\u1FF2-\u1FF4\u1FF6-\u1FFC\u1FFD-\u1FFE\u2126\U00010140-\U00010174\U00010175-\U00010178\U00010179-\U00010189\U0001018A\U0001D200-\U0001D241\U0001D242-\U0001D244\U0001D245]")},
    'gujarati' : {
                'name'  : u"Gujarati",
                'official' : True,
                'regex' : re.compile(ur"[\u0A81-\u0A82\u0A83\u0A85-\u0A8D\u0A8F-\u0A91\u0A93-\u0AA8\u0AAA-\u0AB0\u0AB2-\u0AB3\u0AB5-\u0AB9\u0ABC\u0ABD\u0ABE-\u0AC0\u0AC1-\u0AC5\u0AC7-\u0AC8\u0AC9\u0ACB-\u0ACC\u0ACD\u0AD0\u0AE0-\u0AE1\u0AE2-\u0AE3\u0AE6-\u0AEF\u0AF1]")},
    'gurmukhi' : {
                'name'  : u"Gurmukhi",
                'official' : True,
                'regex' : re.compile(ur"[\u0A01-\u0A02\u0A03\u0A05-\u0A0A\u0A0F-\u0A10\u0A13-\u0A28\u0A2A-\u0A30\u0A32-\u0A33\u0A35-\u0A36\u0A38-\u0A39\u0A3C\u0A3E-\u0A40\u0A41-\u0A42\u0A47-\u0A48\u0A4B-\u0A4D\u0A51\u0A59-\u0A5C\u0A5E\u0A66-\u0A6F\u0A70-\u0A71\u0A72-\u0A74\u0A75]")},
    'hangul' : {
                'name'  : u"Hangul",
                'official' : True,
                'regex' : re.compile(ur"[\u1100-\u11FF\u302E-\u302F\u3131-\u318E\u3200-\u321E\u3260-\u327E\uA960-\uA97C\uAC00-\uD7A3\uD7B0-\uD7C6\uD7CB-\uD7FB\uFFA0-\uFFBE\uFFC2-\uFFC7\uFFCA-\uFFCF\uFFD2-\uFFD7\uFFDA-\uFFDC]")},
    'han' : {
                'name'  : u"Han",
                'official' : True,
                'regex' : re.compile(ur"[\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303A\u303B\u3400-\u4DB5\u4E00-\u9FCC\uF900-\uFA2F\uFA30-\uFA6D\uFA70-\uFAD9\U00020000-\U0002A6D6\U0002A700-\U0002B734\U0002B740-\U0002B81D\U0002F800-\U0002FA1D]")},
    'hanunoo' : {
                'name'  : u"Hanunoo",
                'official' : True,
                'regex' : re.compile(ur"[\u1720-\u1731\u1732-\u1734]")},
    'hebrew' : {
                'name'  : u"Hebrew",
                'official' : True,
                'regex' : re.compile(ur"[\u0591-\u05BD\u05BE\u05BF\u05C0\u05C1-\u05C2\u05C3\u05C4-\u05C5\u05C6\u05C7\u05D0-\u05EA\u05F0-\u05F2\u05F3-\u05F4\uFB1D\uFB1E\uFB1F-\uFB28\uFB29\uFB2A-\uFB36\uFB38-\uFB3C\uFB3E\uFB40-\uFB41\uFB43-\uFB44\uFB46-\uFB4F]")},
    'hiragana' : {
                'name'  : u"Hiragana",
                'official' : True,
                'regex' : re.compile(ur"[\u3041-\u3096\u309D-\u309E\u309F\U0001B001\U0001F200]")},
    'ilianore' : {
                'name'  : u"Ilianore",
                'official' : False,
                'regex' : re.compile(ur"[\uE1B0-\uE1CF]")},
    'imperialaramaic' : {
                'name'  : u"Imperial Aramaic",
                'official' : True,
                'regex' : re.compile(ur"[\U00010840-\U00010855\U00010857\U00010858-\U0001085F]")},
    'noscript' : {
                'name'  : u"noscript",
                'official' : True,
                'regex' : re.compile(ur"[\u0300-\u036F\u0485-\u0486\u064B-\u0655\u065F\u0670\u0951-\u0952\u1CD0-\u1CD2\u1CD4-\u1CE0\u1CE2-\u1CE8\u1CED\u1DC0-\u1DE6\u1DFC-\u1DFF\u200C-\u200D\u20D0-\u20DC\u20DD-\u20E0\u20E1\u20E2-\u20E4\u20E5-\u20F0\u302A-\u302D\u3099-\u309A\uFE00-\uFE0F\uFE20-\uFE26\U000101FD\U0001D167-\U0001D169\U0001D17B-\U0001D182\U0001D185-\U0001D18B\U0001D1AA-\U0001D1AD\U000E0100-\U000E01EF\u1CF3-\u1CF6]")},
    'inscriptionalpahlavi' : {
                'name'  : u"Inscriptional Pahlavi",
                'official' : True,
                'regex' : re.compile(ur"[\U00010B60-\U00010B72\U00010B78-\U00010B7F]")},
    'inscriptionalparthian' : {
                'name'  : u"Inscriptional Parthian",
                'official' : True,
                'regex' : re.compile(ur"[\U00010B40-\U00010B55\U00010B58-\U00010B5F]")},
    'javanese' : {
                'name'  : u"Javanese",
                'official' : True,
                'regex' : re.compile(ur"[\uA980-\uA982\uA983\uA984-\uA9B2\uA9B3\uA9B4-\uA9B5\uA9B6-\uA9B9\uA9BA-\uA9BB\uA9BC\uA9BD-\uA9C0\uA9C1-\uA9CD\uA9CF\uA9D0-\uA9D9\uA9DE-\uA9DF]")},
    'kaithi' : {
                'name'  : u"Kaithi",
                'official' : True,
                'regex' : re.compile(ur"[\U00011080-\U00011081\U00011082\U00011083-\U000110AF\U000110B0-\U000110B2\U000110B3-\U000110B6\U000110B7-\U000110B8\U000110B9-\U000110BA\U000110BB-\U000110BC\U000110BD\U000110BE-\U000110C1]")},
    'kannada' : {
                'name'  : u"Kannada",
                'official' : True,
                'regex' : re.compile(ur"[\u0C82-\u0C83\u0C85-\u0C8C\u0C8E-\u0C90\u0C92-\u0CA8\u0CAA-\u0CB3\u0CB5-\u0CB9\u0CBC\u0CBD\u0CBE\u0CBF\u0CC0-\u0CC4\u0CC6\u0CC7-\u0CC8\u0CCA-\u0CCB\u0CCC-\u0CCD\u0CD5-\u0CD6\u0CDE\u0CE0-\u0CE1\u0CE2-\u0CE3\u0CE6-\u0CEF\u0CF1-\u0CF2]")},
    'katakana' : {
                'name'  : u"Katakana",
                'official' : True,
                'regex' : re.compile(ur"[\u30A1-\u30FA\u30FD-\u30FE\u30FF\u31F0-\u31FF\u32D0-\u32FE\u3300-\u3357\uFF66-\uFF6F\uFF71-\uFF9D\U0001B000]")},
    'kayahli' : {
                'name'  : u"Kayah Li",
                'official' : True,
                'regex' : re.compile(ur"[\uA900-\uA909\uA90A-\uA925\uA926-\uA92D\uA92E-\uA92F]")},
    'kazatakkorou' : {
                'name'  : u"Kazat ?Akkorou",
                'official' : False,
                'regex' : re.compile(ur"[\uE430-\uE44F]")},
    'kazvarad' : {
                'name'  : u"Kazvarad",
                'official' : False,
                'regex' : re.compile(ur"[\uE450-\uE46F]")},
    'kelwathi' : {
                'name'  : u"Kelwathi",
                'official' : False,
                'regex' : re.compile(ur"[\uE4F0-\uE4FF]")},
    'kharoshthi' : {
                'name'  : u"Kharoshthi",
                'official' : True,
                'regex' : re.compile(ur"[\U00010A00\U00010A01-\U00010A03\U00010A05-\U00010A06\U00010A0C-\U00010A0F\U00010A10-\U00010A13\U00010A15-\U00010A17\U00010A19-\U00010A33\U00010A38-\U00010A3A\U00010A3F\U00010A40-\U00010A47\U00010A50-\U00010A58]")},
    'khmer' : {
                'name'  : u"Khmer",
                'official' : True,
                'regex' : re.compile(ur"[\u1780-\u17B3\u17B4-\u17B5\u17B6\u17B7-\u17BD\u17BE-\u17C5\u17C6\u17C7-\u17C8\u17C9-\u17D3\u17D4-\u17D6\u17D7\u17D8-\u17DA\u17DB\u17DC\u17DD\u17E0-\u17E9\u17F0-\u17F9\u19E0-\u19FF]")},
    'kinya' : {
                'name'  : u"Kinya",
                'official' : False,
                'regex' : re.compile(ur"[\uE150-\uE1AF\U000F0000-\U000F0E69]")},
    'klingon' : {
                'name'  : u"Klingon",
                'official' : False,
                'regex' : re.compile(ur"[\uF8D0-\uF8FF]")},
    'lao' : {
                'name'  : u"Lao",
                'official' : True,
                'regex' : re.compile(ur"[\u0E81-\u0E82\u0E84\u0E87-\u0E88\u0E8A\u0E8D\u0E94-\u0E97\u0E99-\u0E9F\u0EA1-\u0EA3\u0EA5\u0EA7\u0EAA-\u0EAB\u0EAD-\u0EB0\u0EB1\u0EB2-\u0EB3\u0EB4-\u0EB9\u0EBB-\u0EBC\u0EBD\u0EC0-\u0EC4\u0EC6\u0EC8-\u0ECD\u0ED0-\u0ED9\u0EDC-\u0EDF]")},
    'latin' : {
                'name'  : u"Latin",
                'official' : True,
                'regex' : re.compile(ur"[\u0041-\u005A\u0061-\u007A\u00AA\u00BA\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u01BA\u01BB\u01BC-\u01BF\u01C0-\u01C3\u01C4-\u0293-\u02AF\u02B0-\u02B8\u02E0-\u02E4\u1D00-\u1D25\u1D2C-\u1D5C\u1D62-\u1D65\u1D6B-\u1D77\u1D79-\u1D9A\u1D9B-\u1DBE\u1E00-\u1EFF\u2071\u207F\u2090-\u209C\u212A-\u212B\u2132\u214E\u2160-\u2182\u2183-\u2184\u2185-\u2188\u2C60-\u2C7C\u2C7D\u2C7E-\u2C7F\uA7AA\uA7F8\uA7F9\uA792\uA793\uA722-\uA76F\uA770\uA771-\uA787\uA78B-\uA78E\uA790-\uA791\uA7A0-\uA7A9\uA7FA\uA7FB-\uA7FF\uFB00-\uFB06\uFF21-\uFF3A\uFF41-\uFF5A]")},
    'lepcha' : {
                'name'  : u"Lepcha",
                'official' : True,
                'regex' : re.compile(ur"[\u1C00-\u1C23\u1C24-\u1C2B\u1C2C-\u1C33\u1C34-\u1C35\u1C36-\u1C37\u1C3B-\u1C3F\u1C40-\u1C49\u1C4D-\u1C4F]")},
    'lhenazi' : {
                'name'  : u"Lhenazi",
                'official' : False,
                'regex' : re.compile(ur"[\uEA00-\uEA9F]")},
    'limbu' : {
                'name'  : u"Limbu",
                'official' : True,
                'regex' : re.compile(ur"[\u1900-\u191C\u1920-\u1922\u1923-\u1926\u1927-\u1928\u1929-\u192B\u1930-\u1931\u1932\u1933-\u1938\u1939-\u193B\u1940\u1944-\u1945\u1946-\u194F]")},
    'linearb' : {
                'name'  : u"Linear B",
                'official' : True,
                'regex' : re.compile(ur"[\U00010000-\U0001000B\U0001000D-\U00010026\U00010028-\U0001003A\U0001003C-\U0001003D\U0001003F-\U0001004D\U00010050-\U0001005D\U00010080-\U000100FA]")},
    'lisu' : {
                'name'  : u"Lisu",
                'official' : True,
                'regex' : re.compile(ur"[\uA4D0-\uA4F7\uA4F8-\uA4FD\uA4FE-\uA4FF]")},
    'lycian' : {
                'name'  : u"Lycian",
                'official' : True,
                'regex' : re.compile(ur"[\U00010280-\U0001029C]")},
    'lydian' : {
                'name'  : u"Lydian",
                'official' : True,
                'regex' : re.compile(ur"[\U00010920-\U00010939\U0001093F]")},
    'malayalam' : {
                'name'  : u"Malayalam",
                'official' : True,
                'regex' : re.compile(ur"[\u0D02-\u0D03\u0D05-\u0D0C\u0D0E-\u0D10\u0D12-\u0D3A\u0D3D\u0D3E-\u0D40\u0D41-\u0D44\u0D46-\u0D48\u0D4A-\u0D4C\u0D4D\u0D4E\u0D57\u0D60-\u0D61\u0D62-\u0D63\u0D66-\u0D6F\u0D70-\u0D75\u0D79\u0D7A-\u0D7F]")},
    'mandaic' : {
                'name'  : u"Mandaic",
                'official' : True,
                'regex' : re.compile(ur"[\u0840-\u0858\u0859-\u085B\u085E]")},
    'meeteimayek' : {
                'name'  : u"Meetei Mayek",
                'official' : True,
                'regex' : re.compile(ur"[\uABC0-\uABE2\uABE3-\uABE4\uABE5\uABE6-\uABE7\uABE8\uABE9-\uABEA\uABEB\uABEC\uABED\uABF0-\uABF9\uAAE0-\uAAFF]")},
    'meroitic' : {
                'name'  : u"Meroitic",
                'official' : True,
                'regex' : re.compile(ur"[\U00010980-\U0001099F\U000109A0-\U000109FF]")},
    'miao' : {
                'name'  : u"Miao",
                'official' : True,
                'regex' : re.compile(ur"[\U00016F00-\U00016F9F]")},
    'mizarian' : {
                'name'  : u"Mizarian",
                'official' : False,
                'regex' : re.compile(ur"[\uE300-\uE33F]")},
    'mongolian' : {
                'name'  : u"Mongolian",
                'official' : True,
                'regex' : re.compile(ur"[\u1800-\u1801\u1804\u1806\u1807-\u180A\u180B-\u180D\u180E\u1810-\u1819\u1820-\u1842\u1843\u1844-\u1877\u1880-\u18A8\u18A9\u18AA]")},
    'monofon' : {
                'name'  : u"Monofon",
                'official' : False,
                'regex' : re.compile(ur"[\uE800-\uE82F]")},
    'myanmar' : {
                'name'  : u"Myanmar",
                'official' : True,
                'regex' : re.compile(ur"[\u1000-\u102A\u102B-\u102C\u102D-\u1030\u1031\u1032-\u1037\u1038\u1039-\u103A\u103B-\u103C\u103D-\u103E\u103F\u1040-\u1049\u104A-\u104F\u1050-\u1055\u1056-\u1057\u1058-\u1059\u105A-\u105D\u105E-\u1060\u1061\u1062-\u1064\u1065-\u1066\u1067-\u106D\u106E-\u1070\u1071-\u1074\u1075-\u1081\u1082\u1083-\u1084\u1085-\u1086\u1087-\u108C\u108D\u108E\u108F\u1090-\u1099\u109A-\u109C\u109D\u109E-\u109F\uAA60-\uAA6F\uAA70\uAA71-\uAA76\uAA77-\uAA79\uAA7A\uAA7B]")},
    'newtailue' : {
                'name'  : u"New Tai Lue",
                'official' : True,
                'regex' : re.compile(ur"[\u1980-\u19AB\u19B0-\u19C0\u19C1-\u19C7\u19C8-\u19C9\u19D0-\u19D9\u19DA\u19DE-\u19DF]")},
    'niskloz' : {
                'name'  : u"Nísklôz",
                'official' : False,
                'regex' : re.compile(ur"[\uE400-\uE42F]")},
    'nko' : {
                'name'  : u"Nko",
                'official' : True,
                'regex' : re.compile(ur"[\u07C0-\u07C9\u07CA-\u07EA\u07EB-\u07F3\u07F4-\u07F5\u07F6\u07F7-\u07F9\u07FA]")},
    'ogham' : {
                'name'  : u"Ogham",
                'official' : True,
                'regex' : re.compile(ur"[\u1680\u1681-\u169A\u169B\u169C]")},
    'olaetyan' : {
                'name'  : u"Olaetyan",
                'official' : False,
                'regex' : re.compile(ur"[\uE3B0-\uE3FF]")},
    'olchiki' : {
                'name'  : u"Ol Chiki",
                'official' : True,
                'regex' : re.compile(ur"[\u1C50-\u1C59\u1C5A-\u1C77\u1C78-\u1C7D\u1C7E-\u1C7F]")},
    'olditalic' : {
                'name'  : u"Old Italic",
                'official' : True,
                'regex' : re.compile(ur"[\U00010300-\U0001031E\U00010320-\U00010323]")},
    'oldpersian' : {
                'name'  : u"Old Persian",
                'official' : True,
                'regex' : re.compile(ur"[\U000103A0-\U000103C3\U000103C8-\U000103CF\U000103D0\U000103D1-\U000103D5]")},
    'oldsoutharabian' : {
                'name'  : u"Old South Arabian",
                'official' : True,
                'regex' : re.compile(ur"[\U00010A60-\U00010A7C\U00010A7D-\U00010A7E\U00010A7F]")},
    'oldturkic' : {
                'name'  : u"Old Turkic",
                'official' : True,
                'regex' : re.compile(ur"[\U00010C00-\U00010C48]")},
    'ophidian' : {
                'name'  : u"Ophidian",
                'official' : False,
                'regex' : re.compile(ur"[\uE5E0-\uE5FF]")},
    'oriya' : {
                'name'  : u"Oriya",
                'official' : True,
                'regex' : re.compile(ur"[\u0B01\u0B02-\u0B03\u0B05-\u0B0C\u0B0F-\u0B10\u0B13-\u0B28\u0B2A-\u0B30\u0B32-\u0B33\u0B35-\u0B39\u0B3C\u0B3D\u0B3E\u0B3F\u0B40\u0B41-\u0B44\u0B47-\u0B48\u0B4B-\u0B4C\u0B4D\u0B56\u0B57\u0B5C-\u0B5D\u0B5F-\u0B61\u0B62-\u0B63\u0B66-\u0B6F\u0B70\u0B71\u0B72-\u0B77]")},
    'osmanya' : {
                'name'  : u"Osmanya",
                'official' : True,
                'regex' : re.compile(ur"[\U00010480-\U0001049D\U000104A0-\U000104A9]")},
    'phagspa' : {
                'name'  : u"Phags Pa",
                'official' : True,
                'regex' : re.compile(ur"[\uA840-\uA873\uA874-\uA877]")},
    'phoenician' : {
                'name'  : u"Phoenician",
                'official' : True,
                'regex' : re.compile(ur"[\U00010900-\U00010915\U00010916-\U0001091B\U0001091F]")},
    'pikto' : {
                'name'  : u"Pikto",
                'official' : False,
                'regex' : re.compile(ur"[\U000F0E70-\U000F16AF]")},
    'rejang' : {
                'name'  : u"Rejang",
                'official' : True,
                'regex' : re.compile(ur"[\uA930-\uA946\uA947-\uA951\uA952-\uA953\uA95F]")},
    'rozhxh' : {
                'name'  : u"Røzhxh",
                'official' : False,
                'regex' : re.compile(ur"[\uE490-\uE4BF]")},
    'runic' : {
                'name'  : u"Runic",
                'official' : True,
                'regex' : re.compile(ur"[\u16A0-\u16EA\u16EE-\u16F0]")},
    'rynnan' : {
                'name'  : u"Rynnan",
                'official' : False,
                'regex' : re.compile(ur"[\uE520-\uE54F]")},
    'saklor' : {
                'name'  : u"Saklor",
                'official' : False,
                'regex' : re.compile(ur"[\uE500-\uE51F]")},
    'samaritan' : {
                'name'  : u"Samaritan",
                'official' : True,
                'regex' : re.compile(ur"[\u0800-\u0815\u0816-\u0819\u081A-\u082D\u0830-\u083E]")},
    'sarkai' : {
                'name'  : u"Sarkai",
                'official' : False,
                'regex' : re.compile(ur"[\uE360-\uE37F]")},
    'saurashtra' : {
                'name'  : u"Saurashtra",
                'official' : True,
                'regex' : re.compile(ur"[\uA880-\uA881\uA882-\uA8B3\uA8B4-\uA8C3\uA8C4\uA8CE-\uA8CF\uA8D0-\uA8D9]")},
    'serivelna' : {
                'name'  : u"Serivelna",
                'official' : False,
                'regex' : re.compile(ur"[\uE4C0-\uE4EF]")},
    'seussian' : {
                'name'  : u"Latin",
                'official' : False,
                'regex' : re.compile(ur"[ Latin\uE630-\uE64F]")},
    'sharada' : {
                'name'  : u"Sharada",
                'official' : True,
                'regex' : re.compile(ur"[\U00011180-\U000111DF]")},
    'shavian' : {
                'name'  : u"Shavian",
                'official' : True,
                'regex' : re.compile(ur"[\U00010450-\U0001047F]")},
    'sinhala' : {
                'name'  : u"Sinhala",
                'official' : True,
                'regex' : re.compile(ur"[\u0D82-\u0D83\u0D85-\u0D96\u0D9A-\u0DB1\u0DB3-\u0DBB\u0DBD\u0DC0-\u0DC6\u0DCA\u0DCF-\u0DD1\u0DD2-\u0DD4\u0DD6\u0DD8-\u0DDF\u0DF2-\u0DF3\u0DF4]")},
    'solresol' : {
                'name'  : u"Solresol",
                'official' : False,
                'regex' : re.compile(ur"[\uE770-\uE77F]")},
    'sorasompeng' : {
                'name'  : u"Sora Sompeng",
                'official' : True,
                'regex' : re.compile(ur"[\U000110D0-\U000110FF]")},
    'ssuraki' : {
                'name'  : u"Ssûraki",
                'official' : False,
                'regex' : re.compile(ur"[\uE5A0-\uE5BF]")},
    'streich' : {
                'name'  : u"Streich",
                'official' : False,
                'regex' : re.compile(ur"[\uE2D0-\uE2DF]")},
    'sundanese' : {
                'name'  : u"Sundanese",
                'official' : True,
                'regex' : re.compile(ur"[\u1B80-\u1B81\u1B82\u1B83-\u1BA0\u1BA1\u1BA2-\u1BA5\u1BA6-\u1BA7\u1BA8-\u1BA9\u1BAD\u1BAE-\u1BAF\u1BB0-\u1BB9\u1BBA-\u1BBF\u1CC0-\u1CCF]")},
    'syai' : {
                'name'  : u"Syai",
                'official' : False,
                'regex' : re.compile(ur"[\uE1D0-\uE1FF]")},
    'sylotinagri' : {
                'name'  : u"Syloti Nagri",
                'official' : True,
                'regex' : re.compile(ur"[\uA800-\uA801\uA802\uA803-\uA805\uA806\uA807-\uA80A\uA80B\uA80C-\uA822\uA823-\uA824\uA825-\uA826\uA827\uA828-\uA82B]")},
    'syriac' : {
                'name'  : u"Syriac",
                'official' : True,
                'regex' : re.compile(ur"[\u0700-\u070D\u070F\u0710-\u072F\u0730-\u074A\u074D-\u074F]")},
    'tagalog' : {
                'name'  : u"Tagalog",
                'official' : True,
                'regex' : re.compile(ur"[\u1700-\u170C\u170E-\u1711\u1712-\u1714]")},
    'tagbanwa' : {
                'name'  : u"Tagbanwa",
                'official' : True,
                'regex' : re.compile(ur"[\u1760-\u176C\u176E-\u1770\u1772-\u1773]")},
    'taile' : {
                'name'  : u"Tai Le",
                'official' : True,
                'regex' : re.compile(ur"[\u1950-\u196D\u1970-\u1974]")},
    'taitham' : {
                'name'  : u"Tai Tham",
                'official' : True,
                'regex' : re.compile(ur"[\u1A20-\u1A54\u1A55\u1A56\u1A57\u1A58-\u1A5E\u1A60\u1A61\u1A62\u1A63-\u1A64\u1A65-\u1A6C\u1A6D-\u1A72\u1A73-\u1A7C\u1A7F\u1A80-\u1A89\u1A90-\u1A99\u1AA0-\u1AA6\u1AA7\u1AA8-\u1AAD]")},
    'taiviet' : {
                'name'  : u"Tai Viet",
                'official' : True,
                'regex' : re.compile(ur"[\uAA80-\uAAAF\uAAB0\uAAB1\uAAB2-\uAAB4\uAAB5-\uAAB6\uAAB7-\uAAB8\uAAB9-\uAABD\uAABE-\uAABF\uAAC0\uAAC1\uAAC2\uAADB-\uAADC\uAADD\uAADE-\uAADF]")},
    'takri' : {
                'name'  : u"Takri",
                'official' : True,
                'regex' : re.compile(ur"[\U00011680-\U000116CF]")},
    'tamil' : {
                'name'  : u"Tamil",
                'official' : True,
                'regex' : re.compile(ur"[\u0B82\u0B83\u0B85-\u0B8A\u0B8E-\u0B90\u0B92-\u0B95\u0B99-\u0B9A\u0B9C\u0B9E-\u0B9F\u0BA3-\u0BA4\u0BA8-\u0BAA\u0BAE-\u0BB9\u0BBE-\u0BBF\u0BC0\u0BC1-\u0BC2\u0BC6-\u0BC8\u0BCA-\u0BCC\u0BCD\u0BD0\u0BD7\u0BE6-\u0BEF\u0BF0-\u0BF2\u0BF3-\u0BF8\u0BF9\u0BFA]")},
    'telarasso' : {
                'name'  : u"Telarasso",
                'official' : False,
                'regex' : re.compile(ur"[\uE580-\uE59F]")},
    'telugu' : {
                'name'  : u"Telugu",
                'official' : True,
                'regex' : re.compile(ur"[\u0C01-\u0C03\u0C05-\u0C0C\u0C0E-\u0C10\u0C12-\u0C28\u0C2A-\u0C33\u0C35-\u0C39\u0C3D\u0C3E-\u0C40\u0C41-\u0C44\u0C46-\u0C48\u0C4A-\u0C4D\u0C55-\u0C56\u0C58-\u0C59\u0C60-\u0C61\u0C62-\u0C63\u0C66-\u0C6F\u0C78-\u0C7E\u0C7F]")},
    'tengwar' : {
                'name'  : u"Tengwar",
                'official' : False,
                'regex' : re.compile(ur"[\uE000-\uE07F]")},
    'thaana' : {
                'name'  : u"Thaana",
                'official' : True,
                'regex' : re.compile(ur"[\u0780-\u07A5\u07A6-\u07B0\u07B1]")},
    'thai' : {
                'name'  : u"Thai",
                'official' : True,
                'regex' : re.compile(ur"[\u0E01-\u0E30\u0E31\u0E32-\u0E33\u0E34-\u0E3A\u0E40-\u0E45\u0E46\u0E47-\u0E4E\u0E4F\u0E50-\u0E59\u0E5A-\u0E5B]")},
    'thelwik' : {
                'name'  : u"Thelwik",
                'official' : False,
                'regex' : re.compile(ur"[\uE380-\uE3AF]")},
    'tibetan' : {
                'name'  : u"Tibetan",
                'official' : True,
                'regex' : re.compile(ur"[\u0F00\u0F01-\u0F03\u0F04-\u0F12\u0F13-\u0F17\u0F18-\u0F19\u0F1A-\u0F1F\u0F20-\u0F29\u0F2A-\u0F33\u0F34\u0F35\u0F36\u0F37\u0F38\u0F39\u0F3A\u0F3B\u0F3C\u0F3D\u0F3E-\u0F3F\u0F40-\u0F47\u0F49-\u0F6C\u0F71-\u0F7E\u0F7F\u0F80-\u0F84\u0F85\u0F86-\u0F87\u0F88-\u0F8C\u0F8D-\u0F97\u0F99-\u0FBC\u0FBE-\u0FC5\u0FC6\u0FC7-\u0FCC\u0FCE-\u0FCF\u0FD0-\u0FD4\u0FD9-\u0FDA]")},
    'tifinagh' : {
                'name'  : u"Tifinagh",
                'official' : True,
                'regex' : re.compile(ur"[\u2D30-\u2D67\u2D6F\u2D70\u2D7F]")},
    'ugaritic' : {
                'name'  : u"Ugaritic",
                'official' : True,
                'regex' : re.compile(ur"[\U00010380-\U0001039D\U0001039F]")},
    'unifon' : {
                'name'  : u"Unifon",
                'official' : False,
                'regex' : re.compile(ur"[\uE740-\uE76F]")},
    'vai' : {
                'name'  : u"Vai",
                'official' : True,
                'regex' : re.compile(ur"[\uA500-\uA60B\uA60C\uA60D-\uA60F\uA610-\uA61F\uA620-\uA629\uA62A-\uA62B]")},
    'verdurian' : {
                'name'  : u"Verdurian",
                'official' : False,
                'regex' : re.compile(ur"[\uE200-\uE26F]")},
    'visiblespeech' : {
                'name'  : u"Visible Speech",
                'official' : False,
                'regex' : re.compile(ur"[\uE780-\uE7FF]")},
    'xaini' : {
                'name'  : u"Xaîni",
                'official' : False,
                'regex' : re.compile(ur"[\uE2E0-\uE2FF]")},
    'yi' : {
                'name'  : u"Yi",
                'official' : True,
                'regex' : re.compile(ur"[\uA000-\uA014\uA015\uA016-\uA48C\uA490-\uA4C6]")},
    'zarkhand' : {
                'name'  : u"Zarkhánd",
                'official' : False,
                'regex' : re.compile(ur"[\uE470-\uE48F]")},
    'zirinka' : {
                'name'  : u"Zírí:Nka",
                'official' : False,
                'regex' : re.compile(ur"[\uE340-\uE35F]")}
}

def func_p(parser, teststr, onlyofficial = False):
    try:
        if teststr is not None :
            testchar = teststr
            for script in scripts['scripts'] :
                match = scripts[script]['regex'].match(testchar)
                if match :
                    if scripts[script]['official'] == False :
                        if onlyofficial :
                            return "Common or Unknown"
                        else :
                            return script
                    else :
                        return script
    except ValueError:
        pass
    return "Common or Unknown"

register_script_function(func_p, "p")
