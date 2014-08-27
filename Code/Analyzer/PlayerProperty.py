'''
定义用于球员雷达图的数据类型
'''
import DAL


class AccurateLayoffs():
	
	__Property = 'accurate_layoffs'
	Name = 'accurate_layoffs'
	Max = 7.35
	Min = 0.00
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerAvg(season, AccurateLayoffs.__Property, playerid)
	#	self.max = DAL.GetMaxAvg(season, AccurateLayoffs.__Property)
	#	self.min = DAL.GetMinAvg(season, AccurateLayoffs.__Property)


class AccurateThroughBall():
	
	__Property = 'accurate_through_ball'
	Name = 'accurate_through_ball'
	Max = 0.67
	Min = 0.00
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerAvg(season, AccurateThroughBall.__Property, playerid)
	#	self.max = DAL.GetMaxAvg(season, AccurateThroughBall.__Property)
	#	self.min = DAL.GetMinAvg(season, AccurateThroughBall.__Property)


class AerialWonPercentage():
	
	__Property1 = 'aerial_won'
	__Property2 = 'aerial_lost'
	__Range = 80
	Name = 'Aerial %'
	Max = 84.06
	Min = 16.81
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerPercentage2(season, AerialWonPercentage.__Property1, AerialWonPercentage.__Property2, playerid)
	#	self.max = DAL.GetMaxPercentage2(season, AerialWonPercentage.__Property1, AerialWonPercentage.__Property2, AerialWonPercentage.__Range)
	#	self.min = DAL.GetMinPercentage2(season, AerialWonPercentage.__Property1, AerialWonPercentage.__Property2, AerialWonPercentage.__Range)


class AerialWon():
	
	__Property = 'aerial_won'
	Name = 'AerialWon'
	Max = 8.77
	Min = 0.00
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerAvg(season, AerialWon.__Property, playerid)
	#	self.max = DAL.GetMaxAvg(season, AerialWon.__Property)
	#	self.min = DAL.GetMinAvg(season, AerialWon.__Property)


class AttAssistOpenplay():
	
	__Property = 'att_assist_openplay'
	Name = 'Create Openplay Attempts'
	Max = 2.40
	Min = 0.00
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerAvg(season, AttAssistOpenplay.__Property, playerid)
	#	self.max = DAL.GetMaxAvg(season, AttAssistOpenplay.__Property)
	#	self.min = DAL.GetMinAvg(season, AttAssistOpenplay.__Property)


class BigChanceCreated():
	
	__Property = 'big_chance_created'
	Name = 'Create Big Chance'
	Max = 0.75
	Min = 0.00
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerAvg(season, BigChanceCreated.__Property, playerid)
	#	self.max = DAL.GetMaxAvg(season, BigChanceCreated.__Property)
	#	self.min = DAL.GetMinAvg(season, BigChanceCreated.__Property)
	

class BigChanceScoredPercentage():
	
	__Property1 = 'big_chance_scored'
	__Property2 = 'big_chance_missed'
	__Range = 10
	Name = 'Big Chance Conversion'
	Max = 100.00
	Min = 15.38
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerPercentage2(season, BigChanceScoredPercentage.__Property1, BigChanceScoredPercentage.__Property2, playerid)
	#	self.max = DAL.GetMaxPercentage2(season, BigChanceScoredPercentage.__Property1, BigChanceScoredPercentage.__Property2, BigChanceScoredPercentage.__Range)
	#	self.min = DAL.GetMinPercentage2(season, BigChanceScoredPercentage.__Property1, BigChanceScoredPercentage.__Property2, BigChanceScoredPercentage.__Range)


class CrossingAccuratePercentage():
	
	__Property1 = 'accurate_cross_nocorner'
	__Property2 = 'total_cross_nocorner'
	__PropertyRange = 'total_cross_nocorner'
	__Range = 80
	Name = 'Crossing %'
	Max = 46.16
	Min = 5.33
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerPercentage1(season, CrossingAccuratePercentage.__Property1, CrossingAccuratePercentage.__Property2, playerid)
	#	self.max = DAL.GetMaxPercentage1(season, CrossingAccuratePercentage.__Property1, CrossingAccuratePercentage.__Property2, CrossingAccuratePercentage.__PropertyRange, CrossingAccuratePercentage.__Range)
	#	self.min = DAL.GetMinPercentage1(season, CrossingAccuratePercentage.__Property1, CrossingAccuratePercentage.__Property2, CrossingAccuratePercentage.__PropertyRange, CrossingAccuratePercentage.__Range)


class ContestWonPercentage():
	
	__Property1 = 'won_contest'
	__Property2 = 'total_contest'
	__PropertyRange = 'total_contest'
	__Range = 40
	Name = 'Contest %'
	Max = 86.05
	Min = 21.43
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerPercentage1(season, ContestWonPercentage.__Property1, ContestWonPercentage.__Property2, playerid)
	#	self.max = DAL.GetMaxPercentage1(season, ContestWonPercentage.__Property1, ContestWonPercentage.__Property2, ContestWonPercentage.__PropertyRange, ContestWonPercentage.__Range)
	#	self.min = DAL.GetMinPercentage1(season, ContestWonPercentage.__Property1, ContestWonPercentage.__Property2, ContestWonPercentage.__PropertyRange, ContestWonPercentage.__Range)


class GoalAssistOpenplay():
	
	__Property = 'goal_assist_openplay'
	Name = 'Openplay Assists'
	Max = 0.44
	Min = 0.00
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerAvg(season, GoalAssistOpenplay.__Property, playerid)
	#	self.max = DAL.GetMaxAvg(season, GoalAssistOpenplay.__Property)
	#	self.min = DAL.GetMinAvg(season, GoalAssistOpenplay.__Property)
		

class GoalNormal():
	
	__Property = 'goal_normal'
	Name = 'Goals (except penalty)'
	Max = 0.94
	Min = 0.00
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerAvg(season, GoalNormal.__Property, playerid)
	#	self.max = DAL.GetMaxAvg(season, GoalNormal.__Property)
	#	self.min = DAL.GetMinAvg(season, GoalNormal.__Property)


class GoalConversion():
	
	__Property1 = 'goals'
	__Property2 = 'att_openplay'
	__Property3 = 'att_setpiece'
	__Range = 20
	Name = 'Goals Conversion'
	Max = 0.47
	Min = 0.00
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerPercentage3(season, GoalConversion.__Property1, GoalConversion.__Property2, GoalConversion.__Property3, playerid)
	#	self.max = DAL.GetMaxPercentage3(season, GoalConversion.__Property1, GoalConversion.__Property2, GoalConversion.__Property3, GoalConversion.__Range)
	#	self.min = DAL.GetMinPercentage3(season, GoalConversion.__Property1, GoalConversion.__Property2, GoalConversion.__Property3, GoalConversion.__Range)

	
class PassingAccuratePercentage():
	
	__Property1 = 'accurate_pass'
	__Property2 = 'total_pass'
	__PropertyRange = 'total_fwd_zone_pass'
	__Range = 800
	Name = 'Passing %'
	Max = 92.62
	Min = 63.35
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerPercentage1(season, PassingAccuratePercentage.__Property1, PassingAccuratePercentage.__Property2, playerid)
	#	self.max = DAL.GetMaxPercentage1(season, PassingAccuratePercentage.__Property1, PassingAccuratePercentage.__Property2, PassingAccuratePercentage.__PropertyRange, PassingAccuratePercentage.__Range)
	#	self.min = DAL.GetMinPercentage1(season, PassingAccuratePercentage.__Property1, PassingAccuratePercentage.__Property2, PassingAccuratePercentage.__PropertyRange, PassingAccuratePercentage.__Range)


class SuccessfulFinalThirdPasses():
	
	__Property = 'successful_final_third_passes'
	Name = 'successful_final_third_passes'
	Max = 28.25
	Min = 0.12
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerAvg(season, SuccessfulFinalThirdPasses.__Property, playerid)
	#	self.max = DAL.GetMaxAvg(season, SuccessfulFinalThirdPasses.__Property)
	#	self.min = DAL.GetMinAvg(season, SuccessfulFinalThirdPasses.__Property)


class WasFouled():
	
	__Property = 'was_fouled'
	Name = 'was_fouled'
	Max = 4.79
	Min = 0.00
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerAvg(season, WasFouled.__Property, playerid)
	#	self.max = DAL.GetMaxAvg(season, WasFouled.__Property)
	#	self.min = DAL.GetMinAvg(season, WasFouled.__Property)


class WonContest():
	
	__Property = 'won_contest'
	Name = 'Won Contests'
	Max = 5.55
	Min = 0.00
	
	def __init__(self, season, playerid):
		self.player = DAL.GetPlayerAvg(season, WonContest.__Property, playerid)
	#	self.max = DAL.GetMaxAvg(season, WonContest.__Property)
	#	self.min = DAL.GetMinAvg(season, WonContest.__Property)