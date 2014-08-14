import sqlite3
import Global


def GetPlayerStatistics(cursorObj, PlayerID):
	
	strMins = 'mins_played'
	strProperty1 = 'won_contest';
	strProperty2 = 'total_contest'
	strSearch = 'SELECT AVG(' + strProperty1 + ') AS goal, AVG(' + strProperty2 + ') AS total, SUM(' + strMins + ') AS total_mins, player_id, player_name FROM PlayerStatistics WHERE (league = \"England_BarclaysPL\" or league = \"France_Ligue1\" or league = \"Germany_Bundesliga\" or league = \"Italy_SerieA\" or league = \"Spain_LigaBBVA\") and (position = \"dl\" or position = \"dr\") GROUP BY player_id ORDER BY goal DESC LIMIT 0,  40';
	
	cursorObj.execute(strSearch)
	players = cursorObj.fetchall()
	
	for player in players:
		if (player[2] > 2400):
			print(str(player[0]) + ' ' + str(player[1]) + ' ' + player[4].encode('utf-8').decode('gbk'))


if __name__ == '__main__':

	season = '1314'
	playerID = 11
	
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	GetPlayerStatistics(cursorObj, playerID)
	
	cursorObj.close()
	conn.close()