import os, re


Property = {}

Dir_Root_1314 = 'E:\\WhoScoredRoot\\1314\\'
Fn_LiveScores = 'LiveScores.txt'
Fn_Property_Class = 'Property_Team_Class.txt'
Fn_Property_Table = 'Property_Team_Table.txt'
League = ['England_BarclaysPL', 'England_FLChampionship', 'France_Ligue1', 'Germany_Bundesliga', 'Italy_SerieA', 'Netherlands_Eredivisie', 'Russia_RussianLeague', 'Spain_LigaBBVA']
Encoding_WhoScored = 'utf-8'

Regex_FN_Match = '(?:\d+)'
Regex_MatchInfo = '(?<=var\sinitialData\s=\s).*?(?:])'
Regex_Property = '(?:\[\')(?P<Property>\w+)\',\[\d+?(?:\]\])'
Re_FN_Match = re.compile(Regex_FN_Match, re.I)
Re_MatchInfo = re.compile(Regex_MatchInfo, re.I)
Re_Property = re.compile(Regex_Property, re.I)


def OutputProperty_Class():
	
	fileProperty = open(Fn_Property_Class, 'w')
	fileProperty.write('class TeamStatistics:\n')
	fileProperty.write('\tdef __init__(self):\n')
	fileProperty.write('\t\tself.id = \'\'\n')
	fileProperty.write('\t\tself.name = \'\'\n')
	fileProperty.write('\t\tself.home = \'\'\n')
	fileProperty.write('\t\tself.rating = \'\'\n')
	
	for key in sorted(Property.keys()):
		fileProperty.write('\t\tself.' + key + ' = \'\'\n')
	
	fileProperty.close()
	
	
def OutputProperty_Table():
	
	fileProperty = open(Fn_Property_Table, 'w')
	fileProperty.write('-- ----------------------------\n')
	fileProperty.write('-- Table structure for TeamStatistics\n')
	fileProperty.write('-- ----------------------------\n')
	fileProperty.write('CREATE TABLE IF NOT EXISTS \"TeamStatistics\" (\n')
	fileProperty.write('\"id\" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\n')
	fileProperty.write('\"team_id\" INTEGER NOT NULL,\n')
	fileProperty.write('\"team_name\" TEXT(40) NOT NULL,\n')
	fileProperty.write('\"league\" TEXT(40) NOT NULL,\n')
	fileProperty.write('\"match_id\" INTEGER NOT NULL,\n')
	fileProperty.write('\"home\" INTEGER NOT NULL,\n')
	fileProperty.write('\"rating\" REAL NOT NULL,\n')
	
	for key in sorted(Property.keys()):
		fileProperty.write('\"' + key + '\" REAL NOT NULL,\n')
	
	fileProperty.write(');\n')
	fileProperty.close()

def GetMatchIDs(league):

	matchIDs = []
	dirLeague = Dir_Root_1314 + league
	
	#  Add match id in original match id list
	for root, dirs, files in os.walk(dirLeague):
		for fn in files:
			if fn != Fn_LiveScores and os.path.getsize(os.path.join(root, fn)) > 1024:
				matchIDs.append(Re_FN_Match.findall(fn)[0])
	
	return matchIDs


def GetMatchContent(league, matchID):
	
	fpMatch = Dir_Root_1314 + league + '\\' + matchID + '.txt'
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
	
	print('Analyzing match ' + matchID, end = '\r')
	contentMatch = GetMatchContent(league, matchID)
	contentMatchInfo = Re_MatchInfo.findall(contentMatch)[0].replace('[','').replace('\'','').replace(']','').split(',')
	
	contentPropertyHomeTeam = Re_Property.findall(GetTeamStatistics(contentMatchInfo[0], contentMatchInfo[2], contentMatch))
	for property in contentPropertyHomeTeam:
		Property[property] = property
		
	contentPropertyAwayTeam = Re_Property.findall(GetTeamStatistics(contentMatchInfo[1], contentMatchInfo[3], contentMatch))
	for property in contentPropertyAwayTeam:
		Property[property] = property

	
if __name__ == '__main__':
	
	for league in League:
		matches = GetMatchIDs(league)
		for matchID in matches:
			GetProperty(league, matchID)
	
	OutputProperty_Table()