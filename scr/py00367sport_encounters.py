from toee import *
from utilities import *
from combat_standard_routines import *


def san_enter_combat( attachee, triggerer ):
	if (attachee.map == 5070 or attachee.map == 5071 or attachee.map == 5072 or attachee.map == 5073 or attachee.map == 5074 or attachee.map == 5075 or attachee.map == 5076 or attachee.map == 5077):
		if (attachee.name == 14290):
		# pirates spawn brigands
			if (game.global_vars[564] == 1):
				brig = game.obj_create( 14574, attachee.location-6 )
				brig.rotation = game.random_range(1,5)
				brig.concealed_set(1)
				brig.unconceal()
				game.global_vars[564] = 2
		elif (attachee.name == 14173):
		# bugbears spawn orcs
			if (game.global_vars[564] == 1):
				orci = game.obj_create( 14899, attachee.location-6 )
				orci.rotation = game.random_range(1,5)
				orci.concealed_set(1)
				orci.unconceal()
				game.global_vars[564] = 2
		elif (attachee.name == 14912):
		# bugbear archers spawn orc archers
			if (game.global_vars[564] == 1):
				orci = game.obj_create( 14467, attachee.location-10 )
				orci.rotation = game.random_range(1,5)
				orci.concealed_set(1)
				orci.unconceal()
				game.global_vars[564] = 2
		elif (attachee.name == 14572):
		# hill giants spawn ettins
			if (game.global_vars[564] == 1):
				etti = game.obj_create( 14573, attachee.location-6 )
				etti.rotation = game.random_range(1,5)
				etti.concealed_set(1)
				etti.unconceal()
				game.global_vars[564] = 2
		elif (attachee.name == 14686):
		# bugbears spawn female bugbears
			if (game.global_vars[564] == 1):
				bugi = game.obj_create( 14216, attachee.location-6 )
				bugi.rotation = game.random_range(1,5)
				bugi.concealed_set(1)
				bugi.unconceal()
				game.global_vars[564] = 2
		elif (attachee.name == 14123):
		# zombies spawn lacedons
			if (game.global_vars[564] == 1):
				lace = game.obj_create( 14688, attachee.location-6 )
				lace.rotation = game.random_range(1,5)
				lace.concealed_set(1)
				lace.unconceal()
				game.global_vars[564] = 2
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT