from toee import *

def OnBeginSpellCast( spell ):
	print "Fear OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Fear OnSpellEffect"

	#remove_list = []

	npc = spell.caster
	if npc.name == 14358:	## Balor Guardian 	
		spell.dc = 25

	if npc.name == 14999:   ## Old White Dragon frightful presence
		spell.dc = 23
		
	if npc.name == 14280:   ## Groaning Spirit
		spell.dc = 19
		
	spell.duration = min( 1 * spell.caster_level, 10 )

	if npc.name == 14958:   ## Nightwalker
		spell.dc = 24
		spell.duration = game.random_range(1, 8)
	
	game.particles( 'sp-Fear', spell.caster )

	# get all targets in a 25ft + 2ft/level cone (60')
	for target_item in spell.target_list:
		if npc.name == 14999:
			if target_item.obj.type == obj_t_pc:
				if target_item.obj.stat_level_get(stat_level) >= 18:
					## creatures with equal or greater HD than the dragon are unaffected
					continue
		if not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

			# saving throw unsuccessful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			target_item.obj.condition_add_with_args( 'sp-Fear', spell.id, spell.duration, 0 )
			target_item.partsys_id = game.particles( 'sp-Fear-Hit', target_item.obj )

		else:

			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			#target_item.obj.condition_add_with_args( 'sp-Fear', spell.id, 1, 1 )
			#target_item.partsys_id = game.particles( 'sp-Fear-Hit', target_item.obj )
	
	#spell.target_list.remove_list( remove_list )
	#spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Fear OnBeginRound"

def OnEndSpellCast( spell ):
	print "Fear OnEndSpellCast"