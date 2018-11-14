from toee import *

def OnBeginSpellCast( spell ):
	print "Glitterdust OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Glitterdust OnSpellEffect"

	spell.duration = 1 * spell.caster_level

	game.particles( 'sp-Glitter Dust', spell.target_loc )

	# get all targets in a 10ft radius
	for target_item in spell.target_list:

		if not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
			# saving throw unsuccesful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			# apply blindness
			target_item.obj.condition_add_with_args( 'sp-Glitterdust Blindness', spell.id, spell.duration, 0 )

		else:
			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

		# always affected by dust
		target_item.obj.condition_add_with_args( 'sp-Glitterdust', spell.id, spell.duration, 0 )
		target_item.partsys_id = game.particles( 'sp-Glitter Dust-HIT', target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Glitterdust OnBeginRound"

def OnEndSpellCast( spell ):
	print "Glitterdust OnEndSpellCast"