'''
在这里定义了可能会用到的常量
'''

'''
是否更新LiveScores文件
'''
UpdateLiveScores = False


'''
路径和文件名
'''
Dir_Root = 'E:\\WhoScoredRoot\\'
Fn_LiveScores = 'LiveScores.txt'


'''
url
'''
Url_League = {
    'Brazil_LigaDoBrasil' : '/Regions/31/Tournaments/95/Seasons/4185',
	'England_BarclaysPL' : '/Regions/252/Tournaments/2/Seasons/3853',
	'England_FLChampionship' : '/Regions/252/Tournaments/7/Seasons/3859/Stages/7800',
	'France_Ligue1' : '/Regions/74/Tournaments/22/Seasons/3836',
	'Germany_Bundesliga' : '/Regions/81/Tournaments/3/Seasons/3863',
	'Italy_SerieA' : '/Regions/108/Tournaments/5/Seasons/3978',
	'Netherlands_Eredivisie' : '/Regions/155/Tournaments/13/Seasons/3851/Stages/7790',
	'Russia_RussianLeague' : '/Regions/182/Tournaments/77/Seasons/3861',
	'Spain_LigaBBVA' : '/Regions/206/Tournaments/4/Seasons/3922',
	'USA_MLS' : '/Regions/233/Tournaments/85/Seasons/4091'
	}
Url_WhoScored_Home = 'http://www.whoscored.com'
Url_WhoScored_LiveStat = '/LiveStatistics'
Url_WhoScored_Match = 'http://www.whoscored.com/Matches/'


'''
编码和伪装成浏览量所需的Header
'''
Encoding_WhoScored = 'utf-8'
Header_Mozilla = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}


'''
正则表达式
'''
Regex_FN_Match = '(?:\d+)'
Regex_Match = '(?:<a).*?(?:id=\"(?P<ID>\d+)\"\stitle=\"(?P<HomeTeam>\w+?\s?\w+)\s(?P<Score>\d+\S\d+)\s(?P<AwayTeam>\w+?\s?\w+))(?:\"\/>)'
Regex_Standing = '(?:DataStore\.prime\(\'standings\'[\s\S]).*?(?:\)\;)'