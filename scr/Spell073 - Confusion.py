from toee import *

def OnBeginSpellCast( spell ):
	print "Confusion OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Confusion OnSpellEffect"

	remove_list = []

	npc = spell.caster

	if npc.name == 14359:	## Glabrezu Guardian 	
		spell.dc = 19
	elif npc.name == 14958:	## Nightwalker
		spell.dc = 18

	spell.duration = 1 * spell.caster_level
	game.particles( 'sp-Confusion', spell.target_loc )

	for target_item in spell.target_list:

		if target_item.obj.name == 14303 and target_item.obj.map == 5085 and npc.name == 14607 :
			remove_list.append( target_item.obj )
		elif not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
			# saving throw unsuccesful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			target_item.obj.condition_add_with_args( 'sp-Confusion', spell.id, spell.duration, 0 )
			target_item.partsys_id = game.particles( 'sp-Confusion-Hit', target_item.obj )
		else:
			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			game.particles( 'Fizzle', target_item.obj )
			remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Confusion OnBeginRound"

def OnEndSpellCast( spell ):
	print "Confusion OnEndSpellCast"