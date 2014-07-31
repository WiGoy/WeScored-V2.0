import re


def GetStat(regex, content):
	
	regex_Stat = '(?<=\[\'' + regex + '\',\[).*?(?=]+,)'
	print(regex_Stat)
	re_Stat = re.compile(regex_Stat, re.I)
	stat = re_Stat.findall(content)[0]
	print(stat)


def GetTeamStat(teamID, teamName, content):
	
	regex_TeamStat = '(?:\[' + teamID + ',\'' + teamName + '\',).*?(?:\]\]\]\])'
	re_TeamStat = re.compile(regex_TeamStat, re.I)
	contentTeamStat = re_TeamStat.findall(content)[0]
	
	print(contentTeamStat)
	GetStat('open_play_pass', contentTeamStat)