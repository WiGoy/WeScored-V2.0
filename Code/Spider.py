'''
下载LiveScores和所有Match的页面
'''
import os, re, time, urllib.request
import Global
import Analyzer_LiveScores
from ThreadPool import ThreadPool


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
	dir = params[0]
	fileName = params[1]
	url = params[2]
	info = params[3]
	
	try:
		req = urllib.request.Request(url = url, headers = Global.Header_Mozilla)
		page = urllib.request.urlopen(req)
		text = page.read().decode(Global.Encoding_WhoScored)
		page.close()
		
		#  delete(replace) newline
		text = text.replace('\r\n', '')
		text = text.replace('\n', '')
		
		EnsureDirectory(dir)
		fileLiveScores = open(dir + '\\' + fileName, 'w', encoding = Global.Encoding_WhoScored)
		fileLiveScores.write(text)
		fileLiveScores.close()
		print(info)
		
	except Exception as e:
		print(e)
		return 0

		
def GetLiveScoresPage():
	'''
	更新（抓取）所有目标联赛的LiveScores页面
	'''
	tp = ThreadPool()
	print('Start updating LiveScores pages...')
	
	for (key, value) in Global.Url_League.items():
		dirLeague = Global.Dir_Root + key
		urlLeague = Global.Url_WhoScored_Home + value
		info = key + ' downloading complete!'
		tp.add_job(GetPageText, dirLeague, Global.Fn_LiveScores, urlLeague, info)
	
	tp.wait_for_complete()
	print('Updating complete!')


def GetMatchPage(league, matches):
	'''
	获取指定联赛的Match页面
	'''
	tp = ThreadPool()
	print('Start updating ' + league + ' matches...')
	dirLeague = Global.Dir_Root + league
	
	for key in sorted(matches.keys()):
		
		fnMatch = '\\' + key + '.txt'
		urlMatch = matches.get(key)
		info = 'Match ' + key + ' downloading complete!'
		tp.add_job(GetPageText, dirLeague, fnMatch, urlMatch, info)
		
	tp.wait_for_complete()
	print(league + ' updating complete!')

		
def GetOriginalMatchID(league):
	'''
	获取指定联赛已下载的MatchID（有对应txt文件且大于1024b）
	'''
	originalMatchID = []
	dirLeague = Global.Dir_Root + league
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
	MatchesNeedToDownload = {}
	MatchesOriginal = GetOriginalMatchID(league)
	MatchesAll = Analyzer_LiveScores.GetMatchID(league)
	
	for key in MatchesAll.keys():
		bOriginal = False
		
		for matchOriginal in MatchesOriginal:
			if key == matchOriginal:
				bOriginal = True
				break
		
		if not bOriginal:
			MatchesNeedToDownload[key] = MatchesAll.get(key)
			
	return MatchesNeedToDownload


def test_job(params):
	
	dirLeague = params[0]
	match = params[1]
	url = params[2]
	
	fnMatch = '\\' + match + '.txt'
	print(url)
	
	fileMatch = open(dirLeague + fnMatch, 'w', encoding = Global.Encoding_WhoScored)
	fileMatch.write(GetPageText(url))
	fileMatch.close()
	
	
def test(league):
	
	matches = GetMatchID(league)
	dirLeague = Global.Dir_Root + league
	EnsureDirectory(dirLeague)
	
	print('Start downloading...')
	tp = ThreadPool()
	
	for key in sorted(matches.keys()):
		tp.add_job(test_job, dirLeague, key, matches.get(key))
	
	tp.wait_for_complete()
	print('End downloading!')


if __name__ == '__main__':
	'''
	自动抓取所有目标联赛
	'''
	t = time.time()
	if Global.UpdateLiveScores:
		GetLiveScoresPage()
	
	for (key, value) in Global.Url_League.items():
		matches = GetMatchID(key)
		GetMatchPage(key, matches)
	
	print('s:'+str(time.time()-t))