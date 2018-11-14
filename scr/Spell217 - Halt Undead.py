from toee import *

def OnBeginSpellCast( spell ):
	print "Halt Undead OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Halt Undead OnSpellEffect"

	remove_list = []

	spell.duration = 1 * spell.caster_level

	for target_item in spell.target_list:

		# check if target is undead
		if target_item.obj.is_category_type( mc_type_undead ):

			# intelligent undead get a will save
			if target_item.obj.stat_level_get( stat_intelligence ) > 0:
	
				if not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
			
					# saving throw unsuccessful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
		
					target_item.obj.condition_add_with_args( 'sp-Halt Undead', spell.id, spell.duration, 0 )
					target_item.partsys_id = game.particles( 'sp-Halt Undead', target_item.obj )
			
				else:
			
					# saving throw successful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
		
					game.particles( 'Fizzle', target_item.obj )
					remove_list.append( target_item.obj )
	
			else:
				# no saving throw
				target_item.obj.condition_add_with_args( 'sp-Halt Undead', spell.id, spell.duration, 0 )
				target_item.partsys_id = game.particles( 'sp-Halt Undead', target_item.obj )

		else:
			# not an undead
			game.particles( 'Fizzle', target_item.obj )
			remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Halt Undead OnBeginRound"

def OnEndSpellCast( spell ):
	print "Halt Undead OnEndSpellCast"