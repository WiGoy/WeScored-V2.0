import re
import Global, Analyzer_Team, Analyzer_Player


Re_MatchInfo = re.compile(Global.Regex_MatchInfo, re.I)


def GetMatchContent(league, matchID):
	
	fpMatch = Global.Dir_Root_1314 + league + '\\' + matchID + '.txt'
	fileMatch = open(fpMatch, 'r')
	content = fileMatch.read()
	fileMatch.close()
	
	return content


def GetMatchInfo(league, matchID):

	contentMatch = GetMatchContent(league, matchID)
	contentMatchInfo = Re_MatchInfo.findall(contentMatch)[0].replace('[','').replace('\'','').replace(']','').split(',')
	
	matchInfo = Global.MatchInfo()
	matchInfo.id = matchID
	matchInfo.league = league
	matchInfo.season = '1314'
	matchInfo.homeTeamID = contentMatchInfo[0]
	matchInfo.awayTeamID = contentMatchInfo[1]
	matchInfo.homeTeam = contentMatchInfo[2]
	matchInfo.awayTeam = contentMatchInfo[3]
	matchInfo.startTime = contentMatchInfo[4]
	
	homeTeamStat = Analyzer_Team.GetTeamStat(matchInfo.homeTeamID, matchInfo.homeTeam, True, contentMatch)
	homePlayerStat = Analyzer_Player.GetPlayerStat(matchInfo.homeTeamID, matchInfo.homeTeam, True, contentMatch)
	
	'''
	homeTeamStat = Analyzer_Team.GetTeamStat(matchInfo.homeTeamID, matchInfo.homeTeam, True, contentMatch)
	
	for key in homeTeamStat.__dict__:
		print(key + ' : ' + str(homeTeamStat.__dict__[key]))
	'''


if __name__ == '__main__':
	league = 'England_BarclaysPL'
	matchID = '719920'
	
	GetMatchInfo(league, matchID)