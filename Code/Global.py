'''
在这里定义了可能会用到的常量
'''


'''
路径和文件名
'''
Dir_Root = 'E:\\WhoScoredRoot\\'
Fn_LiveScores = 'LiveScores.txt'


'''
url
'''
Url_League = {
#	'Brazil_LigaDoBrasil' : '/tournamentsfeed/8677/Fixtures/?d=',
	'England_BarclaysPL' : '/tournamentsfeed/7794/Fixtures/?d=',
	'England_FLChampionship' : '/tournamentsfeed/7800/Fixtures/?d=',
	'France_Ligue1' : '/tournamentsfeed/7771/Fixtures/?d=',
	'Germany_Bundesliga' : '/tournamentsfeed/7806/Fixtures/?d=',
	'Italy_SerieA' : '/tournamentsfeed/8019/Fixtures/?d=',
	'Netherlands_Eredivisie' : '/tournamentsfeed/7790/Fixtures/?d=',
	'Russia_RussianLeague' : '/tournamentsfeed/7803/Fixtures/?d=',
	'Spain_LigaBBVA' : '/tournamentsfeed/7920/Fixtures/?d='
#	'USA_MLS' : '/tournamentsfeed/8358/Fixtures/?d='
	}
Url_Request_Suffix = '&isAggregate=false'
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
Regex_Match = '(?<=\[)(?P<ID>\d+).*?(?:\])'