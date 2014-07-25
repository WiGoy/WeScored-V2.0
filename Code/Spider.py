'''
下载LiveScores和所有Match的页面
'''
import os, re, urllib.request
import Global
import Analyzer_LiveScores


def EnsureDirectory(dir):
	'''
	判断路径是否存在，不存在就新建
	'''
	if not os.path.isdir(dir):
		os.makedirs(dir)
	
	
def GetPageText(url):
	'''
	从网页抓取Html
	'''
	req = urllib.request.Request(url = url, headers = Global.Header_Mozilla)
	
	try:
		page = urllib.request.urlopen(req)
		text = page.read().decode(Global.Encoding_WhoScored)
		page.close()
		
		#  delete(replace) newline
		text = text.replace('\r\n', '')
		text = text.replace('\n', '')
		return text
		
	except Exception as e:
		print(e)
		return 0

		
def GetLiveScoresPage():
	'''
	更新（抓取）所有目标联赛的LiveScores页面
	'''
	for (key, value) in Global.Url_League.items():
		dirLeague = Global.Dir_Root + key
		urlLeague = Global.Url_WhoScored_Home + value
		
		EnsureDirectory(dirLeague)
		fileLiveScores = open(dirLeague + '\\' + Global.Fn_LiveScores, 'w', encoding = Global.Encoding_WhoScored)
		fileLiveScores.write(GetPageText(urlLeague))
		fileLiveScores.close()
		
		print(key + ' downloading complete!')


def GetMatchPage(league, matches):
	'''
	获取指定联赛的Match页面
	'''
	dirLeague = Global.Dir_Root + league
	
	for key in sorted(matches.keys()):
		
		fnMatch = '\\' + key + '.txt'
		urlMatch = matches.get(key)
		print(urlMatch)
		
		EnsureDirectory(dirLeague)
		fileMatch = open(dirLeague + fnMatch, 'w', encoding = Global.Encoding_WhoScored)
		fileMatch.write(GetPageText(urlMatch))
		fileMatch.close()

		
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
	
		
if __name__ == '__main__':
	'''
	自动抓取所有目标联赛
	'''
	if Global.UpdateLiveScores:
		GetLiveScoresPage()
	
	for (key, value) in Global.Url_League.items():
		print(key)
		matches = GetMatchID(key)
		GetMatchPage(key, matches)