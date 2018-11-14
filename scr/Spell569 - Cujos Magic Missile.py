from toee import *

def OnBeginSpellCast( spell ):
	print "Magic Missile OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Magic Missile OnSpellEffect"


def OnBeginRound( spell ):
	print "Magic Missile OnBeginRound"

def OnBeginProjectile( spell, projectile, index_of_target ):
	print "Magic Missile OnBeginProjectile"

	projectile.obj_set_int( obj_f_projectile_part_sys_id, game.particles( 'sp-magic missle-proj', projectile ) )
	

def OnEndProjectile( spell, projectile, index_of_target ):
	print "Magic Missile OnEndProjectile"

	game.particles_end( projectile.obj_get_int( obj_f_projectile_part_sys_id ) )

	target = spell.target_list[ index_of_target ]

	damage_dice = dice_new( '5d12' )
	damage_dice.bonus = 1

	# always hits
	target.obj.spell_damage( spell.caster, D20DT_FORCE, damage_dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
	target.partsys_id = game.particles( 'sp-magic missle-hit', target.obj )
	
	#spell.target_list.remove_target_by_index( index_of_target )
	spell.num_of_projectiles = spell.num_of_projectiles - 1

	if ( spell.num_of_projectiles == 0 ):
##		loc = target.obj.location
##		target.obj.destroy()
##		mxcr = game.obj_create( 12021, loc )
##		game.global_vars[30] = game.global_vars[30] + 1
		spell.spell_end( spell.id, 1 )

def OnEndSpellCast( spell ):
	print "Magic Missile OnEndSpellCast"