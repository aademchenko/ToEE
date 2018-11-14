from toee import *

def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 10 )
	return SKIP_DEFAULT
