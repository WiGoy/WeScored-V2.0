import os, re


Property = {}

Dir_Root_1314 = 'E:\\WhoScoredRoot\\1314\\'
Fn_LiveScores = 'LiveScores.txt'
Fn_Property_Class = 'Property_Player_Class.txt'
League = ['England_BarclaysPL', 'England_FLChampionship', 'France_Ligue1', 'Germany_Bundesliga', 'Italy_SerieA', 'Netherlands_Eredivisie', 'Russia_RussianLeague', 'Spain_LigaBBVA']
Encoding_WhoScored = 'utf-8'

Regex_FN_Match = '(?:\d+)'
Regex_MatchInfo = '(?<=var\sinitialData\s=\s).*?(?:])'
Regex_PlayerStatistics = '(?:\[\d+\,\').*?(?:\d+,\d+,\d+\])'
Regex_Property = '(?:\[\')(?P<Property>\w+)\',\[\d+?(?:\]\])'
Re_FN_Match = re.compile(Regex_FN_Match, re.I)
Re_MatchInfo = re.compile(Regex_MatchInfo, re.I)
Re_PlayerStatistics = re.compile(Regex_PlayerStatistics, re.I)
Re_Property = re.compile(Regex_Property, re.I)


def OutputProperty_Class():
	
	fileProperty = open(Fn_Property_Class, 'w')
	fileProperty.write('class PlayerStatistics:\n')
	fileProperty.write('\tdef __init__(self):\n')
	fileProperty.write('\t\tself.id = \'\'\n')
	fileProperty.write('\t\tself.name = \'\'\n')
	fileProperty.write('\t\tself.position = \'\'\n')
	
	for key in sorted(Property.keys()):
		fileProperty.write('\t\tself.' + key + ' = \'\'\n')
	
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
	

def GetPlayerStatistics(content):

	contentProperty = Re_Property.findall(content)
	
	for property in contentProperty:
		Property[property] = property


def GetProperty(league, matchID):
	
	print('Analyzing match ' + matchID, end = '\r')
	contentMatch = GetMatchContent(league, matchID)
	contentMatchInfo = Re_MatchInfo.findall(contentMatch)[0].replace('[','').replace('\'','').replace(']','').split(',')
	contentPlayers = Re_PlayerStatistics.findall(contentMatch)
	
	for content in contentPlayers:
		GetPlayerStatistics(content)


if __name__ == '__main__':
	
	for league in League:
		matches = GetMatchIDs(league)
		for matchID in matches:
			GetProperty(league, matchID)

	OutputProperty_Class()