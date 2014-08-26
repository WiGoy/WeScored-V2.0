from flask import Flask, jsonify, render_template, request
import DAL, Player
import random

app = Flask(__name__)


@app.route('/_get_teams')
def get_teams():
	
	season = request.args.get('season', type=str)
	league = request.args.get('league', type=str)
	teams = DAL.GetTeams(season, league)
	
	return jsonify(result = teams)

	
@app.route('/_get_players')
def get_players():
	
	season = request.args.get('season', type=str)
	teamID = request.args.get('teamid', type=int)
	players = DAL.GetPlayers(season, teamID)
	
	return jsonify(result = players)
	

@app.route('/_scan_player')
def scan_player():
	
	season = request.args.get('season', type=str)
	playerID = request.args.get('playerid', type=int)
	fpMap = Player.ScannPlayer(season, playerID)
	
	return jsonify(result = fpMap)


@app.route('/')
def index():
	return render_template('index.html')

	
if __name__ == '__main__':  
	app.run(debug = True, host='0.0.0.0')