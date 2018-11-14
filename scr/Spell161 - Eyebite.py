from toee import *

def OnBeginSpellCast( spell ):
	print "Eyebite OnBeginSpellCast"
	print "spell.target_list=", spell.target_list, " id= ", spell.id
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-cast", spell.caster )

def	OnSpellEffect( spell ):
	print "Eyebite OnSpellEffect"

	spell.duration = 100 * spell.caster_level	# 10 mins / caster level

	targettingDuration = len(spell.target_list) - 1
	#print "Applying slow to caster for ", targettingDuration
	spell.caster.condition_add_with_args('sp-Slow', spell.id, targettingDuration, 0)	# Only get single action.

	time = 0
	for target in spell.target_list:
		if (time == 0):
			biteTarget(target.obj, spell.caster, spell.id, spell.dc, spell.duration)
		else:
			#print "addimg timeevent for ", target.obj, " in ", time
			game.timeevent_add(biteTarget, (target.obj, spell.caster, spell.id, spell.dc, spell.duration), time)
		time = time + 1000


#	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Eyebite OnBeginRound"

def OnEndSpellCast( spell ):
	print "Eyebite OnEndSpellCast"

def OnSpellStruck( spell ):
	print "Eyebite OnSpellStruck"
	

def biteTarget(target, caster, spell_id, spell_dc, duration):

	print "Eyebiting ", target
	# Fortitude saving throw to negate
	if target.saving_throw_spell(spell_dc, D20_Save_Fortitude, D20STD_F_NONE, caster, spell_id):
		# saving throw successful
		target.float_mesfile_line('mes\\spell.mes', 30001)
		game.particles('Fizzle', target)
	else:
		# saving throw unsuccessful
		target.float_mesfile_line('mes\\spell.mes', 30002)

		print target, "is shaken"	# shaken
		#target.condition_add_with_args('sp-Emotion Despair', spell_id, duration, 0)
		target.condition_add_with_args('sp-Doom', spell_id, duration, 0)

		if (target.hit_dice_num < 5):
			print target, "is comatose"	# comatose
			#target.condition_add_with_args( 'sp-Command', spell.id, spell.duration, 4 )
			target.condition_add_with_args('sp-Tashas Hideous Laughter', spell_id, duration, 0)
		elif (target.hit_dice_num < 10):
			print target, "is panicked"	# panicked
			target.condition_add_with_args('sp-Fear', spell_id, game.random_range(1,4), 0)

		game.particles('sp-Cause Fear', target)
