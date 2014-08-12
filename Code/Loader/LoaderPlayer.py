'''
从比赛文件获取球员的统计数据
'''
import re
import Global


Re_PlayerStatistics = re.compile(Global.Regex_PlayerStatistics, re.I)
	
	
def GetStat(regex, content):
	'''
	获取对应的技术统计数据
	'''
	regex_Stat = '(?<=\[\'' + regex + '\',\[).*?(?=]+,)'
	re_Stat = re.compile(regex_Stat, re.I)
	stat = re_Stat.findall(content)
	
	if len(stat) > 0:
		if regex == 'position':
			return stat[0]
		else:
			return float(stat[0])
	else:
		return float(0)


def GetPlayerStat(teamID, teamName, home, content):
	'''
	获取一支球队中所有球员的单场技术统计数据
	'''
	playerStatList = []
	
	regex_HomeTeam = '(?<=\[' + teamID + ',\'' + teamName + '\',).*?(?:\]\]\]\],\[\d+)'
	regex_AwayTeam = '(?<=\[' + teamID + ',\'' + teamName + '\',).*?(?:\]\]\]\]\])'
	re_TeamStat = re.compile(regex_HomeTeam, re.I) if home else re.compile(regex_AwayTeam, re.I)
	contentTeamStat = re_TeamStat.findall(content)[0]
	contentPlayerStat = Re_PlayerStatistics.findall(contentTeamStat)
	
	for content in contentPlayerStat:
		playerStat = Global.PlayerStatistics()
		for key in playerStat.__dict__:
			playerStat.__dict__[key] = GetStat(key, content)
		
		contentPlayerInfo = content.replace('[','').replace('\'','').replace(']','').split(',')
		playerStat.id = contentPlayerInfo[0]
		playerStat.name = contentPlayerInfo[1]
		playerStatList.append(playerStat)
	
	return playerStatList