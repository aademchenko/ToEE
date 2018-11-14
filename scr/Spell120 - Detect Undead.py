from toee import *

def OnBeginSpellCast( spell ):
	print "Detect Undead OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-divination-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Detect Undead OnSpellEffect"

	spell.duration = 10 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Detect Undead', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Detect Undead', target.obj )

def OnBeginRound( spell ):
	print "Detect Undead OnBeginRound"

	# get all targets in a 90' cone, apply magical_aura particle systems
	for obj in game.obj_list_cone( spell.caster, OLC_CRITTERS, spell.range_exact, -45, 90 ):

		if obj.is_category_type( mc_type_undead ):
			if obj.hit_dice_num >= 11:
				game.particles( 'sp-Detect Undead 3 High', obj )
			elif obj.hit_dice_num >= 5:
				game.particles( 'sp-Detect Undead 2 Med', obj )
			else:
				game.particles( 'sp-Detect Undead 1 Low', obj )

def OnEndSpellCast( spell ):
	print "Detect Undead OnEndSpellCast"