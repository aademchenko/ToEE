from toee import *
from utilities import  * 

def OnBeginSpellCast( spell ):	
	print "Prismatic Spray OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect ( spell ):
	
	print "Prismatic Spray OnSpellEffect"
	
	remove_list = []
	game.particles( 'sp-Prismatic Spray', spell.caster )
	dam = dice_new('1d1')
	npc = spell.caster
	effect1 = 0
	effect_list = []
	spell.duration = 1000
	#### Caster is NOT in game party
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL:
		range = 60
		target_list = list(game.obj_list_cone( spell.caster, OLC_CRITTERS, range, -30, 60 ))
		target_list.remove(spell.caster)
		# get all targets in a 25ft + 2ft/level cone (60')
		soundfizzle = 0
		for t in target_list:			
			effect_list = []
			
			effect1 = game.random_range(1,8)
			if effect1 == 8:
				effect_list.append(game.random_range(1,8))
				effect_list.append(game.random_range(1,8))
			else:
				effect_list.append(effect1)
			if len(effect_list)==1:
				if effect_list[0] == 5 or effect_list[0] == 6:
					pass
				else:
					remove_list.append(t)
			if len(effect_list) == 2:
				if effect_list[0] == 5 or effect_list[0]==6 or effect_list[1]==5 or effect_list[1]==6:
					pass
				else:
					remove_list.append(t)
			for effect in effect_list:
				
				if effect == 1:
					#20 fire damage
					dam.number = 20
					xx,yy = location_to_axis(t.location)
					if t.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
						# Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
						t.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1 )
			
						game.particles( 'swirled gas', t )
						soundfizzle = 1
					else:
						if t.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_FIRE, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ) > 0:
							# saving throw successful
							t.float_mesfile_line( 'mes\\spell.mes', 30001 )
						else:
							# saving throw unsuccessful
							t.float_mesfile_line( 'mes\\spell.mes', 30002 )
					
				elif effect == 2:
					#40 acid damage
					dam.number = 40
					if t.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_ACID, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ) > 0:
						# saving throw successful
						t.float_mesfile_line( 'mes\\spell.mes', 30001 )
					else:
						# saving throw unsuccessful
						t.float_mesfile_line( 'mes\\spell.mes', 30002 )
				elif effect == 3:
					#80 Electricity damage
					dam.number = 80
					if t.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_ELECTRICITY, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ) > 0:
						# saving throw successful
						t.float_mesfile_line( 'mes\\spell.mes', 30001 )
					else:
						# saving throw unsuccessful
						t.float_mesfile_line( 'mes\\spell.mes', 30002 )
				elif effect == 4:
					#poisoned no save = die save = 1-10 con damage
					if t.is_category_type(mc_type_ooze) == 0 and t.is_category_type(mc_type_plant) == 0 and t.is_category_type(mc_type_undead) == 0:

						#if not t.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
							# saving throw unsuccessful
							t.float_mesfile_line( 'mes\\spell.mes', 30002 )
							t.critter_kill_by_effect()
						#else:
							# saving throw successful
							poison_index = 23
							time_to_secondary = 10
							poison_dc = 200
							t.float_mesfile_line( 'mes\\spell.mes', 30001 )
							t.condition_add_with_args( 'Poisoned', poison_index, time_to_secondary, poison_dc )
							#t.condition.add_with_args( 'sp-Neutralize Poison', spell.id, spell.duration, 0 )
							game.timevent_add(end_poison,(spell, t), 12000)#don't want secondary damage here
							
					
				elif effect == 5:
					#turned to stone
					
					if t.saving_throw( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, D20A_CAST_SPELL ):
						# saving throw successful
						t.float_mesfile_line( 'mes\\spell.mes', 30001 )

					else:
						# saving throw unsuccessful
						t.float_mesfile_line( 'mes\\spell.mes', 30002 )
						# HTN - apply condition HALT (Petrified)
						t.condition_add_with_args( 'sp-Command', spell.id, spell.duration, 4 )
						game.particles( 'sp-Bestow Curse', t )
						

				elif effect == 6:
					#insane					
					dc = spell.dc						
					if not t.saving_throw_spell( dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
						t.float_mesfile_line( 'mes\\spell.mes', 30002 )
						t.condition_add_with_args( 'sp-Confusion', spell.id, spell.duration, 1 )						
					else:
						t.float_mesfile_line( 'mes\\spell.mes', 30001 )	
		if soundfizzle == 1:
			game.sound(7581,1)
			game.sound(7581,1)
			

	#### Caster is in game party
	
	if npc.type == obj_t_pc or npc.leader_get() != OBJ_HANDLE_NULL:			
		soundfizzle = 0
		for t in spell.target_list:
			
			effect_list = []
			
			effect1 = game.random_range(1,8)
			if effect1 == 8:
				effect_list.append(game.random_range(1,8))
				effect_list.append(game.random_range(1,8))
			else:
				effect_list.append(effect1)
			if len(effect_list)==1:
				if effect_list[0] == 5 or effect_list[0] == 6:
					pass
				else:
					remove_list.append(t.obj)
			if len(effect_list) == 2:
				if effect_list[0] == 5 or effect_list[0]==6 or effect_list[1]==5 or effect_list[1]==6:
					pass
				else:
					remove_list.append(t.obj)
			for effect in effect_list:
				
				if effect == 1:
					#20 fire damage
					dam.number = 20
					xx,yy = location_to_axis(t.obj.location)
					if t.obj.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
						# Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
						t.obj.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1 )
			
						game.particles( 'swirled gas', t.obj )
						soundfizzle = 1
					else:
						if t.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_FIRE, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ) > 0:
							# saving throw successful
							t.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
						else:
							# saving throw unsuccessful
							t.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
					
				elif effect == 2:
					#40 acid damage
					dam.number = 40
					if t.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_ACID, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ) > 0:
						# saving throw successful
						t.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
					else:
						# saving throw unsuccessful
						t.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
				elif effect == 3:
					#80 Electricity damage
					dam.number = 80
					if t.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_ELECTRICITY, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ) > 0:
						# saving throw successful
						t.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
					else:
						# saving throw unsuccessful
						t.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
				elif effect == 4:
					#poisoned no save = die save = 1-10 con damage
					if t.obj.is_category_type(mc_type_ooze) == 0 and t.obj.is_category_type(mc_type_plant) == 0 and t.obj.is_category_type(mc_type_undead) == 0 and t.obj.is_category_type(mc_type_construct) == 0:

						if not t.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
							# saving throw unsuccessful
							t.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
							# So you'll get awarded XP for the kill
							if not t.obj in game.leader.group_list():
								t.obj.damage( game.leader , D20DT_UNSPECIFIED, dice_new( "1d1" ) )
							t.obj.critter_kill_by_effect()
						else:
							# saving throw successful
							poison_index = 23
							time_to_secondary = 10
							poison_dc = 200
							t.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
							t.obj.condition_add_with_args( 'Poisoned', poison_index, time_to_secondary, poison_dc )
							game.timevent_add(end_poison,(spell, t.obj), 6000)#don't want secondary damage here
							
					
				elif effect == 5:
					#turned to stone
					
					if t.obj.saving_throw( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, D20A_CAST_SPELL ):
						# saving throw successful
						t.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

					else:
						# saving throw unsuccessful
						t.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
						# HTN - apply condition HALT (Petrified)
						t.obj.condition_add_with_args( 'sp-Command', spell.id, spell.duration, 4 )
						game.particles( 'sp-Bestow Curse', t.obj )
						

				elif effect == 6:
					#insane					
					dc = spell.dc						
					if not t.obj.saving_throw_spell( dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
						t.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
						t.obj.condition_add_with_args( 'sp-Confusion', spell.id, spell.duration, 1 )						
					else:
						t.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
					
				elif effect == 7:
					#sent to another plane- kill and destroy for now
					dc = spell.dc					
					if not t.obj.saving_throw_spell( dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
						t.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
						# So you'll get awarded XP for the kill
						if not t.obj in game.leader.group_list():
							t.obj.damage( game.leader , D20DT_UNSPECIFIED, dice_new( "1d1" ) )
						t.obj.critter_kill_by_effect()
						t.obj.destroy()
					else:
						t.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			del effect_list	
		if soundfizzle == 1:
			game.sound(7581,1)
			game.sound(7581,1)
	
	spell.target_list.remove_list( remove_list )
	spell.spell_end(spell.id)
	

def OnBeginRound( spell ):
	print "Prismatic Spray OnBeginRound"

def OnEndSpellCast( spell ):
	print "Prismatic Spray OnEndSpellCast"
def end_poison( spell, id):
	id.condition_add_with_args( 'sp-Neutralize Poison', spell.id, spell.duration, 0 )

		
