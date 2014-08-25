'''
生成所有联赛的LiveScores信息
'''
import datetime, os, time, urllib.request
import Global


def DateBefore(year, week):
	'''
	判断是否大于当前日期
	'''
	nowYear = int(time.strftime("%Y",time.localtime()))
	nowWeek = int(time.strftime("%W",time.localtime()))
	
	if int(year[0:4]) < nowYear:
		return True
	elif int(year[0:4]) == nowYear and week <= nowWeek:
		return True
	else:
		return False


def EnsureDirectory(dir):
	'''
	判断路径是否存在，不存在就新建
	'''
	if not os.path.isdir(dir):
		os.makedirs(dir)


def GetPageText(url, dir):
	'''
	发送请求，抓取返回值，并写入LiveScores文件
	'''
	fpLiveScores = dir + '\\' + Global.Fn_LiveScores
	
	try:
		req = urllib.request.Request(url = url, headers = Global.Header_Mozilla)
		page = urllib.request.urlopen(req)
		text = page.read().decode(Global.Encoding_WhoScored)
		page.close()
		
		#  delete(replace) newline
		text = text.replace('\r\n', '')
		text = text.replace('\n', '')
		
		EnsureDirectory(dir)
		fileLiveScores = open(fpLiveScores, 'a', encoding = Global.Encoding_WhoScored)
		fileLiveScores.write(text + '\n')
		fileLiveScores.close()
	
	except Exception as e:
		print(e)
		return

		
def GetLiveScores(season, league):
	'''
	下载指定联赛每周的比赛结果
	'''
	dir = Global.Dir_Root + season + '\\' + league
	urlLeague = Global.Url_League_1314.get(league) if season == '1314' else Global.Url_League_1415.get(league)
	year1 = '20' + season[0:2] + 'W'
	year2 = '20' + season[2:4] + 'W'
	
	#  第一年的第25周~第52周
	for week in range(25, 53):
		if (DateBefore(year1, week)):
			url = Global.Url_WhoScored_Home + urlLeague + year1 + str(week) + Global.Url_Request_Suffix
			GetPageText(url, dir)
			time.sleep(0.5)
		else:
			break
	
	#  第二年的第1周~第30周
	for week in range(1, 30):
		if (DateBefore(year2, week)):
			url = Global.Url_WhoScored_Home + urlLeague + year2 + str(week) + Global.Url_Request_Suffix
			GetPageText(url, dir)
			time.sleep(0.5)
		else:
			break	
	
	print(league + ' downloading complete!')
	

if __name__ == '__main__':
	
	for league in Global.Url_League_1415.keys():
		GetLiveScores(league)