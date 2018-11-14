from toee import *

def OnBeginSpellCast( spell ):
	print "Detect Chaos OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-divination-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Detect Chaos OnSpellEffect"

	spell.duration = 100 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Detect Chaos', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Detect Alignment', target.obj )

def OnBeginRound( spell ):
	print "Detect Chaos OnBeginRound"

	# get all targets in a 90' cone, apply magical_aura particle systems
	for obj in game.obj_list_cone( spell.caster, OLC_CRITTERS, spell.range_exact, -45, 90 ):

		if obj.critter_get_alignment() & ALIGNMENT_CHAOTIC:

			# HTN - WIP! check "power"
			game.particles( 'sp-Detect Alignment Chaos', obj )

def OnEndSpellCast( spell ):
	print "Detect Chaos OnEndSpellCast"