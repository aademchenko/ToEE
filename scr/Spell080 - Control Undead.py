from toee import *
from utilities import location_from_axis, location_to_axis, create_item_in_inventory

def OnBeginSpellCast( spell ):
	print "Control Undead OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Control Undead OnSpellEffect"

	remove_list = []

	spell.duration = 10 * spell.caster_level
	hitDiceAmount = 2 * spell.caster_level

	controlled_undead = 0
	lich_number = 0

	for target_item in spell.target_list:

		# check critter hit dice
		targetHitDice = target_item.obj.hit_dice_num

		# check if target does not exceed the amount allowed
		if hitDiceAmount >= targetHitDice:

			# check if target is undead
			if target_item.obj.is_category_type( mc_type_undead ):

				# subtract the target's hit dice from the amount allowed
				hitDiceAmount = hitDiceAmount - targetHitDice

				# check if target is Mathel or Angra Mainyu (a lich has +4 turn resistance)
				if (target_item.obj.name == 14785) or (target_item.obj.name == 8812) or (target_item.obj.name == 14984) or (target_item.obj.name == 8893):
					spell_dc = spell.dc
					spell.dc = spell.dc - 4
					lich_number = 1

				# check if target is not already rebuked
				if target_item.obj.d20_query(Q_Commanded) == 1:
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 20045 )
					game.particles( 'Fizzle', target_item.obj )

				elif not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
					# saving throw unsuccessful
					spell.caster.ai_follower_add( target_item.obj )
					target_item.obj.condition_add_with_args( 'Commanded', spell.id, spell.duration, 0 )
					game.particles( 'sp-Feeblemind', target_item.obj )

					# add target to initiative, just in case
					target_item.obj.add_to_initiative()
					game.update_combat_ui()

					# add time event
					game.timevent_add( removeControlUndead, (spell.caster, target_item.obj), spell.duration * 6000 )

					controlled_undead = 1

				else:
					# saving throw successful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
					game.particles( 'Fizzle', target_item.obj )

				# reset Lich turn resistance bonus
				if lich_number == 1:
					spell.dc = spell_dc
					lich_number = 0

			else:
				# not an undead
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31008 )
				game.particles( 'Fizzle', target_item.obj )

		else:
			# ran out of allowed HD
			game.particles( 'Fizzle', target_item.obj )

		remove_list.append( target_item.obj )

	if controlled_undead == 1:
		spell.caster.condition_add_with_args( 'sp-Owls Wisdom', spell.id, spell.duration, 0 )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Control Undead OnBeginRound"

def OnEndSpellCast( spell ):
	print "Control Undead OnEndSpellCast"

def removeControlUndead( caster, target ):
	print "Control Undead - removing control. ", caster, target

	old_undead = target.name
	old_undead_hp = target.obj_get_int(obj_f_hp_pts)
	old_undead_dam = target.obj_get_int(obj_f_hp_damage)
	old_undead_IQ = target.stat_level_get(stat_intelligence)

	undead_loc = target.location
	xx,yy = location_to_axis(target.location)
	undead_rot = target.rotation

	old_weapon = target.item_worn_at(3)
	old_shield1 = target.item_worn_at(4)
	old_shield2 = target.item_worn_at(11)
	old_ammo = target.item_worn_at(9)
	if (old_ammo != OBJ_HANDLE_NULL):
		old_quantity = old_ammo.obj_get_int(obj_f_ammo_quantity)

	caster.ai_follower_remove(target)
	caster.follower_remove(target)

	if target.d20_query(Q_Dead) == 0:
		target.destroy()

		if old_undead == 8812:		## Mathel fix
			old_undead = 14785
		if old_undead == 8893:		## Angra Mainyu fix
			old_undead = 14984
		# added to stop Skeleton crossbowmen from spawning more ammo on their first heartbeat
		if (old_undead == 14107) or (old_undead == 14600):
			old_undead = 14603

		new_undead = game.obj_create( old_undead, undead_loc )
		new_undead.obj_set_int(obj_f_hp_pts, old_undead_hp)
		new_undead.obj_set_int(obj_f_hp_damage, old_undead_dam)

		new_undead.move(location_from_axis(xx, yy))
		new_undead.rotation = undead_rot

		if (new_undead.item_worn_at(3) != OBJ_HANDLE_NULL):
			new_undead.item_worn_at(3).destroy()
		if (new_undead.item_worn_at(4) != OBJ_HANDLE_NULL):
			new_undead.item_worn_at(4).destroy()
		if (new_undead.item_worn_at(11) != OBJ_HANDLE_NULL):
			new_undead.item_worn_at(11).destroy()
		if (new_undead.item_worn_at(9) != OBJ_HANDLE_NULL):
			new_undead.item_worn_at(9).destroy()
		if (old_weapon != OBJ_HANDLE_NULL):
			create_item_in_inventory( old_weapon.name, new_undead )
		if (old_shield1 != OBJ_HANDLE_NULL):
			create_item_in_inventory( old_shield1.name, new_undead )
		if (old_shield2 != OBJ_HANDLE_NULL):
			create_item_in_inventory( old_shield2.name, new_undead )
		if (old_ammo != OBJ_HANDLE_NULL):
			new_ammo = game.obj_create( old_ammo.name, undead_loc )
			new_ammo.obj_set_int(obj_f_ammo_quantity, old_quantity)
			new_undead.item_get(new_ammo)
		new_undead.item_wield_best_all()

		if (old_undead_IQ > 0):
			if (old_undead == 14785) or (old_undead == 14984):	## Lich attack
				new_undead.float_mesfile_line( 'mes\\gd_cls_m2m.mes', 19013, tf_red )
				new_undead.attack(caster)
			else:
				new_undead_strat = new_undead.obj_get_int(obj_f_critter_strategy)	## critter strategy
				if (new_undead.item_find(4096) != OBJ_HANDLE_NULL) or (new_undead.item_find(4097) != OBJ_HANDLE_NULL):
					new_undead.obj_set_int(obj_f_critter_strategy, 183)	## Mage-Sniper strategy
				elif (new_undead.item_find(4194) != OBJ_HANDLE_NULL):
					new_undead.obj_set_int(obj_f_critter_strategy, 234)	## Skeleton Longspear (target dying) strategy
				else:
					new_undead.obj_set_int(obj_f_critter_strategy, 180)	## Assassin strategy
				game.timevent_add( resetControlUndead, (new_undead, new_undead_strat), 1000 )
				new_undead.attack(caster)

def resetControlUndead( target, strategy ):
	print "Control Undead - resetting strategy. ", target, strategy

	target.obj_set_int(obj_f_critter_strategy, strategy)
