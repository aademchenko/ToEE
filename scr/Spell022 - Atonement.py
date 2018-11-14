from toee import *

def OnBeginSpellCast( spell ):
	print "Atonement OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Atonement OnSpellEffect"

	spell.duration = 0
	XP_cost = 500

	target_item = spell.target_list[0]

	deity_list = [2, 3, 6, 8, 10, 11, 15, 16, 19]	## only good deities and St. Cuthbert (any suggestions?)
	caster_deity = spell.caster.stat_level_get(stat_deity)
	deity_command = 0

	caster_XP = spell.caster.stat_level_get(stat_experience)
	caster_level = spell.caster.stat_level_get(stat_level)

	# fix for spell caster NOT in game party
	if (spell.caster.type != obj_t_pc) and (spell.caster.leader_get() == OBJ_HANDLE_NULL):
		XP_cost = 0
		caster_XP = 0
		caster_level = 1

	# check if spell caster has enough XP
	if has_enoughXP(caster_XP, caster_level, XP_cost) == 1:

		# check if target is among the living
		if (target_item.obj.d20_query(Q_Dead) == 0) and (not target_item.obj.is_category_type( mc_type_undead ) or not target_item.obj.is_category_type( mc_type_construct )):

			# check if target is a paladin
			if target_item.obj.stat_level_get(stat_level_paladin) >= 1:

				# check if paladin has fallen
				if target_item.obj.d20_query(Q_IsFallenPaladin) == 1:

					# check deity
					for atone_deity in deity_list:
						if atone_deity == caster_deity:		## deity is answering
							target_item.obj.float_mesfile_line( 'mes\\skill_ui.mes', caster_deity + 910, tf_light_blue )
							game.particles( 'Paladin-Atoned', target_item.obj )
							target_item.obj.has_atoned()
							if (spell.caster.type == obj_t_pc) or (spell.caster.leader_get() != OBJ_HANDLE_NULL):
								spell.caster.stat_base_set(stat_experience, caster_XP - XP_cost)
							deity_list.remove_target( atone_deity )
							deity_command = 0

						else:
							deity_command = 1		## deity is not answering

					# give deity's comment
					if deity_command == 1:
						if caster_deity == 0:
							target_item.obj.float_mesfile_line( 'mes\\item.mes', 201, tf_green )

						else:
							target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30019 )
							target_item.obj.float_mesfile_line( 'mes\\deity.mes', caster_deity, tf_red )

				else:
					# not fallen
					game.particles( 'Fizzle', target_item.obj )

			else:
				# target is not a paladin
				game.particles( 'Fizzle', target_item.obj )

		else:
			# target is not among the living
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30003 )
			game.particles( 'Fizzle', target_item.obj )

	else:
		# not enough XP
		spell.caster.float_mesfile_line( 'mes\\action.mes', 1019 )

	spell.target_list.remove_target( target_item.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Atonement OnBeginRound"

def OnEndSpellCast( spell ):
	print "Atonement OnEndSpellCast"

def has_enoughXP( caster_XP, caster_level, XP_cost ):
	print "has_enoughXP"

	XP = 0
	level = 1
	while (level <= caster_level):
		XP = ((level - 1) * 1000) + XP
		if level == caster_level:
			if (caster_XP >= (XP + XP_cost)):
				return 1
			else:
				return 0
		level = level + 1
	return
