# GEProvider.py
# hansololz HanSeoulOh
# han-duo


C_CURDATASOURCE = """http://services.runescape.com/m=itemdb_rs/api/"""
C_HISTORICALDATASOURCEBEGIN = """http://runescape.wikia.com/wiki/Module:Exchange/"""
C_HISTORICALDATASOURCEEND = """/Data"""


def getHistoricalDataUrl(itemname):
	return """{wikibegin}{itemname}{wikiend}""".format(
		wikibegin = C_HISTORICALDATASOURCEBEGIN,
		itemname = itemname,
		wikiend = C_HISTORICALDATASOURCEEND)


getHistoricalDataUrl("test")