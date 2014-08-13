import sqlite3
import Global


def GetPlayerStatistics(cursorObj, PlayerID):
	
	strProperty1 = 'goals_conceded_gk';
	strProperty2 = 'goal_scored_by_team_fwr'
	strSearch = 'SELECT SUM(' + strProperty1 + ') AS goal, SUM(' + strProperty2 + ') AS total, player_id, player_name FROM PlayerStatistics WHERE (league = \"England_BarclaysPL\" or league = \"France_Ligue1\" or league = \"Germany_Bundesliga\" or league = \"Italy_SerieA\" or league = \"Spain_LigaBBVA\") GROUP BY player_id ORDER BY SUM(' + strProperty1 + ') DESC LIMIT 0,  20';
	
	cursorObj.execute(strSearch)
	players = cursorObj.fetchall()
	
	for player in players:
		print(str(player[0]) + ' ' + str(player[1]) + ' ' + player[3].encode('utf-8').decode('gbk'))


if __name__ == '__main__':

	season = '1314'
	playerID = 11
	
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	GetPlayerStatistics(cursorObj, playerID)
	
	cursorObj.close()
	conn.close()