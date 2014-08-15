import sqlite3
import Global


def GetMaxPercentageProperty(cursorObj, listLeague, property1, property2, propertyRange, range):
	
	strSearch = Global.Player_Search + 'Avg(' + property1 + ' / ' + property2 + ') AS percentage FROM PlayerStatistics WHERE '
	for league in listLeague:
		strSearch += 'league = \"' + league + '\" OR '
	strSearch = strSearch[0:(len(strSearch) - 4)] + ' GROUP BY player_id HAVING position <> \'GK\' AND Sum(mins_played) >= ' + str(Global.Player_Mins) + ' AND Sum(' + propertyRange + ') >=  ' + str(range) + ' ORDER BY percentage DESC LIMIT 0, 1'
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	max = round(player[4], 4)
	
	print(str(max) + ' ' + player[1])
	return max


def GetMinPercentageProperty(cursorObj, listLeague, property1, property2, propertyRange, range):
	
	strSearch = Global.Player_Search + 'Avg(' + property1 + ' / ' + property2 + ') AS percentage FROM PlayerStatistics WHERE '
	for league in listLeague:
		strSearch += 'league = \"' + league + '\" OR '
	strSearch = strSearch[0:(len(strSearch) - 4)] + ' GROUP BY player_id HAVING position <> \'GK\' AND Sum(mins_played) >= ' + str(Global.Player_Mins) + ' AND Sum(' + propertyRange + ') >=  ' + str(range) + ' ORDER BY percentage ASC LIMIT 0, 1'
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	min = round(player[4], 4)
	
	print(min)
	return min
	

def GetPlayerPercentageProperty(cursorObj, listLeague, property1, property2, playerID):
	strSearch = Global.Player_Search + 'Avg(' + property1 + ' / ' + property2 + ') AS property FROM PlayerStatistics WHERE player_id = ' + str(playerID)
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	perc = round(player[4], 4)
	
	print(perc)
	return perc


def GetMaxAvgProperty(cursorObj, listLeague, property):
	
	strSearch = Global.Player_Search + 'Avg(' + property + ') AS property FROM PlayerStatistics WHERE '
	for league in listLeague:
		strSearch += 'league = \"' + league + '\" OR '
	strSearch = strSearch[0:(len(strSearch) - 4)] + ' GROUP BY player_id HAVING position <> \'GK\' AND Sum(mins_played) >= ' + str(Global.Player_Mins) + ' ORDER BY property DESC LIMIT 0, 1'
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	max = round(player[4], 2)
	
	print(str(max) + ' ' + player[1])
	return max


def GetMinAvgProperty(cursorObj, listLeague, property):
	
	strSearch = Global.Player_Search + 'Avg(' + property + ') AS property FROM PlayerStatistics WHERE '
	for league in listLeague:
		strSearch += 'league = \"' + league + '\" OR '
	strSearch = strSearch[0:(len(strSearch) - 4)] + ' GROUP BY player_id HAVING position <> \'GK\' AND Sum(mins_played) >= ' + str(Global.Player_Mins) + ' ORDER BY property ASC LIMIT 0, 1'
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	min = round(player[4], 2)
	
	print(min)
	return min
	

def GetPlayerAvgProperty(cursorObj, listLeague, property, playerID):
	
	strSearch = Global.Player_Search + 'Avg(' + property + ') AS property FROM PlayerStatistics WHERE player_id = ' + str(playerID)
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	avg = round(player[4], 2)
	
	print(avg)
	return avg


if __name__ == '__main__':

	season = '1314'
	listLeague = ['England_BarclaysPL', 'France_Ligue1', 'Germany_Bundesliga', 'Italy_SerieA', 'Spain_LigaBBVA', 'Netherlands_Eredivisie']
	property = 'accurate_long_balls'
	property1 = 'accurate_pass'
	property2 = 'total_pass'
	propertyRange = 'total_fwd_zone_pass'
	range = 800
	playerID = 17#97692
	
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	'''
	GetPlayerAvgProperty(cursorObj, listLeague, property, playerID)
	GetMaxAvgProperty(cursorObj, listLeague, property)
	GetMinAvgProperty(cursorObj, listLeague, property)
	'''
	GetPlayerPercentageProperty(cursorObj, listLeague, property1, property2, playerID)
	GetMaxPercentageProperty(cursorObj, listLeague, property1, property2, propertyRange, range)
	GetMinPercentageProperty(cursorObj, listLeague, property1, property2, propertyRange, range)
	
	cursorObj.close()
	conn.close()