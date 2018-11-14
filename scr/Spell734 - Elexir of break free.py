from toee import *

def OnBeginSpellCast( spell ):
	print "Elixir of break free OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level

def	OnSpellEffect( spell ):
	print "Elixir of break free OnSpellEffect"

	target = spell.target_list[0]
	spell.duration = 0

#	target.obj.condition_add_with_args( 'Elixer Timed Skill Bonus', 2, 0, 0 )

	if target.obj.d20_query(Q_Is_BreakFree_Possible):
		game.global_vars[756] = target.obj.stat_level_get(stat_strength)
		target.obj.stat_base_set(stat_strength, 50)
		target.obj.d20_send_signal(S_BreakFree)
		target.obj.stat_base_set(stat_strength, game.global_vars[756])

#picker_obj.stat_base_set(stat_experience, game.global_vars[752])}

#	while(target.obj.d20_query(Q_Is_BreakFree_Possible)):
#		target.obj.d20_send_signal(S_BreakFree)
#	if not target.obj.d20_query(Q_Is_BreakFree_Possible):
#		target.obj.condition_add_with_args( 'sp-Freedom of Movement', spell.id, 0, 0 )
#		target.obj.condition_add_with_args( 'sp-Bulls Strength', spell.id, spell.duration, 40)

def OnBeginRound( spell ):
	print "Elixir of break free OnBeginRound"

def OnEndSpellCast( spell ):
	print "Elixir of break free OnEndSpellCast"