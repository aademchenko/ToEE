from toee import *
from utilities import *

def OnBeginSpellCast( spell ):
	print "Magic Missile OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

	#spell.num_of_projectiles = spell.num_of_projectiles + 1
	#spell.target_list.push_target(spell.caster)     # didn't work :(
	# generally the sequence is: OnBeginSpellCast, OnBeginProjectile, OnSpellEffect,OnEndProjectile (OnBeginRound isn't called)

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


	damage_dice = dice_new( '1d4' )
	damage_dice.bonus = 1

	target_item_obj = target.obj
	if (not spell.caster in game.party[0].group_list() ) and target_item_obj.d20_query(Q_Critter_Is_Charmed ) :
		# NPC enemy is trying to cast on a charmed target - this is mostly meant for the Cult of the Siren encounter
		target_item_obj = party_closest( spell.caster, conscious_only= 1, mode_select= 1, exclude_warded= 1, exclude_charmed = 1) # select nearest conscious PC instead, who isn't already charmed
		if target_item_obj == OBJ_HANDLE_NULL:
			target_item_obj = target.obj

	# always hits
	target_item_obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
	target.partsys_id = game.particles( 'sp-magic missle-hit', target_item_obj )
	
	npc = spell.caster

	
	## The following section scripts extra damage dice for NPC casters
	## This is necessary because they can't shoot more than one bolt of Magic Missile (hardcoded engine limitation)
	## The workaround is to apply extra damage for that single bolt, custom tailored for each NPC caster
	
	if (not spell.caster in game.party ): 
		if npc.name == 8036:
		## Wizard level 3/4 => 1 extra Magic Missile
		## 8036 - Deggum 
			target_item_obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target_item_obj )

		if npc.name in [14827, 14424, 14333, 14598, 14599, 14820, 8075, 8076]:
		## Wizard level 5/6 => 2 extra Magic Missiles
		## 14827 - Temple Tower Wizard
		## 14424 - Wizard
		## 14333 - Half Elven Wizard
		## 14598 - Undead Wizard (Red)
		## 14599 - Undead Wizard (Blue)
		## 14820 - Wizard Zombie
		## 8075 - Hedrack Ally Wizard 1 (object name)
		## 8076 - Hedrack Ally Wizard 2 (object name)

			target_item_obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target_item_obj )
			target_item_obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target_item_obj )

		elif npc.name in [14888]:
			# Level 8 -> 3 extra missiles
			# 14888 - Siren Cultist
			target_item_obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target_item_obj )
			target_item_obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target_item_obj )
			target_item_obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target_item_obj )

		elif npc.name == 8729 or npc.name == 14607 or npc.name == 20123 or npc.name == 14779 or npc.name == 14658 or npc.name == 8738 or npc.name == 8739 or npc.name == 8740 or npc.name == 8741:
		## Wizard level 9+ => 4 extra Magic Missiles
		## 8729 - Senshock
		## 14607 - Enchantress (from revenge encounter)
		## 20123 - Falrinth
		## 14779 - Verbobonc Mage
		## 14658 - Verbobonc Mage
		## 8738, 8739, 8740, 8741 - Hextor Mage
			target.obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target.obj )
			target.obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target.obj )
			target.obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target.obj )
			target.obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target.obj )

		elif npc.name == 8054 and npc.leader_get() == OBJ_HANDLE_NULL:	
		##  added so Burne can cast
			target.obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target.obj )
			target.obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target.obj )
			target.obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target.obj )

		elif npc.name == 14271 and npc.leader_get() == OBJ_HANDLE_NULL:	
		##  added so Sargen can cast
			target.obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
			target.partsys_id = game.particles( 'sp-magic missle-hit', target.obj )
			target.obj.condition_add_with_args( 'sp-Magic Missile', spell.id, spell.duration, damage_dice.roll() )
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