'''
与数据库交互
'''
import sqlite3
import Global


def GetPlayerName(season, playerID):
	'''
	根据球员ID获取姓名
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = 'SELECT player_name FROM PlayerStatistics WHERE player_id = ' + str(playerID) + ' Group By player_id'
	cursorObj.execute(strSearch)
	playerName = cursorObj.fetchone()
	
	cursorObj.close()
	conn.close()
	return playerName


def GetTeamList(season, league):
	'''
	获取某个联赛的球队
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = 'SELECT team_id, team_name, league FROM TeamStatistics WHERE league = \"' + league + '\" Group By team_id ORDER BY team_name ASC'
	cursorObj.execute(strSearch)
	teamList = cursorObj.fetchall()
	
	cursorObj.close()
	conn.close()
	return teamList


def GetPlayerList(season, teamID):
	'''
	获取某个球队的球员
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = 'SELECT player_id, player_name, team_id FROM PlayerStatistics WHERE team_id = ' + str(teamID) + ' Group By player_id ORDER BY player_name ASC'
	cursorObj.execute(strSearch)
	playerList = cursorObj.fetchall()
	
	cursorObj.close()
	conn.close()
	return playerList


def GetMaxPercentage1(season, property1, property2, propertyRange, range):
	'''
	获取数据的平均最高百分比
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = Global.Player_Search + '(Sum(' + property1 + ') / Sum(' + property2 + ')) AS percentage FROM PlayerStatistics WHERE '
	for league in Global.League:
		strSearch += 'league = \"' + league + '\" OR '
	strSearch = strSearch[0:(len(strSearch) - 4)] + ' GROUP BY player_id HAVING position <> \"\'GK\'\" AND Sum(mins_played) >= ' + str(Global.Player_Mins) + ' AND Sum(' + propertyRange + ') >=  ' + str(range) + ' ORDER BY percentage DESC LIMIT 0, 1'
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	max = round(player[4] * 100, 2)
	
#	print(str(max) + ' ' + str(player[0]) + ' ' + player[2] + ' ' + player[1].encode('utf-8').decode('gbk'))
	cursorObj.close()
	conn.close()
	return max


def GetMinPercentage1(season, property1, property2, propertyRange, range):
	'''
	获取数据的平均最高百分比
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = Global.Player_Search + '(Sum(' + property1 + ') / Sum(' + property2 + ')) AS percentage FROM PlayerStatistics WHERE '
	for league in Global.League:
		strSearch += 'league = \"' + league + '\" OR '
	strSearch = strSearch[0:(len(strSearch) - 4)] + ' GROUP BY player_id HAVING position <> \"\'GK\'\" AND Sum(mins_played) >= ' + str(Global.Player_Mins) + ' AND Sum(' + propertyRange + ') >=  ' + str(range) + ' ORDER BY percentage ASC LIMIT 0, 1'
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	min = round(player[4] * 100, 2)
	
	cursorObj.close()
	conn.close()
	return min
	

def GetPlayerPercentage1(season, property1, property2, playerID):
	'''
	获取球员该数据的百分比值
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = Global.Player_Search + '(Sum(' + property1 + ') / Sum(' + property2 + ')) AS property FROM PlayerStatistics WHERE player_id = ' + str(playerID)
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	percentage = round(player[4] * 100, 2)
	
	cursorObj.close()
	conn.close()
	return percentage


def GetMaxPercentage2(season, property1, property2, range):
	'''
	获取数据的最高值
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = Global.Player_Search + '(Sum(' + property1 + ') / (Sum(' + property1 + ') + Sum(' + property2 + '))) AS percentage FROM PlayerStatistics WHERE '
	for league in Global.League:
		strSearch += 'league = \"' + league + '\" OR '
	strSearch = strSearch[0:(len(strSearch) - 4)] + ' GROUP BY player_id HAVING position <> \"\'GK\'\" AND Sum(mins_played) >= ' + str(Global.Player_Mins) + ' AND Sum(' + property1 + ' + ' + property2 + ') >=  ' + str(range) + ' ORDER BY percentage DESC LIMIT 0, 1'
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	max = round(player[4] * 100, 2)
	
#	print(str(max) + ' ' + str(player[0]) + ' ' + player[2] + ' ' + player[1].encode('utf-8').decode('gbk'))
	cursorObj.close()
	conn.close()
	return max
	

def GetMinPercentage2(season, property1, property2, range):
	'''
	获取数据的最低值
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = Global.Player_Search + '(Sum(' + property1 + ') / (Sum(' + property1 + ') + Sum(' + property2 + '))) AS percentage FROM PlayerStatistics WHERE '
	for league in Global.League:
		strSearch += 'league = \"' + league + '\" OR '
	strSearch = strSearch[0:(len(strSearch) - 4)] + ' GROUP BY player_id HAVING position <> \"\'GK\'\" AND Sum(mins_played) >= ' + str(Global.Player_Mins) + ' AND Sum(' + property1 + ' + ' + property2 + ') >=  ' + str(range) + ' ORDER BY percentage ASC LIMIT 0, 1'
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	min = round(player[4] * 100, 2)
	
	cursorObj.close()
	conn.close()
	return min


def GetPlayerPercentage2(season, property1, property2, playerID):
	'''
	获取球员该数据的值
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = Global.Player_Search + '(Sum(' + property1 + ') / (Sum(' + property1 + ') + Sum(' + property2 + '))) AS property FROM PlayerStatistics WHERE player_id = ' + str(playerID)
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	percentage = round(player[4] * 100, 2)
	
	cursorObj.close()
	conn.close()
	return percentage

	
def GetMaxPercentage3(season, property1, property2, property3, range):
	'''
	获取数据的最高值
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = Global.Player_Search + '(Sum(' + property1 + ') / (Sum(' + property2 + ') + Sum(' + property3 + '))) AS percentage FROM PlayerStatistics WHERE '
	for league in Global.League:
		strSearch += 'league = \"' + league + '\" OR '
	strSearch = strSearch[0:(len(strSearch) - 4)] + ' GROUP BY player_id HAVING position <> \"\'GK\'\" AND Sum(mins_played) >= ' + str(Global.Player_Mins) + ' AND Sum(' + property2 + ' + ' + property3 + ') >=  ' + str(range) + ' ORDER BY percentage DESC LIMIT 0, 1'
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	max = round(player[4], 2)
	
#	print(str(max) + ' ' + str(player[0]) + ' ' + player[2] + ' ' + player[1].encode('utf-8').decode('gbk'))
	cursorObj.close()
	conn.close()
	return max
	

def GetMinPercentage3(season, property1, property2, property3, range):
	'''
	获取数据的最低值
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = Global.Player_Search + '(Sum(' + property1 + ') / (Sum(' + property2 + ') + Sum(' + property3 + '))) AS percentage FROM PlayerStatistics WHERE '
	for league in Global.League:
		strSearch += 'league = \"' + league + '\" OR '
	strSearch = strSearch[0:(len(strSearch) - 4)] + ' GROUP BY player_id HAVING position <> \"\'GK\'\" AND Sum(mins_played) >= ' + str(Global.Player_Mins) + ' AND Sum(' + property2 + ' + ' + property3 + ') >=  ' + str(range) + ' ORDER BY percentage ASC LIMIT 0, 1'
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	min = round(player[4], 2)
	
	cursorObj.close()
	conn.close()
	return min


def GetPlayerPercentage3(season, property1, property2, property3, playerID):
	'''
	获取球员该数据的值
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = Global.Player_Search + '(Sum(' + property1 + ') / (Sum(' + property2 + ') + Sum(' + property3 + '))) AS property FROM PlayerStatistics WHERE player_id = ' + str(playerID)
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	percentage = round(player[4], 2)
	
	cursorObj.close()
	conn.close()
	return percentage


def GetMaxAvg(season, property):
	'''
	获取数据的平均最高值
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = Global.Player_Search + 'Avg(' + property + ') AS property FROM PlayerStatistics WHERE '
	for league in Global.League:
		strSearch += 'league = \"' + league + '\" OR '
	strSearch = strSearch[0:(len(strSearch) - 4)] + ' GROUP BY player_id HAVING position <> \"\'GK\'\" AND Sum(mins_played) >= ' + str(Global.Player_Mins) + ' ORDER BY property DESC LIMIT 0, 1'
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	max = round(player[4], 2)
	
#	print(str(max) + ' ' + str(player[0]) + ' ' + player[2] + ' ' + player[1].encode('utf-8').decode('gbk'))
	cursorObj.close()
	conn.close()
	return max


def GetMinAvg(season, property):
	'''
	获取数据的平均最低值
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = Global.Player_Search + 'Avg(' + property + ') AS property FROM PlayerStatistics WHERE '
	for league in Global.League:
		strSearch += 'league = \"' + league + '\" OR '
	strSearch = strSearch[0:(len(strSearch) - 4)] + ' GROUP BY player_id HAVING position <> \"\'GK\'\" AND Sum(mins_played) >= ' + str(Global.Player_Mins) + ' ORDER BY property ASC LIMIT 0, 1'
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	min = round(player[4], 2)
	
	cursorObj.close()
	conn.close()
	return min
	

def GetPlayerAvg(season, property, playerID):
	'''
	获取球员该数据的值
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = Global.Player_Search + 'Avg(' + property + ') AS property FROM PlayerStatistics WHERE player_id = ' + str(playerID)
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	stat = round(player[4], 2)
	
	cursorObj.close()
	conn.close()
	return stat


def GetPlayerSum(season, property, playerID):
	'''
	获取球员该数据的值
	'''
	fpDatabase = Global.Dir_Root + season + '\\' + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	strSearch = Global.Player_Search + 'Sum(' + property + ') AS property FROM PlayerStatistics WHERE player_id = ' + str(playerID)
	
	cursorObj.execute(strSearch)
	player = cursorObj.fetchone()
	stat = round(player[4], 2)
	#print(player)
	cursorObj.close()
	conn.close()
	return stat