import re
import Analyzer_Team


Dir_Root = 'E:\\WhoScoredRoot\\'
Regex_MatchInfo = '(?<=var\sinitialData\s=\s\[\[\[)(?P<HTID>\d+),(?P<ATID>\d+),\'(?P<HT>\w+)\',\'(?P<AT>\w+)\',\'(?P<Time>\S+\s\S+)\',\'.*?(?:\])'
Regex_Team = ''
Re_MatchInfo = re.compile(Regex_MatchInfo, re.I)
Re_Team = re.compile(Regex_Team, re.I)


class MatchInfo:
	ID = ''
	StartTime = ''
	League = ''
	HomeTeam_ID = ''
	HomeTeam = ''
	AwayTeam_ID = ''
	AwayTeam = ''


def GetMatchContent(league, matchID):
	
	fpMatch = Dir_Root + league + '\\' + matchID + '.txt'
	fileMatch = open(fpMatch, 'r')
	content = fileMatch.read()
	fileMatch.close()
	
	return content


def GetMatchInfo(league, matchID):

	contentMatch = GetMatchContent(league, matchID)
	
	matchInfo = MatchInfo()
	matchInfo.ID = matchID
	matchInfo.League = league

	contentMatchInfo = Re_MatchInfo.finditer(contentMatch)
	for s in contentMatchInfo:
		matchInfo.StartTime = s.group('Time')
		matchInfo.HomeTeam_ID = s.group('HTID')
		matchInfo.HomeTeam = s.group('HT')
		matchInfo.AwayTeam_ID = s.group('ATID')
		matchInfo.AwayTeam = s.group('AT')
		break
	
	Analyzer_Team.GetTeamStat(matchInfo.HomeTeam_ID, matchInfo.HomeTeam, contentMatch)
	Analyzer_Team.GetTeamStat(matchInfo.AwayTeam_ID, matchInfo.AwayTeam, contentMatch)
	
	return matchInfo


if __name__ == '__main__':
	league = 'England_BarclaysPL'
	matchID = '720750'
	
	GetMatchInfo(league, matchID)