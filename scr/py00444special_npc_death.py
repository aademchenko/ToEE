from toee import *
from py00439script_daemon import record_time_stamp, get_v, set_v, npc_set, npc_unset, npc_get, tsc, tpsts, within_rect_by_corners
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if attachee.name == 14248:
		# Ogre Chief
		record_time_stamp(505)
		record_time_stamp(508)
		set_v(499, get_v(499) + 1 )
		if ( get_v(498) / 75.0 )**3 +  ( get_v(499) / 38.0 ) ** 3  + ( get_v(500) / 13.0 )**3 >= 1:
			record_time_stamp(510)
	elif attachee.name == 14156:
		# Earth Commander
		record_time_stamp(506)
		record_time_stamp(507)
		set_v(500, get_v(500) + 1 )
		if ( get_v(498) / 75.0 )**3 +  ( get_v(499) / 38.0 ) ** 3  + ( get_v(500) / 13.0 )**3 >= 1:
			record_time_stamp(511)
	elif attachee.name == 8045:
		# Romag
		#actually, he already has a san_dying of his own, so no need for this one
		#we'll keep it as "infrastructure"
		record_time_stamp(456)

	elif attachee.name == 14154:
		# Hartsch
		record_time_stamp(506)
		set_v(500, get_v(500) + 1 )
		if get_v(500) >= 10:
			record_time_stamp(511)

	elif attachee.name == 14244:
		# Juggernaut; makes it go kaboom and fade out
		attachee.object_flag_set(OF_SEE_THROUGH)
		attachee.object_flag_set(OF_FLAT)
		attachee.object_flag_set(OF_TRANSLUCENT)
		attachee.object_flag_set(OF_CLICK_THROUGH)
		attachee.object_flag_set(OF_NOHEIGHT)
		attachee.fade_to(0, 1, 10)
		#attachee.scripts[14] = 444 # so that upon end of combat the Jug will become click-through
		game.particles( "sp-polymorph other" , attachee)
		game.particles( "sp-unholy water" , attachee)
		game.particles( "sp-enervation-hit" , attachee)
		game.particles( "sp-pyrotechnics-fireworks" , attachee)
		game.particles( "sp-ray of enfeeblement-end" , attachee)
		game.particles( "mon-earthelem-unconceal" , attachee)
		game.particles( "Ass Sunburst" , attachee)
		game.particles( "ef-minocloud" , attachee)
		game.particles( "sp-flare" , attachee)
		game.particles( "sp-mage hand" , attachee)
		game.sound(15122,1)
		game.sound(15122,1)
	return RUN_DEFAULT


def san_exit_combat(attachee, triggerer):
	if attachee.name == 14244:
		attachee.object_flag_set(OF_CLICK_THROUGH)
		attachee.fade_to(110, 1, 3)
	return RUN_DEFAULT