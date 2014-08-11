import re
import Global, Analyzer_Team, Analyzer_Player


Re_MatchInfo = re.compile(Global.Regex_MatchInfo, re.I)


def GetMatchContent(league, matchID):
	
	fpMatch = Global.Dir_Root_1314 + league + '\\' + matchID + '.txt'
	fileMatch = open(fpMatch, 'r', encoding = Global.Encoding_WhoScored)
	content = fileMatch.read()
	fileMatch.close()
	
	return content


def GetMatchInfo(league, matchID):

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
	
	matchInfo.homeTeamStat = Analyzer_Team.GetTeamStat(homeTeamID, homeTeam, True, contentMatch)
	matchInfo.homeTeamPlayerStat = Analyzer_Player.GetPlayerStat(homeTeamID, homeTeam, True, contentMatch)
	matchInfo.awayTeamStat = Analyzer_Team.GetTeamStat(awayTeamID, awayTeam, False, contentMatch)
	matchInfo.awayTeamPlayerStat = Analyzer_Player.GetPlayerStat(awayTeamID, awayTeam, False, contentMatch)
	
	if matchInfo.homeTeamStat.goals > matchInfo.awayTeamStat.goals:
		matchInfo.homeTeamPoints = 3
		matchInfo.awayTeamPoints = 0
	elif matchInfo.homeTeamStat.goals == matchInfo.awayTeamStat.goals:
		matchInfo.homeTeamPoints = 1
		matchInfo.awayTeamPoints = 1
	else:
		matchInfo.homeTeamPoints = 0
		matchInfo.awayTeamPoints = 3
	
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
	matchID = '719920'
	
	GetMatchInfo(league, matchID)