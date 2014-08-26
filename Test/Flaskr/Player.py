import Global, PlayerProperty, RadarChart


def ScannPlayer(season, playerID):
	
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
	
	playerStatistics = [player1]
	
	Global.Player_Radar_Data['Property'] = property
	Global.Player_Radar_Data['Max'] = max
	Global.Player_Radar_Data['Min'] = min
	Global.Player_Radar_Data['PlayerStatistics'] = playerStatistics
	
	fpMap = RadarChart.ShowMap(Global.Player_Radar_Data)
	return fpMap


if __name__ == '__main__':
	
	# 22221 Luis Suárez
	# 11119 Lionel Messi
	# 23736 Daniel Sturridge
	# 14260 Sergio Agüero
	# 24444 Olivier Giroud
	# 4056 Fernando Torres
	# 41330 Marco Reus
	# 3281 Zlatan Ibrahimovic
	# 18701 Falcao
	# 33799 Mario Balotelli
	# 24248 Diego Costa
	# 5583 Cristiano Ronaldo
	# 14296 Karim Benzema
	# 78498 Romelu Lukaku
	# 33404 Eden Hazard
	# 42705 Wilfried Bony
	# 8409 Rickie Lambert
	# 21683 Adam Lallana
	# 3859 Wayne Rooney
	# 23757 Álvaro Negredo
	# 97692 Raheem Sterling
	# 29400 Robert Lewandowski
	season = '1314'
	playerID1 = 22221
	playerID2 = 11119
	
	'''
	goal = PlayerProperty.GoalPerAttempting(season, playerID1)
	print(goal.player)
	print(goal.max)
	print(goal.min)
	'''
	player1 = [PlayerProperty.WonContest(season, playerID1).player,
			PlayerProperty.ContestWonPercentage(season, playerID1).player,
			PlayerProperty.WasFouled(season, playerID1).player,
			PlayerProperty.AerialWonPercentage(season, playerID1).player,
			PlayerProperty.GoalConversion(season, playerID1).player,
			PlayerProperty.BigChanceScoredPercentage(season, playerID1).player,
			PlayerProperty.GoalNormal(season, playerID1).player,
			PlayerProperty.BigChanceCreated(season, playerID1).player,
			PlayerProperty.AttAssistOpenplay(season, playerID1).player,
			PlayerProperty.GoalAssistOpenplay(season, playerID1).player,
			PlayerProperty.PassingAccuratePercentage(season, playerID1).player,
			PlayerProperty.CrossingAccuratePercentage(season, playerID1).player]
	
	player2 = [PlayerProperty.WonContest(season, playerID2).player,
			PlayerProperty.ContestWonPercentage(season, playerID2).player,
			PlayerProperty.WasFouled(season, playerID2).player,
			PlayerProperty.AerialWonPercentage(season, playerID2).player,
			PlayerProperty.GoalConversion(season, playerID2).player,
			PlayerProperty.BigChanceScoredPercentage(season, playerID2).player,
			PlayerProperty.GoalNormal(season, playerID2).player,
			PlayerProperty.BigChanceCreated(season, playerID2).player,
			PlayerProperty.AttAssistOpenplay(season, playerID2).player,
			PlayerProperty.GoalAssistOpenplay(season, playerID2).player,
			PlayerProperty.PassingAccuratePercentage(season, playerID2).player,
			PlayerProperty.CrossingAccuratePercentage(season, playerID2).player]
	
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
	
	playerStatistics = [player1, player2]
	
	Global.Player_Radar_Data['Property'] = property
	Global.Player_Radar_Data['Max'] = max
	Global.Player_Radar_Data['Min'] = min
	Global.Player_Radar_Data['PlayerStatistics'] = playerStatistics
	RadarChart.ShowMap(Global.Player_Radar_Data)
	
	
	#['goal_assist_openplay', 'att_assist_openplay', 'big_chance_created', 'accurate_through_ball', 'accurate_layoffs', 'successful_final_third_passes', 'goal_normal', 'was_fouled', 'won_contest', 'touches per turnover','crossing %', 'passing %'],
	