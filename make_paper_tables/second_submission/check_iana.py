import json
import glob
#from iso3166 import countries
from language_tags import *

"""
{'de': {'0': {'c': 92, 'i': 422}, '1': {'c': 425, 'i': 723}, '3': {'c': 2475, 'i': 256}, '6': {'c': 308, 'i': 2}, '7': {'c': 89, 'i': 1}, '5': {'c': 305, 'i': 2}, '8': {'c': 5}, '4': {'c': 787, 'i': 5}, '2': {'c': 1641, 'i': 797}}, 'en': {'0': {'c': 1, 'i': 184}, '1': {'c': 135, 'i': 849}, '3': {'c': 1611, 'i': 1516}, '6': {'c': 350}, '7': {'c': 144}, '5': {'c': 303, 'i': 7}, '8': {'c': 8}, '4': {'c': 901, 'i': 202}, '2': {'c': 690, 'i': 1466}}, 'fr': {'0': {'c': 31, 'i': 164}, '1': {'c': 397, 'i': 365}, '3': {'c': 2843, 'i': 328}, '6': {'c': 365, 'i': 3}, '7': {'c': 153, 'i': 1}, '5': {'c': 293, 'i': 2}, '8': {'c': 11}, '4': {'c': 1557, 'i': 30}, '2': {'c': 1352, 'i': 458}}}
"""

def getJson():
	counter=0
	langsCountJson={}
	for f in glob.glob('../../tika/*.json'):
		o=open(f, 'r')
		j=json.load(o)
		tagged=j["tagged"]	
		for lang in tagged:
			num=0
			for bucket in tagged[lang]:
				for c_i in ['c', 'i']:
					if c_i in tagged[lang][bucket]:
						num+=tagged[lang][bucket][c_i]
			if lang in langsCountJson:
				langsCountJson[lang]+=num
			else:
				langsCountJson[lang]=num
		counter+=1
		if counter%10000==0:
			print(counter, "files elapsed")
	print(langsCountJson)

def sortByValue(d):
	return sorted(d.items(), key=lambda t:t[1], reverse=True)

myJson={'dv': 1790, 'pe': 7, 'kb': 3087, 'nm': 291, 'go': 401, 'sk': 11461764, 'it': 105248217, 'pa': 448333, 'ig': 24647, 'gs': 80119, 'om': 23049, 'vo': 5257396, 'kr': 4739, 'hs': 31627, 'xa': 12723, 'fa': 22710647, 'bu': 30185, 'vu': 291, 'yp': 1, 'lt': 8819932, 'ew': 291, 'mi': 596182, 'xu': 3, 'ko': 15031558, 'eo': 7405999, 'zs': 523, 'ha': 53642, 'mh': 19582, 'va': 577, 'kw': 94521, 'bl': 4, 'as': 105004, 'eb': 291, 'lz': 22067, 'bh': 23885, 'gn': 28557, 'di': 23396, 'un': 98, 'sl': 7417142, 'bx': 13173, 'cy': 1663827, 'kk': 7609848, 'mn': 68354, 'cg': 289, 'an': 1989898, 'be': 4550851, 'ch': 45843, 'kl': 28774, 'lo': 68375, 'id': 12487878, 'na': 91639, 'ty': 3700, 'el': 5126659, 'si': 88388, 'ug': 30053, 'rw': 6349, 'yi': 200553, 'en': 965493615, 'xh': 1646, 'sy': 24, 'zx': 848, 'mr': 1353675, 'ps': 34391, 'ik': 2175, 'av': 26550, 'dt': 18, 'lg': 1462, 'fu': 32989, 'in': 1035561, 'sg': 50869, 'uk': 20325656, 'me': 291, 'jg': 110, 'to': 3636, 'sb': 291, 'rs': 1, 'ku': 2737419, 'ii': 147, 'dy': 174, 'bo': 28126, 'ra': 3, 'la': 3669687, 'vr': 15809, 'lk': 14, 'qq': 1331, 'ma': 865, 'kh': 307, 'ge': 754, 'ms': 9257497, 'aa': 172, 'tr': 12141055, 'iw': 1103397, 'tp': 12963, 'ke': 468, 'cr': 36665, 'gc': 391, 'ur': 1101028, 'st': 34427, 'lu': 887, 'tc': 26, 'su': 611555, 'km': 32972, 'nb': 8106713, 'cz': 41, 'xo': 290, 'is': 2164673, 'sd': 22730, 'sr': 11375388, 'ky': 188479, 'ny': 1312, 'ri': 26, 'te': 1055067, 'cp': 52, 'au': 16, 'ne': 2103083, 'sc': 242021, 'ab': 24401, 'ag': 291, 'tw': 23210, 'wu': 22268, 'zu': 56396, 'af': 1438738, 'es': 83714010, 'hu': 16715115, 'nn': 13276516, 'li': 103132, 'pd': 3084, 'ck': 1191661, 'vm': 9507, 'e': 1, 'no': 12470512, 'ng': 118, 'tk': 31572, 'th': 5277923, 'vi': 28206001, 'wa': 1741776, 'os': 57307, 'kv': 13441, 'ns': 13147, 'cs': 20118083, 'nu': 117, 'ca': 22092247, 'jb': 2663, 'hi': 3554476, 'io': 875074, 'dk': 16, 'ak': 23930, 'sm': 1223, 'ga': 948152, 'cn': 292, 'ks': 24021, 'ai': 43, 'fj': 22397, 'kn': 496155, 'gd': 222924, 'us': 1943, 'tz': 293, 'il': 1041376, 'ac': 18917, 'dz': 919, 'al': 1522, 'hr': 8665740, 'he': 8704835, 'sn': 4436, 'cd': 13490, 'lb': 1197391, 'wo': 35032, 'ki': 22802, 'ht': 2472892, 'po': 137, 'gl': 7547811, 'yo': 854500, 'nr': 357, 'pl': 60775079, 'jm': 291, 'mu': 544, 'bb': 42, 'lv': 3388696, 'bp': 31739, 'md': 13369, 'za': 23231, 'ee': 24522, 'so': 32098, 'ir': 33, 'x-': 155782, 'ud': 5684, 'eg': 112, 'ro': 12915609, 'iu': 1398, 'ti': 1395, 'ia': 380435, 'pt': 57490705, 'bq': 24, 'fy': 553910, 'sh': 383459, 'pr': 4819, 'se': 90458, 'on': 4, 'ae': 21, 'ph': 7, 'br': 1512165, 'gm': 9, 'tt': 1397913, 'we': 15, 'bg': 8836414, 'fr': 131325395, 'fk': 460, 'fi': 23392899, 'ts': 23139, 'da': 14512594, 'mt': 75366, 'pi': 23496, 'sa': 65969, 'ba': 1044178, 'lr': 1, 'et': 7579695, 'vl': 23568, 'qw': 4, 'jp': 119, 'ju': 26, 'oc': 4562855, 'nl': 76313247, 'pf': 3025, 'uz': 4873992, 'rg': 4815, 'cm': 2066, 'ta': 2324983, 'hz': 47, 'ce': 1647329, 'sp': 313, 'rn': 1410, 'xm': 20641, 'nv': 8393, 'pm': 97898, 'hy': 1812154, 'ni': 15, 'am': 226606, 'ka': 3381920, 'by': 289, 'n': 20, 'bj': 18160, 'jr': 1, 'zh': 41904888, 'cb': 13943, 'tn': 22921, 'jv': 2286416, 'yu': 67729, 'ex': 22434, 'mw': 18208, 'ui': 1, 'gu': 1133190, 'mo': 5444, 'az': 3860387, 'lm': 69622, 'sw': 1247380, 'eu': 8477012, 'sv': 48482727, 'ua': 26, 'qu': 706303, 'nd': 1546285, 'co': 80648, 'hb': 37, 'wi': 31, 'ie': 58114, 'mg': 1132047, 'ml': 1636943, 'mk': 8975058, 'ya': 289, 'tl': 18828622, 'ds': 20368, 'ja': 43772334, 'tg': 388690, 'my': 821633, 'ze': 4905, 'ay': 30042, 'ru': 78762005, 'sz': 10193, 'bs': 1977536, 'bm': 31360, 'ff': 22816, 'le': 3299, 'ic': 496, 'mf': 291, 'em': 24909, 'ar': 10012760, 'fo': 56420, 'kg': 54592, 'ss': 1336, 'kd': 291, 'dj': 290, 'bi': 22839, 'mz': 25311, 'kj': 55, 'tu': 472, 'lf': 67, 'bc': 24805, 'xl': 2, 'bn': 6416615, 'gv': 109198, 'pc': 20557, 'rm': 90565, 'pn': 54846, 'cu': 24900, 'ot': 313, 'ln': 28446, 'gr': 2142, 'cv': 427922, 'de': 147310169, 've': 55821, 'sq': 1860464, 'ho': 44, 'or': 666182, 'du': 155}

inIANA={}
notInIANA={}

for l in myJson:
	if tags.tag(l).language:
		inIANA[l]=myJson[l]
	else:
		notInIANA[l]=myJson[l]

print("Languages in IANA ", len(inIANA))
print("LTS in IANA", sum(inIANA.values()))
print("In IANA - sorted by value", sortByValue(inIANA))
print("Languages outside IANA", len(notInIANA))
print("LTS outside IANA", sum(notInIANA.values()))
print("Outside IANA - sorted by value", sortByValue(notInIANA))

