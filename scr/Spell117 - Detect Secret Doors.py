from toee import *

def OnBeginSpellCast( spell ):
	print "Detect Secret Doors OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-divination-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Detect Secret Doors OnSpellEffect"

	spell.duration = 10 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Detect Secret Doors', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Detect Secret Doors', target.obj )

def OnBeginRound( spell ):
	print "Detect Secret Doors OnBeginRound"

	# get all targets in a 90' cone, apply detetct_secret_doors_aura particle systems
	for obj in game.obj_list_cone( spell.caster, OLC_ALL, spell.range_exact, -45, 90 ):

		obj.secretdoor_detect( spell.caster )

def OnEndSpellCast( spell ):
	print "Detect Secret Doors OnEndSpellCast"