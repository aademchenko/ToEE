from toee import *
from utilities import *
from Co8 import *

def OnBeginSpellCast( spell ):
	print "Destruction OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Destruction OnSpellEffect"

	dam = dice_new( "10d6" )
	spell.duration = 0
	# changed_con = 0

	target_item = spell.target_list[0]

	# determine focus
	focus = 0
	if (spell.caster.type != obj_t_pc) and (spell.caster.leader_get() == OBJ_HANDLE_NULL):
		# for NPCs not in game party
		focus = 1
	else:
		if spell.caster.money_get() >= 50000:
			focus = 1

	# check for focus
	if focus == 1:
		game.particles( 'sp-Disintegrate-Hit', target_item.obj )

		if (target_item.obj.name == 14629 or target_item.obj.name == 14621 or target_item.obj.name == 14604) and not is_spell_flag_set(target_item.obj, OSF_IS_FLAMING_SPHERE):
			game.particles( 'sp-Stoneskin', target_item.obj.location )
			target_item.obj.destroy()

		elif target_item.obj.is_category_type( mc_type_construct ) or target_item.obj.is_category_type( mc_type_undead ):
			game.particles( 'Fizzle', target_item.obj )
			# if target_item.obj.stat_base_get(stat_constitution) < 0:
				# target_item.obj.stat_base_set(stat_constitution, 10)
				# changed_con = 1

		elif (target_item.obj.type == obj_t_pc) or (target_item.obj.type == obj_t_npc):
			if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
				target_item.obj.spell_damage( spell.caster, D20DT_FORCE, dam, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )

			else:
				# So you'll get awarded XP for the kill
				if not target_item.obj in game.leader.group_list():
					target_item.obj.damage( game.leader, D20DT_UNSPECIFIED, dice_new( "1d1" ) )
				target_item.obj.critter_kill_by_effect()	
				target_item.obj.condition_add_with_args( 'sp-Animate Dead', spell.id, spell.duration, 3 )
				game.particles( 'sp-Stoneskin', target_item.obj )

		else:
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30003 )
			game.particles( 'Fizzle', target_item.obj )

	else:
		# no focus
		spell.caster.float_mesfile_line( 'mes\\spell.mes', 16009 )

	# if changed_con == 1:
		# target_item.obj.stat_base_set(stat_constitution, -1)

	spell.target_list.remove_target( target_item.obj )
	spell.spell_end( spell.id )

def OnEndSpellCast( spell ):
	print "Destruction OnEndSpellCast"