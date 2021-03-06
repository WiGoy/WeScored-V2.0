﻿'''
分析LiveScores.txt，并从中获取MatchID
'''
import re
import Global

'''
Compile regexes
'''
Re_Match = re.compile(Global.Regex_Match, re.I)


def GetLiveScoresContent(season, league):
	'''
	读取LiveScores.txt
	'''
	fpLiveScores = Global.Dir_Root + season + '\\' + league + '\\' + Global.Fn_LiveScores
	fileLiveScores = open(fpLiveScores, 'r')
	content = fileLiveScores.read()
	fileLiveScores.close()
	
	return content


def GetMatchID(season, league):
	'''
	获取指定联赛的MatchID
	返回dict(key[id], value[url])
	'''
	matches = {}
	contentMatches = Re_Match.finditer(GetLiveScoresContent(season, league))

	for s in contentMatches:
		url = Global.Url_WhoScored_Match + s.group('ID') + Global.Url_WhoScored_LiveStat
		matches[s.group('ID')] = url
	
	return matches