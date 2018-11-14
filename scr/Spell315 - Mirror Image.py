from toee import *

def OnBeginSpellCast( spell ):
	print "Mirror Image OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-illusion-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Mirror Image OnSpellEffect"

	spell.duration = 10 * spell.caster_level
	target_item = spell.target_list[0]

	dice = dice_new( '1d4' )
	dice.bonus = 1 + (spell.caster_level / 3)

	num_of_images = dice.roll()
	if num_of_images > 8:
		num_of_images = 8

	#print "num of images=", num_of_images, "bonus=", 1 + (spell.caster_level / 3)

	game.particles( 'sp-Mirror Image', target_item.obj )
	target_item.obj.condition_add_with_args( 'sp-Mirror Image', spell.id, spell.duration, num_of_images )
	#target_item.partsys_id = game.particles( 'sp-Mirror Image', target_item.obj )

def OnBeginRound( spell ):
	print "Mirror Image OnBeginRound"

def OnEndSpellCast( spell ):
	print "Mirror Image OnEndSpellCast"