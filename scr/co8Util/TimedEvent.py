"""  LONG DURATION TIMED EVENT METHOD by Cerulean the Blue

You must put these in the global namespace of your function:

import _include
from co8Util.TimedEvent import *

Furthermore "import _include" (without quotes) must be included
in the namespace of utilities.py for the method to function across
saves and loads.  Without this the game will not be able to import
co8Util.TimedEvent at startup and the save will be deemed corrupt.

Call form:

timedEventAdd(<function name>, (<arguments>), <interval>, stopFlags =[<stopFlags>], stopVars=[<stopVars>], stopQuests=[<stopQuests>])

<function name> - Name of the function you want executed after 
the interval.  The function must be in the same module as the 
call, or imported to the module.

<arguments> - The arguments you want passed to the function 
separated by comas, i.e. "attachee, triggerer".

<interval> - An int specifying the delay, in hours, till you 
want the function to execute.

<stopFlags> - OPTIONAL - The flag numbers of global flags that 
should stop the function from executing separated by comas.  
If having the flag set should cause the stop just list the flag 
number.  If not having the flag set should cause the stop, put 
the flag number and 0 separated by a coma in parenthesis, i.e. (85,0).  
Any number of stop flags can be passed.
Example: [58, (51,0)]

<stopVars> - OPTIONAL - Like stopFlags, but for global variables.  
Put each number of the global variable and the value that should 
cause the stop, separated by a coma,in parenthesis.  Any number 
of variables can be listed.
Example:  [(21, 4), (36, 10)]

<stopQuests> - OPTIONAL - Like stopFlags, but for quests.  Put each 
quest number and the quest state that should cause the stop, separated 
by a coma, in parenthesis.  Any number of quests can be listed.
Example:  [(21, qs_accepted), (101, qs_completed), (34, qs_botched)]

Sample Calls:

2 arguments, 10 hour delay, no stops:  
timedEventAdd(spawn, (attachee, triggerer), 10)

No arguments, 100 hour delay, flag stops:  
timedEventAdd(spawn, (), 100, stopFlags=[58, (51,0)])

No arguments, 34 hour delay, variable stops:  
timedEventAdd(spawn, (), 34, stopVars=[(21,4)])

3 arguments, 56 hour delay, flag and quest stops:  
timedEventAdd(give_reward, (x,y,z), 56, stopFlags=[82, 132], stopQuests=[(22, qs_completed)])

Logging has been left in to facilitate debugging.  
The log, named LOG_co8Util.TimedEvent.log, will be 
in the modules folder of the module being run."""


from toee import *
from __main__ import game
import _include
from co8Util.Logger import Logger

logger = Logger(__name__)


def timedEventAdd(eventFunc, args, interval, stopFlags = [], stopVars = [], stopQuests = []):
	eventTime = game.time.time_game_in_hours2(game.time) + interval	# Current elapsed game time plus the time delay, in hours
	sequence(eventFunc, args, eventTime, stopFlags, stopVars, stopQuests)
	return eventTime

def sequence(eventFunc, args, eventTime, stopFlags, stopVars, stopQuests): # time is now the elapsed game time until event happens.
	currentTime = game.time.time_game_in_hours2(game.time) # Current game time in hours when this function is run.
	if eventTime > currentTime: # Not yet time for event to happen.
		if eventTime >= (currentTime + 24): # 24 or more hours until event happens.
			interval = 86400000 # 24 hours in milliseconds
		else: # Less than 24 hours until event happens.
			interval = 3600000 # 1 hour in milliseconds
		game.timevent_add(sequence, (eventFunc, args, eventTime, stopFlags, stopVars, stopQuests), interval) # Sets timed event for determined interval.
		
		## Logging calls
		logger.logme(eventFunc.__name__ + " - Current time: %s" % currentTime)
		logger.logme(eventFunc.__name__ + " - Event time: %s" % eventTime)
		logger.logme(eventFunc.__name__ + " - interval: %s" % interval + "\n")
		##########
			
		return
		
	## This section is for stopping the event.
		
	stopEvent = 0
	if len(stopFlags) != 0: # List of global flags for preventing event exists.
		for flag in stopFlags:
			if type(flag)is int:
				if game.global_flags[flag]:
					stopEvent = 1 # Flag for stopping timed event from happening once it has been initiated.
					logger.logme(eventFunc.__name__ + " - Event stopped by flag: %s" % flag) ## Logging call
			else:
				if game.global_flags[flag[0]] == flag[1]:
					stopEvent = 1 # Flag for stopping timed event from happening once it has been initiated.
					logger.logme(eventFunc.__name__ + " - Event stopped by flag: %s" % flag[0]) ## Logging call
	if len(stopVars) != 0: # List of global vars for preventing event exists.
		for var in stopVars:
			if game.global_vars[var[0]] == var[1]:
				stopEvent = 1 # Flag for stopping timed event from happening once it has been initiated.
				logger.logme(eventFunc.__name__ + " - Event stopped by var: %s" % var[0]) ## Logging call
	if len(stopQuests) != 0: # List of quests for preventing event exists.
		for quest in stopQuests:
			if game.quests[quest[0]].state == quest[1]:
				stopEvent = 1 # Flag for stopping timed event from happening once it has been initiated.
				logger.logme(eventFunc.__name__ + " - Event stopped by quest: %s" % quest[0]) ## Logging call
	if not stopEvent:
		eventFunc(*args)
		logger.logme(eventFunc.__name__ + " - Event executed at: %s" % currentTime + "\n") ## Logging call
	else:
		logger.logme(eventFunc.__name__ + " - Event stopped at: %s" % currentTime + "\n")
	return
	