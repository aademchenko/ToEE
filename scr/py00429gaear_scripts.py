from toee import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	if ( (game.global_flags[164] == 1) and (attachee.map == 5105) ):		## turns on falrinth bugbear guards
		attachee.object_flag_unset(OF_OFF)
	if ( (game.global_vars[959] == 3) and (attachee.map == 5068) ):			## turns on bearded devils at Imeryds Run
		attachee.object_flag_unset(OF_OFF)
	if ( (is_daytime() != 1) and (attachee.map == 5121) ):				## turns off Verbobonc citizens at night
		attachee.object_flag_set(OF_OFF)
	if ( (is_daytime() == 1) and (attachee.map == 5121) ):				## turns on Verbobonc citizens during the day
		attachee.object_flag_unset(OF_OFF)
	if ( (is_daytime() == 1) and (attachee.map == 5124) ):				## turns off Spruce Goose patrons during the day
		attachee.object_flag_set(OF_OFF)
	if ( (is_daytime() != 1) and (attachee.map == 5124) ):				## turns on Spruce Goose patrons at night
		attachee.object_flag_unset(OF_OFF)
	if ( (is_daytime() != 1) and (attachee.map == 5125) ):				## turns off Spruce Goose housekeeping at night
		attachee.object_flag_set(OF_OFF)
	if ( (is_daytime() == 1) and (attachee.map == 5125) ):				## turns on Spruce Goose housekeeping during the day
		attachee.object_flag_unset(OF_OFF)
	if ( (is_daytime() != 1) and (attachee.map == 5163) ):				## turns off Castle basement staff at night
		attachee.object_flag_set(OF_OFF)
	if ( (is_daytime() == 1) and (attachee.map == 5163) ):				## turns on Castle basement staff during the day
		attachee.object_flag_unset(OF_OFF)
	if ( (is_daytime() != 1) and (attachee.map == 5164) ):				## turns off Castle first floor staff at night
		attachee.object_flag_set(OF_OFF)
	if ( (is_daytime() == 1) and (attachee.map == 5164) ):				## turns on Castle first floor staff during the day
		attachee.object_flag_unset(OF_OFF)
	if ( (is_daytime() != 1) and (attachee.map == 5165) ):				## turns off Castle second floor staff at night
		attachee.object_flag_set(OF_OFF)
	if ( (is_daytime() == 1) and (attachee.map == 5165) ):				## turns on Castle second floor staff during the day
		attachee.object_flag_unset(OF_OFF)
	if ( (game.global_vars[696] == 6) and (attachee.map == 5002) ):			## turns on Moathouse exterior water snake
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT