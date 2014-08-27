$(function() {
	var change_seasonorleague = function(e) {
		$.getJSON($SCRIPT_ROOT + '/_get_teams', {
			season:$('select[id="Season"]').val(),
			league:$('select[id="League"]').val()
		},
		function(data) {
			$('select#Teams').empty();
			$('select#Players').empty();
			$('select#Teams').append("<option>球队</option>");
			$('select#Players').append("<option>球员</option>");
			for (var i = 0; i < data.result.length; i++) {
				var option = $("<option>").val(data.result[i][0]).text(data.result[i][1]);
				$('select#Teams').append(option);
			}			
		});
	};
	
	var change_team = function(e) {
		$.getJSON($SCRIPT_ROOT + '/_get_players', {
			season:$('select[id="Season"]').val(),
			teamid:$('select[id="Teams"]').val()
		},
		function(data) {
			$('select#Players').empty();
			$('select#Players').append("<option>球员</option>");
			for (var i = 0; i < data.result.length; i++) {
				var option = $("<option>").val(data.result[i][0]).text(data.result[i][1]);
				$('select#Players').append(option);
			}
		});
	};
	
	var scan_player = function(e) {
		$.getJSON($SCRIPT_ROOT + '/_get_player_radar', {
			season:$('select[id="Season"]').val(),
			playerid:$('select[id="Players"]').val()
		},
		function(data) {
			$('img#Radar').attr("src", data.result);
		});
	};
	
	$('select#Season').bind('change', change_seasonorleague);
	$('select#League').bind('change', change_seasonorleague);
	$('select#Teams').bind('change', change_team);
	$('input#Drawing').bind('click', scan_player);
});