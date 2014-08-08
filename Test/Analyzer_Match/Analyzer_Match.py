import re
import Global
import Analyzer_Team


Regex_Team = ''
Re_MatchInfo = re.compile(Global.Regex_MatchInfo, re.I)
Re_Team = re.compile(Regex_Team, re.I)


def GetMatchContent(league, matchID):
	
	fpMatch = Global.Dir_Root_1314 + league + '\\' + matchID + '.txt'
	fileMatch = open(fpMatch, 'r')
	content = fileMatch.read()
	fileMatch.close()
	
	return content


def GetMatchInfo(league, matchID):

	contentMatch = GetMatchContent(league, matchID)
	
	matchInfo = Global.MatchInfo()
	matchInfo.id = matchID
	matchInfo.league = league

	contentMatchInfo = Re_MatchInfo.finditer(contentMatch)
	for s in contentMatchInfo:
		matchInfo.startTime = s.group('Time')
		matchInfo.homeTeamID = s.group('HTID')
		matchInfo.homeTeam = s.group('HT')
		matchInfo.awayTeamID = s.group('ATID')
		matchInfo.awayTeam = s.group('AT')
		break
	
	homeTeamStat = Analyzer_Team.GetTeamStat(matchInfo.homeTeamID, matchInfo.homeTeam, True, contentMatch)
	
	for key in homeTeamStat.__dict__:
		print(key + ' : ' + str(homeTeamStat.__dict__[key]))
#	Analyzer_Team.GetTeamStat(matchInfo.AwayTeam_ID, matchInfo.AwayTeam, contentMatch)


if __name__ == '__main__':
	league = 'England_BarclaysPL'
	matchID = '720750'
	
	GetMatchInfo(league, matchID)