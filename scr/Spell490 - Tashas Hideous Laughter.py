from utilities import *
from toee import *

def OnBeginSpellCast( spell ):
	print "Tasha's Hideous Laughter OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Tasha's Hideous Laughter OnSpellEffect"

	spell.duration = 1 * spell.caster_level

	target = spell.target_list[0]

	npc = spell.caster			##  added so NPC's will choose valid targets
	if npc.name == 14333:
		spell.duration = 5
		spell.caster_level = 5
		for obj in game.party[0].group_list():
			target.obj = obj
##	if npc.name == 14424 and target.obj.stat_level_get( stat_intelligence ) < 3:
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL and (target.obj.stat_level_get( stat_intelligence ) < 3 or critter_is_unconscious(target.obj) == 1 or target.obj.d20_query(Q_Prone)):
		game.global_flags[811] = 0	
		for obj in game.party[0].group_list():
			if obj.distance_to(npc) <= 5 and critter_is_unconscious(obj) != 1 and obj.stat_level_get( stat_intelligence ) >= 3 and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
				target.obj = obj
				game.global_flags[811] = 1
		for obj in game.party[0].group_list():
			if obj.distance_to(npc) <= 10 and critter_is_unconscious(obj) != 1 and obj.stat_level_get( stat_intelligence ) >= 3 and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
				target.obj = obj
				game.global_flags[811] = 1
		for obj in game.party[0].group_list():
			if obj.distance_to(npc) <= 15 and critter_is_unconscious(obj) != 1 and obj.stat_level_get( stat_intelligence ) >= 3 and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
				target.obj = obj
				game.global_flags[811] = 1
		for obj in game.party[0].group_list():
			if obj.distance_to(npc) <= 20 and critter_is_unconscious(obj) != 1 and obj.stat_level_get( stat_intelligence ) >= 3 and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
				target.obj = obj
				game.global_flags[811] = 1
		for obj in game.party[0].group_list():
			if obj.distance_to(npc) <= 25 and critter_is_unconscious(obj) != 1 and obj.stat_level_get( stat_intelligence ) >= 3 and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
				target.obj = obj
				game.global_flags[811] = 1
		for obj in game.party[0].group_list():
			if obj.distance_to(npc) <= 30 and critter_is_unconscious(obj) != 1 and obj.stat_level_get( stat_intelligence ) >= 3 and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
				target.obj = obj
				game.global_flags[811] = 1
		for obj in game.party[0].group_list():
			if obj.distance_to(npc) <= 35 and critter_is_unconscious(obj) != 1 and obj.stat_level_get( stat_intelligence ) >= 3 and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
				target.obj = obj
				game.global_flags[811] = 1
		for obj in game.party[0].group_list():
			if obj.distance_to(npc) <= 40 and critter_is_unconscious(obj) != 1 and obj.stat_level_get( stat_intelligence ) >= 3 and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
				target.obj = obj
				game.global_flags[811] = 1
		for obj in game.party[0].group_list():
			if obj.distance_to(npc) <= 45 and critter_is_unconscious(obj) != 1 and obj.stat_level_get( stat_intelligence ) >= 3 and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
				target.obj = obj
				game.global_flags[811] = 1
		for obj in game.party[0].group_list():
			if obj.distance_to(npc) <= 50 and critter_is_unconscious(obj) != 1 and obj.stat_level_get( stat_intelligence ) >= 3 and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
				target.obj = obj
				game.global_flags[811] = 1
		for obj in game.party[0].group_list():
			if obj.distance_to(npc) <= 100 and critter_is_unconscious(obj) != 1 and obj.stat_level_get( stat_intelligence ) >= 3 and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
				target.obj = obj
				game.global_flags[811] = 1

	if ( target.obj.stat_level_get( stat_intelligence ) < 3 ):

		#print target.obj, " unaffected! (int < 3)"
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 31014 )
		# not affected
		game.particles( 'Fizzle', target.obj )
		spell.target_list.remove_target( target.obj )

	else:

		# if monster type of caster and target differ, +4 to save (or -4 to DC)
		if not( target.obj.get_category_type() == spell.caster.get_category_type() ):
			print "category types differ for ", spell.caster, " and ", target.obj, "!"
			spell.dc = spell.dc - 4

		# allow Will saving throw to negate
		if target.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

			# saving throw successful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			game.particles( 'Fizzle', target.obj )
			spell.target_list.remove_target( target.obj )
		else:

			# saving throw unsuccessful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			target.obj.condition_add_with_args( 'sp-Tashas Hideous Laughter', spell.id, spell.duration, 0 )
			target.partsys_id = game.particles( 'sp-Tashas Hideous Laughter', target.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Tasha's Hideous Laughter OnBeginRound"

def OnEndSpellCast( spell ):
	print "Tasha's Hideous Laughter OnEndSpellCast"