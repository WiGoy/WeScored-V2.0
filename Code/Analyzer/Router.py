'''
核心路由
'''
from flask import Flask, jsonify, render_template, request
import DAL, Player


app = Flask(__name__)


@app.route('/_get_teams')
def get_teams():
	'''
	根据赛季和联赛获取当季的球队
	'''
	season = request.args.get('season', type=str)
	league = request.args.get('league', type=str)
	
	if (league != 'League'):
		teamList = DAL.GetTeamList(season, league)
		return jsonify(result = teamList)
	else:
		return jsonify(result = None)

	
@app.route('/_get_players')
def get_players():
	'''
	根据赛季和球队获取该球队当季的球员
	'''
	season = request.args.get('season', type=str)
	teamID = request.args.get('teamid', type=int)
	playerList = DAL.GetPlayerList(season, teamID)
	
	return jsonify(result = playerList)
	

@app.route('/_get_player_radar')
def get_player_radar():
	'''
	获取球员的雷达图
	'''
	season = request.args.get('season', type=str)
	playerID = request.args.get('playerid', type=int)
	playerName = DAL.GetPlayerName(season, playerID)
	fpMap = Player.GetPlayerRadar(season, playerID, playerName)
	
	return jsonify(result = fpMap)


@app.route('/')
def index():
	'''
	显示主页
	'''
	return render_template('index.html')

	
if __name__ == '__main__':  
	app.run(debug = True, host='0.0.0.0')