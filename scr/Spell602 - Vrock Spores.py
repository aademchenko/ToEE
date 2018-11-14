from toee import *

def OnBeginSpellCast( spell ):
	print "Vrock Spores OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level

def	OnSpellEffect( spell ):
	print "Vrock Spores OnSpellEffect"

	remove_list = []

	spell.duration = 10
	damage_dice = dice_new( '1d8' )
	game.particles( 'Mon-Vrock-Spores', spell.caster )

	for target_item in spell.target_list:
		if not target_item.obj.is_category_subtype( mc_subtype_demon ):
			# damage 1-8 (no save)
			target_item.obj.spell_damage( spell.caster, D20DT_POISON, damage_dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

			# add SPORE condition
			target_item.obj.condition_add_with_args( 'sp-Vrock Spores', spell.id, spell.duration, 0 )
			target_item.partsys_id = game.particles( 'Mon-Vrock-Spores-Hit', target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Vrock Spores OnBeginRound"

def OnEndSpellCast( spell ):
	print "Vrock Spores OnEndSpellCast"
