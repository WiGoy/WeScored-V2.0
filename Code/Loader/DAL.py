﻿'''
将统计数据写入数据库
'''
import os, re, sqlite3, time
import Global, LoaderMatch


Re_FN_Match = re.compile(Global.Regex_FN_Match, re.I)


def InsertMatchInfo(cursorObj, matchInfo):
	'''
	将比赛统计写入数据库
	'''
	strInsert = 'INSERT INTO MatchInformation VALUES (' + str(matchInfo.id) + ', \"' + matchInfo.startTime + '\", \"' + matchInfo.league + '\", ' + str(matchInfo.homeTeamStat.id) + ', \"' + matchInfo.homeTeamStat.name + '\", ' + str(matchInfo.homeTeamStat.rating) + ', ' + str(matchInfo.homeTeamStat.goals) + ', ' + str(matchInfo.homeTeamPoints) + ', ' + str(matchInfo.awayTeamStat.id) + ', \"' + matchInfo.awayTeamStat.name + '\", ' + str(matchInfo.awayTeamStat.rating) + ', ' + str(matchInfo.awayTeamStat.goals) + ', ' + str(matchInfo.awayTeamPoints) + ', ' + str(matchInfo.manOfTheMatchPlayerID) + ', \"' + matchInfo.manOfTheMatchPlayerName + '\")'
	
	cursorObj.execute(strInsert)
	

def InsertTeamStatistics(cursorObj, matchID, league, home, teamStat):
	'''
	将球队数据写入数据库
	'''
	strInsert ='INSERT INTO TeamStatistics (team_id, team_name, league, match_id, home, rating, accurate_back_zone_pass, accurate_chipped_pass, accurate_corners_intobox, accurate_cross, accurate_cross_nocorner, accurate_flick_on, accurate_freekick_cross, accurate_fwd_zone_pass, accurate_goal_kicks, accurate_keeper_sweeper, accurate_keeper_throws, accurate_launches, accurate_layoffs, accurate_long_balls, accurate_pass, accurate_pull_back, accurate_through_ball, accurate_throws, aerial_lost, aerial_won, att_assist_openplay, att_assist_setplay, att_bx_centre, att_bx_left, att_bx_right, att_cmiss_high, att_cmiss_high_left, att_cmiss_high_right, att_cmiss_left, att_cmiss_right, att_fastbreak, att_freekick_goal, att_freekick_miss, att_freekick_post, att_freekick_target, att_freekick_total, att_goal_high_centre, att_goal_high_left, att_goal_high_right, att_goal_low_centre, att_goal_low_left, att_goal_low_right, att_hd_goal, att_hd_miss, att_hd_post, att_hd_target, att_hd_total, att_ibox_blocked, att_ibox_goal, att_ibox_miss, att_ibox_own_goal, att_ibox_post, att_ibox_target, att_lf_goal, att_lf_target, att_lf_total, att_lg_centre, att_lg_left, att_lg_right, att_miss_high, att_miss_high_left, att_miss_high_right, att_miss_left, att_miss_right, att_obox_blocked, att_obox_goal, att_obox_miss, att_obox_own_goal, att_obox_post, att_obox_target, att_obp_goal, att_obx_centre, att_obx_left, att_obx_right, att_obxd_left, att_obxd_right, att_one_on_one, att_openplay, att_pen_goal, att_pen_miss, att_pen_post, att_pen_target, att_post_high, att_post_left, att_post_right, att_rf_goal, att_rf_target, att_rf_total, att_setpiece, att_sv_high_centre, att_sv_high_left, att_sv_high_right, att_sv_low_centre, att_sv_low_left, att_sv_low_right, attempted_tackle_foul, attempts_conceded_ibox, attempts_conceded_obox, backward_pass, ball_recovery, big_chance_created, big_chance_missed, big_chance_scored, blocked_cross, blocked_pass, blocked_scoring_att, challenge_lost, clean_sheet, clearance_off_line, contentious_decision, corner_taken, cross_inaccurate, crosses_18yard, crosses_18yardplus, defender_goals, dispossessed, diving_save, dribble_lost, duel_ground_lost, duel_ground_won, duel_lost, duel_won, effective_blocked_cross, effective_clearance, effective_head_clearance, error_lead_to_goal, error_lead_to_shot, failed_to_block, fifty_fifty, final_third_entries, first_half_goals, fk_foul_lost, fk_foul_won, formation_used, forward_goals, foul_throw_in, fouled_final_third, freekick_cross, fwd_pass, goal_assist, goal_assist_deadball, goal_assist_intentional, goal_assist_openplay, goal_assist_setplay, goal_fastbreak, goal_kicks, goals, goals_conceded, goals_conceded_ibox, goals_conceded_obox, goals_openplay, good_high_claim, hand_ball, head_clearance, hit_woodwork, interception, interception_won, interceptions_in_box, keeper_throws, last_man_tackle, leftside_pass, long_pass_own_to_opp, long_pass_own_to_opp_success, lost_corners, midfielder_goals, offtarget_att_assist, ontarget_att_assist, ontarget_scoring_att, open_play_pass, outfielder_block, overrun, own_goal_accrued, own_goals, passes_left, passes_right, pen_area_entries, pen_goals_conceded, penalty_conceded, penalty_faced, penalty_missed, penalty_save, penalty_won, poss_lost_all, poss_lost_ctrl, poss_won_att_3rd, poss_won_def_3rd, poss_won_mid_3rd, possession_percentage, post_scoring_att, punches, put_through, rescinded_red_card, rightside_pass, saved_ibox, saved_obox, saves, second_yellow, shield_ball_oop, shot_fastbreak, shot_off_target, six_yard_block, subs_made, successful_fifty_fifty, successful_final_third_passes, successful_open_play_pass, successful_put_through, tackle_lost, total_att_assist, total_back_zone_pass, total_chipped_pass, total_clearance, total_contest, total_corners_intobox, total_cross, total_cross_nocorner, total_fastbreak, total_final_third_passes, total_flick_on, total_fwd_zone_pass, total_high_claim, total_keeper_sweeper, total_launches, total_layoffs, total_long_balls, total_offside, total_pass, total_pull_back, total_red_card, total_scoring_att, total_tackle, total_through_ball, total_throws, total_yel_card, touches, unsuccessful_touch, won_contest, won_corners, won_tackle) VALUES (' + str(teamStat.id) + ', \"' + teamStat.name + '\", \"' + league + '\", ' + str(matchID) + ', ' + str(home) + ', ' + str(teamStat.rating) + ', ' + str(teamStat.accurate_back_zone_pass) + ', ' + str(teamStat.accurate_chipped_pass) + ', ' + str(teamStat.accurate_corners_intobox) + ', ' + str(teamStat.accurate_cross) + ', ' + str(teamStat.accurate_cross_nocorner) + ', ' + str(teamStat.accurate_flick_on) + ', ' + str(teamStat.accurate_freekick_cross) + ', ' + str(teamStat.accurate_fwd_zone_pass) + ', ' + str(teamStat.accurate_goal_kicks) + ', ' + str(teamStat.accurate_keeper_sweeper) + ', ' + str(teamStat.accurate_keeper_throws) + ', ' + str(teamStat.accurate_launches) + ', ' + str(teamStat.accurate_layoffs) + ', ' + str(teamStat.accurate_long_balls) + ', ' + str(teamStat.accurate_pass) + ', ' + str(teamStat.accurate_pull_back) + ', ' + str(teamStat.accurate_through_ball) + ', ' + str(teamStat.accurate_throws) + ', ' + str(teamStat.aerial_lost) + ', ' + str(teamStat.aerial_won) + ', ' + str(teamStat.att_assist_openplay) + ', ' + str(teamStat.att_assist_setplay) + ', ' + str(teamStat.att_bx_centre) + ', ' + str(teamStat.att_bx_left) + ', ' + str(teamStat.att_bx_right) + ', ' + str(teamStat.att_cmiss_high) + ', ' + str(teamStat.att_cmiss_high_left) + ', ' + str(teamStat.att_cmiss_high_right) + ', ' + str(teamStat.att_cmiss_left) + ', ' + str(teamStat.att_cmiss_right) + ', ' + str(teamStat.att_fastbreak) + ', ' + str(teamStat.att_freekick_goal) + ', ' + str(teamStat.att_freekick_miss) + ', ' + str(teamStat.att_freekick_post) + ', ' + str(teamStat.att_freekick_target) + ', ' + str(teamStat.att_freekick_total) + ', ' + str(teamStat.att_goal_high_centre) + ', ' + str(teamStat.att_goal_high_left) + ', ' + str(teamStat.att_goal_high_right) + ', ' + str(teamStat.att_goal_low_centre) + ', ' + str(teamStat.att_goal_low_left) + ', ' + str(teamStat.att_goal_low_right) + ', ' + str(teamStat.att_hd_goal) + ', ' + str(teamStat.att_hd_miss) + ', ' + str(teamStat.att_hd_post) + ', ' + str(teamStat.att_hd_target) + ', ' + str(teamStat.att_hd_total) + ', ' + str(teamStat.att_ibox_blocked) + ', ' + str(teamStat.att_ibox_goal) + ', ' + str(teamStat.att_ibox_miss) + ', ' + str(teamStat.att_ibox_own_goal) + ', ' + str(teamStat.att_ibox_post) + ', ' + str(teamStat.att_ibox_target) + ', ' + str(teamStat.att_lf_goal) + ', ' + str(teamStat.att_lf_target) + ', ' + str(teamStat.att_lf_total) + ', ' + str(teamStat.att_lg_centre) + ', ' + str(teamStat.att_lg_left) + ', ' + str(teamStat.att_lg_right) + ', ' + str(teamStat.att_miss_high) + ', ' + str(teamStat.att_miss_high_left) + ', ' + str(teamStat.att_miss_high_right) + ', ' + str(teamStat.att_miss_left) + ', ' + str(teamStat.att_miss_right) + ', ' + str(teamStat.att_obox_blocked) + ', ' + str(teamStat.att_obox_goal) + ', ' + str(teamStat.att_obox_miss) + ', ' + str(teamStat.att_obox_own_goal) + ', ' + str(teamStat.att_obox_post) + ', ' + str(teamStat.att_obox_target) + ', ' + str(teamStat.att_obp_goal) + ', ' + str(teamStat.att_obx_centre) + ', ' + str(teamStat.att_obx_left) + ', ' + str(teamStat.att_obx_right) + ', ' + str(teamStat.att_obxd_left) + ', ' + str(teamStat.att_obxd_right) + ', ' + str(teamStat.att_one_on_one) + ', ' + str(teamStat.att_openplay) + ', ' + str(teamStat.att_pen_goal) + ', ' + str(teamStat.att_pen_miss) + ', ' + str(teamStat.att_pen_post) + ', ' + str(teamStat.att_pen_target) + ', ' + str(teamStat.att_post_high) + ', ' + str(teamStat.att_post_left) + ', ' + str(teamStat.att_post_right) + ', ' + str(teamStat.att_rf_goal) + ', ' + str(teamStat.att_rf_target) + ', ' + str(teamStat.att_rf_total) + ', ' + str(teamStat.att_setpiece) + ', ' + str(teamStat.att_sv_high_centre) + ', ' + str(teamStat.att_sv_high_left) + ', ' + str(teamStat.att_sv_high_right) + ', ' + str(teamStat.att_sv_low_centre) + ', ' + str(teamStat.att_sv_low_left) + ', ' + str(teamStat.att_sv_low_right) + ', ' + str(teamStat.attempted_tackle_foul) + ', ' + str(teamStat.attempts_conceded_ibox) + ', ' + str(teamStat.attempts_conceded_obox) + ', ' + str(teamStat.backward_pass) + ', ' + str(teamStat.ball_recovery) + ', ' + str(teamStat.big_chance_created) + ', ' + str(teamStat.big_chance_missed) + ', ' + str(teamStat.big_chance_scored) + ', ' + str(teamStat.blocked_cross) + ', ' + str(teamStat.blocked_pass) + ', ' + str(teamStat.blocked_scoring_att) + ', ' + str(teamStat.challenge_lost) + ', ' + str(teamStat.clean_sheet) + ', ' + str(teamStat.clearance_off_line) + ', ' + str(teamStat.contentious_decision) + ', ' + str(teamStat.corner_taken) + ', ' + str(teamStat.cross_inaccurate) + ', ' + str(teamStat.crosses_18yard) + ', ' + str(teamStat.crosses_18yardplus) + ', ' + str(teamStat.defender_goals) + ', ' + str(teamStat.dispossessed) + ', ' + str(teamStat.diving_save) + ', ' + str(teamStat.dribble_lost) + ', ' + str(teamStat.duel_ground_lost) + ', ' + str(teamStat.duel_ground_won) + ', ' + str(teamStat.duel_lost) + ', ' + str(teamStat.duel_won) + ', ' + str(teamStat.effective_blocked_cross) + ', ' + str(teamStat.effective_clearance) + ', ' + str(teamStat.effective_head_clearance) + ', ' + str(teamStat.error_lead_to_goal) + ', ' + str(teamStat.error_lead_to_shot) + ', ' + str(teamStat.failed_to_block) + ', ' + str(teamStat.fifty_fifty) + ', ' + str(teamStat.final_third_entries) + ', ' + str(teamStat.first_half_goals) + ', ' + str(teamStat.fk_foul_lost) + ', ' + str(teamStat.fk_foul_won) + ', ' + str(teamStat.formation_used) + ', ' + str(teamStat.forward_goals) + ', ' + str(teamStat.foul_throw_in) + ', ' + str(teamStat.fouled_final_third) + ', ' + str(teamStat.freekick_cross) + ', ' + str(teamStat.fwd_pass) + ', ' + str(teamStat.goal_assist) + ', ' + str(teamStat.goal_assist_deadball) + ', ' + str(teamStat.goal_assist_intentional) + ', ' + str(teamStat.goal_assist_openplay) + ', ' + str(teamStat.goal_assist_setplay) + ', ' + str(teamStat.goal_fastbreak) + ', ' + str(teamStat.goal_kicks) + ', ' + str(teamStat.goals) + ', ' + str(teamStat.goals_conceded) + ', ' + str(teamStat.goals_conceded_ibox) + ', ' + str(teamStat.goals_conceded_obox) + ', ' + str(teamStat.goals_openplay) + ', ' + str(teamStat.good_high_claim) + ', ' + str(teamStat.hand_ball) + ', ' + str(teamStat.head_clearance) + ', ' + str(teamStat.hit_woodwork) + ', ' + str(teamStat.interception) + ', ' + str(teamStat.interception_won) + ', ' + str(teamStat.interceptions_in_box) + ', ' + str(teamStat.keeper_throws) + ', ' + str(teamStat.last_man_tackle) + ', ' + str(teamStat.leftside_pass) + ', ' + str(teamStat.long_pass_own_to_opp) + ', ' + str(teamStat.long_pass_own_to_opp_success) + ', ' + str(teamStat.lost_corners) + ', ' + str(teamStat.midfielder_goals) + ', ' + str(teamStat.offtarget_att_assist) + ', ' + str(teamStat.ontarget_att_assist) + ', ' + str(teamStat.ontarget_scoring_att) + ', ' + str(teamStat.open_play_pass) + ', ' + str(teamStat.outfielder_block) + ', ' + str(teamStat.overrun) + ', ' + str(teamStat.own_goal_accrued) + ', ' + str(teamStat.own_goals) + ', ' + str(teamStat.passes_left) + ', ' + str(teamStat.passes_right) + ', ' + str(teamStat.pen_area_entries) + ', ' + str(teamStat.pen_goals_conceded) + ', ' + str(teamStat.penalty_conceded) + ', ' + str(teamStat.penalty_faced) + ', ' + str(teamStat.penalty_missed) + ', ' + str(teamStat.penalty_save) + ', ' + str(teamStat.penalty_won) + ', ' + str(teamStat.poss_lost_all) + ', ' + str(teamStat.poss_lost_ctrl) + ', ' + str(teamStat.poss_won_att_3rd) + ', ' + str(teamStat.poss_won_def_3rd) + ', ' + str(teamStat.poss_won_mid_3rd) + ', ' + str(teamStat.possession_percentage) + ', ' + str(teamStat.post_scoring_att) + ', ' + str(teamStat.punches) + ', ' + str(teamStat.put_through) + ', ' + str(teamStat.rescinded_red_card) + ', ' + str(teamStat.rightside_pass) + ', ' + str(teamStat.saved_ibox) + ', ' + str(teamStat.saved_obox) + ', ' + str(teamStat.saves) + ', ' + str(teamStat.second_yellow) + ', ' + str(teamStat.shield_ball_oop) + ', ' + str(teamStat.shot_fastbreak) + ', ' + str(teamStat.shot_off_target) + ', ' + str(teamStat.six_yard_block) + ', ' + str(teamStat.subs_made) + ', ' + str(teamStat.successful_fifty_fifty) + ', ' + str(teamStat.successful_final_third_passes) + ', ' + str(teamStat.successful_open_play_pass) + ', ' + str(teamStat.successful_put_through) + ', ' + str(teamStat.tackle_lost) + ', ' + str(teamStat.total_att_assist) + ', ' + str(teamStat.total_back_zone_pass) + ', ' + str(teamStat.total_chipped_pass) + ', ' + str(teamStat.total_clearance) + ', ' + str(teamStat.total_contest) + ', ' + str(teamStat.total_corners_intobox) + ', ' + str(teamStat.total_cross) + ', ' + str(teamStat.total_cross_nocorner) + ', ' + str(teamStat.total_fastbreak) + ', ' + str(teamStat.total_final_third_passes) + ', ' + str(teamStat.total_flick_on) + ', ' + str(teamStat.total_fwd_zone_pass) + ', ' + str(teamStat.total_high_claim) + ', ' + str(teamStat.total_keeper_sweeper) + ', ' + str(teamStat.total_launches) + ', ' + str(teamStat.total_layoffs) + ', ' + str(teamStat.total_long_balls) + ', ' + str(teamStat.total_offside) + ', ' + str(teamStat.total_pass) + ', ' + str(teamStat.total_pull_back) + ', ' + str(teamStat.total_red_card) + ', ' + str(teamStat.total_scoring_att) + ', ' + str(teamStat.total_tackle) + ', ' + str(teamStat.total_through_ball) + ', ' + str(teamStat.total_throws) + ', ' + str(teamStat.total_yel_card) + ', ' + str(teamStat.touches) + ', ' + str(teamStat.unsuccessful_touch) + ', ' + str(teamStat.won_contest) + ', ' + str(teamStat.won_corners) + ', ' + str(teamStat.won_tackle) + ')'	
	
	cursorObj.execute(strInsert)


def InsertPlayerStatistics(cursorObj, matchID, league, home, teamID, teamName, playerStat):
	'''
	将球员数据写入数据库
	'''
	strInsert = 'INSERT INTO PlayerStatistics (player_id, player_name, team_id, team_name, league, match_id, home, accurate_back_zone_pass, accurate_chipped_pass, accurate_corners_intobox, accurate_cross, accurate_cross_nocorner, accurate_flick_on, accurate_freekick_cross, accurate_fwd_zone_pass, accurate_goal_kicks, accurate_keeper_sweeper, accurate_keeper_throws, accurate_launches, accurate_layoffs, accurate_long_balls, accurate_pass, accurate_pull_back, accurate_through_ball, accurate_throws, aerial_lost, aerial_won, assist_attempt_saved, assist_blocked_shot, assist_free_kick_won, assist_handball_won, assist_own_goal, assist_pass_lost, assist_penalty_won, assist_post, att_assist_openplay, att_assist_setplay, att_bx_centre, att_bx_left, att_bx_right, att_cmiss_high, att_cmiss_high_left, att_cmiss_high_right, att_cmiss_left, att_cmiss_right, att_fastbreak, att_freekick_goal, att_freekick_miss, att_freekick_post, att_freekick_target, att_freekick_total, att_goal_high_centre, att_goal_high_left, att_goal_high_right, att_goal_low_centre, att_goal_low_left, att_goal_low_right, att_hd_goal, att_hd_miss, att_hd_post, att_hd_target, att_hd_total, att_ibox_blocked, att_ibox_goal, att_ibox_miss, att_ibox_post, att_ibox_target, att_lf_goal, att_lf_target, att_lf_total, att_lg_centre, att_lg_left, att_lg_right, att_miss_high, att_miss_high_left, att_miss_high_right, att_miss_left, att_miss_right, att_obox_blocked, att_obox_goal, att_obox_miss, att_obox_post, att_obox_target, att_obp_goal, att_obx_centre, att_obx_left, att_obx_right, att_obxd_left, att_obxd_right, att_one_on_one, att_openplay, att_pen_goal, att_pen_miss, att_pen_post, att_pen_target, att_post_high, att_post_left, att_post_right, att_rf_goal, att_rf_target, att_rf_total, att_setpiece, att_sv_high_centre, att_sv_high_left, att_sv_high_right, att_sv_low_centre, att_sv_low_left, att_sv_low_right, attempted_tackle_foul, attempts_conceded_ibox, attempts_conceded_obox, back_pass, backward_pass, ball_recovery, big_chance_created, big_chance_missed, big_chance_scored, blocked_cross, blocked_pass, blocked_scoring_att, challenge_lost, clean_sheet_amc, clean_sheet_aml, clean_sheet_amr, clean_sheet_dc, clean_sheet_dl, clean_sheet_dmc, clean_sheet_dml, clean_sheet_dmr, clean_sheet_dr, clean_sheet_fw, clean_sheet_fwl, clean_sheet_fwr, clean_sheet_gk, clean_sheet_mc, clean_sheet_ml, clean_sheet_mr, clearance_off_line, corner_taken, cross_inaccurate, cross_not_claimed, crosses_18yard, crosses_18yardplus, dangerous_play, dispossessed, dive_catch, dive_save, diving_save, dribble_lost, duel_ground_lost, duel_ground_won, duel_lost, duel_won, effective_blocked_cross, effective_clearance, effective_head_clearance, error_lead_to_goal, error_lead_to_shot, failed_to_block, fifty_fifty, final_third_entries, formation_place, foul_throw_in, fouled_final_third, fouls, freekick_cross, fwd_pass, game_started, gk_smother, goal_assist, goal_assist_deadball, goal_assist_intentional, goal_assist_openplay, goal_assist_setplay, goal_fastbreak, goal_kicks, goal_normal, goal_scored_by_team_amc, goal_scored_by_team_aml, goal_scored_by_team_amr, goal_scored_by_team_dc, goal_scored_by_team_dl, goal_scored_by_team_dmc, goal_scored_by_team_dml, goal_scored_by_team_dmr, goal_scored_by_team_dr, goal_scored_by_team_fw, goal_scored_by_team_fwl, goal_scored_by_team_fwr, goal_scored_by_team_gk, goal_scored_by_team_mc, goal_scored_by_team_ml, goal_scored_by_team_mr, goal_scored_by_team_sub, goals, goals_conceded_amc, goals_conceded_aml, goals_conceded_amr, goals_conceded_dc, goals_conceded_dl, goals_conceded_dmc, goals_conceded_dml, goals_conceded_dmr, goals_conceded_dr, goals_conceded_fw, goals_conceded_fwl, goals_conceded_fwr, goals_conceded_gk, goals_conceded_ibox, goals_conceded_mc, goals_conceded_ml, goals_conceded_mr, goals_conceded_obox_amc, goals_conceded_obox_aml, goals_conceded_obox_amr, goals_conceded_obox_dc, goals_conceded_obox_dl, goals_conceded_obox_dmc, goals_conceded_obox_dml, goals_conceded_obox_dmr, goals_conceded_obox_dr, goals_conceded_obox_fw, goals_conceded_obox_fwl, goals_conceded_obox_fwr, goals_conceded_obox_gk, goals_conceded_obox_mc, goals_conceded_obox_ml, goals_conceded_obox_mr, goals_conceded_obox_sub, goals_conceded_sub, goals_openplay, good_high_claim, hand_ball, head_clearance, head_pass, hit_woodwork, interception, interception_won, interceptions_in_box, keeper_claim_high_lost, keeper_claim_lost, keeper_pick_up, keeper_sweeper_lost, keeper_throws, last_man_tackle, leftside_pass, long_pass_own_to_opp, long_pass_own_to_opp_success, lost_corners, man_of_the_match, mins_played, offside_provoked, offtarget_att_assist, ontarget_att_assist, ontarget_scoring_att, open_play_pass, outfielder_block, overrun, own_goals, pass_backzone_inaccurate, pass_forwardzone_inaccurate, pass_inaccurate, pass_longball_inaccurate, pass_throughball_inacurate, passes_left, passes_right, pen_area_entries, pen_goals_conceded, penalty_conceded, penalty_faced, penalty_missed, penalty_save, penalty_shootout_conceded_gk, penalty_shootout_missed_off_target, penalty_shootout_saved, penalty_shootout_saved_gk, penalty_shootout_scored, penalty_won, poss_lost_all, poss_lost_ctrl, poss_won_att_3rd, poss_won_def_3rd, poss_won_mid_3rd, post_scoring_att, punches, put_through, rating, rating_defensive, rating_defensive_points, rating_offensive, rating_offensive_points, rating_points, red_card, rescinded_red_card, rightside_pass, saved_ibox, saved_obox, saves, second_goal_assist, second_yellow, shield_ball_oop, shot_fastbreak, shot_off_target, six_second_violation, six_yard_block, stand_catch, stand_save, successful_fifty_fifty, successful_final_third_passes, successful_open_play_pass, successful_put_through, tackle_lost, total_att_assist, total_back_zone_pass, total_chipped_pass, total_clearance, total_contest, total_corners_intobox, total_cross, total_cross_nocorner, total_fastbreak, total_final_third_passes, total_flick_on, total_fwd_zone_pass, total_high_claim, total_keeper_sweeper, total_launches, total_layoffs, total_long_balls, total_offside, total_pass, total_pull_back, total_scoring_att, total_sub_off, total_sub_on, total_tackle, total_through_ball, total_throws, touches, turnover, unsuccessful_touch, was_fouled, won_contest, won_corners, won_tackle, yellow_card) VALUES (' + str(playerStat.id) + ', \"' + playerStat.name + '\", ' + str(teamID) + ', \"' + teamName + '\", \"' + league + '\", ' + str(matchID) + ', ' + str(home) + ', ' + str(playerStat.accurate_back_zone_pass) + ', ' + str(playerStat.accurate_chipped_pass) + ', ' + str(playerStat.accurate_corners_intobox) + ', ' + str(playerStat.accurate_cross) + ', ' + str(playerStat.accurate_cross_nocorner) + ', ' + str(playerStat.accurate_flick_on) + ', ' + str(playerStat.accurate_freekick_cross) + ', ' + str(playerStat.accurate_fwd_zone_pass) + ', ' + str(playerStat.accurate_goal_kicks) + ', ' + str(playerStat.accurate_keeper_sweeper) + ', ' + str(playerStat.accurate_keeper_throws) + ', ' + str(playerStat.accurate_launches) + ', ' + str(playerStat.accurate_layoffs) + ', ' + str(playerStat.accurate_long_balls) + ', ' + str(playerStat.accurate_pass) + ', ' + str(playerStat.accurate_pull_back) + ', ' + str(playerStat.accurate_through_ball) + ', ' + str(playerStat.accurate_throws) + ', ' + str(playerStat.aerial_lost) + ', ' + str(playerStat.aerial_won) + ', ' + str(playerStat.assist_attempt_saved) + ', ' + str(playerStat.assist_blocked_shot) + ', ' + str(playerStat.assist_free_kick_won) + ', ' + str(playerStat.assist_handball_won) + ', ' + str(playerStat.assist_own_goal) + ', ' + str(playerStat.assist_pass_lost) + ', ' + str(playerStat.assist_penalty_won) + ', ' + str(playerStat.assist_post) + ', ' + str(playerStat.att_assist_openplay) + ', ' + str(playerStat.att_assist_setplay) + ', ' + str(playerStat.att_bx_centre) + ', ' + str(playerStat.att_bx_left) + ', ' + str(playerStat.att_bx_right) + ', ' + str(playerStat.att_cmiss_high) + ', ' + str(playerStat.att_cmiss_high_left) + ', ' + str(playerStat.att_cmiss_high_right) + ', ' + str(playerStat.att_cmiss_left) + ', ' + str(playerStat.att_cmiss_right) + ', ' + str(playerStat.att_fastbreak) + ', ' + str(playerStat.att_freekick_goal) + ', ' + str(playerStat.att_freekick_miss) + ', ' + str(playerStat.att_freekick_post) + ', ' + str(playerStat.att_freekick_target) + ', ' + str(playerStat.att_freekick_total) + ', ' + str(playerStat.att_goal_high_centre) + ', ' + str(playerStat.att_goal_high_left) + ', ' + str(playerStat.att_goal_high_right) + ', ' + str(playerStat.att_goal_low_centre) + ', ' + str(playerStat.att_goal_low_left) + ', ' + str(playerStat.att_goal_low_right) + ', ' + str(playerStat.att_hd_goal) + ', ' + str(playerStat.att_hd_miss) + ', ' + str(playerStat.att_hd_post) + ', ' + str(playerStat.att_hd_target) + ', ' + str(playerStat.att_hd_total) + ', ' + str(playerStat.att_ibox_blocked) + ', ' + str(playerStat.att_ibox_goal) + ', ' + str(playerStat.att_ibox_miss) + ', ' + str(playerStat.att_ibox_post) + ', ' + str(playerStat.att_ibox_target) + ', ' + str(playerStat.att_lf_goal) + ', ' + str(playerStat.att_lf_target) + ', ' + str(playerStat.att_lf_total) + ', ' + str(playerStat.att_lg_centre) + ', ' + str(playerStat.att_lg_left) + ', ' + str(playerStat.att_lg_right) + ', ' + str(playerStat.att_miss_high) + ', ' + str(playerStat.att_miss_high_left) + ', ' + str(playerStat.att_miss_high_right) + ', ' + str(playerStat.att_miss_left) + ', ' + str(playerStat.att_miss_right) + ', ' + str(playerStat.att_obox_blocked) + ', ' + str(playerStat.att_obox_goal) + ', ' + str(playerStat.att_obox_miss) + ', ' + str(playerStat.att_obox_post) + ', ' + str(playerStat.att_obox_target) + ', ' + str(playerStat.att_obp_goal) + ', ' + str(playerStat.att_obx_centre) + ', ' + str(playerStat.att_obx_left) + ', ' + str(playerStat.att_obx_right) + ', ' + str(playerStat.att_obxd_left) + ', ' + str(playerStat.att_obxd_right) + ', ' + str(playerStat.att_one_on_one) + ', ' + str(playerStat.att_openplay) + ', ' + str(playerStat.att_pen_goal) + ', ' + str(playerStat.att_pen_miss) + ', ' + str(playerStat.att_pen_post) + ', ' + str(playerStat.att_pen_target) + ', ' + str(playerStat.att_post_high) + ', ' + str(playerStat.att_post_left) + ', ' + str(playerStat.att_post_right) + ', ' + str(playerStat.att_rf_goal) + ', ' + str(playerStat.att_rf_target) + ', ' + str(playerStat.att_rf_total) + ', ' + str(playerStat.att_setpiece) + ', ' + str(playerStat.att_sv_high_centre) + ', ' + str(playerStat.att_sv_high_left) + ', ' + str(playerStat.att_sv_high_right) + ', ' + str(playerStat.att_sv_low_centre) + ', ' + str(playerStat.att_sv_low_left) + ', ' + str(playerStat.att_sv_low_right) + ', ' + str(playerStat.attempted_tackle_foul) + ', ' + str(playerStat.attempts_conceded_ibox) + ', ' + str(playerStat.attempts_conceded_obox) + ', ' + str(playerStat.back_pass) + ', ' + str(playerStat.backward_pass) + ', ' + str(playerStat.ball_recovery) + ', ' + str(playerStat.big_chance_created) + ', ' + str(playerStat.big_chance_missed) + ', ' + str(playerStat.big_chance_scored) + ', ' + str(playerStat.blocked_cross) + ', ' + str(playerStat.blocked_pass) + ', ' + str(playerStat.blocked_scoring_att) + ', ' + str(playerStat.challenge_lost) + ', ' + str(playerStat.clean_sheet_amc) + ', ' + str(playerStat.clean_sheet_aml) + ', ' + str(playerStat.clean_sheet_amr) + ', ' + str(playerStat.clean_sheet_dc) + ', ' + str(playerStat.clean_sheet_dl) + ', ' + str(playerStat.clean_sheet_dmc) + ', ' + str(playerStat.clean_sheet_dml) + ', ' + str(playerStat.clean_sheet_dmr) + ', ' + str(playerStat.clean_sheet_dr) + ', ' + str(playerStat.clean_sheet_fw) + ', ' + str(playerStat.clean_sheet_fwl) + ', ' + str(playerStat.clean_sheet_fwr) + ', ' + str(playerStat.clean_sheet_gk) + ', ' + str(playerStat.clean_sheet_mc) + ', ' + str(playerStat.clean_sheet_ml) + ', ' + str(playerStat.clean_sheet_mr) + ', ' + str(playerStat.clearance_off_line) + ', ' + str(playerStat.corner_taken) + ', ' + str(playerStat.cross_inaccurate) + ', ' + str(playerStat.cross_not_claimed) + ', ' + str(playerStat.crosses_18yard) + ', ' + str(playerStat.crosses_18yardplus) + ', ' + str(playerStat.dangerous_play) + ', ' + str(playerStat.dispossessed) + ', ' + str(playerStat.dive_catch) + ', ' + str(playerStat.dive_save) + ', ' + str(playerStat.diving_save) + ', ' + str(playerStat.dribble_lost) + ', ' + str(playerStat.duel_ground_lost) + ', ' + str(playerStat.duel_ground_won) + ', ' + str(playerStat.duel_lost) + ', ' + str(playerStat.duel_won) + ', ' + str(playerStat.effective_blocked_cross) + ', ' + str(playerStat.effective_clearance) + ', ' + str(playerStat.effective_head_clearance) + ', ' + str(playerStat.error_lead_to_goal) + ', ' + str(playerStat.error_lead_to_shot) + ', ' + str(playerStat.failed_to_block) + ', ' + str(playerStat.fifty_fifty) + ', ' + str(playerStat.final_third_entries) + ', ' + str(playerStat.formation_place) + ', ' + str(playerStat.foul_throw_in) + ', ' + str(playerStat.fouled_final_third) + ', ' + str(playerStat.fouls) + ', ' + str(playerStat.freekick_cross) + ', ' + str(playerStat.fwd_pass) + ', ' + str(playerStat.game_started) + ', ' + str(playerStat.gk_smother) + ', ' + str(playerStat.goal_assist) + ', ' + str(playerStat.goal_assist_deadball) + ', ' + str(playerStat.goal_assist_intentional) + ', ' + str(playerStat.goal_assist_openplay) + ', ' + str(playerStat.goal_assist_setplay) + ', ' + str(playerStat.goal_fastbreak) + ', ' + str(playerStat.goal_kicks) + ', ' + str(playerStat.goal_normal) + ', ' + str(playerStat.goal_scored_by_team_amc) + ', ' + str(playerStat.goal_scored_by_team_aml) + ', ' + str(playerStat.goal_scored_by_team_amr) + ', ' + str(playerStat.goal_scored_by_team_dc) + ', ' + str(playerStat.goal_scored_by_team_dl) + ', ' + str(playerStat.goal_scored_by_team_dmc) + ', ' + str(playerStat.goal_scored_by_team_dml) + ', ' + str(playerStat.goal_scored_by_team_dmr) + ', ' + str(playerStat.goal_scored_by_team_dr) + ', ' + str(playerStat.goal_scored_by_team_fw) + ', ' + str(playerStat.goal_scored_by_team_fwl) + ', ' + str(playerStat.goal_scored_by_team_fwr) + ', ' + str(playerStat.goal_scored_by_team_gk) + ', ' + str(playerStat.goal_scored_by_team_mc) + ', ' + str(playerStat.goal_scored_by_team_ml) + ', ' + str(playerStat.goal_scored_by_team_mr) + ', ' + str(playerStat.goal_scored_by_team_sub) + ', ' + str(playerStat.goals) + ', ' + str(playerStat.goals_conceded_amc) + ', ' + str(playerStat.goals_conceded_aml) + ', ' + str(playerStat.goals_conceded_amr) + ', ' + str(playerStat.goals_conceded_dc) + ', ' + str(playerStat.goals_conceded_dl) + ', ' + str(playerStat.goals_conceded_dmc) + ', ' + str(playerStat.goals_conceded_dml) + ', ' + str(playerStat.goals_conceded_dmr) + ', ' + str(playerStat.goals_conceded_dr) + ', ' + str(playerStat.goals_conceded_fw) + ', ' + str(playerStat.goals_conceded_fwl) + ', ' + str(playerStat.goals_conceded_fwr) + ', ' + str(playerStat.goals_conceded_gk) + ', ' + str(playerStat.goals_conceded_ibox) + ', ' + str(playerStat.goals_conceded_mc) + ', ' + str(playerStat.goals_conceded_ml) + ', ' + str(playerStat.goals_conceded_mr) + ', ' + str(playerStat.goals_conceded_obox_amc) + ', ' + str(playerStat.goals_conceded_obox_aml) + ', ' + str(playerStat.goals_conceded_obox_amr) + ', ' + str(playerStat.goals_conceded_obox_dc) + ', ' + str(playerStat.goals_conceded_obox_dl) + ', ' + str(playerStat.goals_conceded_obox_dmc) + ', ' + str(playerStat.goals_conceded_obox_dml) + ', ' + str(playerStat.goals_conceded_obox_dmr) + ', ' + str(playerStat.goals_conceded_obox_dr) + ', ' + str(playerStat.goals_conceded_obox_fw) + ', ' + str(playerStat.goals_conceded_obox_fwl) + ', ' + str(playerStat.goals_conceded_obox_fwr) + ', ' + str(playerStat.goals_conceded_obox_gk) + ', ' + str(playerStat.goals_conceded_obox_mc) + ', ' + str(playerStat.goals_conceded_obox_ml) + ', ' + str(playerStat.goals_conceded_obox_mr) + ', ' + str(playerStat.goals_conceded_obox_sub) + ', ' + str(playerStat.goals_conceded_sub) + ', ' + str(playerStat.goals_openplay) + ', ' + str(playerStat.good_high_claim) + ', ' + str(playerStat.hand_ball) + ', ' + str(playerStat.head_clearance) + ', ' + str(playerStat.head_pass) + ', ' + str(playerStat.hit_woodwork) + ', ' + str(playerStat.interception) + ', ' + str(playerStat.interception_won) + ', ' + str(playerStat.interceptions_in_box) + ', ' + str(playerStat.keeper_claim_high_lost) + ', ' + str(playerStat.keeper_claim_lost) + ', ' + str(playerStat.keeper_pick_up) + ', ' + str(playerStat.keeper_sweeper_lost) + ', ' + str(playerStat.keeper_throws) + ', ' + str(playerStat.last_man_tackle) + ', ' + str(playerStat.leftside_pass) + ', ' + str(playerStat.long_pass_own_to_opp) + ', ' + str(playerStat.long_pass_own_to_opp_success) + ', ' + str(playerStat.lost_corners) + ', ' + str(playerStat.man_of_the_match) + ', ' + str(playerStat.mins_played) + ', ' + str(playerStat.offside_provoked) + ', ' + str(playerStat.offtarget_att_assist) + ', ' + str(playerStat.ontarget_att_assist) + ', ' + str(playerStat.ontarget_scoring_att) + ', ' + str(playerStat.open_play_pass) + ', ' + str(playerStat.outfielder_block) + ', ' + str(playerStat.overrun) + ', ' + str(playerStat.own_goals) + ', ' + str(playerStat.pass_backzone_inaccurate) + ', ' + str(playerStat.pass_forwardzone_inaccurate) + ', ' + str(playerStat.pass_inaccurate) + ', ' + str(playerStat.pass_longball_inaccurate) + ', ' + str(playerStat.pass_throughball_inacurate) + ', ' + str(playerStat.passes_left) + ', ' + str(playerStat.passes_right) + ', ' + str(playerStat.pen_area_entries) + ', ' + str(playerStat.pen_goals_conceded) + ', ' + str(playerStat.penalty_conceded) + ', ' + str(playerStat.penalty_faced) + ', ' + str(playerStat.penalty_missed) + ', ' + str(playerStat.penalty_save) + ', ' + str(playerStat.penalty_shootout_conceded_gk) + ', ' + str(playerStat.penalty_shootout_missed_off_target) + ', ' + str(playerStat.penalty_shootout_saved) + ', ' + str(playerStat.penalty_shootout_saved_gk) + ', ' + str(playerStat.penalty_shootout_scored) + ', ' + str(playerStat.penalty_won) + ', ' + str(playerStat.poss_lost_all) + ', ' + str(playerStat.poss_lost_ctrl) + ', ' + str(playerStat.poss_won_att_3rd) + ', ' + str(playerStat.poss_won_def_3rd) + ', ' + str(playerStat.poss_won_mid_3rd) + ', ' + str(playerStat.post_scoring_att) + ', ' + str(playerStat.punches) + ', ' + str(playerStat.put_through) + ', ' + str(playerStat.rating) + ', ' + str(playerStat.rating_defensive) + ', ' + str(playerStat.rating_defensive_points) + ', ' + str(playerStat.rating_offensive) + ', ' + str(playerStat.rating_offensive_points) + ', ' + str(playerStat.rating_points) + ', ' + str(playerStat.red_card) + ', ' + str(playerStat.rescinded_red_card) + ', ' + str(playerStat.rightside_pass) + ', ' + str(playerStat.saved_ibox) + ', ' + str(playerStat.saved_obox) + ', ' + str(playerStat.saves) + ', ' + str(playerStat.second_goal_assist) + ', ' + str(playerStat.second_yellow) + ', ' + str(playerStat.shield_ball_oop) + ', ' + str(playerStat.shot_fastbreak) + ', ' + str(playerStat.shot_off_target) + ', ' + str(playerStat.six_second_violation) + ', ' + str(playerStat.six_yard_block) + ', ' + str(playerStat.stand_catch) + ', ' + str(playerStat.stand_save) + ', ' + str(playerStat.successful_fifty_fifty) + ', ' + str(playerStat.successful_final_third_passes) + ', ' + str(playerStat.successful_open_play_pass) + ', ' + str(playerStat.successful_put_through) + ', ' + str(playerStat.tackle_lost) + ', ' + str(playerStat.total_att_assist) + ', ' + str(playerStat.total_back_zone_pass) + ', ' + str(playerStat.total_chipped_pass) + ', ' + str(playerStat.total_clearance) + ', ' + str(playerStat.total_contest) + ', ' + str(playerStat.total_corners_intobox) + ', ' + str(playerStat.total_cross) + ', ' + str(playerStat.total_cross_nocorner) + ', ' + str(playerStat.total_fastbreak) + ', ' + str(playerStat.total_final_third_passes) + ', ' + str(playerStat.total_flick_on) + ', ' + str(playerStat.total_fwd_zone_pass) + ', ' + str(playerStat.total_high_claim) + ', ' + str(playerStat.total_keeper_sweeper) + ', ' + str(playerStat.total_launches) + ', ' + str(playerStat.total_layoffs) + ', ' + str(playerStat.total_long_balls) + ', ' + str(playerStat.total_offside) + ', ' + str(playerStat.total_pass) + ', ' + str(playerStat.total_pull_back) + ', ' + str(playerStat.total_scoring_att) + ', ' + str(playerStat.total_sub_off) + ', ' + str(playerStat.total_sub_on) + ', ' + str(playerStat.total_tackle) + ', ' + str(playerStat.total_through_ball) + ', ' + str(playerStat.total_throws) + ', ' + str(playerStat.touches) + ', ' + str(playerStat.turnover) + ', ' + str(playerStat.unsuccessful_touch) + ', ' + str(playerStat.was_fouled) + ', ' + str(playerStat.won_contest) + ', ' + str(playerStat.won_corners) + ', ' + str(playerStat.won_tackle) + ', ' + str(playerStat.yellow_card) + ')'
	
	cursorObj.execute(strInsert)

	
def UpdateMatchInfo(league, matchID, cursorObj):
	'''
	从文件读取数据，并写入数据库
	'''
	matchInfo = LoaderMatch.GetMatchInfo(league, matchID)
	InsertMatchInfo(cursorObj, matchInfo)
	InsertTeamStatistics(cursorObj, matchInfo.id, matchInfo.league, 1, matchInfo.homeTeamStat)
	InsertTeamStatistics(cursorObj, matchInfo.id, matchInfo.league, 0, matchInfo.awayTeamStat)
		
	for playerStat in matchInfo.homeTeamPlayerStat:
		InsertPlayerStatistics(cursorObj, matchInfo.id, matchInfo.league, 1, matchInfo.homeTeamStat.id, matchInfo.homeTeamStat.name, playerStat)
		
	for playerStat in matchInfo.awayTeamPlayerStat:
		InsertPlayerStatistics(cursorObj, matchInfo.id, matchInfo.league, 0, matchInfo.awayTeamStat.id, matchInfo.awayTeamStat.name, playerStat)


def GetMatchIDs(dirLeague):
	'''
	获取所有比赛的matchID
	'''
	matchIDs = []
	
	#  Add match id in original match id list
	for root, dirs, files in os.walk(dirLeague):
		for fn in files:
			if fn != Global.Fn_LiveScores and os.path.getsize(os.path.join(root, fn)) > 1024:
				matchIDs.append(Re_FN_Match.findall(fn)[0])
	
	return matchIDs


if __name__ == '__main__':
	
	league = 'England_BarclaysPL'

	conn = sqlite3.connect(Global.Fn_Database)
	cursorObj = conn.cursor()
	
	t = time.time()
	
	matches = GetMatchIDs(league)
	for matchID in matches:
		print(matchID, end = '\r')
		UpdateMatchInfo(league, matchID, cursorObj)
	
	conn.commit()
	cursorObj.close()
	conn.close()
	
	print('s:'+str(time.time()-t))