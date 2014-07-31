import time, urllib.request


Fn_LiveScores = 'LiveScores.txt'

Url_WhoScored_Home = 'http://www.whoscored.com'

Encoding_WhoScored = 'utf-8'
Header_Mozilla = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
 
 
def GetPageText(year, week):
#	http://www.whoscored.com/tournamentsfeed/7794/Fixtures/?d=2014W17&isAggregate=false
	urlGet = '/tournamentsfeed/7794/Fixtures/?d=' + str(year) + 'W' + str(week) + '&isAggregate=false'
	url = Url_WhoScored_Home + urlGet
	print(url)
	
	try:
		req = urllib.request.Request(url = url, headers = Header_Mozilla)
		page = urllib.request.urlopen(req)
		text = page.read().decode(Encoding_WhoScored)
		page.close()
		'''
		#  delete(replace) newline
		text = text.replace('\r\n', '')
		text = text.replace('\n', '')
		'''
		
		fileLiveScores = open(Fn_LiveScores, 'a', encoding = Encoding_WhoScored)
		fileLiveScores.write(url + '\n')
		fileLiveScores.write(text + '\n')
		fileLiveScores.close()
	
	except Exception as e:
		print(e)
		return 0

		   
if __name__ == '__main__':
	for i in range(52):
		time.sleep(1)
		GetPageText(2013, i)

	for i in range(52):
		time.sleep(1)
		GetPageText(2014, i)
#	GetPageText(2013, 48)