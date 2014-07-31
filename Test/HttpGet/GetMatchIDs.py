import re


MatchIDs = {}

Fn_LiveScores = 'LiveScores.txt'
Fn_MatchIDs = 'Matches.txt'
#[720385,1,'Thursday, Dec 26 2013','12:45',214,'Hull',0,32,'Manchester United',1,'2 : 3','2 : 2',1,1,'FT','2',0,1,19,0]
Regex_Match = '(?<=\[)(?P<ID>\d+).*?(?:\])'
Re_Match = re.compile(Regex_Match, re.I)


def OutputMatchIDs():
	
	fileMatchIDs = open(Fn_MatchIDs, 'w')
	
	for key in sorted(MatchIDs.keys()):
		fileMatchIDs.write(key + ' ' + MatchIDs.get(key) + '\n')
	
	fileMatchIDs.close()


def GetLiveScoresContent():

	fileLiveScores = open(Fn_LiveScores, 'r')
	content = fileLiveScores.read()
	fileLiveScores.close()
	
	return content


def GetMatchID():
	
	contentMatches = Re_Match.finditer(GetLiveScoresContent())
	
	for s in contentMatches:
		MatchIDs[s.group('ID')] = s.group('ID')


if __name__ == '__main__':
	
	GetMatchID()
	OutputMatchIDs()