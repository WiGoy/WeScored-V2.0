import os, re


Property = {}

Dir_Root = 'E:\\WhoScoredRoot\\'
Fn_LiveScores = 'LiveScores.txt'
Fn_Property = 'Property_Team.txt'
League = ['England_BarclaysPL', 'England_FLChampionship', 'France_Ligue1', 'Germany_Bundesliga', 'Italy_SerieA', 'Netherlands_Eredivisie', 'Russia_RussianLeague', 'Spain_LigaBBVA']
Encoding_WhoScored = 'utf-8'

Regex_FN_Match = '(?:\d+)'
Regex_MatchInfo = '(?<=var\sinitialData\s=\s\[\[\[)(?P<HTID>\d+),(?P<ATID>\d+),\'(?P<HT>\w+)\',\'(?P<AT>\w+)\',\'(?P<Time>\S+\s\S+)\',\'.*?(?:\])'
Regex_Property = '(?:\[\')(?P<Property>\w+)\',\[\d+?(?:\]\])'
Re_FN_Match = re.compile(Regex_FN_Match, re.I)
Re_MatchInfo = re.compile(Regex_MatchInfo, re.I)
Re_Property = re.compile(Regex_Property, re.I)


def GetMatchIDs(league):

	matchIDs = []
	dirLeague = Dir_Root + league
	
	#  Add match id in original match id list
	for root, dirs, files in os.walk(dirLeague):
		for fn in files:
			if fn != Fn_LiveScores and os.path.getsize(os.path.join(root, fn)) > 1024:
				matchIDs.append(Re_FN_Match.findall(fn)[0])
	
	return matchIDs


def OutputProperty():
	
	fileProperty = open(Fn_Property, 'w')
	
	for key in sorted(Property.keys()):
		fileProperty.write(key + '\n')
	
	fileProperty.close()


def GetMatchContent(league, matchID):
	
	fpMatch = Dir_Root + league + '\\' + matchID + '.txt'
	fileMatch = open(fpMatch, 'r', encoding = Encoding_WhoScored)
	content = fileMatch.read()
	fileMatch.close()
	
	return content
	

def GetTeamStatistics(teamID, teamName, content):

	regex_TeamStatistics = '(?:\[' + teamID + ',\'' + teamName + '\',).*?(?:\]\]\]\])'
	re_TeamStatistics = re.compile(regex_TeamStatistics, re.I)
	contentTeamStatistics = re_TeamStatistics.findall(content)[0]
	
	return contentTeamStatistics


def GetProperty(league, matchID):
	
	contentMatch = GetMatchContent(league, matchID)
	contentMatchInfo = Re_MatchInfo.finditer(contentMatch)
	
	for s in contentMatchInfo:
		contentPropertyHomeTeam = Re_Property.findall(GetTeamStatistics(s.group('HTID'), s.group('HT'), contentMatch))
		for property in contentPropertyHomeTeam:
			Property[property] = property
		
		contentPropertyAwayTeam = Re_Property.findall(GetTeamStatistics(s.group('ATID'), s.group('AT'), contentMatch))
		for property in contentPropertyAwayTeam:
			Property[property] = property
		
		break
	
	
if __name__ == '__main__':
	
	for league in League:
		matches = GetMatchIDs(league)
		
		for matchID in matches:
			GetProperty(league, matchID)
	
	OutputProperty()