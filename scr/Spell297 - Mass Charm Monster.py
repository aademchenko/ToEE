from toee import *

def OnBeginSpellCast(spell):
	print "Mass Charm Monster OnBeginSpellCast ", spell.id
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles("sp-enchantment-conjure", spell.caster)

	# Sort the list by hitdice
	spell.spell_target_list_sort(SORT_TARGET_LIST_BY_HIT_DICE_THEN_DIST, SORT_TARGET_LIST_ORDER_ASCENDING)
	print "target_list sorted by hitdice and dist from target_Loc (least to greatest): ", spell.target_list

def	OnSpellEffect(spell):
	print "Mass Charm Monster OnSpellEffect"

	remove_list = []
	spell.duration = 600 * spell.caster_level
	hitDiceAmount = 2 * spell.caster_level

	if game.global_vars[451] & 2**2 != 0:
		if game.combat_is_active():
			spell.dc = spell.dc - 5 # to reflect a bonus to the saving throw for casting charm in combat
	
	
	for target in spell.target_list:

		# Check critter hit dice
		targetHitDice = target.obj.hit_dice_num

		if (targetHitDice <= hitDiceAmount or target == spell.target_list[0]):

			# Subtract the target's hit dice from the amount allowed.
			hitDiceAmount = hitDiceAmount - targetHitDice

			if not target.obj.is_friendly(spell.caster):
				if not target.obj.saving_throw_spell(spell.dc, D20_Save_Will, D20STD_F_CHARM, spell.caster, spell.id):
					# saving throw unsuccessful
					target.obj.float_mesfile_line('mes\\spell.mes', 30002)
					spell.caster.ai_follower_add(target.obj)
					target.obj.condition_add_with_args('sp-Charm Monster', spell.id, spell.duration, target.obj.hit_dice_num)
					target.partsys_id = game.particles('sp-Charm Monster', target.obj)
					# add target to initiative
					target.obj.add_to_initiative()
					game.update_combat_ui()
					# Add time event.
					game.timevent_add(removeCharmMonster, (spell.caster, target.obj), spell.duration * 6000)
				else:
					# saving throw successful
					target.obj.float_mesfile_line('mes\\spell.mes', 30001)
					game.particles('Fizzle', target.obj)
					remove_list.append(target.obj)
			else:
				# can't target friendlies
				game.particles('Fizzle', target.obj)
				remove_list.append(target.obj)
		else:
			# Run out of allowed HD.
			game.particles('Fizzle', target.obj)
			remove_list.append(target.obj)

	spell.target_list.remove_list(remove_list)
	spell.spell_end(spell.id)

def OnBeginRound(spell):
	print "Mass Charm Monster OnBeginRound"

def OnEndSpellCast(spell):
	print "Mass Charm Monster OnEndSpellCast"

def removeCharmMonster(caster, target):
	print "Mass Charm Monster - removing charm. ", caster, target

	caster.ai_follower_remove(target)
	caster.follower_remove(target)
	caster.ai_shitlist_add(target)
