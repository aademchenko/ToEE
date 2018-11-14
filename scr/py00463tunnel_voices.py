from toee import *
from utilities import *
from combat_standard_routines import *


def san_heartbeat( attachee, triggerer ):
	if (game.quests[109].state == qs_mentioned or game.quests[109].state == qs_accepted):
		if (game.global_vars[536] >= 1):
			if (game.global_vars[550] == 0):
				if (attachee.name == 8853):
					if (game.global_vars[547] != 1):
						if (not game.combat_is_active()):
							for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
								if (in_proximity(attachee, obj)):
									drop = game.random_range(1,12)
									game.global_vars[547] = 1
									if (drop == 1):
										if (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
										elif (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
										elif (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
										elif (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
									elif (drop == 2):
										if (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
										elif (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
										elif (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
										elif (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
									elif (drop == 3):
										if (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
										elif (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
										elif (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
										elif (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
									elif (drop == 4):
										if (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
										elif (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
										elif (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
										elif (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
									elif (drop >= 5):
										return RUN_DEFAULT
				if (attachee.name == 8854):
					if (game.global_vars[547] != 2):
						if (not game.combat_is_active()):
							for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
								if (in_proximity(attachee, obj)):
									drop = game.random_range(1,12)
									game.global_vars[547] = 2
									if (drop == 1):
										if (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
										elif (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
										elif (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
										elif (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
									elif (drop == 2):
										if (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
										elif (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
										elif (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
										elif (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
									elif (drop == 3):
										if (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
										elif (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
										elif (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
										elif (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
									elif (drop == 4):
										if (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
										elif (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
										elif (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
										elif (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
									elif (drop >= 5):
										return RUN_DEFAULT
				if (attachee.name == 8855):
					if (game.global_vars[547] != 3):
						if (not game.combat_is_active()):
							for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
								if (in_proximity(attachee, obj)):
									drop = game.random_range(1,12)
									game.global_vars[547] = 3
									if (drop == 1):
										if (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
										elif (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
										elif (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
										elif (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
									elif (drop == 2):
										if (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
										elif (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
										elif (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
										elif (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
									elif (drop == 3):
										if (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
										elif (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
										elif (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
										elif (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
									elif (drop == 4):
										if (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
										elif (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
										elif (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
										elif (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
									elif (drop >= 5):
										return RUN_DEFAULT
				if (attachee.name == 8856):
					if (game.global_vars[547] != 4):
						if (not game.combat_is_active()):
							for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
								if (in_proximity(attachee, obj)):
									drop = game.random_range(1,12)
									game.global_vars[547] = 4
									if (drop == 1):
										if (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
										elif (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
										elif (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
										elif (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
									elif (drop == 2):
										if (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
										elif (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
										elif (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
										elif (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
									elif (drop == 3):
										if (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
										elif (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
										elif (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
										elif (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
									elif (drop == 4):
										if (game.global_vars[532] == 0):
											game.sound ( 4152, 1 )
											game.global_vars[532] = 1
										elif (game.global_vars[529] == 0):
											game.sound ( 4149, 1 )
											game.global_vars[529] = 1
										elif (game.global_vars[530] == 0):
											game.sound ( 4150, 1 )
											game.global_vars[530] = 1
										elif (game.global_vars[531] == 0):
											game.sound ( 4151, 1 )
											game.global_vars[531] = 1
									elif (drop >= 5):
										return RUN_DEFAULT
	return RUN_DEFAULT


def in_proximity( sfx, listener ):
	if (sfx.distance_to(listener) <= 80):
		return 1
	return 0