'''
从比赛文件获取比赛、球队和球员的统计数据
'''
import re
import Global, LoaderTeam, LoaderPlayer


Re_MatchInfo = re.compile(Global.Regex_MatchInfo, re.I)


def GetMatchContent(league, matchID):
	'''
	读取本地数据文件
	'''
	fpMatch = Global.Dir_Root_1314 + league + '\\' + matchID + '.txt'
	fileMatch = open(fpMatch, 'r', encoding = Global.Encoding_WhoScored)
	content = fileMatch.read()
	fileMatch.close()
	
	return content


def GetMatchInfo(league, matchID):
	'''
	获取比赛技术统计：包括比赛、两支球队和两支球队的所有参赛球员
	'''
	contentMatch = GetMatchContent(league, matchID)
	contentMatchInfo = Re_MatchInfo.findall(contentMatch)[0].replace('[','').replace('\'','').replace(']','').split(',')
	
	homeTeamID = contentMatchInfo[0]
	awayTeamID = contentMatchInfo[1]
	homeTeam = contentMatchInfo[2]
	awayTeam = contentMatchInfo[3]
	
	matchInfo = Global.MatchInfo()
	matchInfo.id = matchID
	matchInfo.league = league
	matchInfo.season = '1314'
	matchInfo.startTime = contentMatchInfo[4]
	
	matchInfo.homeTeamStat = LoaderTeam.GetTeamStat(homeTeamID, homeTeam, True, contentMatch)
	matchInfo.homeTeamPlayerStat = LoaderPlayer.GetPlayerStat(homeTeamID, homeTeam, True, contentMatch)
	matchInfo.awayTeamStat = LoaderTeam.GetTeamStat(awayTeamID, awayTeam, False, contentMatch)
	matchInfo.awayTeamPlayerStat = LoaderPlayer.GetPlayerStat(awayTeamID, awayTeam, False, contentMatch)
	
	#  比较双方进球数判断各自得分
	if matchInfo.homeTeamStat.goals > matchInfo.awayTeamStat.goals:
		matchInfo.homeTeamPoints = 3
		matchInfo.awayTeamPoints = 0
	elif matchInfo.homeTeamStat.goals == matchInfo.awayTeamStat.goals:
		matchInfo.homeTeamPoints = 1
		matchInfo.awayTeamPoints = 1
	else:
		matchInfo.homeTeamPoints = 0
		matchInfo.awayTeamPoints = 3
	
	#  遍历球员统计获取当场最佳（可能没有最佳）
	matchInfo.manOfTheMatchPlayerID = 0
	
	for playerStat in matchInfo.homeTeamPlayerStat:
		if playerStat.man_of_the_match == 1:
			matchInfo.manOfTheMatchPlayerID = playerStat.id
			matchInfo.manOfTheMatchPlayerName = playerStat.name
	
	for playerStat in matchInfo.awayTeamPlayerStat:
		if playerStat.man_of_the_match == 1:
			matchInfo.manOfTheMatchPlayerID = playerStat.id
			matchInfo.manOfTheMatchPlayerName = playerStat.name
	
	return matchInfo


if __name__ == '__main__':
	league = 'England_BarclaysPL'
	matchID = '720420'
	
	matchInfo = GetMatchInfo(league, matchID)
	
	for player in matchInfo.awayTeamPlayerStat:
		print(player.name)