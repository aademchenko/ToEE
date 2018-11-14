from toee import *

def OnBeginSpellCast( spell ):
	print "Death Knell OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Death Knell OnSpellEffect"

	target_item = spell.target_list[0]

	npc = spell.caster			##  added so NPC's will choose valid targets
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL:
		for pc in game.party:
			curr = pc.stat_level_get( stat_hp_current )
			if (curr <= 0 and curr >= -9 and pc.distance_to(npc) <= 10):
				target_item.obj = pc

	if npc.name == 14609:
		spell.caster_level = 8
	if npc.name == 14601:
		spell.caster_level = 4

	spell.duration = 100 * target_item.obj.hit_dice_num

	if target_item.obj.stat_level_get( stat_hp_current ) < 0:

		if not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
	
			# saving throw unsuccessful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
	
			#target_item.obj.condition_add_with_args( 'sp-Death Knell', spell.id, spell.duration, 2 )
			spell.caster.float_mesfile_line( 'mes\\spell.mes', 20023 )
			spell.caster.condition_add_with_args( 'sp-Death Knell', spell.id, spell.duration, 2 ) # 2 is STR bonus
			# So you'll get awarded XP for the kill
			if not target_item.obj in game.leader.group_list():
				target_item.obj.damage( game.leader , D20DT_UNSPECIFIED, dice_new( "1d1" ) )
			target_item.obj.critter_kill_by_effect()
			target_item.partsys_id = game.particles( 'sp-Death Knell', target_item.obj )
			
	
		else:
	
			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
	
			game.particles( 'Fizzle', target_item.obj )
			spell.target_list.remove_target( target_item.obj )

	else:

		# target's hp_cur is >= 0
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31006 )

		game.particles( 'Fizzle', target_item.obj )
		spell.target_list.remove_target( target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Death Knell OnBeginRound"

def OnEndSpellCast( spell ):
	print "Death Knell OnEndSpellCast"