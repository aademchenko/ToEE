from toee import *

def OnBeginSpellCast( spell ):
	print "Detect Magic OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-divination-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Detect Magic OnSpellEffect"

	spell.duration = 10 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Detect Magic', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Detect Magic', target.obj )

def OnBeginRound( spell ):
	print "Detect Magic OnBeginRound"

	# get all targets in a 90' cone, apply magical_aura particle systems
	for obj in game.obj_list_cone( spell.caster, OLC_ALL, spell.range_exact, -45, 90 ):

		if obj.type == obj_t_portal:
			if obj.portal_flags_get() & OPF_MAGICALLY_HELD:
				game.particles( 'sp-Detect Magic 1 Low', obj )

		elif obj_is_item( obj ):
			if obj.item_flags_get() & OIF_IS_MAGICAL:
				game.particles( 'sp-Detect Magic 2 Med', obj )

		elif obj.type == obj_t_pc or obj.type == obj_t_npc:
			if obj.has_spell_effects() == 1:
				game.particles( 'sp-Detect Magic 3 High', obj )

def OnEndSpellCast( spell ):
	print "Detect Magic OnEndSpellCast"