'''
从比赛文件获取球队的统计数据
'''
import re
import Global
	

def GetStat(regex, content):
	'''
	获取对应的技术统计数据
	'''
	regex_Stat = '(?<=\[\'' + regex + '\',\[).*?(?=]+,)'
	re_Stat = re.compile(regex_Stat, re.I)
	stat = re_Stat.findall(content)
	
	if len(stat) > 0:
		return float(stat[0])
	else:
		return float(0)


def GetTeamStat(teamID, teamName, home, content):
	'''
	获取球队单场技术统计数据
	'''
	teamStat = Global.TeamStatistics()
	
	regex_TeamStat = '(?:\[' + teamID + ',\'' + teamName + '\',).*?(?:\]\]\]\])'
	regex_TeamRating = '(?:\[' + teamID + ',\'' + teamName + '\',(?P<Rating>\d?.?\d+),).*?(?:\]\]\]\])'
	re_TeamStat = re.compile(regex_TeamStat, re.I)
	re_TeamRating = re.compile(regex_TeamRating, re.I)
	
	contentTeamStat = re_TeamStat.findall(content)[0]
	teamStat.rating = re_TeamRating.findall(contentTeamStat)[0]
	
	for key in teamStat.__dict__:
		teamStat.__dict__[key] = GetStat(key, contentTeamStat)
	
	teamStat.id = teamID
	teamStat.name = teamName
	teamStat.home = home
	teamStat.rating = re_TeamRating.findall(contentTeamStat)[0]
	
	return teamStat