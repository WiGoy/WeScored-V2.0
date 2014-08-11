import os, re, sqlite3, time
import Global, Analyzer_Match


Re_FN_Match = re.compile(Global.Regex_FN_Match, re.I)


def ConnectDB():
	conn = sqlite3.connect(Global.Fn_Database)


def InsertMatchInfo(cursorObj, matchInfo):

	insertStr = 'INSERT INTO MatchInformation VALUES (' + str(matchInfo.id) + ', \"' + matchInfo.startTime + '\", \"' + matchInfo.league + '\", ' + str(matchInfo.homeTeamStat.id) + ', \"' + matchInfo.homeTeamStat.name + '\", ' + str(matchInfo.homeTeamStat.rating) + ', ' + str(matchInfo.homeTeamStat.goals) + ', ' + str(matchInfo.homeTeamPoints) + ', ' + str(matchInfo.awayTeamStat.id) + ', \"' + matchInfo.awayTeamStat.name + '\", ' + str(matchInfo.awayTeamStat.rating) + ', ' + str(matchInfo.awayTeamStat.goals) + ', ' + str(matchInfo.awayTeamPoints) + ', ' + str(matchInfo.manOfTheMatchPlayerID) + ', \"' + matchInfo.manOfTheMatchPlayerName + '\")'
	
	cursorObj.execute(insertStr)
	
	
def GetMatchIDs(league):

	matchIDs = []
	dirLeague = Global.Dir_Root_1314 + league
	
	#  Add match id in original match id list
	for root, dirs, files in os.walk(dirLeague):
		for fn in files:
			if fn != Global.Fn_LiveScores and os.path.getsize(os.path.join(root, fn)) > 1024:
				matchIDs.append(Re_FN_Match.findall(fn)[0])
	
	return matchIDs


if __name__ == '__main__':
	
	league = 'England_BarclaysPL'
	
	t = time.time()
	
	conn = sqlite3.connect(Global.Fn_Database)
	cursorObj = conn.cursor()
	
	matches = GetMatchIDs(league)
	for matchID in matches:
		print(matchID, end = '\r')
		matchInfo = Analyzer_Match.GetMatchInfo(league, matchID)
		InsertMatchInfo(cursorObj, matchInfo)
		
	conn.commit()
	cursorObj.close()
	conn.close()
	
	print('s:'+str(time.time()-t))