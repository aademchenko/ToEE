from toee import *
from utilities import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (attachee.name == 8961):
		hill_backup_ravine_1 = game.obj_create( 14988, location_from_axis (411L, 485L) )
		hill_backup_ravine_1.rotation = 4.71238898038
		hill_backup_ravine_1.concealed_set(1)
		hill_backup_ravine_1.unconceal()
		game.particles( "Mon-EarthElem-Unconceal", hill_backup_ravine_1 )
		for obj in game.obj_list_vicinity(hill_backup_ravine_1.location,OLC_PC):
			hill_backup_ravine_1.attack(obj)
		hill_backup_ravine_2 = game.obj_create( 14988, location_from_axis (418L, 492L) )
		hill_backup_ravine_2.rotation = 4.71238898038
		hill_backup_ravine_2.concealed_set(1)
		hill_backup_ravine_2.unconceal()
		game.particles( "Mon-EarthElem-Unconceal", hill_backup_ravine_2 )
		game.sound( 4176, 1 )
		game.update_combat_ui()
		for obj in game.obj_list_vicinity(hill_backup_ravine_2.location,OLC_PC):
			hill_backup_ravine_2.attack(obj)
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	webbed = break_free( attachee, 3)
	if (attachee != OBJ_HANDLE_NULL and critter_is_unconscious(attachee) != 1 and not attachee.d20_query(Q_Prone) and attachee.leader_get() == OBJ_HANDLE_NULL):
		if (attachee.name == 8910 or attachee.name == 8921):
			if (obj_percent_hp(attachee) <= 75):
				if (attachee.name == 8910):
				## hb gatekeeper east
					if (game.global_vars[787] <= 17):
						attachee.obj_set_int(obj_f_critter_strategy, 540)
						game.global_vars[787] = game.global_vars[787] + 1
					elif (game.global_vars[788] <= 1):
						attachee.obj_set_int(obj_f_critter_strategy, 537)
						game.global_vars[788] = game.global_vars[788] + 1
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 534)
				elif (attachee.name == 8921):
				## hb gatekeeper west
					if (game.global_vars[790] <= 17):
						attachee.obj_set_int(obj_f_critter_strategy, 540)
						game.global_vars[790] = game.global_vars[790] + 1
					elif (game.global_vars[791] <= 1):
						attachee.obj_set_int(obj_f_critter_strategy, 537)
						game.global_vars[791] = game.global_vars[791] + 1
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 534)
			elif (obj_percent_hp(attachee) >= 76):
				if (attachee.name == 8910):
				## hb gatekeeper east
					orcserg01 = find_npc_near( attachee, 8894 )
					orcdomi01 = find_npc_near( attachee, 8895 )
					orcbowm01 = find_npc_near( attachee, 8899 )
					orcbowm02 = find_npc_near( attachee, 8900 )
					orcarch01 = find_npc_near( attachee, 8901 )
					orcarch02 = find_npc_near( attachee, 8902 )
					orcsnip01 = find_npc_near( attachee, 8903 )
					hilgian01 = find_npc_near( attachee, 8904 )
					hilgian02 = find_npc_near( attachee, 8905 )
					hilgian03 = find_npc_near( attachee, 8906 )
					hilgian04 = find_npc_near( attachee, 8907 )
					hilgian05 = find_npc_near( attachee, 8908 )
					orcsham01 = find_npc_near( attachee, 8909 )
					if (obj_percent_hp(orcserg01) <= 75 or obj_percent_hp(orcdomi01) <= 75 or obj_percent_hp(orcbowm01) <= 75 or obj_percent_hp(orcbowm02) <= 75 or obj_percent_hp(orcarch01) <= 75 or obj_percent_hp(orcarch02) <= 75 or obj_percent_hp(orcsnip01) <= 75 or obj_percent_hp(hilgian01) <= 75 or obj_percent_hp(hilgian02) <= 75 or obj_percent_hp(hilgian03) <= 75 or obj_percent_hp(hilgian04) <= 75 or obj_percent_hp(hilgian05) <= 75 or obj_percent_hp(orcsham01) <= 75):
						if (game.global_vars[787] <= 17):
							attachee.obj_set_int(obj_f_critter_strategy, 474)
							game.global_vars[787] = game.global_vars[787] + 1
						elif (game.global_vars[788] <= 1):
							attachee.obj_set_int(obj_f_critter_strategy, 537)
							game.global_vars[788] = game.global_vars[788] + 1
						else:
							attachee.obj_set_int(obj_f_critter_strategy, 534)
					else:
						if (game.global_vars[788] <= 1):
							attachee.obj_set_int(obj_f_critter_strategy, 537)
							game.global_vars[788] = game.global_vars[788] + 1
						else:
							attachee.obj_set_int(obj_f_critter_strategy, 543)
				elif (attachee.name == 8921):
				## hb gatekeeper west
					ogrexxx01 = find_npc_near( attachee, 8911 )
					ettinxx01 = find_npc_near( attachee, 8912 )
					ettinxx02 = find_npc_near( attachee, 8913 )
					ettinxx03 = find_npc_near( attachee, 8914 )
					ettinxx04 = find_npc_near( attachee, 8915 )
					ettinxx05 = find_npc_near( attachee, 8916 )
					orcbowm01 = find_npc_near( attachee, 8917 )
					orcbowm02 = find_npc_near( attachee, 8918 )
					orcarch01 = find_npc_near( attachee, 8919 )
					orcsham01 = find_npc_near( attachee, 8920 )
					if (obj_percent_hp(ogrexxx01) <= 75 or obj_percent_hp(ettinxx01) <= 75 or obj_percent_hp(ettinxx02) <= 75 or obj_percent_hp(ettinxx03) <= 75 or obj_percent_hp(ettinxx04) <= 75 or obj_percent_hp(ettinxx05) <= 75 or obj_percent_hp(orcbowm01) <= 75 or obj_percent_hp(orcbowm02) <= 75 or obj_percent_hp(orcarch01) <= 75 or obj_percent_hp(orcsham01) <= 75):
						if (game.global_vars[790] <= 17):
							attachee.obj_set_int(obj_f_critter_strategy, 474)
							game.global_vars[790] = game.global_vars[790] + 1
						elif (game.global_vars[791] <= 1):
							attachee.obj_set_int(obj_f_critter_strategy, 537)
							game.global_vars[791] = game.global_vars[791] + 1
						else:
							attachee.obj_set_int(obj_f_critter_strategy, 534)
					else:
						if (game.global_vars[791] <= 1):
							attachee.obj_set_int(obj_f_critter_strategy, 537)
							game.global_vars[791] = game.global_vars[791] + 1
						else:
							attachee.obj_set_int(obj_f_critter_strategy, 543)
		elif (attachee.name == 8961 or attachee.name == 8965):
			if (obj_percent_hp(attachee) <= 75):
				if (attachee.name == 8961):
				## hb ravine north
					if (game.global_vars[794] <= 17):
						attachee.obj_set_int(obj_f_critter_strategy, 540)
						game.global_vars[794] = game.global_vars[794] + 1
					elif (game.global_vars[795] <= 1):
						attachee.obj_set_int(obj_f_critter_strategy, 537)
						game.global_vars[795] = game.global_vars[795] + 1
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 534)
				elif (attachee.name == 8965):
				## hb ravine south
					if (game.global_vars[796] <= 17):
						attachee.obj_set_int(obj_f_critter_strategy, 540)
						game.global_vars[796] = game.global_vars[796] + 1
					elif (game.global_vars[797] <= 1):
						attachee.obj_set_int(obj_f_critter_strategy, 537)
						game.global_vars[797] = game.global_vars[797] + 1
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 534)
			elif (obj_percent_hp(attachee) >= 76):
				if (attachee.name == 8961):
				## hb ravine north
					gnollxx01 = find_npc_near( attachee, 8931 )
					gnollxx02 = find_npc_near( attachee, 8932 )
					gnollxx03 = find_npc_near( attachee, 8933 )
					gnollxx04 = find_npc_near( attachee, 8934 )
					gnollxx05 = find_npc_near( attachee, 8935 )
					bugbear01 = find_npc_near( attachee, 8936 )
					bugbear02 = find_npc_near( attachee, 8937 )
					bugbear03 = find_npc_near( attachee, 8938 )
					bugbear04 = find_npc_near( attachee, 8939 )
					ogrexxx01 = find_npc_near( attachee, 8969 )
					ogrexxx02 = find_npc_near( attachee, 8970 )
					ogrexxx03 = find_npc_near( attachee, 8971 )
					orcsham01 = find_npc_near( attachee, 8960 )
					orcbowm01 = find_npc_near( attachee, 8978 )
					orcarch01 = find_npc_near( attachee, 8979 )
					orcsnip01 = find_npc_near( attachee, 8980 )
					orcmark01 = find_npc_near( attachee, 8981 )
					orcsnip02 = find_npc_near( attachee, 8982 )
					orcarch02 = find_npc_near( attachee, 8983 )
					if (obj_percent_hp(gnollxx01) <= 75 or obj_percent_hp(gnollxx02) <= 75 or obj_percent_hp(gnollxx03) <= 75 or obj_percent_hp(gnollxx04) <= 75 or obj_percent_hp(gnollxx05) <= 75 or obj_percent_hp(bugbear01) <= 75 or obj_percent_hp(bugbear02) <= 75 or obj_percent_hp(bugbear03) <= 75 or obj_percent_hp(bugbear04) <= 75 or obj_percent_hp(ogrexxx01) <= 75 or obj_percent_hp(ogrexxx02) <= 75 or obj_percent_hp(ogrexxx03) <= 75 or obj_percent_hp(orcsham01) <= 75 or obj_percent_hp(orcbowm01) <= 75 or obj_percent_hp(orcarch01) <= 75 or obj_percent_hp(orcsnip01) <= 75 or obj_percent_hp(orcmark01) <= 75 or obj_percent_hp(orcsnip02) <= 75 or obj_percent_hp(orcarch02) <= 75):
						if (game.global_vars[794] <= 17):
							attachee.obj_set_int(obj_f_critter_strategy, 474)
							game.global_vars[794] = game.global_vars[794] + 1
						elif (game.global_vars[795] <= 1):
							attachee.obj_set_int(obj_f_critter_strategy, 537)
							game.global_vars[795] = game.global_vars[795] + 1
						else:
							attachee.obj_set_int(obj_f_critter_strategy, 534)
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 543)
				elif (attachee.name == 8965):
				## hb ravine south
					orcserg02 = find_npc_near( attachee, 8950 )
					bugbear06 = find_npc_near( attachee, 8951 )
					bugbear07 = find_npc_near( attachee, 8952 )
					bugbear08 = find_npc_near( attachee, 8953 )
					bugbear09 = find_npc_near( attachee, 8954 )
					gnollxx06 = find_npc_near( attachee, 8955 )
					gnollxx07 = find_npc_near( attachee, 8956 )
					gnollxx08 = find_npc_near( attachee, 8957 )
					gnollxx09 = find_npc_near( attachee, 8958 )
					ettinxx01 = find_npc_near( attachee, 8975 )
					ettinxx02 = find_npc_near( attachee, 8976 )
					ettinxx03 = find_npc_near( attachee, 8977 )
					orcsham02 = find_npc_near( attachee, 8966 )
					orcarch04 = find_npc_near( attachee, 8985 )
					orcsnip03 = find_npc_near( attachee, 8987 )
					orcbowm03 = find_npc_near( attachee, 8989 )
					orcarch05 = find_npc_near( attachee, 8991 )
					if (obj_percent_hp(orcserg02) <= 75 or obj_percent_hp(bugbear06) <= 75 or obj_percent_hp(bugbear07) <= 75 or obj_percent_hp(bugbear08) <= 75 or obj_percent_hp(bugbear09) <= 75 or obj_percent_hp(gnollxx06) <= 75 or obj_percent_hp(gnollxx07) <= 75 or obj_percent_hp(gnollxx08) <= 75 or obj_percent_hp(gnollxx09) <= 75 or obj_percent_hp(ettinxx01) <= 75 or obj_percent_hp(ettinxx02) <= 75 or obj_percent_hp(ettinxx03) <= 75 or obj_percent_hp(orcsham02) <= 75 or obj_percent_hp(orcarch04) <= 75 or obj_percent_hp(orcsnip03) <= 75 or obj_percent_hp(orcbowm03) <= 75 or obj_percent_hp(orcarch05) <= 75):
						if (game.global_vars[796] <= 17):
							attachee.obj_set_int(obj_f_critter_strategy, 474)
							game.global_vars[796] = game.global_vars[796] + 1
						elif (game.global_vars[797] <= 1):
							attachee.obj_set_int(obj_f_critter_strategy, 537)
							game.global_vars[797] = game.global_vars[797] + 1
						else:
							attachee.obj_set_int(obj_f_critter_strategy, 534)
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 543)
	elif (attachee.leader_get() != OBJ_HANDLE_NULL):
		attachee.obj_set_int(obj_f_critter_strategy, 0)
	return RUN_DEFAULT


##########################################################################################
##	SCRIPT DETAIL FOR START COMBAT							##
##########################################################################################
##	if not dead, unconscious, prone, or in party					##
##		if under 75% health							##
##			if haven't cast all 18 healing spells				##
##				set strategy to self healing				##
##				increment healing variable				##
##			otherwise, if haven't cast all 2 attack spells			##
##				set strategy to attack casting				##
##				increment attack casting variable			##
##			otherwise (if have cast all healing and attack spells)		##
##				set strategy to melee					##
##		otherwise (if over 75% health)						##
##			find friends							##
##			if any are under 75% health					##
##				if haven't cast all 18 healing spells			##
##					set strategy to friend healing			##
##					increment healing variable			##
##				otheriwse, if haven't cast all 2 attack spells		##
##					set strategy to attack casting			##
##					increment attack casting variable		##
##				otherwise (if have cast all healing and attack spells)	##
##					set strategy to melee				##
##			otherwise							##
##				if haven't cast all 2 attack spells			##
##					set strategy to attack casting			##
##					increment attack casting variable		##
##				otherwise						##
##					set strategy to guard				##
##	otherwise, if in party								##
##		set strategy to default							##
##	run default									##
##########################################################################################