'''
在这里定义了可能会用到的常量和数据结构
'''


'''
路径和文件名
'''
Dir_Root = 'C:\\WorkSpace\\GitHub\\WhoScoredRoot\\'
Fn_Database = 'WhoScored.db'


'''
搜索包含的联赛
'''
League = ['England_BarclaysPL', 'France_Ligue1', 'Germany_Bundesliga', 'Italy_SerieA', 'Spain_LigaBBVA']


'''
常用数据库搜索语句
'''
Player_Mins = 1440
Player_Search = 'SELECT player_id, player_name, team_name, position, '


'''
球员雷达图数据
'''
Player_Radar_Data = {'Property':[], 'Max':[], 'Min':[], 'PlayerStatistics':[]}