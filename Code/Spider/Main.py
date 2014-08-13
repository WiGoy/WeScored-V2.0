import Global, SpiderLiveScores, SpiderMatches


#  选择赛季
Season = '1314'


if __name__ == '__main__':
	
	if Season == '1314':
		for league in Global.Url_League_1314.keys():
			SpiderLiveScores.GetLiveScores(Season, league)	
			matches = SpiderMatches.GetMatchID(Season, league)
			SpiderMatches.GetMatchPage(Season, league, matches)
	
	elif Season == '1415':
		for league in Global.Url_League_1415.keys():
			SpiderLiveScores.GetLiveScores(Season, league)
			matches = SpiderMatches.GetMatchID(Season, league)
			SpiderMatches.GetMatchPage(Season, league, matches)
		
	print('Updating complete!')