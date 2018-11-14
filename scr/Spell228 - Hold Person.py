from utilities import *
from toee import *

def OnBeginSpellCast( spell ):
	print "Hold Person OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Hold Person OnSpellEffect"

	spell.duration = 1 * spell.caster_level

	target = spell.target_list[0]

	npc = spell.caster			##  added so NPC's will choose valid targets

	#ff = open('hold_person_feedback.txt', 'w')
	#ffws = 'Original target: ' + str(target) + '\n' + str(target.obj) + '\n' + 'Caster: ' + str(npc)

	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL:
		#ffws += '\n\nEntering NPC if clause...\n\n'
		if target.obj.is_category_type( mc_type_humanoid ) and target.obj.get_size < STAT_SIZE_LARGE and critter_is_unconscious(target.obj) != 1 and not target.obj.d20_query(Q_Prone):
			npc = spell.caster
			#ffws += 'Target Okayed!\n'
		else:
			#ffws += 'Target NOT Okayed!\n'
			game.global_flags[811] = 0

			for obj in game.party[0].group_list():
				ffws += str(obj) + '\n'
				if obj.distance_to(npc) <= 5 and critter_is_unconscious(obj) != 1 and obj.is_category_type( mc_type_humanoid ) and obj.get_size < STAT_SIZE_LARGE and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
					target.obj = obj
					game.global_flags[811] = 1
			for obj in game.party[0].group_list():
				if obj.distance_to(npc) <= 10 and critter_is_unconscious(obj) != 1 and obj.is_category_type( mc_type_humanoid ) and obj.get_size < STAT_SIZE_LARGE and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
					target.obj = obj
					game.global_flags[811] = 1
			for obj in game.party[0].group_list():
				if obj.distance_to(npc) <= 15 and critter_is_unconscious(obj) != 1 and obj.is_category_type( mc_type_humanoid ) and obj.get_size < STAT_SIZE_LARGE and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
					target.obj = obj
					game.global_flags[811] = 1
			for obj in game.party[0].group_list():
				if obj.distance_to(npc) <= 20 and critter_is_unconscious(obj) != 1 and obj.is_category_type( mc_type_humanoid ) and obj.get_size < STAT_SIZE_LARGE and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
					target.obj = obj
					game.global_flags[811] = 1
			for obj in game.party[0].group_list():
				if obj.distance_to(npc) <= 25 and critter_is_unconscious(obj) != 1 and obj.is_category_type( mc_type_humanoid ) and obj.get_size < STAT_SIZE_LARGE and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
					target.obj = obj
					game.global_flags[811] = 1
			for obj in game.party[0].group_list():
				if obj.distance_to(npc) <= 30 and critter_is_unconscious(obj) != 1 and obj.is_category_type( mc_type_humanoid ) and obj.get_size < STAT_SIZE_LARGE and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
					target.obj = obj
					game.global_flags[811] = 1
			for obj in game.party[0].group_list():
				if obj.distance_to(npc) <= 100 and critter_is_unconscious(obj) != 1 and obj.is_category_type( mc_type_humanoid ) and obj.get_size < STAT_SIZE_LARGE and game.global_flags[811] == 0 and not obj.d20_query(Q_Prone):
					target.obj = obj
					game.global_flags[811] = 1

	#ff.write(ffws)
	#ff.close()			
	if target.obj.is_category_type( mc_type_humanoid ):

		if target.obj.get_size < STAT_SIZE_LARGE:

			# allow Will saving throw to negate
			if target.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

				# saving throw successful
				target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

				game.particles( 'Fizzle', target.obj )
				spell.target_list.remove_target( target.obj )
			else:
				# saving throw unsuccessful
				target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

				# HTN - apply condition HOLD (paralyzed)
				target.obj.condition_add_with_args( 'sp-Hold Person', spell.id, spell.duration, 0 )
				target.partsys_id = game.particles( 'sp-Hold Person', target.obj )
		else:
			# not medium sized or smaller
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
			targe.obj.float_mesfile_line( 'mes\\spell.mes', 31005 )

			game.particles( 'Fizzle', target.obj )
			spell.target_list.remove_target( target.obj )

	else:
		# not a person
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
		target.obj.float_mesfile_line( 'mes\\spell.mes', 31004 )

		game.particles( 'Fizzle', target.obj )
		spell.target_list.remove_target( target.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Hold Person OnBeginRound"

def OnEndSpellCast( spell ):
	print "Hold Person OnEndSpellCast"
