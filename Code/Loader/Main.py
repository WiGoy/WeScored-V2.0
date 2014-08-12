import sqlite3, time
import Global, DAL


if __name__ == '__main__':
	
	fpDatabase = Global.Dir_Root_1314 + Global.Fn_Database
	conn = sqlite3.connect(fpDatabase)
	cursorObj = conn.cursor()
	
	t = time.time()
	
	for league in Global.League:
		
		print('Update league ' + league)
		dirLeague = Global.Dir_Root_1314 + league
		matches = DAL.GetMatchIDs(dirLeague)
		for matchID in matches:
			DAL.UpdateMatchInfo(league, matchID, cursorObj)
		
	conn.commit()
	cursorObj.close()
	conn.close()
	
	print('Updating complete!')
	print('s:'+str(time.time()-t))