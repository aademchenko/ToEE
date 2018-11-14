from toee import *
from combat_standard_routines import *
from utilities import *

def OnBeginSpellCast( spell ):
	print "Dimension Door OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Dimension Door OnSpellEffect"

	game.particles( 'sp-Dimension Door', spell.caster )
	target = spell.caster

	if spell.caster.name == 8042 and spell.caster.map == 5121:	# Iuz teleport in Verbobonc
		stop_condition = 0
		target_loc = party_closest(spell.caster, 1, mode_select = 1, exclude_warded = 1).location
		xx_o , yy_o = location_to_axis( target_loc )
		xx = xx_o
		yy = yy_o
		attempt_count = 0
		while stop_condition == 0 and attempt_count < 15:
			attempt_count += 1
			loc_list = []
			for obj in game.obj_list_vicinity(target_loc, OLC_NPC | OLC_PC):
				if obj.is_unconscious() == 0:
					loc_list.append( location_to_axis(obj.location) )
			if dist_from_set(xx, yy, loc_list) < 2 or ( xx >= 516 and xx <= 528 and yy >= 629 and yy <= 641 ):
				xx = xx_o + game.random_range(-4, 3)
				yy = yy_o + game.random_range(-4, 3)
			elif attempt_count >= 15:
				xx = xx_o
				yy = yy_o
			else:
				#game.global_vars[498] = (xx_o - xx)**2 + 1000* (yy_o-yy)**2
				#game.global_vars[499] = attempt_count
				stop_condition = 1
		target_loc = location_from_axis( xx, yy )
		target.fade_to( 0, 10, 40 )
		# WIP! SMM: added timeevent to trigger fadein (in realtime)
		game.particles( 'sp-Dimension Door', target )
		game.timevent_add( fade_back_in, ( target, target_loc, spell ), 750, 1 )

	elif target.d20_query_has_spell_condition( sp_Dimensional_Anchor ) == 0:
		target.fade_to( 0, 10, 40 )
		# WIP! SMM: added timeevent to trigger fadein (in realtime)
		game.particles( 'sp-Dimension Door', target )
		game.timevent_add( fade_back_in, ( target, spell.target_loc, spell ), 750, 1 )

	else:
		target.float_mesfile_line( 'mes\\spell.mes', 30011 )
		game.particles( 'Fizzle', target )
		spell.target_list.remove_target( target )
		spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Dimension Door OnBeginRound"

def OnEndSpellCast( spell ):
	print "Dimension Door OnEndSpellCast"

def fade_back_in( target, loc, spell ):
	target.move( loc, 0.0, 0.0 )
	game.particles( 'sp-Dimension Door', target )
	target.fade_to( 255, 10, 5 )
	spell.target_list.remove_target( target )
	spell.spell_end( spell.id )
	target.obj_set_int(324, 453)

def dist_from_set( xx, yy, loc_list ):
	dist_min = 100000
	for loc_tup in loc_list:
		dist_xy = ( ( xx-loc_tup[0] )**2 + ( yy-loc_tup[1] )**2 )**0.5
		if dist_xy < dist_min:
			dist_min = dist_xy
	return dist_min