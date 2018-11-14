from utilities import *
from toee import *
from toee import anyone
from Co8 import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.map == 5158):
		if (game.global_flags[989] == 1):
			triggerer.begin_dialog( attachee, 130 )
		elif (not attachee.has_met( triggerer )):
			triggerer.begin_dialog( attachee, 1 )
		elif (game.global_flags[982] == 1):
			triggerer.begin_dialog( attachee, 180 )
		elif (attachee.has_met( triggerer )) and (game.global_flags[983] == 0) and (game.global_vars[930] == 0):
			triggerer.begin_dialog( attachee, 140 )
		elif (attachee.has_met( triggerer )) and (game.global_flags[983] == 1) and (game.global_vars[930] == 0):
			triggerer.begin_dialog( attachee, 150 )
		elif (attachee.has_met( triggerer )) and (game.global_flags[983] == 0) and (game.global_vars[930] == 2):
			triggerer.begin_dialog( attachee, 160 )
		elif (attachee.has_met( triggerer )) and (game.global_flags[983] == 0) and (game.global_vars[930] == 1):
			triggerer.begin_dialog( attachee, 280 )
	elif (attachee.map == 5071 or attachee.map == 5072 or attachee.map == 5073 or attachee.map == 5075 or attachee.map == 5076 or attachee.map == 5077):
		triggerer.begin_dialog( attachee, 150 )
	else:
		return RUN_DEFAULT
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if ( (game.global_vars[959] == 1) and (attachee.map == 5052) ):
		attachee.object_flag_unset(OF_OFF)
	if ( (game.global_vars[978] == 1) and (attachee.map == 5121) ):
		attachee.object_flag_unset(OF_OFF)
		if (game.global_flags[961] == 0):
			game.timevent_add( term_surv, (), 864000000 )	# 10 days
			game.global_flags[961] = 1
	if ( (game.global_vars[978] == 2) and (game.global_flags[967] == 1) and (attachee.map == 5174) ):
		attachee.object_flag_unset(OF_OFF)
		attachee.runoff(attachee.location-3)
		game.global_vars[978] = 3
	if ( (game.global_vars[978] == 2) and (game.global_flags[997] == 1) and (attachee.map == 5152) ):
		attachee.object_flag_unset(OF_OFF)
		attachee.runoff(attachee.location-3)
		game.global_vars[978] = 4
	if ( (game.global_vars[978] == 2) and (game.global_flags[966] == 1) and (attachee.map == 5146) ):
		attachee.object_flag_unset(OF_OFF)
		attachee.runoff(attachee.location-3)
		game.global_vars[978] = 5
	if ( (game.global_vars[978] >= 2) and (attachee.map == 5121) ):
		attachee.object_flag_set(OF_OFF)
	if (attachee.map == 5158 or attachee.map == 5159 or attachee.map == 5160):
		if (game.global_vars[945] >= 25):
			attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	gloves = attachee.item_find(6201)
	gloves.destroy()
	create_item_in_inventory( 6046, attachee )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	if (attachee.map == 5071 or attachee.map == 5072 or attachee.map == 5073 or attachee.map == 5075 or attachee.map == 5076 or attachee.map == 5077):
		game.global_vars[943] = game.global_vars[943] + 1
		if (attachee.name == 14653):
			if (game.global_vars[943] == 0):
				return RUN_DEFAULT
			elif (game.global_vars[943] == 1):
				attachee.obj_set_int(obj_f_critter_strategy, 418)
				return RUN_DEFAULT
			elif (game.global_vars[943] == 2):
				attachee.obj_set_int(obj_f_critter_strategy, 419)
				return RUN_DEFAULT
			elif (game.global_vars[943] == 3):
				attachee.obj_set_int(obj_f_critter_strategy, 420)
				return RUN_DEFAULT
			elif (game.global_vars[943] == 4):
				attachee.obj_set_int(obj_f_critter_strategy, 417)
				return RUN_DEFAULT
			elif (game.global_vars[943] >= 5):
				run_off_2( attachee, triggerer )
				return SKIP_DEFAULT
		elif (attachee.name == 14652):
			if (game.global_vars[943] >= 5):
				run_off_2( attachee, triggerer )
				return SKIP_DEFAULT
			else:
				return RUN_DEFAULT


def san_end_combat( attachee, triggerer ):
	if (game.global_vars[943] <= 4):
		game.sound( 4116, 1 )
		for obj in game.obj_list_vicinity( triggerer.location, OLC_PC ):
			game.particles( "Trap-Spores", obj )
			obj.condition_add_with_args("Poisoned",3,0)
			obj.condition_add_with_args("Poisoned",25,0)
			obj.condition_add_with_args("Prone",4,0)
		for obj in game.obj_list_vicinity( triggerer.location, OLC_NPC ):
			if (obj.name == 8000 or obj.name == 8001 or obj.name == 8002 or obj.name == 8003 or obj.name == 8004 or obj.name == 8005 or obj.name == 8010 or obj.name == 8014 or obj.name == 8015 or obj.name == 8020 or obj.name == 8021 or obj.name == 8022 or obj.name == 8023 or obj.name == 8025 or obj.name == 8026 or obj.name == 8029 or obj.name == 8030 or obj.name == 8031 or obj.name == 8034 or obj.name == 8039 or obj.name == 8040 or obj.name == 8050 or obj.name == 8054 or obj.name == 8056 or obj.name == 8057 or obj.name == 8058 or obj.name == 8060 or obj.name == 8061 or obj.name == 8062 or obj.name == 8067 or obj.name == 8069 or obj.name == 8070 or obj.name == 8071 or obj.name == 8072 or obj.name == 8714 or obj.name == 8716 or obj.name == 8717 or obj.name == 8718 or obj.name == 8730):
				game.particles( "Trap-Spores", obj )
				obj.condition_add_with_args("Poisoned",3,0)
				obj.condition_add_with_args("Poisoned",25,0)
				obj.condition_add_with_args("Prone",4,0)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.map == 5052):
		if (not game.combat_is_active()):
			if (is_better_to_talk(attachee, game.party[0])):
				if (game.global_vars[959] == 1):
					game.party[0].turn_towards(attachee)
					game.party[0].begin_dialog(attachee,230)
					game.global_vars[959] = 2
	elif (attachee.map == 5071 or attachee.map == 5075):	# re forest
		if (not game.combat_is_active()):
			if (attachee.name == 14651):
				if (game.global_vars[945] == 13 or game.global_vars[945] == 14 or game.global_vars[945] == 15):
					if (is_better_to_talk(attachee, game.party[0])):
						StopCombat(attachee, 0)
						attachee.float_line(10000,triggerer)
						game.new_sid = 0
				elif (game.global_vars[945] == 19 or game.global_vars[945] == 20 or game.global_vars[945] == 21):
					if (is_better_to_talk(attachee, game.party[0])):
						game.global_vars[945] = 22
						game.party[0].begin_dialog(attachee,200)
	elif (attachee.map == 5072 or attachee.map == 5076):	# re swamp
		if (not game.combat_is_active()):
			if (attachee.name == 14651):
				if (game.global_vars[945] == 13 or game.global_vars[945] == 14 or game.global_vars[945] == 15):
					if (is_better_to_talk(attachee, game.party[0])):
						StopCombat(attachee, 0)
						attachee.float_line(20000,triggerer)
						game.new_sid = 0
				elif (game.global_vars[945] == 19 or game.global_vars[945] == 20 or game.global_vars[945] == 21):
					if (is_better_to_talk(attachee, game.party[0])):
						game.global_vars[945] = 23
						game.party[0].begin_dialog(attachee,200)
	elif (attachee.map == 5073 or attachee.map == 5077):	# re river
		if (not game.combat_is_active()):
			if (attachee.name == 14651):
				if (game.global_vars[945] == 13 or game.global_vars[945] == 14 or game.global_vars[945] == 15):
					if (is_better_to_talk(attachee, game.party[0])):
						StopCombat(attachee, 0)
						attachee.float_line(30000,triggerer)
						game.new_sid = 0
				elif (game.global_vars[945] == 19 or game.global_vars[945] == 20 or game.global_vars[945] == 21):
					if (is_better_to_talk(attachee, game.party[0])):
						game.global_vars[945] = 24
						game.party[0].begin_dialog(attachee,200)
	return RUN_DEFAULT


def san_will_kos( attachee, triggerer ):
	if (game.global_flags[989] == 1):
		return RUN_DEFAULT
	return SKIP_DEFAULT


def wait_a_day( attachee, triggerer ):
	game.timevent_add( wait, ( attachee, ), 86400000 )	# 1 day
	return RUN_DEFAULT


def wait( attachee ):
	game.global_vars[930] = 2
	return RUN_DEFAULT


def term_surv():
	game.global_vars[978] = 2
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 50):
		return 1
	return 0


def go_away( attachee ):
	attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	game.timevent_add( go_away, ( attachee, ), 5000 )
	return RUN_DEFAULT


def run_off_2( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	nephew1 = find_npc_near(attachee,14653)
	nephew1.runoff(attachee.location-3)
	nephew2 = find_npc_near(attachee,14653)
	nephew2.runoff(attachee.location-3)
	nephew3 = find_npc_near(attachee,14653)
	nephew3.runoff(attachee.location-3)
	cousin1 = find_npc_near(attachee,14652)
	cousin1.runoff(attachee.location-3)
	if (game.global_flags[866] == 0):
		game.global_flags[866] = 1
		if (attachee.map == 5071 or attachee.map == 5075):
			game.timevent_add( pass_out_1_a, ( attachee, triggerer ), 2000 )			# 2 seconds
			for obj in game.obj_list_vicinity( triggerer.location, OLC_PC ):
				obj.condition_add_with_args("Prone",8200,0)
				obj.condition_add_with_args("Paralyzed",8200,0)
			for obj in game.obj_list_vicinity( triggerer.location, OLC_NPC ):
				if (obj.name == 8000 or obj.name == 8001 or obj.name == 8002 or obj.name == 8003 or obj.name == 8004 or obj.name == 8005 or obj.name == 8010 or obj.name == 8014 or obj.name == 8015 or obj.name == 8020 or obj.name == 8021 or obj.name == 8022 or obj.name == 8023 or obj.name == 8025 or obj.name == 8026 or obj.name == 8029 or obj.name == 8030 or obj.name == 8031 or obj.name == 8034 or obj.name == 8039 or obj.name == 8040 or obj.name == 8050 or obj.name == 8054 or obj.name == 8056 or obj.name == 8057 or obj.name == 8058 or obj.name == 8060 or obj.name == 8061 or obj.name == 8062 or obj.name == 8067 or obj.name == 8069 or obj.name == 8070 or obj.name == 8071 or obj.name == 8072 or obj.name == 8714 or obj.name == 8716 or obj.name == 8717 or obj.name == 8718 or obj.name == 8730):
					obj.condition_add_with_args("Prone",8200,0)
					obj.condition_add_with_args("Paralyzed",8200,0)
		elif (attachee.map == 5072 or attachee.map == 5073 or attachee.map == 5076 or attachee.map == 5077):
			game.timevent_add( pass_out_1_b, ( attachee, triggerer ), 2000 )			# 2 seconds
			for obj in game.obj_list_vicinity( triggerer.location, OLC_PC ):
				obj.condition_add_with_args("Prone",8200,0)
				obj.condition_add_with_args("Paralyzed",8200,0)
			for obj in game.obj_list_vicinity( triggerer.location, OLC_NPC ):
				if (obj.name == 8000 or obj.name == 8001 or obj.name == 8002 or obj.name == 8003 or obj.name == 8004 or obj.name == 8005 or obj.name == 8010 or obj.name == 8014 or obj.name == 8015 or obj.name == 8020 or obj.name == 8021 or obj.name == 8022 or obj.name == 8023 or obj.name == 8025 or obj.name == 8026 or obj.name == 8029 or obj.name == 8030 or obj.name == 8031 or obj.name == 8034 or obj.name == 8039 or obj.name == 8040 or obj.name == 8050 or obj.name == 8054 or obj.name == 8056 or obj.name == 8057 or obj.name == 8058 or obj.name == 8060 or obj.name == 8061 or obj.name == 8062 or obj.name == 8067 or obj.name == 8069 or obj.name == 8070 or obj.name == 8071 or obj.name == 8072 or obj.name == 8714 or obj.name == 8716 or obj.name == 8717 or obj.name == 8718 or obj.name == 8730):
					obj.condition_add_with_args("Prone",8200,0)
					obj.condition_add_with_args("Paralyzed",8200,0)
	return RUN_DEFAULT


def run_off_3( attachee, triggerer ):
	attachee.object_flag_set(OF_OFF)
	game.particles( "sp-Invisibility", attachee )
	cousin1 = find_npc_near(attachee,14651)
	cousin1.object_flag_set(OF_OFF)
	game.particles( "sp-Invisibility", cousin1 )
	cousin2 = find_npc_near(attachee,14652)
	cousin2.object_flag_set(OF_OFF)
	game.particles( "sp-Invisibility", cousin2 )
	cousin3 = find_npc_near(attachee,14652)
	cousin3.object_flag_set(OF_OFF)
	game.particles( "sp-Invisibility", cousin3 )
	cousin4 = find_npc_near(attachee,14652)
	cousin4.object_flag_set(OF_OFF)
	game.particles( "sp-Invisibility", cousin4 )
	cousin5 = find_npc_near(attachee,14652)
	cousin5.object_flag_set(OF_OFF)
	game.particles( "sp-Invisibility", cousin5 )
	cousin6 = find_npc_near(attachee,14652)
	cousin6.object_flag_set(OF_OFF)
	game.particles( "sp-Invisibility", cousin6 )
	cousin7 = find_npc_near(attachee,14652)
	cousin7.object_flag_set(OF_OFF)
	game.particles( "sp-Invisibility", cousin7 )
	cousin8 = find_npc_near(attachee,14652)
	cousin8.object_flag_set(OF_OFF)
	game.particles( "sp-Invisibility", cousin8 )
	game.sound( 4031, 1 )
	return RUN_DEFAULT


def pass_out_1_a( attachee, triggerer ):
	game.fade(43200,4119,0,12)
	game.sound( 4119, 1 )
	game.timevent_add( start_snowing, (), 12000 )		# 12 seconds
	if (game.global_vars[945] == 7):
		game.global_vars[945] = 10
		if (attachee.map == 5071 or attachee.map == 5075): 
			game.timevent_add( spawn_cousins_circle_forest, (), 14000 )		# 14 seconds
		elif (attachee.map == 5072 or attachee.map == 5073 or attachee.map == 5076 or attachee.map == 5077):
			game.timevent_add( spawn_cousins_circle_swamp_river, (), 14000 )	# 14 seconds
	elif (game.global_vars[945] == 8):
		game.global_vars[945] = 11
		if (attachee.map == 5071 or attachee.map == 5075): 
			game.timevent_add( spawn_cousins_circle_forest, (), 14000 )		# 14 seconds
		elif (attachee.map == 5072 or attachee.map == 5073 or attachee.map == 5076 or attachee.map == 5077):
			game.timevent_add( spawn_cousins_circle_swamp_river, (), 14000 )	# 14 seconds
	elif (game.global_vars[945] == 9):
		game.global_vars[945] = 12
		if (attachee.map == 5071 or attachee.map == 5075): 
			game.timevent_add( spawn_cousins_circle_forest, (), 14000 )		# 14 seconds
		elif (attachee.map == 5072 or attachee.map == 5073 or attachee.map == 5076 or attachee.map == 5077):
			game.timevent_add( spawn_cousins_circle_swamp_river, (), 14000 )	# 14 seconds
	return


def pass_out_1_b( attachee, triggerer ):
	game.fade(43200,4117,0,12)
	game.sound( 4117, 1 )
	game.timevent_add( start_raining, (), 12000 )		# 12 seconds
	if (game.global_vars[945] == 7):
		game.global_vars[945] = 10
		if (attachee.map == 5071 or attachee.map == 5075): 
			game.timevent_add( spawn_cousins_circle_forest, (), 14000 )		# 14 seconds
		elif (attachee.map == 5072 or attachee.map == 5073 or attachee.map == 5076 or attachee.map == 5077):
			game.timevent_add( spawn_cousins_circle_swamp_river, (), 14000 )	# 14 seconds
	elif (game.global_vars[945] == 8):
		game.global_vars[945] = 11
		if (attachee.map == 5071 or attachee.map == 5075): 
			game.timevent_add( spawn_cousins_circle_forest, (), 14000 )		# 14 seconds
		elif (attachee.map == 5072 or attachee.map == 5073 or attachee.map == 5076 or attachee.map == 5077):
			game.timevent_add( spawn_cousins_circle_swamp_river, (), 14000 )	# 14 seconds
	elif (game.global_vars[945] == 9):
		game.global_vars[945] = 12
		if (attachee.map == 5071 or attachee.map == 5075): 
			game.timevent_add( spawn_cousins_circle_forest, (), 14000 )		# 14 seconds
		elif (attachee.map == 5072 or attachee.map == 5073 or attachee.map == 5076 or attachee.map == 5077):
			game.timevent_add( spawn_cousins_circle_swamp_river, (), 14000 )	# 14 seconds
	return


def start_snowing():
	game.particles( "ef-air node", location_from_axis(460, 460) )
	game.particles( "ef-air node", location_from_axis(500, 500) )
	game.particles( "ef-air node", location_from_axis(500, 460) )
	game.particles( "ef-air node", location_from_axis(460, 500) )
	return


def start_raining():
	game.particles( "Rain Test", location_from_axis(460, 460) )
	game.particles( "Rain Test", location_from_axis(500, 500) )
	game.particles( "Rain Test", location_from_axis(500, 460) )
	game.particles( "Rain Test", location_from_axis(460, 500) )
	return


def spawn_cousins_circle_forest():
	cousin1 = game.obj_create(14651, location_from_axis(472, 472))
	cousin1.turn_towards(game.party[0])
	cousin1.concealed_set(1)
	cousin1.unconceal()
	cousin1.npc_flag_unset(ONF_KOS)
	cousin2 = game.obj_create(14652, location_from_axis(488, 488))
	cousin2.turn_towards(game.party[0])
	cousin2.concealed_set(1)
	cousin2.unconceal()
	cousin2.npc_flag_unset(ONF_KOS)
	cousin3 = game.obj_create(14652, location_from_axis(488, 472))
	cousin3.turn_towards(game.party[0])
	cousin3.concealed_set(1)
	cousin3.unconceal()
	cousin3.npc_flag_unset(ONF_KOS)
	cousin4 = game.obj_create(14652, location_from_axis(472, 488))
	cousin4.turn_towards(game.party[0])
	cousin4.concealed_set(1)
	cousin4.unconceal()
	cousin4.npc_flag_unset(ONF_KOS)
	cousin5 = game.obj_create(14652, location_from_axis(480, 470))
	cousin5.turn_towards(game.party[0])
	cousin5.concealed_set(1)
	cousin5.unconceal()
	cousin5.npc_flag_unset(ONF_KOS)
	cousin6 = game.obj_create(14652, location_from_axis(480, 490))
	cousin6.turn_towards(game.party[0])
	cousin6.concealed_set(1)
	cousin6.unconceal()
	cousin6.npc_flag_unset(ONF_KOS)
	cousin7 = game.obj_create(14652, location_from_axis(490, 480))
	cousin7.turn_towards(game.party[0])
	cousin7.concealed_set(1)
	cousin7.unconceal()
	cousin7.npc_flag_unset(ONF_KOS)
	cousin8 = game.obj_create(14652, location_from_axis(470, 480))
	cousin8.turn_towards(game.party[0])
	cousin8.concealed_set(1)
	cousin8.unconceal()
	cousin8.npc_flag_unset(ONF_KOS)
	if (game.global_vars[945] == 10):
		game.global_vars[945] = 13
	elif (game.global_vars[945] == 11):
		game.global_vars[945] = 14
	elif (game.global_vars[945] == 12):
		game.global_vars[945] = 15
	game.timevent_add( pass_out_2_a, (), 4000 )		# 4 seconds
	return


def spawn_cousins_circle_swamp_river():
	cousin1 = game.obj_create(14651, location_from_axis(472, 472))
	cousin1.turn_towards(game.party[0])
	cousin1.concealed_set(1)
	cousin1.unconceal()
	cousin1.npc_flag_unset(ONF_KOS)
	cousin2 = game.obj_create(14652, location_from_axis(488, 488))
	cousin2.turn_towards(game.party[0])
	cousin2.concealed_set(1)
	cousin2.unconceal()
	cousin2.npc_flag_unset(ONF_KOS)
	cousin3 = game.obj_create(14652, location_from_axis(488, 472))
	cousin3.turn_towards(game.party[0])
	cousin3.concealed_set(1)
	cousin3.unconceal()
	cousin3.npc_flag_unset(ONF_KOS)
	cousin4 = game.obj_create(14652, location_from_axis(472, 488))
	cousin4.turn_towards(game.party[0])
	cousin4.concealed_set(1)
	cousin4.unconceal()
	cousin4.npc_flag_unset(ONF_KOS)
	cousin5 = game.obj_create(14652, location_from_axis(480, 470))
	cousin5.turn_towards(game.party[0])
	cousin5.concealed_set(1)
	cousin5.unconceal()
	cousin5.npc_flag_unset(ONF_KOS)
	cousin6 = game.obj_create(14652, location_from_axis(480, 490))
	cousin6.turn_towards(game.party[0])
	cousin6.concealed_set(1)
	cousin6.unconceal()
	cousin6.npc_flag_unset(ONF_KOS)
	cousin7 = game.obj_create(14652, location_from_axis(490, 480))
	cousin7.turn_towards(game.party[0])
	cousin7.concealed_set(1)
	cousin7.unconceal()
	cousin7.npc_flag_unset(ONF_KOS)
	cousin8 = game.obj_create(14652, location_from_axis(470, 480))
	cousin8.turn_towards(game.party[0])
	cousin8.concealed_set(1)
	cousin8.unconceal()
	cousin8.npc_flag_unset(ONF_KOS)
	if (game.global_vars[945] == 10):
		game.global_vars[945] = 13
	elif (game.global_vars[945] == 11):
		game.global_vars[945] = 14
	elif (game.global_vars[945] == 12):
		game.global_vars[945] = 15
	game.timevent_add( pass_out_2_b, (), 4000 )		# 4 seconds
	return


def pass_out_2_a():
	game.fade(21600,0,0,6)
	if (game.global_vars[945] == 13):
		game.global_vars[945] = 16
		game.timevent_add( spawn_boss_forest, (), 6000 )	# 6 seconds
	elif (game.global_vars[945] == 14):
		game.global_vars[945] = 17
		game.timevent_add( spawn_boss_forest, (), 6000 )	# 6 seconds
	elif (game.global_vars[945] == 15):
		game.global_vars[945] = 18
		game.timevent_add( spawn_boss_forest, (), 6000 )	# 6 seconds
	return


def pass_out_2_b():
	game.fade(21600,0,0,6)
	if (game.global_vars[945] == 13):
		game.global_vars[945] = 16
		game.timevent_add( spawn_boss_swamp_river, (), 6000 )	# 6 seconds
	elif (game.global_vars[945] == 14):
		game.global_vars[945] = 17
		game.timevent_add( spawn_boss_swamp_river, (), 6000 )	# 6 seconds
	elif (game.global_vars[945] == 15):
		game.global_vars[945] = 18
		game.timevent_add( spawn_boss_swamp_river, (), 6000 )	# 6 seconds
	return


def strip_forest( attachee, triggerer ):
	for obj in game.obj_list_vicinity( triggerer.location, OLC_PC ):
		unequip_forest( 3, obj )
		unequip_forest( 5, obj )
	for obj in game.obj_list_vicinity( triggerer.location, OLC_NPC ):
		if (obj.name == 8000 or obj.name == 8001 or obj.name == 8002 or obj.name == 8003 or obj.name == 8004 or obj.name == 8005 or obj.name == 8010 or obj.name == 8014 or obj.name == 8015 or obj.name == 8020 or obj.name == 8021 or obj.name == 8022 or obj.name == 8023 or obj.name == 8025 or obj.name == 8026 or obj.name == 8029 or obj.name == 8030 or obj.name == 8031 or obj.name == 8034 or obj.name == 8039 or obj.name == 8040 or obj.name == 8050 or obj.name == 8054 or obj.name == 8056 or obj.name == 8057 or obj.name == 8058 or obj.name == 8060 or obj.name == 8061 or obj.name == 8062 or obj.name == 8067 or obj.name == 8069 or obj.name == 8070 or obj.name == 8071 or obj.name == 8072 or obj.name == 8714 or obj.name == 8716 or obj.name == 8717 or obj.name == 8718 or obj.name == 8730):
			unequip_forest( 3, obj )
			unequip_forest( 5, obj )
	return


def unequip_forest( slot, npc ):
	# doesn't work for npcs with no transfer flag on items
	random_x = game.random_range(513,528)
	random_y = game.random_range(477,492)
	container = game.obj_create(1003, location_from_axis(random_x, random_y))
	container.rotation = 1.0
	item = npc.item_worn_at(slot)
	container.item_get(item)
#	npc.item_get(item)
#	container.destroy()
	return


def strip_swamp( attachee, triggerer ):
	for obj in game.obj_list_vicinity( triggerer.location, OLC_PC ):
		unequip_swamp( 3, obj )
		unequip_swamp( 5, obj )
	for obj in game.obj_list_vicinity( triggerer.location, OLC_NPC ):
		if (obj.name == 8000 or obj.name == 8001 or obj.name == 8002 or obj.name == 8003 or obj.name == 8004 or obj.name == 8005 or obj.name == 8010 or obj.name == 8014 or obj.name == 8015 or obj.name == 8020 or obj.name == 8021 or obj.name == 8022 or obj.name == 8023 or obj.name == 8025 or obj.name == 8026 or obj.name == 8029 or obj.name == 8030 or obj.name == 8031 or obj.name == 8034 or obj.name == 8039 or obj.name == 8040 or obj.name == 8050 or obj.name == 8054 or obj.name == 8056 or obj.name == 8057 or obj.name == 8058 or obj.name == 8060 or obj.name == 8061 or obj.name == 8062 or obj.name == 8067 or obj.name == 8069 or obj.name == 8070 or obj.name == 8071 or obj.name == 8072 or obj.name == 8714 or obj.name == 8716 or obj.name == 8717 or obj.name == 8718 or obj.name == 8730):
			unequip_swamp( 3, obj )
			unequip_swamp( 5, obj )
	return


def unequip_swamp( slot, npc ):
	# doesn't work for npcs with no transfer flag on items
	random_x = game.random_range(467,478)
	random_y = game.random_range(444,455)
	container = game.obj_create(1003, location_from_axis(random_x, random_y))
	container.rotation = 2.5
	item = npc.item_worn_at(slot)
	container.item_get(item)
#	npc.item_get(item)
#	container.destroy()
	return


def strip_river( attachee, triggerer ):
	for obj in game.obj_list_vicinity( triggerer.location, OLC_PC ):
		unequip_river( 3, obj )
		unequip_river( 5, obj )
	for obj in game.obj_list_vicinity( triggerer.location, OLC_NPC ):
		if (obj.name == 8000 or obj.name == 8001 or obj.name == 8002 or obj.name == 8003 or obj.name == 8004 or obj.name == 8005 or obj.name == 8010 or obj.name == 8014 or obj.name == 8015 or obj.name == 8020 or obj.name == 8021 or obj.name == 8022 or obj.name == 8023 or obj.name == 8025 or obj.name == 8026 or obj.name == 8029 or obj.name == 8030 or obj.name == 8031 or obj.name == 8034 or obj.name == 8039 or obj.name == 8040 or obj.name == 8050 or obj.name == 8054 or obj.name == 8056 or obj.name == 8057 or obj.name == 8058 or obj.name == 8060 or obj.name == 8061 or obj.name == 8062 or obj.name == 8067 or obj.name == 8069 or obj.name == 8070 or obj.name == 8071 or obj.name == 8072 or obj.name == 8714 or obj.name == 8716 or obj.name == 8717 or obj.name == 8718 or obj.name == 8730):
			unequip_river( 3, obj )
			unequip_river( 5, obj )
	return


def unequip_river( slot, npc ):
	# doesn't work for npcs with no transfer flag on items
	random_x = game.random_range(469,484)
	random_y = game.random_range(511,526)
	container = game.obj_create(1049, location_from_axis(random_x, random_y))
	container.rotation = 5.5
	item = npc.item_worn_at(slot)
	container.item_get(item)
#	npc.item_get(item)
#	container.destroy()
	return


def spawn_boss_forest():
	cousin9 = game.obj_create(14651, location_from_axis(475, 475))
	cousin9.turn_towards(game.party[0])
	cousin9.npc_flag_unset(ONF_KOS)
	wind_sound_1 = game.obj_create(2145, location_from_axis(460, 460))
	wind_sound_2 = game.obj_create(2145, location_from_axis(500, 500))
	wind_sound_3 = game.obj_create(2145, location_from_axis(500, 460))
	wind_sound_4 = game.obj_create(2145, location_from_axis(460, 500))
	if (game.global_vars[945] == 16):
		game.global_vars[945] = 19
	elif (game.global_vars[945] == 17):
		game.global_vars[945] = 20
	elif (game.global_vars[945] == 18):
		game.global_vars[945] = 21
	return


def spawn_boss_swamp_river():
	cousin9 = game.obj_create(14651, location_from_axis(475, 475))
	cousin9.turn_towards(game.party[0])
	cousin9.npc_flag_unset(ONF_KOS)
	wind_sound_1 = game.obj_create(2144, location_from_axis(460, 460))
	wind_sound_2 = game.obj_create(2144, location_from_axis(500, 500))
	wind_sound_3 = game.obj_create(2144, location_from_axis(500, 460))
	wind_sound_4 = game.obj_create(2144, location_from_axis(460, 500))
	if (game.global_vars[945] == 16):
		game.global_vars[945] = 19
	elif (game.global_vars[945] == 17):
		game.global_vars[945] = 20
	elif (game.global_vars[945] == 18):
		game.global_vars[945] = 21
	return


def spawn_attackers_for_snitch( attachee, triggerer ):
	if (attachee.map == 5071 or attachee.map == 5075):	# forests
		tyrant1 = game.obj_create(14648, location_from_axis(495, 480))
		tyrant1.turn_towards(game.party[0])
		tyrant1.concealed_set(1)
		tyrant1.unconceal()
		tyrant1.attack(triggerer)
		tyrant2 = game.obj_create(14648, location_from_axis(465, 480))
		tyrant2.turn_towards(game.party[0])
		tyrant2.concealed_set(1)
		tyrant2.unconceal()
		tyrant2.attack(triggerer)
		tyrant3 = game.obj_create(14648, location_from_axis(480, 465))
		tyrant3.turn_towards(game.party[0])
		tyrant3.concealed_set(1)
		tyrant3.unconceal()
		tyrant3.attack(triggerer)
		tyrant4 = game.obj_create(14648, location_from_axis(480, 495))
		tyrant4.turn_towards(game.party[0])
		tyrant4.concealed_set(1)
		tyrant4.unconceal()
		tyrant4.attack(triggerer)
		umberhulk = game.obj_create(14260, location_from_axis(520, 484))
		umberhulk.turn_towards(game.party[0])
		ogre1 = game.obj_create(14689, location_from_axis(472, 465))
		ogre1.turn_towards(game.party[0])
		ogre1.concealed_set(1)
		ogre1.unconceal()
		ogre1.attack(triggerer)
		ogre2 = game.obj_create(14689, location_from_axis(465, 472))
		ogre2.turn_towards(game.party[0])
		ogre2.concealed_set(1)
		ogre2.unconceal()
		ogre2.attack(triggerer)
		ogre3 = game.obj_create(14689, location_from_axis(495, 488))
		ogre3.turn_towards(game.party[0])
		ogre3.concealed_set(1)
		ogre3.unconceal()
		ogre3.attack(triggerer)
		ogre4 = game.obj_create(14689, location_from_axis(488, 495))
		ogre4.turn_towards(game.party[0])
		ogre4.concealed_set(1)
		ogre4.unconceal()
		ogre4.attack(triggerer)
		owlbear3 = game.obj_create(14693, location_from_axis(488, 465))
		owlbear3.turn_towards(game.party[0])
		owlbear3.concealed_set(1)
		owlbear3.unconceal()
		owlbear3.attack(triggerer)
		owlbear4 = game.obj_create(14693, location_from_axis(495, 472))
		owlbear4.turn_towards(game.party[0])
		owlbear4.concealed_set(1)
		owlbear4.unconceal()
		owlbear4.attack(triggerer)
		hillgiant3 = game.obj_create(14696, location_from_axis(465, 488))
		hillgiant3.turn_towards(game.party[0])
		hillgiant3.concealed_set(1)
		hillgiant3.unconceal()
		hillgiant3.attack(triggerer)
		hillgiant4 = game.obj_create(14696, location_from_axis(472, 495))
		hillgiant4.turn_towards(game.party[0])
		hillgiant4.concealed_set(1)
		hillgiant4.unconceal()
		hillgiant4.attack(triggerer)
	elif (attachee.map == 5072 or attachee.map == 5076):	# swamps
		tyrant1 = game.obj_create(14650, location_from_axis(465, 480))
		tyrant1.turn_towards(game.party[0])
		tyrant1.concealed_set(1)
		tyrant1.unconceal()
		tyrant1.attack(triggerer)
		tyrant2 = game.obj_create(14650, location_from_axis(495, 480))
		tyrant2.turn_towards(game.party[0])
		tyrant2.concealed_set(1)
		tyrant2.unconceal()
		tyrant2.attack(triggerer)
		tyrant3 = game.obj_create(14650, location_from_axis(480, 465))
		tyrant3.turn_towards(game.party[0])
		tyrant3.concealed_set(1)
		tyrant3.unconceal()
		tyrant3.attack(triggerer)
		tyrant4 = game.obj_create(14650, location_from_axis(480, 495))
		tyrant4.turn_towards(game.party[0])
		tyrant4.concealed_set(1)
		tyrant4.unconceal()
		tyrant4.attack(triggerer)
		kingfrog = game.obj_create(14445, location_from_axis(472, 449))
		kingfrog.turn_towards(game.party[0])
		troll1 = game.obj_create(14691, location_from_axis(472, 465))
		troll1.turn_towards(game.party[0])
		troll1.concealed_set(1)
		troll1.unconceal()
		troll1.attack(triggerer)
		troll2 = game.obj_create(14691, location_from_axis(465, 472))
		troll2.turn_towards(game.party[0])
		troll2.concealed_set(1)
		troll2.unconceal()
		troll2.attack(triggerer)
		giantgar1 = game.obj_create(14692, location_from_axis(495, 488))
		giantgar1.turn_towards(game.party[0])
		giantgar1.concealed_set(1)
		giantgar1.unconceal()
		giantgar1.attack(triggerer)
		giantgar2 = game.obj_create(14692, location_from_axis(488, 495))
		giantgar2.turn_towards(game.party[0])
		giantgar2.concealed_set(1)
		giantgar2.unconceal()
		giantgar2.attack(triggerer)
		troll3 = game.obj_create(14691, location_from_axis(488, 465))
		troll3.turn_towards(game.party[0])
		troll3.concealed_set(1)
		troll3.unconceal()
		troll3.attack(triggerer)
		troll4 = game.obj_create(14691, location_from_axis(495, 472))
		troll4.turn_towards(game.party[0])
		troll4.concealed_set(1)
		troll4.unconceal()
		troll4.attack(triggerer)
		ettin3 = game.obj_create(14697, location_from_axis(465, 488))
		ettin3.turn_towards(game.party[0])
		ettin3.concealed_set(1)
		ettin3.unconceal()
		ettin3.attack(triggerer)
		ettin4 = game.obj_create(14697, location_from_axis(472, 495))
		ettin4.turn_towards(game.party[0])
		ettin4.concealed_set(1)
		ettin4.unconceal()
		ettin4.attack(triggerer)
	elif (attachee.map == 5073 or attachee.map == 5077):	# rivers
		tyrant1 = game.obj_create(14649, location_from_axis(465, 480))
		tyrant1.turn_towards(game.party[0])
		tyrant1.concealed_set(1)
		tyrant1.unconceal()
		tyrant1.attack(triggerer)
		tyrant2 = game.obj_create(14649, location_from_axis(495, 480))
		tyrant2.turn_towards(game.party[0])
		tyrant2.concealed_set(1)
		tyrant2.unconceal()
		tyrant2.attack(triggerer)
		tyrant3 = game.obj_create(14649, location_from_axis(480, 465))
		tyrant3.turn_towards(game.party[0])
		tyrant3.concealed_set(1)
		tyrant3.unconceal()
		tyrant3.attack(triggerer)
		tyrant4 = game.obj_create(14649, location_from_axis(480, 495))
		tyrant4.turn_towards(game.party[0])
		tyrant4.concealed_set(1)
		tyrant4.unconceal()
		tyrant4.attack(triggerer)
		vodyanoi = game.obj_create(14261, location_from_axis(476, 518))
		vodyanoi.turn_towards(game.party[0])
		merrow1 = game.obj_create(14690, location_from_axis(472, 465))
		merrow1.turn_towards(game.party[0])
		merrow1.concealed_set(1)
		merrow1.unconceal()
		merrow1.attack(triggerer)
		merrow2 = game.obj_create(14690, location_from_axis(465, 472))
		merrow2.turn_towards(game.party[0])
		merrow2.concealed_set(1)
		merrow2.unconceal()
		merrow2.attack(triggerer)
		merrow3 = game.obj_create(14690, location_from_axis(495, 488))
		merrow3.turn_towards(game.party[0])
		merrow3.concealed_set(1)
		merrow3.unconceal()
		merrow3.attack(triggerer)
		merrow4 = game.obj_create(14690, location_from_axis(488, 495))
		merrow4.turn_towards(game.party[0])
		merrow4.concealed_set(1)
		merrow4.unconceal()
		merrow4.attack(triggerer)
		stonegiant3 = game.obj_create(14695, location_from_axis(488, 465))
		stonegiant3.turn_towards(game.party[0])
		stonegiant3.concealed_set(1)
		stonegiant3.unconceal()
		stonegiant3.attack(triggerer)
		stonegiant4 = game.obj_create(14695, location_from_axis(495, 472))
		stonegiant4.turn_towards(game.party[0])
		stonegiant4.concealed_set(1)
		stonegiant4.unconceal()
		stonegiant4.attack(triggerer)
		crawler3 = game.obj_create(14694, location_from_axis(465, 488))
		crawler3.turn_towards(game.party[0])
		crawler3.concealed_set(1)
		crawler3.unconceal()
		crawler3.attack(triggerer)
		crawler4 = game.obj_create(14694, location_from_axis(472, 495))
		crawler4.turn_towards(game.party[0])
		crawler4.concealed_set(1)
		crawler4.unconceal()
		crawler4.attack(triggerer)
	game.global_vars[945] = 28
	return


def spawn_attackers_for_narc( attachee, triggerer ):
	if (attachee.map == 5071 or attachee.map == 5075):	# forests
		tyrant1 = game.obj_create(14648, location_from_axis(495, 480))
		tyrant1.turn_towards(game.party[0])
		tyrant1.concealed_set(1)
		tyrant1.unconceal()
		tyrant1.attack(triggerer)
		tyrant2 = game.obj_create(14648, location_from_axis(465, 480))
		tyrant2.turn_towards(game.party[0])
		tyrant2.concealed_set(1)
		tyrant2.unconceal()
		tyrant2.attack(triggerer)
		tyrant3 = game.obj_create(14648, location_from_axis(480, 465))
		tyrant3.turn_towards(game.party[0])
		tyrant3.concealed_set(1)
		tyrant3.unconceal()
		tyrant3.attack(triggerer)
		tyrant4 = game.obj_create(14648, location_from_axis(480, 495))
		tyrant4.turn_towards(game.party[0])
		tyrant4.concealed_set(1)
		tyrant4.unconceal()
		tyrant4.attack(triggerer)
		umberhulk = game.obj_create(14260, location_from_axis(520, 484))
		umberhulk.turn_towards(game.party[0])
		ogre1 = game.obj_create(14689, location_from_axis(472, 465))
		ogre1.turn_towards(game.party[0])
		ogre1.concealed_set(1)
		ogre1.unconceal()
		ogre1.attack(triggerer)
		ogre2 = game.obj_create(14689, location_from_axis(465, 472))
		ogre2.turn_towards(game.party[0])
		ogre2.concealed_set(1)
		ogre2.unconceal()
		ogre2.attack(triggerer)
		owlbear1 = game.obj_create(14693, location_from_axis(495, 488))
		owlbear1.turn_towards(game.party[0])
		owlbear1.concealed_set(1)
		owlbear1.unconceal()
		owlbear1.attack(triggerer)
		owlbear2 = game.obj_create(14693, location_from_axis(488, 495))
		owlbear2.turn_towards(game.party[0])
		owlbear2.concealed_set(1)
		owlbear2.unconceal()
		owlbear2.attack(triggerer)
		owlbear3 = game.obj_create(14693, location_from_axis(488, 465))
		owlbear3.turn_towards(game.party[0])
		owlbear3.concealed_set(1)
		owlbear3.unconceal()
		owlbear3.attack(triggerer)
		owlbear4 = game.obj_create(14693, location_from_axis(495, 472))
		owlbear4.turn_towards(game.party[0])
		owlbear4.concealed_set(1)
		owlbear4.unconceal()
		owlbear4.attack(triggerer)
		hillgiant3 = game.obj_create(14696, location_from_axis(465, 488))
		hillgiant3.turn_towards(game.party[0])
		hillgiant3.concealed_set(1)
		hillgiant3.unconceal()
		hillgiant3.attack(triggerer)
		hillgiant4 = game.obj_create(14696, location_from_axis(472, 495))
		hillgiant4.turn_towards(game.party[0])
		hillgiant4.concealed_set(1)
		hillgiant4.unconceal()
		hillgiant4.attack(triggerer)
	elif (attachee.map == 5072 or attachee.map == 5076):	# swamps
		tyrant1 = game.obj_create(14650, location_from_axis(465, 480))
		tyrant1.turn_towards(game.party[0])
		tyrant1.concealed_set(1)
		tyrant1.unconceal()
		tyrant1.attack(triggerer)
		tyrant2 = game.obj_create(14650, location_from_axis(495, 480))
		tyrant2.turn_towards(game.party[0])
		tyrant2.concealed_set(1)
		tyrant2.unconceal()
		tyrant2.attack(triggerer)
		tyrant3 = game.obj_create(14650, location_from_axis(480, 465))
		tyrant3.turn_towards(game.party[0])
		tyrant3.concealed_set(1)
		tyrant3.unconceal()
		tyrant3.attack(triggerer)
		tyrant4 = game.obj_create(14650, location_from_axis(480, 495))
		tyrant4.turn_towards(game.party[0])
		tyrant4.concealed_set(1)
		tyrant4.unconceal()
		tyrant4.attack(triggerer)
		kingfrog = game.obj_create(14445, location_from_axis(472, 449))
		kingfrog.turn_towards(game.party[0])
		troll1 = game.obj_create(14691, location_from_axis(472, 465))
		troll1.turn_towards(game.party[0])
		troll1.concealed_set(1)
		troll1.unconceal()
		troll1.attack(triggerer)
		troll2 = game.obj_create(14691, location_from_axis(465, 472))
		troll2.turn_towards(game.party[0])
		troll2.concealed_set(1)
		troll2.unconceal()
		troll2.attack(triggerer)
		giantgar1 = game.obj_create(14692, location_from_axis(495, 488))
		giantgar1.turn_towards(game.party[0])
		giantgar1.concealed_set(1)
		giantgar1.unconceal()
		giantgar1.attack(triggerer)
		giantgar2 = game.obj_create(14692, location_from_axis(488, 495))
		giantgar2.turn_towards(game.party[0])
		giantgar2.concealed_set(1)
		giantgar2.unconceal()
		giantgar2.attack(triggerer)
		ettin3 = game.obj_create(14697, location_from_axis(488, 465))
		ettin3.turn_towards(game.party[0])
		ettin3.concealed_set(1)
		ettin3.unconceal()
		ettin3.attack(triggerer)
		ettin4 = game.obj_create(14697, location_from_axis(495, 472))
		ettin4.turn_towards(game.party[0])
		ettin4.concealed_set(1)
		ettin4.unconceal()
		ettin4.attack(triggerer)
		giantgar3 = game.obj_create(14692, location_from_axis(465, 488))
		giantgar3.turn_towards(game.party[0])
		giantgar3.concealed_set(1)
		giantgar3.unconceal()
		giantgar3.attack(triggerer)
		giantgar4 = game.obj_create(14692, location_from_axis(472, 495))
		giantgar4.turn_towards(game.party[0])
		giantgar4.concealed_set(1)
		giantgar4.unconceal()
		giantgar4.attack(triggerer)
	elif (attachee.map == 5073 or attachee.map == 5077):	# rivers
		tyrant1 = game.obj_create(14649, location_from_axis(465, 480))
		tyrant1.turn_towards(game.party[0])
		tyrant1.concealed_set(1)
		tyrant1.unconceal()
		tyrant1.attack(triggerer)
		tyrant2 = game.obj_create(14649, location_from_axis(495, 480))
		tyrant2.turn_towards(game.party[0])
		tyrant2.concealed_set(1)
		tyrant2.unconceal()
		tyrant2.attack(triggerer)
		tyrant3 = game.obj_create(14649, location_from_axis(480, 465))
		tyrant3.turn_towards(game.party[0])
		tyrant3.concealed_set(1)
		tyrant3.unconceal()
		tyrant3.attack(triggerer)
		tyrant4 = game.obj_create(14649, location_from_axis(480, 495))
		tyrant4.turn_towards(game.party[0])
		tyrant4.concealed_set(1)
		tyrant4.unconceal()
		tyrant4.attack(triggerer)
		vodyanoi = game.obj_create(14261, location_from_axis(476, 518))
		vodyanoi.turn_towards(game.party[0])
		merrow1 = game.obj_create(14690, location_from_axis(472, 465))
		merrow1.turn_towards(game.party[0])
		merrow1.concealed_set(1)
		merrow1.unconceal()
		merrow1.attack(triggerer)
		merrow2 = game.obj_create(14690, location_from_axis(465, 472))
		merrow2.turn_towards(game.party[0])
		merrow2.concealed_set(1)
		merrow2.unconceal()
		merrow2.attack(triggerer)
		stonegiant1 = game.obj_create(14695, location_from_axis(495, 488))
		stonegiant1.turn_towards(game.party[0])
		stonegiant1.concealed_set(1)
		stonegiant1.unconceal()
		stonegiant1.attack(triggerer)
		stonegiant2 = game.obj_create(14695, location_from_axis(488, 495))
		stonegiant2.turn_towards(game.party[0])
		stonegiant2.concealed_set(1)
		stonegiant2.unconceal()
		stonegiant2.attack(triggerer)
		crawler1 = game.obj_create(14694, location_from_axis(488, 465))
		crawler1.turn_towards(game.party[0])
		crawler1.concealed_set(1)
		crawler1.unconceal()
		crawler1.attack(triggerer)
		crawler2 = game.obj_create(14694, location_from_axis(495, 472))
		crawler2.turn_towards(game.party[0])
		crawler2.concealed_set(1)
		crawler2.unconceal()
		crawler2.attack(triggerer)
		crawler3 = game.obj_create(14694, location_from_axis(465, 488))
		crawler3.turn_towards(game.party[0])
		crawler3.concealed_set(1)
		crawler3.unconceal()
		crawler3.attack(triggerer)
		crawler4 = game.obj_create(14694, location_from_axis(472, 495))
		crawler4.turn_towards(game.party[0])
		crawler4.concealed_set(1)
		crawler4.unconceal()
		crawler4.attack(triggerer)
	game.global_vars[945] = 29
	return


def spawn_attackers_for_whistleblower( attachee, triggerer ):
	if (attachee.map == 5071 or attachee.map == 5075):	# forests
		tyrant1 = game.obj_create(14648, location_from_axis(495, 480))
		tyrant1.turn_towards(game.party[0])
		tyrant1.concealed_set(1)
		tyrant1.unconceal()
		tyrant1.attack(triggerer)
		tyrant2 = game.obj_create(14648, location_from_axis(465, 480))
		tyrant2.turn_towards(game.party[0])
		tyrant2.concealed_set(1)
		tyrant2.unconceal()
		tyrant2.attack(triggerer)
		tyrant3 = game.obj_create(14648, location_from_axis(480, 465))
		tyrant3.turn_towards(game.party[0])
		tyrant3.concealed_set(1)
		tyrant3.unconceal()
		tyrant3.attack(triggerer)
		tyrant4 = game.obj_create(14648, location_from_axis(480, 495))
		tyrant4.turn_towards(game.party[0])
		tyrant4.concealed_set(1)
		tyrant4.unconceal()
		tyrant4.attack(triggerer)
		umberhulk = game.obj_create(14260, location_from_axis(520, 484))
		umberhulk.turn_towards(game.party[0])
		ogre1 = game.obj_create(14689, location_from_axis(472, 465))
		ogre1.turn_towards(game.party[0])
		ogre1.concealed_set(1)
		ogre1.unconceal()
		ogre1.attack(triggerer)
		ogre2 = game.obj_create(14689, location_from_axis(465, 472))
		ogre2.turn_towards(game.party[0])
		ogre2.concealed_set(1)
		ogre2.unconceal()
		ogre2.attack(triggerer)
		owlbear1 = game.obj_create(14693, location_from_axis(495, 488))
		owlbear1.turn_towards(game.party[0])
		owlbear1.concealed_set(1)
		owlbear1.unconceal()
		owlbear1.attack(triggerer)
		owlbear2 = game.obj_create(14693, location_from_axis(488, 495))
		owlbear2.turn_towards(game.party[0])
		owlbear2.concealed_set(1)
		owlbear2.unconceal()
		owlbear2.attack(triggerer)
		hillgiant1 = game.obj_create(14696, location_from_axis(488, 465))
		hillgiant1.turn_towards(game.party[0])
		hillgiant1.concealed_set(1)
		hillgiant1.unconceal()
		hillgiant1.attack(triggerer)
		hillgiant2 = game.obj_create(14696, location_from_axis(495, 472))
		hillgiant2.turn_towards(game.party[0])
		hillgiant2.concealed_set(1)
		hillgiant2.unconceal()
		hillgiant2.attack(triggerer)
		hillgiant3 = game.obj_create(14696, location_from_axis(465, 488))
		hillgiant3.turn_towards(game.party[0])
		hillgiant3.concealed_set(1)
		hillgiant3.unconceal()
		hillgiant3.attack(triggerer)
		hillgiant4 = game.obj_create(14696, location_from_axis(472, 495))
		hillgiant4.turn_towards(game.party[0])
		hillgiant4.concealed_set(1)
		hillgiant4.unconceal()
		hillgiant4.attack(triggerer)
	elif (attachee.map == 5072 or attachee.map == 5076):	# swamps
		tyrant1 = game.obj_create(14650, location_from_axis(465, 480))
		tyrant1.turn_towards(game.party[0])
		tyrant1.concealed_set(1)
		tyrant1.unconceal()
		tyrant1.attack(triggerer)
		tyrant2 = game.obj_create(14650, location_from_axis(495, 480))
		tyrant2.turn_towards(game.party[0])
		tyrant2.concealed_set(1)
		tyrant2.unconceal()
		tyrant2.attack(triggerer)
		tyrant3 = game.obj_create(14650, location_from_axis(480, 465))
		tyrant3.turn_towards(game.party[0])
		tyrant3.concealed_set(1)
		tyrant3.unconceal()
		tyrant3.attack(triggerer)
		tyrant4 = game.obj_create(14650, location_from_axis(480, 495))
		tyrant4.turn_towards(game.party[0])
		tyrant4.concealed_set(1)
		tyrant4.unconceal()
		tyrant4.attack(triggerer)
		kingfrog = game.obj_create(14445, location_from_axis(472, 449))
		kingfrog.turn_towards(game.party[0])
		troll1 = game.obj_create(14691, location_from_axis(472, 465))
		troll1.turn_towards(game.party[0])
		troll1.concealed_set(1)
		troll1.unconceal()
		troll1.attack(triggerer)
		troll2 = game.obj_create(14691, location_from_axis(465, 472))
		troll2.turn_towards(game.party[0])
		troll2.concealed_set(1)
		troll2.unconceal()
		troll2.attack(triggerer)
		giantgar1 = game.obj_create(14692, location_from_axis(495, 488))
		giantgar1.turn_towards(game.party[0])
		giantgar1.concealed_set(1)
		giantgar1.unconceal()
		giantgar1.attack(triggerer)
		giantgar2 = game.obj_create(14692, location_from_axis(488, 495))
		giantgar2.turn_towards(game.party[0])
		giantgar2.concealed_set(1)
		giantgar2.unconceal()
		giantgar2.attack(triggerer)
		ettin1 = game.obj_create(14697, location_from_axis(488, 465))
		ettin1.turn_towards(game.party[0])
		ettin1.concealed_set(1)
		ettin1.unconceal()
		ettin1.attack(triggerer)
		ettin2 = game.obj_create(14697, location_from_axis(495, 472))
		ettin2.turn_towards(game.party[0])
		ettin2.concealed_set(1)
		ettin2.unconceal()
		ettin2.attack(triggerer)
		ettin3 = game.obj_create(14697, location_from_axis(465, 488))
		ettin3.turn_towards(game.party[0])
		ettin3.concealed_set(1)
		ettin3.unconceal()
		ettin3.attack(triggerer)
		ettin4 = game.obj_create(14697, location_from_axis(472, 495))
		ettin4.turn_towards(game.party[0])
		ettin4.concealed_set(1)
		ettin4.unconceal()
		ettin4.attack(triggerer)
	elif (attachee.map == 5073 or attachee.map == 5077):	# rivers
		tyrant1 = game.obj_create(14649, location_from_axis(465, 480))
		tyrant1.turn_towards(game.party[0])
		tyrant1.concealed_set(1)
		tyrant1.unconceal()
		tyrant1.attack(triggerer)
		tyrant2 = game.obj_create(14649, location_from_axis(495, 480))
		tyrant2.turn_towards(game.party[0])
		tyrant2.concealed_set(1)
		tyrant2.unconceal()
		tyrant2.attack(triggerer)
		tyrant3 = game.obj_create(14649, location_from_axis(480, 465))
		tyrant3.turn_towards(game.party[0])
		tyrant3.concealed_set(1)
		tyrant3.unconceal()
		tyrant3.attack(triggerer)
		tyrant4 = game.obj_create(14649, location_from_axis(480, 495))
		tyrant4.turn_towards(game.party[0])
		tyrant4.concealed_set(1)
		tyrant4.unconceal()
		tyrant4.attack(triggerer)
		vodyanoi = game.obj_create(14261, location_from_axis(476, 518))
		vodyanoi.turn_towards(game.party[0])
		merrow1 = game.obj_create(14690, location_from_axis(472, 465))
		merrow1.turn_towards(game.party[0])
		merrow1.concealed_set(1)
		merrow1.unconceal()
		merrow1.attack(triggerer)
		merrow2 = game.obj_create(14690, location_from_axis(465, 472))
		merrow2.turn_towards(game.party[0])
		merrow2.concealed_set(1)
		merrow2.unconceal()
		merrow2.attack(triggerer)
		stonegiant1 = game.obj_create(14695, location_from_axis(495, 488))
		stonegiant1.turn_towards(game.party[0])
		stonegiant1.concealed_set(1)
		stonegiant1.unconceal()
		stonegiant1.attack(triggerer)
		stonegiant2 = game.obj_create(14695, location_from_axis(488, 495))
		stonegiant2.turn_towards(game.party[0])
		stonegiant2.concealed_set(1)
		stonegiant2.unconceal()
		stonegiant2.attack(triggerer)
		stonegiant3 = game.obj_create(14695, location_from_axis(488, 465))
		stonegiant3.turn_towards(game.party[0])
		stonegiant3.concealed_set(1)
		stonegiant3.unconceal()
		stonegiant3.attack(triggerer)
		stonegiant4 = game.obj_create(14695, location_from_axis(495, 472))
		stonegiant4.turn_towards(game.party[0])
		stonegiant4.concealed_set(1)
		stonegiant4.unconceal()
		stonegiant4.attack(triggerer)
		crawler3 = game.obj_create(14694, location_from_axis(465, 488))
		crawler3.turn_towards(game.party[0])
		crawler3.concealed_set(1)
		crawler3.unconceal()
		crawler3.attack(triggerer)
		crawler4 = game.obj_create(14694, location_from_axis(472, 495))
		crawler4.turn_towards(game.party[0])
		crawler4.concealed_set(1)
		crawler4.unconceal()
		crawler4.attack(triggerer)
	game.global_vars[945] = 30
	return