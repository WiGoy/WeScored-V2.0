'''
获取球员雷达图
'''
import Global, PlayerProperty, RadarChart


def GetPlayerRadar(season, playerID, playerName):
	'''
	获取球员雷达图
	'''
	player1 = [PlayerProperty.WonContest(season, playerID).player,
			PlayerProperty.ContestWonPercentage(season, playerID).player,
			PlayerProperty.WasFouled(season, playerID).player,
			PlayerProperty.AerialWonPercentage(season, playerID).player,
			PlayerProperty.GoalConversion(season, playerID).player,
			PlayerProperty.BigChanceScoredPercentage(season, playerID).player,
			PlayerProperty.GoalNormal(season, playerID).player,
			PlayerProperty.BigChanceCreated(season, playerID).player,
			PlayerProperty.AttAssistOpenplay(season, playerID).player,
			PlayerProperty.GoalAssistOpenplay(season, playerID).player,
			PlayerProperty.PassingAccuratePercentage(season, playerID).player,
			PlayerProperty.CrossingAccuratePercentage(season, playerID).player]
	
	property = [PlayerProperty.WonContest.Name,
			PlayerProperty.ContestWonPercentage.Name,
			PlayerProperty.WasFouled.Name,
			PlayerProperty.AerialWonPercentage.Name,
			PlayerProperty.GoalConversion.Name,
			PlayerProperty.BigChanceScoredPercentage.Name,
			PlayerProperty.GoalNormal.Name,
			PlayerProperty.BigChanceCreated.Name,
			PlayerProperty.AttAssistOpenplay.Name,
			PlayerProperty.GoalAssistOpenplay.Name,
			PlayerProperty.PassingAccuratePercentage.Name,
			PlayerProperty.CrossingAccuratePercentage.Name]
	
	max = [PlayerProperty.WonContest.Max,
		PlayerProperty.ContestWonPercentage.Max,
		PlayerProperty.WasFouled.Max,
		PlayerProperty.AerialWonPercentage.Max,
		PlayerProperty.GoalConversion.Max,
		PlayerProperty.BigChanceScoredPercentage.Max,
		PlayerProperty.GoalNormal.Max,
		PlayerProperty.BigChanceCreated.Max,
		PlayerProperty.AttAssistOpenplay.Max,
		PlayerProperty.GoalAssistOpenplay.Max,
		PlayerProperty.PassingAccuratePercentage.Max,
		PlayerProperty.CrossingAccuratePercentage.Max]
	
	min = [PlayerProperty.WonContest.Min,
		PlayerProperty.ContestWonPercentage.Min,
		PlayerProperty.WasFouled.Min,
		PlayerProperty.AerialWonPercentage.Min,
		PlayerProperty.GoalConversion.Min,
		PlayerProperty.BigChanceScoredPercentage.Min,
		PlayerProperty.GoalNormal.Min,
		PlayerProperty.BigChanceCreated.Min,
		PlayerProperty.AttAssistOpenplay.Min,
		PlayerProperty.GoalAssistOpenplay.Min,
		PlayerProperty.PassingAccuratePercentage.Min,
		PlayerProperty.CrossingAccuratePercentage.Min]
	
	playerNames = (playerName)
	playerStatistics = [player1]
	
	Global.Player_Radar_Data['Property'] = property
	Global.Player_Radar_Data['Max'] = max
	Global.Player_Radar_Data['Min'] = min
	Global.Player_Radar_Data['PlayerStatistics'] = playerStatistics
	
	#  生成雷达图，获取雷达图的访问路径
	fpMap = RadarChart.Drawing(playerNames, Global.Player_Radar_Data)
	return fpMap