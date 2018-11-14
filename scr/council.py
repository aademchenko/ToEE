from toee import *
from utilities import *
from py00439script_daemon import record_time_stamp, get_v, set_v, tsc, within_rect_by_corners



def initialize_council_events():
	#sets persistent variable 'Varrr438' to store the time of the council
	if get_v(435) == 0:
		set_v(435,1)
		c_month = game.time.time_game_in_months(game.time) + 1
		c_year = game.time.time_game_in_years(game.time)
		if c_month == 13:
			c_month = 1
			c_year = c_year + 1	
		set_v(438, c_month + 32*c_year)
	return


def council_time():
	#returns 1 if the time is the first day of the month, between 22:00 and 22:30, the month after Burne said he'd address the council
	#returns 2 if it's on that day, between 22:30 and 23:00
	#returns 3 if it's between 19 and 22
	#returns 4 if it's after the coucil events have played out, and it isn't the time for an ordinary council
	#returns 5 if it's the time for an ordinary council
	#can be used to create council meetings in general!

	g_year = game.time.time_game_in_years(game.time)
	g_month = game.time.time_game_in_months(game.time)
	g_day = game.time.time_game_in_days(game.time)
	g_hour = game.time.time_game_in_hours(game.time)
	g_minute = game.time.time_game_in_minutes(game.time)

	c_month = (get_v(438) & 31)
	c_year = (get_v(438) & (32768 -1 - 31)) / 32 ##uses a bit mask to filter the year, and brings it 5 bits down
	#explanation:
	#32768 = 1000000000000000
	#32768 - 1 = 1000000000000000 - 1 = 0111111111111111
	#32768 - 1 - 31 = 111111111111111 - 11111 = 111111111100000

	if get_v(435) == 0:
		c_year = 2097
		if g_year >= 2097:
			c_year = g_year + 1

	if g_year == c_year and g_month == c_month and g_day == 1 and g_hour == 22 and g_minute >= 0 and g_minute <= 30:
		return 1
	elif ( g_year == c_year and g_month == c_month and g_day == 1 and g_hour == 22 and g_minute > 30):
		return 2
	elif g_month == c_month and g_day == 1 and g_hour >= 19 and g_hour < 22:
		return 3
	elif (g_year > c_year) or ( g_year == c_year and g_month > c_month ) or ( g_year == c_year and g_month == c_month and g_day > 1 ) or ( g_year == c_year and g_month == c_month and g_day == 1 and g_hour >= 23 ):
		if g_day == 1 and g_hour == 22 and g_minute >= 0 and g_minute <= 30:
			return 5
		return 4
	elif g_day == 1 and g_hour == 22 and g_minute >= 0 and g_minute <= 30:
		return 5
	return 0

def council_heartbeat():
	c_time = council_time()
	#1 - between 22:00 and 22:30 on council day
	#2 - between 22:30 and 23:00
	#3 - between 19:00 and 22:00
	#4 - after council events ( >23:00 and beyond that day), but without ordinary council
	#5 - ordinary council time
	#0 - otherwise
	if traders_awol() == 1:
		set_v(435,6)
	if c_time == 5:
		set_v(440,1)
	elif c_time == 1:
		if get_v(435) == 1:
			set_v(435,3)
		elif get_v(435) >= 5 or get_v(435) == 0 and get_v(440) == 0:
			set_v(440,1)
		elif get_v(435) == 4:
			#council_events()
			dummy = 1
	elif c_time == 2:
		if get_v(435) == 3 or get_v(435) == 1:
			set_v(435,4)
			set_v(436,1)
			game.global_flags[432] = 1
			#council_events()
	elif c_time == 3:
		if get_v(435) == 2:
			set_v(435,5)
			set_v(436,5)
			game.global_vars[750] = 3
			game.global_vars[751] = 3
			if (game.party[0].reputation_has(23) == 0 and (game.global_flags[814] == 0 or game.global_flags[815] == 0)):
				game.party[0].reputation_add(23)
	elif (c_time == 0 or c_time == 4):
		if c_time == 0 and game.global_flags[336] == 1 and (get_v(435) == 1 or get_v(435) == 2):
			set_v(435,0)
		elif get_v(435) == 3 or get_v(435) == 4 or (get_v(435) == 1 and c_time == 4):
		##chiefly used for the case where the whole thing played out without you
			if get_v(436) == 0:
				set_v(436,1)
			set_v(435,5)
			if (game.party[0].reputation_has(23) == 0 and (game.global_flags[814] == 0 or game.global_flags[815] == 0)):
				game.party[0].reputation_add(23)
		if get_v(435) == 2 and c_time == 4:
			set_v(435,5)
			set_v(436,5)
			game.global_vars[750] = 3
			game.global_vars[751] = 3
			if (game.party[0].reputation_has(23) == 0 and (game.global_flags[814] == 0 or game.global_flags[815] == 0)):
				game.party[0].reputation_add(23)
		set_v(440,0)
	return

def tptc():
	#time passage till council, in seconds
	#game.fade_and_teleport and game.fade use seconds in their passage of time fields
	if get_v(438) == 13:
		council_month = 1
	else:
		council_month = get_v(438) + 1
	this_month = game.time.time_game_in_months(game.time)
	this_day = game.time.time_game_in_days(game.time)
	this_hour = game.time.time_game_in_hours(game.time)
	this_minute = game.time.time_game_in_minutes(game.time)
	ttw = 0
	if this_minute > 0:
		ttw = ttw + (60-this_minute)*60
		if this_hour == 23:
			this_hour = 0
			if this_day == 28:
				this_day = 1
				if this_month == 13:
					this_month = 1
				else:
					this_month = this_month + 1
			else:
				this_day = this_day + 1
		else:
			this_hour = this_hour + 1
	if this_hour == 23:
		this_hour = 0
		ttw = ttw + 1*(60)*60
		if this_day == 28:
			TED = 1
			this_day = 1
			if this_month == 13:
				this_month = 1
			else:
				this_month = this_month + 1
		else:
			TED = 0
			this_day = this_day + 1
	else:
		TED = 0
	ttw = ttw + (22-this_hour)*60*60
	if (TED == 0):
		ttw = ttw + (29 - this_day)*24*60*60
	return ttw


def traders_awol():
	#this script determines whether the traders fled after being attacked - 
	#the condition being that they surmise they are about to be exposed
	#it uses the time stamps to determine whether they knew this stuff BEFORE you assaulted them
	if game.global_flags[426] == 0:
		return 0
	a = 0
	if (game.quests[15].state == qs_completed and tsc( 427 , 426 ) == 1):
	#laborer spy revealed to Burne
		a = a + 1
	if (game.quests[16].state == qs_completed and tsc( 431 , 426 ) == 1 ):
	#confronted traders about laborer spy
		a = a + 1
	if game.global_flags[444] == 1 or game.global_flags[422] == 1 or (game.global_flags[428] == 1 and (game.global_flags[7] == 1 or (game.time.time_game_in_seconds(game.time) >= get_v(423) + 24*60*60 and game.global_flags[4] == 1) )):
	# Discussed things with badger arrestor, or Confronted Traders about assassination attempt, with either presented hard evidence (Assassin's letter) or Corl was killed too
		a = a + 1
	if (game.quests[17].state == qs_completed and tsc( 430 , 426 ) == 1 ):
	#found out the courier
		a = a + 1
	if a >= 1:
		return 1
	else:
		return 0
