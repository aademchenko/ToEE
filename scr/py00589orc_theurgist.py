from toee import *
from utilities import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	if (attachee.name == 8962):
		stone_backup_ravine_3 = game.obj_create( 14986, location_from_axis (432L, 506L) )
		stone_backup_ravine_3.rotation = 4.71238898038
		stone_backup_ravine_3.concealed_set(1)
		stone_backup_ravine_3.unconceal()
		game.particles( "Mon-EarthElem-Unconceal", stone_backup_ravine_3 )
		for obj in game.obj_list_vicinity(stone_backup_ravine_3.location,OLC_PC):
			stone_backup_ravine_3.attack(obj)
		stone_backup_ravine_4 = game.obj_create( 14986, location_from_axis (440L, 506L) )
		stone_backup_ravine_4.rotation = 4.71238898038
		stone_backup_ravine_4.concealed_set(1)
		stone_backup_ravine_4.unconceal()
		game.particles( "Mon-EarthElem-Unconceal", stone_backup_ravine_4 )
		game.sound( 4176, 1 )
		game.update_combat_ui()
		for obj in game.obj_list_vicinity(stone_backup_ravine_4.location,OLC_PC):
			stone_backup_ravine_4.attack(obj)
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	webbed = break_free( attachee, 3)
	if (attachee != OBJ_HANDLE_NULL and critter_is_unconscious(attachee) != 1 and not attachee.d20_query(Q_Prone) and attachee.leader_get() == OBJ_HANDLE_NULL):
		if (attachee.name == 8962 or attachee.name == 8964):
			if (obj_percent_hp(attachee) <= 75):
				if (attachee.name == 8962):
				## hb ravine central 1
					if (game.global_vars[798] <= 15):
						attachee.obj_set_int(obj_f_critter_strategy, 542)
						game.global_vars[798] = game.global_vars[798] + 1
					elif (game.global_vars[799] <= 3):
						attachee.obj_set_int(obj_f_critter_strategy, 538)
						game.global_vars[799] = game.global_vars[799] + 1
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 536)
				elif (attachee.name == 8964):
				## hb ravine central 2
					if (game.global_vars[800] <= 15):
						attachee.obj_set_int(obj_f_critter_strategy, 542)
						game.global_vars[800] = game.global_vars[800] + 1
					elif (game.global_vars[801] <= 3):
						attachee.obj_set_int(obj_f_critter_strategy, 538)
						game.global_vars[801] = game.global_vars[801] + 1
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 536)
			elif (obj_percent_hp(attachee) >= 76):
				if (attachee.name == 8962):
				## hb ravine central 1
					bugbear05 = find_npc_near( attachee, 8940 )
					orcserg01 = find_npc_near( attachee, 8941 )
					orcfigh01 = find_npc_near( attachee, 8942 )
					orcfigh02 = find_npc_near( attachee, 8943 )
					orcfigh03 = find_npc_near( attachee, 8944 )
					orcmurd01 = find_npc_near( attachee, 8945 )
					orcdomi01 = find_npc_near( attachee, 8946 )
					orcfigh04 = find_npc_near( attachee, 8947 )
					orcfigh05 = find_npc_near( attachee, 8948 )
					orcrund01 = find_npc_near( attachee, 8949 )
					stogian01 = find_npc_near( attachee, 8972 )
					hilgian01 = find_npc_near( attachee, 8973 )
					stogian02 = find_npc_near( attachee, 8974 )
					orctheu02 = find_npc_near( attachee, 8964 )
					orcarch03 = find_npc_near( attachee, 8984 )
					orcbowm02 = find_npc_near( attachee, 8986 )
					orcmark02 = find_npc_near( attachee, 8988 )
					orcsnip04 = find_npc_near( attachee, 8990 )
					if (obj_percent_hp(bugbear05) <= 75 or obj_percent_hp(orcserg01) <= 75 or obj_percent_hp(orcfigh01) <= 75 or obj_percent_hp(orcfigh02) <= 75 or obj_percent_hp(orcfigh03) <= 75 or obj_percent_hp(orcmurd01) <= 75 or obj_percent_hp(orcdomi01) <= 75 or obj_percent_hp(orcfigh04) <= 75 or obj_percent_hp(orcfigh05) <= 75 or obj_percent_hp(orcrund01) <= 75 or obj_percent_hp(stogian01) <= 75 or obj_percent_hp(hilgian01) <= 75 or obj_percent_hp(stogian02) <= 75 or obj_percent_hp(orctheu02) <= 75 or obj_percent_hp(orcarch03) <= 75 or obj_percent_hp(orcbowm02) <= 75 or obj_percent_hp(orcmark02) <= 75 or obj_percent_hp(orcsnip04) <= 75):
						if (game.global_vars[798] <= 15):
							attachee.obj_set_int(obj_f_critter_strategy, 476)
							game.global_vars[798] = game.global_vars[798] + 1
						elif (game.global_vars[799] <= 3):
							attachee.obj_set_int(obj_f_critter_strategy, 538)
							game.global_vars[799] = game.global_vars[799] + 1
						else:
							attachee.obj_set_int(obj_f_critter_strategy, 536)
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 544)
				elif (attachee.name == 8964):
				## hb ravine central 2
					bugbear05 = find_npc_near( attachee, 8940 )
					orcserg01 = find_npc_near( attachee, 8941 )
					orcfigh01 = find_npc_near( attachee, 8942 )
					orcfigh02 = find_npc_near( attachee, 8943 )
					orcfigh03 = find_npc_near( attachee, 8944 )
					orcmurd01 = find_npc_near( attachee, 8945 )
					orcdomi01 = find_npc_near( attachee, 8946 )
					orcfigh04 = find_npc_near( attachee, 8947 )
					orcfigh05 = find_npc_near( attachee, 8948 )
					orcrund01 = find_npc_near( attachee, 8949 )
					stogian01 = find_npc_near( attachee, 8972 )
					hilgian01 = find_npc_near( attachee, 8973 )
					stogian02 = find_npc_near( attachee, 8974 )
					orctheu01 = find_npc_near( attachee, 8962 )
					orcarch03 = find_npc_near( attachee, 8984 )
					orcbowm02 = find_npc_near( attachee, 8986 )
					orcmark02 = find_npc_near( attachee, 8988 )
					orcsnip04 = find_npc_near( attachee, 8990 )
					if (obj_percent_hp(bugbear05) <= 75 or obj_percent_hp(orcserg01) <= 75 or obj_percent_hp(orcfigh01) <= 75 or obj_percent_hp(orcfigh02) <= 75 or obj_percent_hp(orcfigh03) <= 75 or obj_percent_hp(orcmurd01) <= 75 or obj_percent_hp(orcdomi01) <= 75 or obj_percent_hp(orcfigh04) <= 75 or obj_percent_hp(orcfigh05) <= 75 or obj_percent_hp(orcrund01) <= 75 or obj_percent_hp(stogian01) <= 75 or obj_percent_hp(hilgian01) <= 75 or obj_percent_hp(stogian02) <= 75 or obj_percent_hp(orctheu01) <= 75 or obj_percent_hp(orcarch03) <= 75 or obj_percent_hp(orcbowm02) <= 75 or obj_percent_hp(orcmark02) <= 75 or obj_percent_hp(orcsnip04) <= 75):
						if (game.global_vars[800] <= 15):
							attachee.obj_set_int(obj_f_critter_strategy, 476)
							game.global_vars[800] = game.global_vars[800] + 1
						elif (game.global_vars[801] <= 3):
							attachee.obj_set_int(obj_f_critter_strategy, 538)
							game.global_vars[801] = game.global_vars[801] + 1
						else:
							attachee.obj_set_int(obj_f_critter_strategy, 536)
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 544)
		elif (attachee.name == 8998 or attachee.name == 9000):
			if (obj_percent_hp(attachee) <= 75):
				if (attachee.name == 8998):
				## hb pit west 1
					if (game.global_vars[803] <= 15):
						attachee.obj_set_int(obj_f_critter_strategy, 542)
						game.global_vars[803] = game.global_vars[803] + 1
					elif (game.global_vars[804] <= 3):
						attachee.obj_set_int(obj_f_critter_strategy, 538)
						game.global_vars[804] = game.global_vars[804] + 1
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 536)
				elif (attachee.name == 9000):
				## hb pit east 1
					if (game.global_vars[805] <= 15):
						attachee.obj_set_int(obj_f_critter_strategy, 542)
						game.global_vars[805] = game.global_vars[805] + 1
					elif (game.global_vars[806] <= 3):
						attachee.obj_set_int(obj_f_critter_strategy, 538)
						game.global_vars[806] = game.global_vars[806] + 1
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 536)
			elif (obj_percent_hp(attachee) >= 76):
				if (attachee.name == 8998):
				## hb pit west 1
					orcmurd01 = find_npc_near( attachee, 8992 )
					orcserg01 = find_npc_near( attachee, 8993 )
					ogrexxx01 = find_npc_near( attachee, 8994 )
					orcsnip01 = find_npc_near( attachee, 8995 )
					orcsnip02 = find_npc_near( attachee, 8996 )
					orcmark01 = find_npc_near( attachee, 8997 )
					if (obj_percent_hp(orcmurd01) <= 75 or obj_percent_hp(orcserg01) <= 75 or obj_percent_hp(ogrexxx01) <= 75 or obj_percent_hp(orcsnip01) <= 75 or obj_percent_hp(orcsnip02) <= 75 or obj_percent_hp(orcmark01) <= 75):
						if (game.global_vars[803] <= 15):
							attachee.obj_set_int(obj_f_critter_strategy, 476)
							game.global_vars[803] = game.global_vars[803] + 1
						elif (game.global_vars[804] <= 3):
							attachee.obj_set_int(obj_f_critter_strategy, 538)
							game.global_vars[804] = game.global_vars[804] + 1
						else:
							attachee.obj_set_int(obj_f_critter_strategy, 536)
					else:
						if (game.global_vars[804] <= 3):
							attachee.obj_set_int(obj_f_critter_strategy, 538)
							game.global_vars[804] = game.global_vars[804] + 1
						else:
							attachee.obj_set_int(obj_f_critter_strategy, 544)
				elif (attachee.name == 9000):
				## hb pit east 1
					orcassa01 = find_npc_near( attachee, 8999 )
					orcfigh01 = find_npc_near( attachee, 8601 )
					orcfigh02 = find_npc_near( attachee, 8602 )
					orcfigh03 = find_npc_near( attachee, 8603 )
					orcfigh04 = find_npc_near( attachee, 8604 )
					orcfigh05 = find_npc_near( attachee, 8605 )
					orcfigh06 = find_npc_near( attachee, 8606 )
					orcsnip01 = find_npc_near( attachee, 8607 )
					orcsnip02 = find_npc_near( attachee, 8608 )
					orcmark01 = find_npc_near( attachee, 8609 )
					if (obj_percent_hp(orcassa01) <= 75 or obj_percent_hp(orcfigh01) <= 75 or obj_percent_hp(orcfigh02) <= 75 or obj_percent_hp(orcfigh03) <= 75 or obj_percent_hp(orcfigh04) <= 75 or obj_percent_hp(orcfigh05) <= 75 or obj_percent_hp(orcfigh06) <= 75 or obj_percent_hp(orcsnip01) <= 75 or obj_percent_hp(orcsnip02) <= 75 or obj_percent_hp(orcmark01) <= 75):
						if (game.global_vars[805] <= 15):
							attachee.obj_set_int(obj_f_critter_strategy, 476)
							game.global_vars[805] = game.global_vars[805] + 1
						elif (game.global_vars[806] <= 3):
							attachee.obj_set_int(obj_f_critter_strategy, 538)
							game.global_vars[806] = game.global_vars[806] + 1
						else:
							attachee.obj_set_int(obj_f_critter_strategy, 536)
					else:
						if (game.global_vars[806] <= 3):
							attachee.obj_set_int(obj_f_critter_strategy, 538)
							game.global_vars[806] = game.global_vars[806] + 1
						else:
							attachee.obj_set_int(obj_f_critter_strategy, 544)
		elif (attachee.name == 8624):
		## hb cave west
			if (obj_percent_hp(attachee) <= 75):
				if (game.global_vars[807] <= 15):
					attachee.obj_set_int(obj_f_critter_strategy, 542)
					game.global_vars[807] = game.global_vars[807] + 1
				elif (game.global_vars[808] <= 3):
					attachee.obj_set_int(obj_f_critter_strategy, 538)
					game.global_vars[808] = game.global_vars[808] + 1
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 536)
			elif (obj_percent_hp(attachee) >= 76):
				orcwarl01 = find_npc_near( attachee, 8626 )
				orcwitc01 = find_npc_near( attachee, 8627 )
				orcmark01 = find_npc_near( attachee, 8628 )
				orcmark02 = find_npc_near( attachee, 8629 )
				orcsnip01 = find_npc_near( attachee, 8630 )
				orcsnip02 = find_npc_near( attachee, 8631 )
				if (obj_percent_hp(orcwarl01) <= 75 or obj_percent_hp(orcwitc01) <= 75 or obj_percent_hp(orcmark01) <= 75 or obj_percent_hp(orcmark02) <= 75 or obj_percent_hp(orcsnip01) <= 75 or obj_percent_hp(orcsnip02) <= 75):
					if (game.global_vars[807] <= 15):
						attachee.obj_set_int(obj_f_critter_strategy, 476)
						game.global_vars[807] = game.global_vars[807] + 1
					elif (game.global_vars[808] <= 3):
						attachee.obj_set_int(obj_f_critter_strategy, 538)
						game.global_vars[808] = game.global_vars[808] + 1
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 536)
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 544)
		elif (attachee.name == 8625):
		## hb cave east
			if (obj_percent_hp(attachee) <= 75):
				if (game.global_vars[809] <= 15):
					attachee.obj_set_int(obj_f_critter_strategy, 542)
					game.global_vars[809] = game.global_vars[809] + 1
				elif (game.global_vars[810] <= 3):
					attachee.obj_set_int(obj_f_critter_strategy, 538)
					game.global_vars[810] = game.global_vars[810] + 1
				else:
					attachee.obj_set_int(obj_f_critter_strategy, 536)
			elif (obj_percent_hp(attachee) >= 76):
				orcfigh01 = find_npc_near( attachee, 8632 )
				orcfigh02 = find_npc_near( attachee, 8633 )
				gnollxx01 = find_npc_near( attachee, 8634 )
				bugbear01 = find_npc_near( attachee, 8635 )
				boonthagx = find_npc_near( attachee, 8816 )
				kallopxxx = find_npc_near( attachee, 8815 )
				ergoxxxxx = find_npc_near( attachee, 8814 )
				naiglliht = find_npc_near( attachee, 8813 )
				hungousxx = find_npc_near( attachee, 8803 )
				krunchxxx = find_npc_near( attachee, 8802 )
				ruffxxxxx = find_npc_near( attachee, 8817 )
				if (obj_percent_hp(orcfigh01) <= 75 or obj_percent_hp(orcfigh02) <= 75 or obj_percent_hp(gnollxx01) <= 75 or obj_percent_hp(bugbear01) <= 75 or obj_percent_hp(boonthagx) <= 75 or obj_percent_hp(kallopxxx) <= 75 or obj_percent_hp(ergoxxxxx) <= 75 or obj_percent_hp(naiglliht) <= 75 or obj_percent_hp(hungousxx) <= 75 or obj_percent_hp(krunchxxx) <= 75 or obj_percent_hp(ruffxxxxx) <= 75):
					if (game.global_vars[809] <= 15):
						attachee.obj_set_int(obj_f_critter_strategy, 476)
						game.global_vars[809] = game.global_vars[809] + 1
					elif (game.global_vars[810] <= 3):
						attachee.obj_set_int(obj_f_critter_strategy, 538)
						game.global_vars[810] = game.global_vars[810] + 1
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 536)
				else:
					if (game.global_vars[810] <= 3):
						attachee.obj_set_int(obj_f_critter_strategy, 538)
						game.global_vars[810] = game.global_vars[810] + 1
					else:
						attachee.obj_set_int(obj_f_critter_strategy, 544)
	elif (attachee.leader_get() != OBJ_HANDLE_NULL):
		attachee.obj_set_int(obj_f_critter_strategy, 0)
	return RUN_DEFAULT


##########################################################################################
##	SCRIPT DETAIL FOR START COMBAT							##
##########################################################################################
##	if not dead, unconscious, prone, or in party					##
##		if under 60% health							##
##			if haven't cast all 16 healing spells				##
##				set strategy to self healing				##
##				increment healing variable				##
##			otherwise, if haven't cast all 4 attack spells			##
##				set strategy to attack casting				##
##				increment attack casting variable			##
##			otherwise (if have cast all healing and attack spells)		##
##				set strategy to melee					##
##		otherwise (if over 60% health)						##
##			find friends							##
##			if any are under 60% health					##
##				if haven't cast all 16 healing spells			##
##					set strategy to friend healing			##
##					increment healing variable			##
##				otheriwse, if haven't cast all 4 attack spells		##
##					set strategy to attack casting			##
##					increment attack casting variable		##
##				otherwise (if have cast all healing and attack spells)	##
##					set strategy to melee				##
##			otherwise							##
##				if haven't cast all 4 attack spells			##
##					set strategy to attack casting			##
##					increment attack casting variable		##
##				otherwise						##
##					set strategy to guard				##
##	otherwise, if in party								##
##		set strategy to default							##
##	run default									##
##########################################################################################