import os, re, sqlite3, time
import Global, Analyzer_Match


Re_FN_Match = re.compile(Global.Regex_FN_Match, re.I)


def ConnectDB():
	conn = sqlite3.connect(Global.Fn_Database)


def InsertMatchInfo(cursorObj, matchInfo):

	insertStr = 'INSERT INTO MatchInformation (match_id, start_time, league, home_team_id, home_team_name, home_team_rating, home_team_goals_for, home_team_points, away_team_id, away_team_name, away_team_rating, away_team_goals_for, away_team_points, man_of_the_match_player_id, man_of_the_match_player_name) VALUES (' + ')'
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
	
	matches = GetMatchIDs(league)
	for matchID in matches:
		
		if matchID != '720329':
			continue
		
		matchInfo = Analyzer_Match.GetMatchInfo(league, matchID)
		print(matchInfo.id + ' ' + matchInfo.startTime + ' ' + matchInfo.homeTeamStat.name + ' '  + str(matchInfo.homeTeamPoints) + ' '+ matchInfo.awayTeamStat.name + ' ' + str(matchInfo.awayTeamPoints))# + ' ' + matchInfo.manOfTheMatchPlayerName)
	
	print('s:'+str(time.time()-t))