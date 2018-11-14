from Co8 import *

def OnBeginSpellCast( spell ):
	print "ahobm OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "ahobm OnSpellEffect"

	remove_list = []

	spell.duration = 1	
	game.particles( 'sp-Bane', spell.caster )
	

	for target_item in spell.target_list:		
		tar = target_item.obj
		if (tar.name == 8064) or (tar.name == 8042) or (tar.name == 8043) or (tar.name == 14455):
			remove_list.append( tar )
			tar.float_mesfile_line( 'mes\\spell.mes', 20048 )
		elif tar.is_category_type( mc_type_plant ):
			remove_list.append( tar )
			tar.float_mesfile_line( 'mes\\spell.mes', 20049 )
		elif tar.is_category_type( mc_type_ooze ):
			remove_list.append( tar )
			tar.float_mesfile_line( 'mes\\spell.mes', 20049 )
		elif tar.is_category_type( mc_type_aberration ):
			remove_list.append( tar )
			tar.float_mesfile_line( 'mes\\spell.mes', 20049 )
		elif tar.is_category_type( mc_type_undead ):
			remove_list.append( tar )
			tar.float_mesfile_line( 'mes\\spell.mes', 20050 )
		elif tar.name == 14455:
			remove_list.append( tar )
		else:
			tar.float_mesfile_line( 'mes\\spell.mes', 30002 )
			tar.float_mesfile_line( 'mes\\spell.mes', 20047 )
			tar.critter_kill_by_effect()
		
	spell.target_list.remove_list( remove_list )
		
	End_Spell(spell)
		
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "ahobm OnBeginRound"

def OnEndSpellCast( spell ):
	print "ahobm OnBeginRound"

