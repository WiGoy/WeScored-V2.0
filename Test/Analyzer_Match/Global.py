class TeamStatistics:
	name = ''
	home = ''
	rating = ''
	accurate_back_zone_pass = ''
	accurate_chipped_pass = ''
	accurate_corners_intobox = ''
	accurate_cross = ''
	accurate_cross_nocorner = ''
	accurate_flick_on = ''
	accurate_freekick_cross = ''
	accurate_fwd_zone_pass = ''
	accurate_goal_kicks = ''
	accurate_keeper_sweeper = ''
	accurate_keeper_throws = ''
	accurate_launches = ''
	accurate_layoffs = ''
	accurate_long_balls = ''
	accurate_pass = ''
	accurate_through_ball = ''
	accurate_throws = ''
	aerial_lost = ''
	aerial_won = ''
	att_assist_openplay = ''
	att_assist_setplay = ''
	att_bx_centre = ''
	att_bx_left = ''
	att_bx_right = ''
	att_cmiss_high = ''
	att_cmiss_high_right = ''
	att_cmiss_left = ''
	att_cmiss_right = ''
	att_fastbreak = ''
	att_freekick_goal = ''
	att_freekick_miss = ''
	att_freekick_post = ''
	att_freekick_target = ''
	att_freekick_total = ''
	att_goal_high_left = ''
	att_goal_high_right = ''
	att_goal_low_centre = ''
	att_goal_low_left = ''
	att_goal_low_right = ''
	att_hd_goal = ''
	att_hd_miss = ''
	att_hd_post = ''
	att_hd_target = ''
	att_hd_total = ''
	att_ibox_blocked = ''
	att_ibox_goal = ''
	att_ibox_miss = ''
	att_ibox_post = ''
	att_ibox_target = ''
	att_lf_goal = ''
	att_lf_target = ''
	att_lf_total = ''
	att_lg_centre = ''
	att_miss_high = ''
	att_miss_high_left = ''
	att_miss_high_right = ''
	att_miss_left = ''
	att_miss_right= ''
	att_obox_blocked = ''
	att_obox_goal = ''
	att_obox_miss = ''
	att_obox_post = ''
	att_obox_target = ''
	att_obx_centre = ''
	att_obx_left = ''
	att_obxd_right = ''
	att_one_on_one = ''
	att_openplay = ''
	att_pen_goal = ''
	att_pen_target = ''
	att_post_high = ''
	att_post_right = ''
	att_rf_goal = ''
	att_rf_target = ''
	att_rf_total = ''
	att_setpiece = ''
	att_sv_high_centre = ''
	att_sv_high_left = ''
	att_sv_high_right = ''
	att_sv_low_centre = ''
	att_sv_low_left = ''
	att_sv_low_right = ''
	attempted_tackle_foul = ''
	attempts_conceded_ibox = ''
	attempts_conceded_obox = ''
	backward_pass = ''
	ball_recovery = ''
	big_chance_created = ''
	big_chance_missed = ''
	big_chance_scored = ''
	blocked_cross = ''
	blocked_pass = ''
	blocked_scoring_att = ''
	challenge_lost = ''
	clean_sheet = ''
	clearance_off_line = ''
	contentious_decision = ''
	corner_taken = ''
	cross_inaccurate = ''
	crosses_18yard = ''
	crosses_18yardplus;
	defender_goals;
	dispossessed;
	diving_save;
	dribble_lost;
	duel_ground_lost;
	duel_ground_won;
	duel_lost;
	duel_won;
	effective_blocked_cross;
	effective_clearance;
	effective_head_clearance;
	error_lead_to_goal;
	error_lead_to_shot;
	failed_to_block;
	fifty_fifty;
	final_third_entries;
	first_half_goals;
	fk_foul_lost;
	fk_foul_won;
	formation_used;
	forward_goals;
	fouled_final_third;
	freekick_cross;
	fwd_pass;
	goal_assist;
	goal_assist_intentional;
	goal_assist_openplay;
	goal_assist_setplay;
	goal_fastbreak;
	goal_kicks;
	goals;
	goals_conceded;
	goals_conceded_ibox;
	goals_conceded_obox;
	goals_openplay;
	good_high_claim;
	hand_ball;
	head_clearance;
	hit_woodwork;
	interception;
	interception_won;
	interceptions_in_box;
	keeper_throws;
	last_man_tackle;
	leftside_pass;
	long_pass_own_to_opp;
	long_pass_own_to_opp_success;
	lost_corners;
	midfielder_goals;
	offtarget_att_assist;
	ontarget_att_assist;
	ontarget_scoring_att;
	open_play_pass;
	outfielder_block;
	overrun;
	passes_left;
	passes_right;
	pen_area_entries;
	pen_goals_conceded;
	penalty_conceded;
	penalty_faced;
	penalty_missed;
	penalty_save;
	penalty_won;
	poss_lost_all;
	poss_lost_ctrl;
	poss_won_att_3rd;
	poss_won_def_3rd;
	poss_won_mid_3rd;
	possession_percentage;
	post_scoring_att;
	punches;
	put_through;
	rightside_pass;
	saved_ibox;
	saved_obox;
	saves;
	second_yellow;
	shield_ball_oop;
	shot_fastbreak;
	shot_off_target;
	six_yard_block;
	subs_made;
	successful_fifty_fifty;
	successful_final_third_passes;
	successful_open_play_pass;
	successful_put_through;
	tackle_lost;
	total_att_assist;
	total_back_zone_pass;
	total_chipped_pass;
	total_clearance;
	total_contest;
	total_corners_intobox;
	total_cross;
	total_cross_nocorner;
	total_fastbreak;
	total_final_third_passes;
	total_flick_on;
	total_fwd_zone_pass;
	total_high_claim;
	total_keeper_sweeper;
	total_launches;
	total_layoffs;
	total_long_balls;
	total_offside;
	total_pass;
	total_pull_back;
	total_red_card;
	total_scoring_att;
	total_tackle;
	total_through_ball;
	total_throws;
	total_yel_card;
	touches;
	unsuccessful_touch;
	won_contest;
	won_corners;
	won_tackle

    public class PlayerStatistics
    {
        public int id;
        public string name;
        public float accurate_back_zone_pass;
        public float accurate_chipped_pass;
        public float accurate_corners_intobox;
        public float accurate_cross;
        public float accurate_cross_nocorner;
        public float accurate_flick_on;
        public float accurate_freekick_cross;
        public float accurate_fwd_zone_pass;
        public float accurate_goal_kicks;
        public float accurate_keeper_sweeper;
        public float accurate_keeper_throws;
        public float accurate_launches;
        public float accurate_layoffs;
        public float accurate_long_balls;
        public float accurate_pass;
        public float accurate_through_ball;
        public float accurate_throws;
        public float aerial_lost;
        public float aerial_won;
        public float assist_penalty_won;
        public float att_assist_openplay;
        public float att_assist_setplay;
        public float att_bx_centre;
        public float att_bx_left;
        public float att_bx_right;
        public float att_cmiss_high;
        public float att_cmiss_high_right;
        public float att_cmiss_left;
        public float att_cmiss_right;
        public float att_fastbreak;
        public float att_freekick_goal;
        public float att_freekick_miss;
        public float att_freekick_post;
        public float att_freekick_target;
        public float att_freekick_total;
        public float att_goal_high_left;
        public float att_goal_high_right;
        public float att_goal_low_centre;
        public float att_goal_low_left;
        public float att_goal_low_right;
        public float att_hd_goal;
        public float att_hd_miss;
        public float att_hd_post;
        public float att_hd_target;
        public float att_hd_total;
        public float att_ibox_blocked;
        public float att_ibox_goal;
        public float att_ibox_miss;
        public float att_ibox_post;
        public float att_ibox_target;
        public float att_lf_goal;
        public float att_lf_target;
        public float att_lf_total;
        public float att_lg_centre;
        public float att_miss_high;
        public float att_miss_high_left;
        public float att_miss_high_right;
        public float att_miss_left;
        public float att_miss_right;
        public float att_obox_blocked;
        public float att_obox_goal;
        public float att_obox_miss;
        public float att_obox_post;
        public float att_obox_target;
        public float att_obx_centre;
        public float att_obx_left;
        public float att_obxd_right;
        public float att_one_on_one;
        public float att_openplay;
        public float att_pen_goal;
        public float att_pen_target;
        public float att_post_high;
        public float att_post_right;
        public float att_rf_goal;
        public float att_rf_target;
        public float att_rf_total;
        public float att_setpiece;
        public float att_sv_high_centre;
        public float att_sv_high_left;
        public float att_sv_high_right;
        public float att_sv_low_centre;
        public float att_sv_low_left;
        public float att_sv_low_right;
        public float attempted_tackle_foul;
        public float attempts_conceded_ibox;
        public float attempts_conceded_obox;
        public float backward_pass;
        public float ball_recovery;
        public float big_chance_created;
        public float big_chance_missed;
        public float big_chance_scored;
        public float blocked_cross;
        public float blocked_pass;
        public float blocked_scoring_att;
        public float challenge_lost;
        public float clean_sheet_amc;
        public float clean_sheet_amr;
        public float clean_sheet_dc;
        public float clean_sheet_dl;
        public float clean_sheet_dmc;
        public float clean_sheet_dml;
        public float clean_sheet_dmr;
        public float clean_sheet_dr;
        public float clean_sheet_fw;
        public float clean_sheet_gk;
        public float clearance_off_line;
        public float corner_taken;
        public float cross_inaccurate;
        public float crosses_18yard;
        public float crosses_18yardplus;
        public float dangerous_play;
        public float dispossessed;
        public float dive_catch;
        public float dive_save;
        public float diving_save;
        public float dribble_lost;
        public float duel_ground_lost;
        public float duel_ground_won;
        public float duel_lost;
        public float duel_won;
        public float effective_blocked_cross;
        public float effective_clearance;
        public float effective_head_clearance;
        public float error_lead_to_goal;
        public float error_lead_to_shot;
        public float failed_to_block;
        public float fifty_fifty;
        public float final_third_entries;
        public float formation_place;
        public float fouled_final_third;
        public float fouls;
        public float freekick_cross;
        public float fwd_pass;
        public float game_started;
        public float gk_smother;
        public float goal_assist;
        public float goal_assist_intentional;
        public float goal_assist_openplay;
        public float goal_assist_setplay;
        public float goal_fastbreak;
        public float goal_kicks;
        public float goal_normal;
        public float goal_scored_by_team_amc;
        public float goal_scored_by_team_aml;
        public float goal_scored_by_team_amr;
        public float goal_scored_by_team_dc;
        public float goal_scored_by_team_dl;
        public float goal_scored_by_team_dmc;
        public float goal_scored_by_team_dml;
        public float goal_scored_by_team_dmr;
        public float goal_scored_by_team_dr;
        public float goal_scored_by_team_fw;
        public float goal_scored_by_team_fwl;
        public float goal_scored_by_team_fwr;
        public float goal_scored_by_team_gk;
        public float goal_scored_by_team_mc;
        public float goal_scored_by_team_ml;
        public float goal_scored_by_team_mr;
        public float goal_scored_by_team_sub;
        public float goals;
        public float goals_conceded_amc;
        public float goals_conceded_aml;
        public float goals_conceded_amr;
        public float goals_conceded_dc;
        public float goals_conceded_dl;
        public float goals_conceded_dmc;
        public float goals_conceded_dr;
        public float goals_conceded_fw;
        public float goals_conceded_fwl;
        public float goals_conceded_fwr;
        public float goals_conceded_gk;
        public float goals_conceded_ibox;
        public float goals_conceded_mc;
        public float goals_conceded_ml;
        public float goals_conceded_mr;
        public float goals_conceded_obox_amc;
        public float goals_conceded_obox_aml;
        public float goals_conceded_obox_amr;
        public float goals_conceded_obox_dc;
        public float goals_conceded_obox_dl;
        public float goals_conceded_obox_dmc;
        public float goals_conceded_obox_dr;
        public float goals_conceded_obox_fw;
        public float goals_conceded_obox_gk;
        public float goals_conceded_obox_mc;
        public float goals_conceded_obox_ml;
        public float goals_conceded_obox_mr;
        public float goals_conceded_obox_sub;
        public float goals_conceded_sub;
        public float goals_openplay;
        public float good_high_claim;
        public float hand_ball;
        public float head_clearance;
        public float head_pass;
        public float hit_woodwork;
        public float interception;
        public float interception_won;
        public float interceptions_in_box;
        public float keeper_claim_high_lost;
        public float keeper_claim_lost;
        public float keeper_pick_up;
        public float keeper_sweeper_lost;
        public float keeper_throws;
        public float last_man_tackle;
        public float leftside_pass;
        public float long_pass_own_to_opp;
        public float long_pass_own_to_opp_success;
        public float lost_corners;
        public float man_of_the_match;
        public float mins_played;
        public float offside_provoked;
        public float offtarget_att_assist;
        public float ontarget_att_assist;
        public float ontarget_scoring_att;
        public float open_play_pass;
        public float outfielder_block;
        public float overrun;
        public float pass_backzone_inaccurate;
        public float pass_forwardzone_inaccurate;
        public float pass_inaccurate;
        public float pass_longball_inaccurate;
        public float pass_throughball_inacurate;
        public float passes_left;
        public float passes_right;
        public float pen_area_entries;
        public float pen_goals_conceded;
        public float penalty_conceded;
        public float penalty_faced;
        public float penalty_missed;
        public float penalty_save;
        public float penalty_shootout_conceded_gk;
        public float penalty_shootout_missed_off_target;
        public float penalty_shootout_saved;
        public float penalty_shootout_saved_gk;
        public float penalty_shootout_scored;
        public float penalty_won;
        public string position;
        public float poss_lost_all;
        public float poss_lost_ctrl;
        public float poss_won_att_3rd;
        public float poss_won_def_3rd;
        public float poss_won_mid_3rd;
        public float post_scoring_att;
        public float punches;
        public float put_through;
        public float rating;
        public float rating_defensive;
        public float rating_defensive_points;
        public float rating_offensive;
        public float rating_offensive_points;
        public float rating_points;
        public float red_card;
        public float rightside_pass;
        public float saved_ibox;
        public float saved_obox;
        public float saves;
        public float second_goal_assist;
        public float second_yellow;
        public float shield_ball_oop;
        public float shot_fastbreak;
        public float shot_off_target;
        public float six_yard_block;
        public float stand_catch;
        public float successful_fifty_fifty;
        public float successful_final_third_passes;
        public float successful_open_play_pass;
        public float successful_put_through;
        public float tackle_lost;
        public float total_att_assist;
        public float total_back_zone_pass;
        public float total_chipped_pass;
        public float total_clearance;
        public float total_contest;
        public float total_corners_intobox;
        public float total_cross;
        public float total_cross_nocorner;
        public float total_fastbreak;
        public float total_final_third_passes;
        public float total_flick_on;
        public float total_fwd_zone_pass;
        public float total_high_claim;
        public float total_keeper_sweeper;
        public float total_launches;
        public float total_layoffs;
        public float total_long_balls;
        public float total_offside;
        public float total_pass;
        public float total_pull_back;
        public float total_scoring_att;
        public float total_sub_off;
        public float total_sub_on;
        public float total_tackle;
        public float total_through_ball;
        public float total_throws;
        public float touches;
        public float turnover;
        public float unsuccessful_touch;
        public float was_fouled;
        public float won_contest;
        public float won_corners;
        public float won_tackle;
        public float yellow_card;
    }

    public class TeamStatisticsFilter
    {
        public const string ACCURATE_BACK_ZONE_PASS = "accurate_back_zone_pass";
        public const string ACCURATE_CHIPPED_PASS = "accurate_chipped_pass";
        public const string ACCURATE_CORNERS_INTOBOX = "accurate_corners_intobox";
        public const string ACCURATE_CROSS = "accurate_cross";
        public const string ACCURATE_CROSS_NOCORNER = "accurate_cross_nocorner";
        public const string ACCURATE_FLICK_ON = "accurate_flick_on";
        public const string ACCURATE_FREEKICK_CROSS = "accurate_freekick_cross";
        public const string ACCURATE_FWD_ZONE_PASS = "accurate_fwd_zone_pass";
        public const string ACCURATE_GOAL_KICKS = "accurate_goal_kicks";
        public const string ACCURATE_KEEPER_SWEEPER = "accurate_keeper_sweeper";
        public const string ACCURATE_KEEPER_THROWS = "accurate_keeper_throws";
        public const string ACCURATE_LAUNCHES = "accurate_launches";
        public const string ACCURATE_LAYOFFS = "accurate_layoffs";
        public const string ACCURATE_LONG_BALLS = "accurate_long_balls";
        public const string ACCURATE_PASS = "accurate_pass";
        public const string ACCURATE_THROUGH_BALL = "accurate_through_ball";
        public const string ACCURATE_THROWS = "accurate_throws";
        public const string AERIAL_LOST = "aerial_lost";
        public const string AERIAL_WON = "aerial_won";
        public const string ATT_ASSIST_OPENPLAY = "att_assist_openplay";
        public const string ATT_ASSIST_SETPLAY = "att_assist_setplay";
        public const string ATT_BX_CENTRE = "att_bx_centre";
        public const string ATT_BX_LEFT = "att_bx_left";
        public const string ATT_BX_RIGHT = "att_bx_right";
        public const string ATT_CMISS_HIGH = "att_cmiss_high";
        public const string ATT_CMISS_HIGH_RIGHT = "att_cmiss_high_right";
        public const string ATT_CMISS_LEFT = "att_cmiss_left";
        public const string ATT_CMISS_RIGHT = "att_cmiss_right";
        public const string ATT_FASTBREAK = "att_fastbreak";
        public const string ATT_FREEKICK_GOAL = "att_freekick_goal";
        public const string ATT_FREEKICK_MISS = "att_freekick_miss";
        public const string ATT_FREEKICK_POST = "att_freekick_post";
        public const string ATT_FREEKICK_TARGET = "att_freekick_target";
        public const string ATT_FREEKICK_TOTAL = "att_freekick_total";
        public const string ATT_GOAL_HIGH_LEFT = "att_goal_high_left";
        public const string ATT_GOAL_HIGH_RIGHT = "att_goal_high_right";
        public const string ATT_GOAL_LOW_CENTRE = "att_goal_low_centre";
        public const string ATT_GOAL_LOW_LEFT = "att_goal_low_left";
        public const string ATT_GOAL_LOW_RIGHT = "att_goal_low_right";
        public const string ATT_HD_GOAL = "att_hd_goal";
        public const string ATT_HD_MISS = "att_hd_miss";
        public const string ATT_HD_POST = "att_hd_post";
        public const string ATT_HD_TARGET = "att_hd_target";
        public const string ATT_HD_TOTAL = "att_hd_total";
        public const string ATT_IBOX_BLOCKED = "att_ibox_blocked";
        public const string ATT_IBOX_GOAL = "att_ibox_goal";
        public const string ATT_IBOX_MISS = "att_ibox_miss";
        public const string ATT_IBOX_POST = "att_ibox_post";
        public const string ATT_IBOX_TARGET = "att_ibox_target";
        public const string ATT_LF_GOAL = "att_lf_goal";
        public const string ATT_LF_TARGET = "att_lf_target";
        public const string ATT_LF_TOTAL = "att_lf_total";
        public const string ATT_LG_CENTRE = "att_lg_centre";
        public const string ATT_MISS_HIGH = "att_miss_high";
        public const string ATT_MISS_HIGH_LEFT = "att_miss_high_left";
        public const string ATT_MISS_HIGH_RIGHT = "att_miss_high_right";
        public const string ATT_MISS_LEFT = "att_miss_left";
        public const string ATT_MISS_RIGHT = "att_miss_right";
        public const string ATT_OBOX_BLOCKED = "att_obox_blocked";
        public const string ATT_OBOX_GOAL = "att_obox_goal";
        public const string ATT_OBOX_MISS = "att_obox_miss";
        public const string ATT_OBOX_POST = "att_obox_post";
        public const string ATT_OBOX_TARGET = "att_obox_target";
        public const string ATT_OBX_CENTRE = "att_obx_centre";
        public const string ATT_OBX_LEFT = "att_obx_left";
        public const string ATT_OBXD_RIGHT = "att_obxd_right";
        public const string ATT_ONE_ON_ONE = "att_one_on_one";
        public const string ATT_OPENPLAY = "att_openplay";
        public const string ATT_PEN_GOAL = "att_pen_goal";
        public const string ATT_PEN_TARGET = "att_pen_target";
        public const string ATT_POST_HIGH = "att_post_high";
        public const string ATT_POST_RIGHT = "att_post_right";
        public const string ATT_RF_GOAL = "att_rf_goal";
        public const string ATT_RF_TARGET = "att_rf_target";
        public const string ATT_RF_TOTAL = "att_rf_total";
        public const string ATT_SETPIECE = "att_setpiece";
        public const string ATT_SV_HIGH_CENTRE = "att_sv_high_centre";
        public const string ATT_SV_HIGH_LEFT = "att_sv_high_left";
        public const string ATT_SV_HIGH_RIGHT = "att_sv_high_right";
        public const string ATT_SV_LOW_CENTRE = "att_sv_low_centre";
        public const string ATT_SV_LOW_LEFT = "att_sv_low_left";
        public const string ATT_SV_LOW_RIGHT = "att_sv_low_right";
        public const string ATTEMPTED_TACKLE_FOUL = "attempted_tackle_foul";
        public const string ATTEMPTS_CONCEDED_IBOX = "attempts_conceded_ibox";
        public const string ATTEMPTS_CONCEDED_OBOX = "attempts_conceded_obox";
        public const string BACKWARD_PASS = "backward_pass";
        public const string BALL_RECOVERY = "ball_recovery";
        public const string BIG_CHANCE_CREATED = "big_chance_created";
        public const string BIG_CHANCE_MISSED = "big_chance_missed";
        public const string BIG_CHANCE_SCORED = "big_chance_scored";
        public const string BLOCKED_CROSS = "blocked_cross";
        public const string BLOCKED_PASS = "blocked_pass";
        public const string BLOCKED_SCORING_ATT = "blocked_scoring_att";
        public const string CHALLENGE_LOST = "challenge_lost";
        public const string CLEAN_SHEET = "clean_sheet";
        public const string CLEARANCE_OFF_LINE = "clearance_off_line";
        public const string CONTENTIOUS_DECISION = "contentious_decision";
        public const string CORNER_TAKEN = "corner_taken";
        public const string CROSS_INACCURATE = "cross_inaccurate";
        public const string CROSSES_18YARD = "crosses_18yard";
        public const string CROSSES_18YARDPLUS = "crosses_18yardplus";
        public const string DEFENDER_GOALS = "defender_goals";
        public const string DISPOSSESSED = "dispossessed";
        public const string DIVING_SAVE = "diving_save";
        public const string DRIBBLE_LOST = "dribble_lost";
        public const string DUEL_GROUND_LOST = "duel_ground_lost";
        public const string DUEL_GROUND_WON = "duel_ground_won";
        public const string DUEL_LOST = "duel_lost";
        public const string DUEL_WON = "duel_won";
        public const string EFFECTIVE_BLOCKED_CROSS = "effective_blocked_cross";
        public const string EFFECTIVE_CLEARANCE = "effective_clearance";
        public const string EFFECTIVE_HEAD_CLEARANCE = "effective_head_clearance";
        public const string ERROR_LEAD_TO_GOAL = "error_lead_to_goal";
        public const string ERROR_LEAD_TO_SHOT = "error_lead_to_shot";
        public const string FAILED_TO_BLOCK = "failed_to_block";
        public const string FIFTY_FIFTY = "fifty_fifty";
        public const string FINAL_THIRD_ENTRIES = "final_third_entries";
        public const string FIRST_HALF_GOALS = "first_half_goals";
        public const string FK_FOUL_LOST = "fk_foul_lost";
        public const string FK_FOUL_WON = "fk_foul_won";
        public const string FORMATION_USED = "formation_used";
        public const string FORWARD_GOALS = "forward_goals";
        public const string FOULED_FINAL_THIRD = "fouled_final_third";
        public const string FREEKICK_CROSS = "freekick_cross";
        public const string FWD_PASS = "fwd_pass";
        public const string GOAL_ASSIST = "goal_assist";
        public const string GOAL_ASSIST_INTENTIONAL = "goal_assist_intentional";
        public const string GOAL_ASSIST_OPENPLAY = "goal_assist_openplay";
        public const string GOAL_ASSIST_SETPLAY = "goal_assist_setplay";
        public const string GOAL_FASTBREAK = "goal_fastbreak";
        public const string GOAL_KICKS = "goal_kicks";
        public const string GOALS = "goals";
        public const string GOALS_CONCEDED = "goals_conceded";
        public const string GOALS_CONCEDED_IBOX = "goals_conceded_ibox";
        public const string GOALS_CONCEDED_OBOX = "goals_conceded_obox";
        public const string GOALS_OPENPLAY = "goals_openplay";
        public const string GOOD_HIGH_CLAIM = "good_high_claim";
        public const string HAND_BALL = "hand_ball";
        public const string HEAD_CLEARANCE = "head_clearance";
        public const string HIT_WOODWORK = "hit_woodwork";
        public const string INTERCEPTION = "interception";
        public const string INTERCEPTION_WON = "interception_won";
        public const string INTERCEPTIONS_IN_BOX = "interceptions_in_box";
        public const string KEEPER_THROWS = "keeper_throws";
        public const string LAST_MAN_TACKLE = "last_man_tackle";
        public const string LEFTSIDE_PASS = "leftside_pass";
        public const string LONG_PASS_OWN_TO_OPP = "long_pass_own_to_opp";
        public const string LONG_PASS_OWN_TO_OPP_SUCCESS = "long_pass_own_to_opp_success";
        public const string LOST_CORNERS = "lost_corners";
        public const string MIDFIELDER_GOALS = "midfielder_goals";
        public const string OFFTARGET_ATT_ASSIST = "offtarget_att_assist";
        public const string ONTARGET_ATT_ASSIST = "ontarget_att_assist";
        public const string ONTARGET_SCORING_ATT = "ontarget_scoring_att";
        public const string OPEN_PLAY_PASS = "open_play_pass";
        public const string OUTFIELDER_BLOCK = "outfielder_block";
        public const string OVERRUN = "overrun";
        public const string PASSES_LEFT = "passes_left";
        public const string PASSES_RIGHT = "passes_right";
        public const string PEN_AREA_ENTRIES = "pen_area_entries";
        public const string PEN_GOALS_CONCEDED = "pen_goals_conceded";
        public const string PENALTY_CONCEDED = "penalty_conceded";
        public const string PENALTY_FACED = "penalty_faced";
        public const string PENALTY_MISSED = "penalty_missed";
        public const string PENALTY_SAVE = "penalty_save";
        public const string PENALTY_WON = "penalty_won";
        public const string POSS_LOST_ALL = "poss_lost_all";
        public const string POSS_LOST_CTRL = "poss_lost_ctrl";
        public const string POSS_WON_ATT_3RD = "poss_won_att_3rd";
        public const string POSS_WON_DEF_3RD = "poss_won_def_3rd";
        public const string POSS_WON_MID_3RD = "poss_won_mid_3rd";
        public const string POSSESSION_PERCENTAGE = "possession_percentage";
        public const string POST_SCORING_ATT = "post_scoring_att";
        public const string PUNCHES = "punches";
        public const string PUT_THROUGH = "put_through";
        public const string RIGHTSIDE_PASS = "rightside_pass";
        public const string SAVED_IBOX = "saved_ibox";
        public const string SAVED_OBOX = "saved_obox";
        public const string SAVES = "saves";
        public const string SECOND_YELLOW = "second_yellow";
        public const string SHIELD_BALL_OOP = "shield_ball_oop";
        public const string SHOT_FASTBREAK = "shot_fastbreak";
        public const string SHOT_OFF_TARGET = "shot_off_target";
        public const string SIX_YARD_BLOCK = "six_yard_block";
        public const string SUBS_MADE = "subs_made";
        public const string SUCCESSFUL_FIFTY_FIFTY = "successful_fifty_fifty";
        public const string SUCCESSFUL_FINAL_THIRD_PASSES = "successful_final_third_passes";
        public const string SUCCESSFUL_OPEN_PLAY_PASS = "successful_open_play_pass";
        public const string SUCCESSFUL_PUT_THROUGH = "successful_put_through";
        public const string TACKLE_LOST = "tackle_lost";
        public const string TOTAL_ATT_ASSIST = "total_att_assist";
        public const string TOTAL_BACK_ZONE_PASS = "total_back_zone_pass";
        public const string TOTAL_CHIPPED_PASS = "total_chipped_pass";
        public const string TOTAL_CLEARANCE = "total_clearance";
        public const string TOTAL_CONTEST = "total_contest";
        public const string TOTAL_CORNERS_INTOBOX = "total_corners_intobox";
        public const string TOTAL_CROSS = "total_cross";
        public const string TOTAL_CROSS_NOCORNER = "total_cross_nocorner";
        public const string TOTAL_FASTBREAK = "total_fastbreak";
        public const string TOTAL_FINAL_THIRD_PASSES = "total_final_third_passes";
        public const string TOTAL_FLICK_ON = "total_flick_on";
        public const string TOTAL_FWD_ZONE_PASS = "total_fwd_zone_pass";
        public const string TOTAL_HIGH_CLAIM = "total_high_claim";
        public const string TOTAL_KEEPER_SWEEPER = "total_keeper_sweeper";
        public const string TOTAL_LAUNCHES = "total_launches";
        public const string TOTAL_LAYOFFS = "total_layoffs";
        public const string TOTAL_LONG_BALLS = "total_long_balls";
        public const string TOTAL_OFFSIDE = "total_offside";
        public const string TOTAL_PASS = "total_pass";
        public const string TOTAL_PULL_BACK = "total_pull_back";
        public const string TOTAL_RED_CARD = "total_red_card";
        public const string TOTAL_SCORING_ATT = "total_scoring_att";
        public const string TOTAL_TACKLE = "total_tackle";
        public const string TOTAL_THROUGH_BALL = "total_through_ball";
        public const string TOTAL_THROWS = "total_throws";
        public const string TOTAL_YEL_CARD = "total_yel_card";
        public const string TOUCHES = "touches";
        public const string UNSUCCESSFUL_TOUCH = "unsuccessful_touch";
        public const string WON_CONTEST = "won_contest";
        public const string WON_CORNERS = "won_corners";
        public const string WON_TACKLE = "won_tackle";
    }

    public class PlayerStatisticsFilter
    {
        public const string ACCURATE_BACK_ZONE_PASS = "accurate_back_zone_pass";
        public const string ACCURATE_CHIPPED_PASS = "accurate_chipped_pass";
        public const string ACCURATE_CORNERS_INTOBOX = "accurate_corners_intobox";
        public const string ACCURATE_CROSS = "accurate_cross";
        public const string ACCURATE_CROSS_NOCORNER = "accurate_cross_nocorner";
        public const string ACCURATE_FLICK_ON = "accurate_flick_on";
        public const string ACCURATE_FREEKICK_CROSS = "accurate_freekick_cross";
        public const string ACCURATE_FWD_ZONE_PASS = "accurate_fwd_zone_pass";
        public const string ACCURATE_GOAL_KICKS = "accurate_goal_kicks";
        public const string ACCURATE_KEEPER_SWEEPER = "accurate_keeper_sweeper";
        public const string ACCURATE_KEEPER_THROWS = "accurate_keeper_throws";
        public const string ACCURATE_LAUNCHES = "accurate_launches";
        public const string ACCURATE_LAYOFFS = "accurate_layoffs";
        public const string ACCURATE_LONG_BALLS = "accurate_long_balls";
        public const string ACCURATE_PASS = "accurate_pass";
        public const string ACCURATE_THROUGH_BALL = "accurate_through_ball";
        public const string ACCURATE_THROWS = "accurate_throws";
        public const string AERIAL_LOST = "aerial_lost";
        public const string AERIAL_WON = "aerial_won";
        public const string ASSIST_PENALTY_WON = "assist_penalty_won";
        public const string ATT_ASSIST_OPENPLAY = "att_assist_openplay";
        public const string ATT_ASSIST_SETPLAY = "att_assist_setplay";
        public const string ATT_BX_CENTRE = "att_bx_centre";
        public const string ATT_BX_LEFT = "att_bx_left";
        public const string ATT_BX_RIGHT = "att_bx_right";
        public const string ATT_CMISS_HIGH = "att_cmiss_high";
        public const string ATT_CMISS_HIGH_RIGHT = "att_cmiss_high_right";
        public const string ATT_CMISS_LEFT = "att_cmiss_left";
        public const string ATT_CMISS_RIGHT = "att_cmiss_right";
        public const string ATT_FASTBREAK = "att_fastbreak";
        public const string ATT_FREEKICK_GOAL = "att_freekick_goal";
        public const string ATT_FREEKICK_MISS = "att_freekick_miss";
        public const string ATT_FREEKICK_POST = "att_freekick_post";
        public const string ATT_FREEKICK_TARGET = "att_freekick_target";
        public const string ATT_FREEKICK_TOTAL = "att_freekick_total";
        public const string ATT_GOAL_HIGH_LEFT = "att_goal_high_left";
        public const string ATT_GOAL_HIGH_RIGHT = "att_goal_high_right";
        public const string ATT_GOAL_LOW_CENTRE = "att_goal_low_centre";
        public const string ATT_GOAL_LOW_LEFT = "att_goal_low_left";
        public const string ATT_GOAL_LOW_RIGHT = "att_goal_low_right";
        public const string ATT_HD_GOAL = "att_hd_goal";
        public const string ATT_HD_MISS = "att_hd_miss";
        public const string ATT_HD_POST = "att_hd_post";
        public const string ATT_HD_TARGET = "att_hd_target";
        public const string ATT_HD_TOTAL = "att_hd_total";
        public const string ATT_IBOX_BLOCKED = "att_ibox_blocked";
        public const string ATT_IBOX_GOAL = "att_ibox_goal";
        public const string ATT_IBOX_MISS = "att_ibox_miss";
        public const string ATT_IBOX_POST = "att_ibox_post";
        public const string ATT_IBOX_TARGET = "att_ibox_target";
        public const string ATT_LF_GOAL = "att_lf_goal";
        public const string ATT_LF_TARGET = "att_lf_target";
        public const string ATT_LF_TOTAL = "att_lf_total";
        public const string ATT_LG_CENTRE = "att_lg_centre";
        public const string ATT_MISS_HIGH = "att_miss_high";
        public const string ATT_MISS_HIGH_LEFT = "att_miss_high_left";
        public const string ATT_MISS_HIGH_RIGHT = "att_miss_high_right";
        public const string ATT_MISS_LEFT = "att_miss_left";
        public const string ATT_MISS_RIGHT = "att_miss_right";
        public const string ATT_OBOX_BLOCKED = "att_obox_blocked";
        public const string ATT_OBOX_GOAL = "att_obox_goal";
        public const string ATT_OBOX_MISS = "att_obox_miss";
        public const string ATT_OBOX_POST = "att_obox_post";
        public const string ATT_OBOX_TARGET = "att_obox_target";
        public const string ATT_OBX_CENTRE = "att_obx_centre";
        public const string ATT_OBX_LEFT = "att_obx_left";
        public const string ATT_OBXD_RIGHT = "att_obxd_right";
        public const string ATT_ONE_ON_ONE = "att_one_on_one";
        public const string ATT_OPENPLAY = "att_openplay";
        public const string ATT_PEN_GOAL = "att_pen_goal";
        public const string ATT_PEN_TARGET = "att_pen_target";
        public const string ATT_POST_HIGH = "att_post_high";
        public const string ATT_POST_RIGHT = "att_post_right";
        public const string ATT_RF_GOAL = "att_rf_goal";
        public const string ATT_RF_TARGET = "att_rf_target";
        public const string ATT_RF_TOTAL = "att_rf_total";
        public const string ATT_SETPIECE = "att_setpiece";
        public const string ATT_SV_HIGH_CENTRE = "att_sv_high_centre";
        public const string ATT_SV_HIGH_LEFT = "att_sv_high_left";
        public const string ATT_SV_HIGH_RIGHT = "att_sv_high_right";
        public const string ATT_SV_LOW_CENTRE = "att_sv_low_centre";
        public const string ATT_SV_LOW_LEFT = "att_sv_low_left";
        public const string ATT_SV_LOW_RIGHT = "att_sv_low_right";
        public const string ATTEMPTED_TACKLE_FOUL = "attempted_tackle_foul";
        public const string ATTEMPTS_CONCEDED_IBOX = "attempts_conceded_ibox";
        public const string ATTEMPTS_CONCEDED_OBOX = "attempts_conceded_obox";
        public const string BACKWARD_PASS = "backward_pass";
        public const string BALL_RECOVERY = "ball_recovery";
        public const string BIG_CHANCE_CREATED = "big_chance_created";
        public const string BIG_CHANCE_MISSED = "big_chance_missed";
        public const string BIG_CHANCE_SCORED = "big_chance_scored";
        public const string BLOCKED_CROSS = "blocked_cross";
        public const string BLOCKED_PASS = "blocked_pass";
        public const string BLOCKED_SCORING_ATT = "blocked_scoring_att";
        public const string CHALLENGE_LOST = "challenge_lost";
        public const string CLEAN_SHEET_AMC = "clean_sheet_amc";
        public const string CLEAN_SHEET_AMR = "clean_sheet_amr";
        public const string CLEAN_SHEET_DC = "clean_sheet_dc";
        public const string CLEAN_SHEET_DL = "clean_sheet_dl";
        public const string CLEAN_SHEET_DMC = "clean_sheet_dmc";
        public const string CLEAN_SHEET_DML = "clean_sheet_dml";
        public const string CLEAN_SHEET_DMR = "clean_sheet_dmr";
        public const string CLEAN_SHEET_DR = "clean_sheet_dr";
        public const string CLEAN_SHEET_FW = "clean_sheet_fw";
        public const string CLEAN_SHEET_GK = "clean_sheet_gk";
        public const string CLEARANCE_OFF_LINE = "clearance_off_line";
        public const string CORNER_TAKEN = "corner_taken";
        public const string CROSS_INACCURATE = "cross_inaccurate";
        public const string CROSSES_18YARD = "crosses_18yard";
        public const string CROSSES_18YARDPLUS = "crosses_18yardplus";
        public const string DANGEROUS_PLAY = "dangerous_play";
        public const string DISPOSSESSED = "dispossessed";
        public const string DIVE_CATCH = "dive_catch";
        public const string DIVE_SAVE = "dive_save";
        public const string DIVING_SAVE = "diving_save";
        public const string DRIBBLE_LOST = "dribble_lost";
        public const string DUEL_GROUND_LOST = "duel_ground_lost";
        public const string DUEL_GROUND_WON = "duel_ground_won";
        public const string DUEL_LOST = "duel_lost";
        public const string DUEL_WON = "duel_won";
        public const string EFFECTIVE_BLOCKED_CROSS = "effective_blocked_cross";
        public const string EFFECTIVE_CLEARANCE = "effective_clearance";
        public const string EFFECTIVE_HEAD_CLEARANCE = "effective_head_clearance";
        public const string ERROR_LEAD_TO_GOAL = "error_lead_to_goal";
        public const string ERROR_LEAD_TO_SHOT = "error_lead_to_shot";
        public const string FAILED_TO_BLOCK = "failed_to_block";
        public const string FIFTY_FIFTY = "fifty_fifty";
        public const string FINAL_THIRD_ENTRIES = "final_third_entries";
        public const string FORMATION_PLACE = "formation_place";
        public const string FOULED_FINAL_THIRD = "fouled_final_third";
        public const string FOULS = "fouls";
        public const string FREEKICK_CROSS = "freekick_cross";
        public const string FWD_PASS = "fwd_pass";
        public const string GAME_STARTED = "game_started";
        public const string GK_SMOTHER = "gk_smother";
        public const string GOAL_ASSIST = "goal_assist";
        public const string GOAL_ASSIST_INTENTIONAL = "goal_assist_intentional";
        public const string GOAL_ASSIST_OPENPLAY = "goal_assist_openplay";
        public const string GOAL_ASSIST_SETPLAY = "goal_assist_setplay";
        public const string GOAL_FASTBREAK = "goal_fastbreak";
        public const string GOAL_KICKS = "goal_kicks";
        public const string GOAL_NORMAL = "goal_normal";
        public const string GOAL_SCORED_BY_TEAM_AMC = "goal_scored_by_team_amc";
        public const string GOAL_SCORED_BY_TEAM_AML = "goal_scored_by_team_aml";
        public const string GOAL_SCORED_BY_TEAM_AMR = "goal_scored_by_team_amr";
        public const string GOAL_SCORED_BY_TEAM_DC = "goal_scored_by_team_dc";
        public const string GOAL_SCORED_BY_TEAM_DL = "goal_scored_by_team_dl";
        public const string GOAL_SCORED_BY_TEAM_DMC = "goal_scored_by_team_dmc";
        public const string GOAL_SCORED_BY_TEAM_DML = "goal_scored_by_team_dml";
        public const string GOAL_SCORED_BY_TEAM_DMR = "goal_scored_by_team_dmr";
        public const string GOAL_SCORED_BY_TEAM_DR = "goal_scored_by_team_dr";
        public const string GOAL_SCORED_BY_TEAM_FW = "goal_scored_by_team_fw";
        public const string GOAL_SCORED_BY_TEAM_FWL = "goal_scored_by_team_fwl";
        public const string GOAL_SCORED_BY_TEAM_FWR = "goal_scored_by_team_fwr";
        public const string GOAL_SCORED_BY_TEAM_GK = "goal_scored_by_team_gk";
        public const string GOAL_SCORED_BY_TEAM_MC = "goal_scored_by_team_mc";
        public const string GOAL_SCORED_BY_TEAM_ML = "goal_scored_by_team_ml";
        public const string GOAL_SCORED_BY_TEAM_MR = "goal_scored_by_team_mr";
        public const string GOAL_SCORED_BY_TEAM_SUB = "goal_scored_by_team_sub";
        public const string GOALS = "goals";
        public const string GOALS_CONCEDED_AMC = "goals_conceded_amc";
        public const string GOALS_CONCEDED_AML = "goals_conceded_aml";
        public const string GOALS_CONCEDED_AMR = "goals_conceded_amr";
        public const string GOALS_CONCEDED_DC = "goals_conceded_dc";
        public const string GOALS_CONCEDED_DL = "goals_conceded_dl";
        public const string GOALS_CONCEDED_DMC = "goals_conceded_dmc";
        public const string GOALS_CONCEDED_DR = "goals_conceded_dr";
        public const string GOALS_CONCEDED_FW = "goals_conceded_fw";
        public const string GOALS_CONCEDED_FWL = "goals_conceded_fwl";
        public const string GOALS_CONCEDED_FWR = "goals_conceded_fwr";
        public const string GOALS_CONCEDED_GK = "goals_conceded_gk";
        public const string GOALS_CONCEDED_IBOX = "goals_conceded_ibox";
        public const string GOALS_CONCEDED_MC = "goals_conceded_mc";
        public const string GOALS_CONCEDED_ML = "goals_conceded_ml";
        public const string GOALS_CONCEDED_MR = "goals_conceded_mr";
        public const string GOALS_CONCEDED_OBOX_AMC = "goals_conceded_obox_amc";
        public const string GOALS_CONCEDED_OBOX_AML = "goals_conceded_obox_aml";
        public const string GOALS_CONCEDED_OBOX_AMR = "goals_conceded_obox_amr";
        public const string GOALS_CONCEDED_OBOX_DC = "goals_conceded_obox_dc";
        public const string GOALS_CONCEDED_OBOX_DL = "goals_conceded_obox_dl";
        public const string GOALS_CONCEDED_OBOX_DMC = "goals_conceded_obox_dmc";
        public const string GOALS_CONCEDED_OBOX_DR = "goals_conceded_obox_dr";
        public const string GOALS_CONCEDED_OBOX_FW = "goals_conceded_obox_fw";
        public const string GOALS_CONCEDED_OBOX_GK = "goals_conceded_obox_gk";
        public const string GOALS_CONCEDED_OBOX_MC = "goals_conceded_obox_mc";
        public const string GOALS_CONCEDED_OBOX_ML = "goals_conceded_obox_ml";
        public const string GOALS_CONCEDED_OBOX_MR = "goals_conceded_obox_mr";
        public const string GOALS_CONCEDED_OBOX_SUB = "goals_conceded_obox_sub";
        public const string GOALS_CONCEDED_SUB = "goals_conceded_sub";
        public const string GOALS_OPENPLAY = "goals_openplay";
        public const string GOOD_HIGH_CLAIM = "good_high_claim";
        public const string HAND_BALL = "hand_ball";
        public const string HEAD_CLEARANCE = "head_clearance";
        public const string HEAD_PASS = "head_pass";
        public const string HIT_WOODWORK = "hit_woodwork";
        public const string INTERCEPTION = "interception";
        public const string INTERCEPTION_WON = "interception_won";
        public const string INTERCEPTIONS_IN_BOX = "interceptions_in_box";
        public const string KEEPER_CLAIM_HIGH_LOST = "keeper_claim_high_lost";
        public const string KEEPER_CLAIM_LOST = "keeper_claim_lost";
        public const string KEEPER_PICK_UP = "keeper_pick_up";
        public const string KEEPER_SWEEPER_LOST = "keeper_sweeper_lost";
        public const string KEEPER_THROWS = "keeper_throws";
        public const string LAST_MAN_TACKLE = "last_man_tackle";
        public const string LEFTSIDE_PASS = "leftside_pass";
        public const string LONG_PASS_OWN_TO_OPP = "long_pass_own_to_opp";
        public const string LONG_PASS_OWN_TO_OPP_SUCCESS = "long_pass_own_to_opp_success";
        public const string LOST_CORNERS = "lost_corners";
        public const string MAN_OF_THE_MATCH = "man_of_the_match";
        public const string MINS_PLAYED = "mins_played";
        public const string OFFSIDE_PROVOKED = "offside_provoked";
        public const string OFFTARGET_ATT_ASSIST = "offtarget_att_assist";
        public const string ONTARGET_ATT_ASSIST = "ontarget_att_assist";
        public const string ONTARGET_SCORING_ATT = "ontarget_scoring_att";
        public const string OPEN_PLAY_PASS = "open_play_pass";
        public const string OUTFIELDER_BLOCK = "outfielder_block";
        public const string OVERRUN = "overrun";
        public const string PASS_BACKZONE_INACCURATE = "pass_backzone_inaccurate";
        public const string PASS_FORWARDZONE_INACCURATE = "pass_forwardzone_inaccurate";
        public const string PASS_INACCURATE = "pass_inaccurate";
        public const string PASS_LONGBALL_INACCURATE = "pass_longball_inaccurate";
        public const string PASS_THROUGHBALL_INACURATE = "pass_throughball_inacurate";
        public const string PASSES_LEFT = "passes_left";
        public const string PASSES_RIGHT = "passes_right";
        public const string PEN_AREA_ENTRIES = "pen_area_entries";
        public const string PEN_GOALS_CONCEDED = "pen_goals_conceded";
        public const string PENALTY_CONCEDED = "penalty_conceded";
        public const string PENALTY_FACED = "penalty_faced";
        public const string PENALTY_MISSED = "penalty_missed";
        public const string PENALTY_SAVE = "penalty_save";
        public const string PENALTY_SHOOTOUT_CONCEDED_GK = "penalty_shootout_conceded_gk";
        public const string PENALTY_SHOOTOUT_MISSED_OFF_TARGET = "penalty_shootout_missed_off_target";
        public const string PENALTY_SHOOTOUT_SAVED = "penalty_shootout_saved";
        public const string PENALTY_SHOOTOUT_SAVED_GK = "penalty_shootout_saved_gk";
        public const string PENALTY_SHOOTOUT_SCORED = "penalty_shootout_scored";
        public const string PENALTY_WON = "penalty_won";
        public const string POSITION = "position";
        public const string POSS_LOST_ALL = "poss_lost_all";
        public const string POSS_LOST_CTRL = "poss_lost_ctrl";
        public const string POSS_WON_ATT_3RD = "poss_won_att_3rd";
        public const string POSS_WON_DEF_3RD = "poss_won_def_3rd";
        public const string POSS_WON_MID_3RD = "poss_won_mid_3rd";
        public const string POST_SCORING_ATT = "post_scoring_att";
        public const string PUNCHES = "punches";
        public const string PUT_THROUGH = "put_through";
        public const string RATING = "rating";
        public const string RATING_DEFENSIVE = "rating_defensive";
        public const string RATING_DEFENSIVE_POINTS = "rating_defensive_points";
        public const string RATING_OFFENSIVE = "rating_offensive";
        public const string RATING_OFFENSIVE_POINTS = "rating_offensive_points";
        public const string RATING_POINTS = "rating_points";
        public const string RED_CARD = "red_card";
        public const string RIGHTSIDE_PASS = "rightside_pass";
        public const string SAVED_IBOX = "saved_ibox";
        public const string SAVED_OBOX = "saved_obox";
        public const string SAVES = "saves";
        public const string SECOND_GOAL_ASSIST = "second_goal_assist";
        public const string SECOND_YELLOW = "second_yellow";
        public const string SHIELD_BALL_OOP = "shield_ball_oop";
        public const string SHOT_FASTBREAK = "shot_fastbreak";
        public const string SHOT_OFF_TARGET = "shot_off_target";
        public const string SIX_YARD_BLOCK = "six_yard_block";
        public const string STAND_CATCH = "stand_catch";
        public const string SUCCESSFUL_FIFTY_FIFTY = "successful_fifty_fifty";
        public const string SUCCESSFUL_FINAL_THIRD_PASSES = "successful_final_third_passes";
        public const string SUCCESSFUL_OPEN_PLAY_PASS = "successful_open_play_pass";
        public const string SUCCESSFUL_PUT_THROUGH = "successful_put_through";
        public const string TACKLE_LOST = "tackle_lost";
        public const string TOTAL_ATT_ASSIST = "total_att_assist";
        public const string TOTAL_BACK_ZONE_PASS = "total_back_zone_pass";
        public const string TOTAL_CHIPPED_PASS = "total_chipped_pass";
        public const string TOTAL_CLEARANCE = "total_clearance";
        public const string TOTAL_CONTEST = "total_contest";
        public const string TOTAL_CORNERS_INTOBOX = "total_corners_intobox";
        public const string TOTAL_CROSS = "total_cross";
        public const string TOTAL_CROSS_NOCORNER = "total_cross_nocorner";
        public const string TOTAL_FASTBREAK = "total_fastbreak";
        public const string TOTAL_FINAL_THIRD_PASSES = "total_final_third_passes";
        public const string TOTAL_FLICK_ON = "total_flick_on";
        public const string TOTAL_FWD_ZONE_PASS = "total_fwd_zone_pass";
        public const string TOTAL_HIGH_CLAIM = "total_high_claim";
        public const string TOTAL_KEEPER_SWEEPER = "total_keeper_sweeper";
        public const string TOTAL_LAUNCHES = "total_launches";
        public const string TOTAL_LAYOFFS = "total_layoffs";
        public const string TOTAL_LONG_BALLS = "total_long_balls";
        public const string TOTAL_OFFSIDE = "total_offside";
        public const string TOTAL_PASS = "total_pass";
        public const string TOTAL_PULL_BACK = "total_pull_back";
        public const string TOTAL_SCORING_ATT = "total_scoring_att";
        public const string TOTAL_SUB_OFF = "total_sub_off";
        public const string TOTAL_SUB_ON = "total_sub_on";
        public const string TOTAL_TACKLE = "total_tackle";
        public const string TOTAL_THROUGH_BALL = "total_through_ball";
        public const string TOTAL_THROWS = "total_throws";
        public const string TOUCHES = "touches";
        public const string TURNOVER = "turnover";
        public const string UNSUCCESSFUL_TOUCH = "unsuccessful_touch";
        public const string WAS_FOULED = "was_fouled";
        public const string WON_CONTEST = "won_contest";
        public const string WON_CORNERS = "won_corners";
        public const string WON_TACKLE = "won_tackle";
        public const string YELLOW_CARD = "yellow_card";
    }