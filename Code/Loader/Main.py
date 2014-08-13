import sqlite3
import Global, DAL


#  选择赛季
Season = '1415'


if __name__ == '__main__':
	
	fpDatabase = Global.Dir_Root + Season + '\\' + Global.Fn_Database
	DAL.CreateDatabase(fpDatabase)
	
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	for league in Global.League:
		
		print('Update league ' + league)
		matches = DAL.GetMatchIDs(Season, league, cursorObj)
		for matchID in matches:
			DAL.UpdateMatchInfo(Season, league, matchID, cursorObj)
		
	conn.commit()
	cursorObj.close()
	conn.close()