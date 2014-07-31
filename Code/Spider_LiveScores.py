'''
生成所有联赛的LiveScores信息
'''
import os, time, urllib.request
import Global


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
		return 0

		
def GetLiveScores(league):
	'''
	下载指定联赛每周的比赛结果
	'''
	dir = Global.Dir_Root + league
	
	#  2013年（第25周~第52周）
	for week in range(25, 53):
		time.sleep(0.5)
		url = Global.Url_WhoScored_Home + Global.Url_League.get(league) + '2013W' + str(week) + Global.Url_Request_Suffix
		GetPageText(url, dir)
	
	#  2014年（第1周~第30周）
	for week in range(1, 30):
		time.sleep(0.5)
		url = Global.Url_WhoScored_Home + Global.Url_League.get(league) + '2014W' + str(week) + Global.Url_Request_Suffix
		GetPageText(url, dir)
		
	print(league + ' downloading complete!')


if __name__ == '__main__':
	
	for league in Global.Url_League.keys():
		GetLiveScores(league)