# GEProvider.py
# hansololz HanSeoulOh
# han-duo
import mechanize
import json


C_CURDATASOURCE = """http://services.runescape.com/m=itemdb_rs/api/"""
C_HISTORICALDATASOURCEBEGIN = """http://runescape.wikia.com/wiki/Module:Exchange/"""
C_HISTORICALDATASOURCEEND = """/Data"""
# {"types":[],"alpha":[{"letter":"#","items":0},
# {"letter":"a","items":6},{"letter":"b","items":10},
# {"letter":"c","items":6},{"letter":"d","items":4},
# {"letter":"e","items":0},{"letter":"f","items":0},
# {"letter":"g","items":1},{"letter":"h","items":2},
# {"letter":"i","items":5},{"letter":"j","items":0},
# {"letter":"k","items":1},{"letter":"l","items":1},
# {"letter":"m","items":9},{"letter":"n","items":0},
# {"letter":"o","items":25},{"letter":"p","items":0},
# {"letter":"q","items":0},{"letter":"r","items":6},
# {"letter":"s","items":5},{"letter":"t","items":2},
# {"letter":"u","items":0},{"letter":"v","items":1},
# {"letter":"w","items":1},{"letter":"x","items":0},
# {"letter":"y","items":0},{"letter":"z","items":0}]}
def JSONtoDict(JSON):



def getHistoricalDataUrl(itemname):
	return """{wikibegin}{itemname}{wikiend}""".format(
		wikibegin = C_HISTORICALDATASOURCEBEGIN,
		itemname = itemname,
		wikiend = C_HISTORICALDATASOURCEEND)

def retrieveCurData(url): #return JSON
	br = mechanize.Browser()
	response = br.open(url)
	content = response.get_data()
	return content

