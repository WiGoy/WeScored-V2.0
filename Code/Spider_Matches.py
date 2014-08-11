'''
下载LiveScores和所有Match的页面
'''
import os, re, time, urllib.request
import Global
import Analyzer_LiveScores
from ThreadPool import ThreadPool

MatchNumber_Completed = 0
MatchNumber_Total = 0

def EnsureDirectory(dir):
	'''
	判断路径是否存在，不存在就新建
	'''
	if not os.path.isdir(dir):
		os.makedirs(dir)
	
	
def GetPageText(params):
	'''
	从网页抓取Html，并写入目标路径的文件
	'''
	global MatchNumber_Completed
	global MatchNumber_Total
	dir = params[0]
	matchID = params[1]
	url = params[2]
	
	try:
		req = urllib.request.Request(url = url, headers = Global.Header_Mozilla)
		page = urllib.request.urlopen(req)
		text = page.read().decode(Global.Encoding_WhoScored)
		page.close()
		
		#  delete(replace) newline
		text = text.replace('\r\n', '')
		text = text.replace('\n', '')
		
		EnsureDirectory(dir)
		fileLiveScores = open(dir + '\\' + matchID + '.txt', 'w', encoding = Global.Encoding_WhoScored)
		fileLiveScores.write(text)
		fileLiveScores.close()
		
		MatchNumber_Completed += 1
		print('Match ' + matchID + ' downloading success! ( ' + str(MatchNumber_Completed) + ' / ' + str(MatchNumber_Total) + ' )', end = '\r')

	except Exception as e:
		print('Match ' + matchID + ' downloading failure! ( ' + str(MatchNumber_Completed) + ' / ' + str(MatchNumber_Total) + ' )', end = '\r')


def GetMatchPage(league, matches):
	'''
	获取指定联赛的Match页面
	'''
	tp = ThreadPool()
	print('Start updating ' + league + ' matches...')
	dirLeague = Global.Dir_Root_1415 + league
	
	for matchID in sorted(matches.keys()):
		urlMatch = matches.get(matchID)
		tp.add_job(GetPageText, dirLeague, matchID, urlMatch, len(matches))
	
	tp.wait_for_complete()
	
	if len(matches) > 0:
		print('\n' +league + ' updating complete!\n')
	else:
		print(league + ' updating complete!\n')

		
def GetOriginalMatchID(league):
	'''
	获取指定联赛已下载的MatchID（有对应txt文件且大于1024b）
	'''
	originalMatchID = []
	dirLeague = Global.Dir_Root_1415 + league
	Re_FN_Match = re.compile(Global.Regex_FN_Match, re.I)
	
	#  Add match id in original match id list
	for root, dirs, files in os.walk(dirLeague):
		for fn in files:
			if fn != Global.Fn_LiveScores and os.path.getsize(os.path.join(root, fn)) > 1024:
				originalMatchID.append(Re_FN_Match.findall(fn)[0])
	
	return originalMatchID
	
	
def GetMatchID(league):
	'''
	通过对比，获取指定联赛尚未抓取的MatchID
	'''
	global MatchNumber_Completed
	global MatchNumber_Total
	MatchesNeedToDownload = {}
	MatchesOriginal = GetOriginalMatchID(league)
	MatchesAll = Analyzer_LiveScores.GetMatchID(league)
	
	MatchNumber_Completed = len(MatchesOriginal)
	MatchNumber_Total = len(MatchesAll)
	
	for key in MatchesAll.keys():
		bOriginal = False
		
		for matchOriginal in MatchesOriginal:
			if key == matchOriginal:
				bOriginal = True
				break
		
		if not bOriginal:
			MatchesNeedToDownload[key] = MatchesAll.get(key)
			
	return MatchesNeedToDownload


if __name__ == '__main__':
	'''
	自动抓取所有目标联赛
	'''
	t = time.time()
	
	for league in Global.Url_League_1415.keys():
		matches = GetMatchID(league)
		GetMatchPage(league, matches)
	
	print('s:'+str(time.time()-t))