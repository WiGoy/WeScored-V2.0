import Global, SpiderLiveScores, SpiderMatches


if __name__ == '__main__':
	
	for league in Global.Url_League_1415.keys():
		SpiderLiveScores.GetLiveScores(league)
		matches = SpiderMatches.GetMatchID(league)
		SpiderMatches.GetMatchPage(league, matches)
		
	print('Updating complete!')