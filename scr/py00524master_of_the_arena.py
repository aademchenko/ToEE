from utilities import *
from toee import *
from combat_standard_routines import *


def san_dialog(attachee, triggerer):
	if game.global_vars[994] == 0:
		attachee.turn_towards(triggerer)
		triggerer.begin_dialog(attachee, 1)
		return SKIP_DEFAULT
	if game.global_vars[994] == 1:
		if game.global_flags[944] == 1:
			triggerer.begin_dialog(attachee, 100)
			return SKIP_DEFAULT
	if game.global_vars[994] == 2:
		attachee.turn_towards(triggerer)
		if game.global_vars[987] == 3:
			game.global_vars[987] = 0
			triggerer.begin_dialog(attachee, 90)
			return SKIP_DEFAULT
		else:
			triggerer.begin_dialog(attachee, 110)
			return SKIP_DEFAULT
	if game.global_vars[994] == 3:
		attachee.turn_towards(triggerer)
		if game.global_vars[987] == 2:
			game.global_vars[987] = 0
			triggerer.begin_dialog(attachee, 130)
			return SKIP_DEFAULT
		else:
			triggerer.begin_dialog(attachee, 140)
			return SKIP_DEFAULT
	if game.global_vars[994] == 4:
		attachee.turn_towards(triggerer)
		triggerer.begin_dialog(attachee, 160)
		return SKIP_DEFAULT
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	game.particles("ef-MinoCloud", attachee)
	attachee.object_flag_set(OF_OFF)
	game.sound( 4043, 1 )
	return RUN_DEFAULT


def san_heartbeat(attachee, triggerer):
	if (game.global_flags[945] == 1):
		game.particles("ef-MinoCloud", attachee)
		attachee.object_flag_unset(OF_OFF)
		game.sound( 4043, 1 )
		attachee.rotation = 1.5
		game.global_flags[945] = 0
		return RUN_DEFAULT
	elif (not game.combat_is_active()):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (is_better_to_talk(attachee,obj)):
				if game.global_vars[994] == 0:
					obj.begin_dialog(attachee, 1)
					return RUN_DEFAULT
				if game.global_vars[994] == 1:
					if game.global_flags[944] == 1:
						obj.begin_dialog(attachee, 100)
						return RUN_DEFAULT
				if game.global_vars[994] == 2:
					attachee.turn_towards(obj)					
					if game.global_vars[987] == 3:
						game.global_vars[987] = 0
						obj.begin_dialog(attachee, 90)
						return RUN_DEFAULT
					else:
						obj.begin_dialog(attachee, 110)
						return RUN_DEFAULT
				if game.global_vars[994] == 3:
					attachee.turn_towards(obj)					
					if game.global_vars[987] == 2:
						game.global_vars[987] = 0
						obj.begin_dialog(attachee, 130)
						return RUN_DEFAULT
					else:
						obj.begin_dialog(attachee, 140)
						return RUN_DEFAULT
				if game.global_vars[994] == 4:
					obj.begin_dialog(attachee, 160)
					return RUN_DEFAULT				
				return RUN_DEFAULT
	return RUN_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 25):
		return 1
	return 0


def disappear(attachee, triggerer):
	game.particles("ef-MinoCloud", attachee)
	attachee.object_flag_set(OF_OFF)
	game.sound( 4043, 1 )
	return RUN_DEFAULT


def spawn_owlbears(attachee, triggerer):
	game.global_vars[955] = 1
	return RUN_DEFAULT


def spawn_giants(attachee, triggerer):
	game.global_vars[954] = 1
	return RUN_DEFAULT


def spawn_undead(attachee, triggerer):
	sk1 = game.obj_create(14107, location_from_axis(491, 461))
	sk1.rotation = 3.5
	sk1.concealed_set(1)
	sk1.unconceal()
	sk2 = game.obj_create(14107, location_from_axis(491, 464))
	sk2.rotation = 3.5
	sk2.concealed_set(1)
	sk2.unconceal()
	sk3 = game.obj_create(14107, location_from_axis(491, 467))
	sk3.rotation = 3.5
	sk3.concealed_set(1)
	sk3.unconceal()
	sk4 = game.obj_create(14107, location_from_axis(491, 470))
	sk4.rotation = 3.5
	sk4.concealed_set(1)
	sk4.unconceal()
	sk5 = game.obj_create(14107, location_from_axis(512, 482))
	sk5.rotation = 5.5
	sk5.concealed_set(1)
	sk5.unconceal()
	sk6 = game.obj_create(14107, location_from_axis(509, 482))
	sk6.rotation = 5.5
	sk6.concealed_set(1)
	sk6.unconceal()
	sk7 = game.obj_create(14107, location_from_axis(506, 482))
	sk7.rotation = 5.5
	sk7.concealed_set(1)
	sk7.unconceal()
	sk8 = game.obj_create(14107, location_from_axis(503, 482))
	sk8.rotation = 5.5
	sk8.concealed_set(1)
	sk8.unconceal()
	zo1 = game.obj_create(14092, location_from_axis(491, 455))
	zo1.rotation = 3.5
	zo1.concealed_set(1)
	zo1.unconceal()
	go1 = game.obj_create(14095, location_from_axis(488, 455))
	go1.rotation = 3.5
	go1.concealed_set(1)
	go1.unconceal()
	zo2 = game.obj_create(14092, location_from_axis(491, 458))
	zo2.rotation = 3.5
	zo2.concealed_set(1)
	zo2.unconceal()
	go2 = game.obj_create(14095, location_from_axis(488, 458))
	go2.rotation = 3.5
	go2.concealed_set(1)
	go2.unconceal()
	zo3 = game.obj_create(14092, location_from_axis(518, 482))
	zo3.rotation = 5.5
	zo3.concealed_set(1)
	zo3.unconceal()
	zo4 = game.obj_create(14092, location_from_axis(515, 482))
	zo4.rotation = 5.5
	zo4.concealed_set(1)
	zo4.unconceal()
	la1 = game.obj_create(14130, location_from_axis(518, 485))
	la1.rotation = 5.5
	la1.concealed_set(1)
	la1.unconceal()
	la2 = game.obj_create(14130, location_from_axis(515, 485))
	la2.rotation = 5.5
	la2.concealed_set(1)
	la2.unconceal()
	zo5 = game.obj_create(14092, location_from_axis(491, 473))
	zo5.rotation = 3.5
	zo5.concealed_set(1)
	zo5.unconceal()
	go3 = game.obj_create(14095, location_from_axis(488, 473))
	go3.rotation = 3.5
	go3.concealed_set(1)
	go3.unconceal()
	zo6 = game.obj_create(14092, location_from_axis(491, 476))
	zo6.rotation = 3.5
	zo6.concealed_set(1)
	zo6.unconceal()
	go4 = game.obj_create(14095, location_from_axis(488, 476))
	go4.rotation = 3.5
	go4.concealed_set(1)
	go4.unconceal()
	zo7 = game.obj_create(14092, location_from_axis(500, 482))
	zo7.rotation = 5.5
	zo7.concealed_set(1)
	zo7.unconceal()
	zo8 = game.obj_create(14092, location_from_axis(497, 482))
	zo8.rotation = 5.5
	zo8.concealed_set(1)
	zo8.unconceal()
	la3 = game.obj_create(14130, location_from_axis(500, 485))
	la3.rotation = 5.5
	la3.concealed_set(1)
	la3.unconceal()
	la4 = game.obj_create(14130, location_from_axis(497, 485))
	la4.rotation = 5.5
	la4.concealed_set(1)
	la4.unconceal()
	sg1 = game.obj_create(14602, location_from_axis(488, 461))
	sg1.rotation = 3.5
	sg1.concealed_set(1)
	sg1.unconceal()
	sg2 = game.obj_create(14602, location_from_axis(488, 470))
	sg2.rotation = 3.5
	sg2.concealed_set(1)
	sg2.unconceal()
	sg3 = game.obj_create(14602, location_from_axis(512, 485))
	sg3.rotation = 5.5
	sg3.concealed_set(1)
	sg3.unconceal()
	sg4 = game.obj_create(14602, location_from_axis(503, 485))
	sg4.rotation = 5.5
	sg4.concealed_set(1)
	sg4.unconceal()
	uw1 = game.obj_create(14599, location_from_axis(488, 465))
	uw1.rotation = 3.5
	uw1.concealed_set(1)
	uw1.unconceal()
	uw2 = game.obj_create(14598, location_from_axis(507, 485))
	uw2.rotation = 5.5
	uw2.concealed_set(1)
	uw2.unconceal()
	game.sound( 4045, 1 )
	game.global_vars[987] = 0
	return RUN_DEFAULT


def find_npc_near( obj, name ):
	for npc in game.obj_list_vicinity( obj.location, OLC_NPC ):
		if (npc.name == name):
			return npc
	return OBJ_HANDLE_NULL