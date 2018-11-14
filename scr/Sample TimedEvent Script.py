##  These three lines are neccessary
from toee import *
import _include
from co8Util.TimedEvent import *
######################

"""Sample script demonstrating calls to timedEventAdd"""

"""Tset(time) sets into motion the spawning of Furnok.
(time) is the time delay, in hours from the time the script 
is run until Furnok spawns.  Jade Empress is spawned and is 
passed as an arguement, along with the party leader, to show 
that the method preserves PyObjHandles across saves and loads. 
The stopFlags that will keep the spawn from firing are 58 (Furnok dead) 
and 51 (caught Furnok cheating).  Note that flag 51 will only 
stop spawn from firing if it is not set, i.e. game.global_flags[51] == 0."""

def Tset(time):
	Jade = game.obj_create(14455, game.party[0].location+5)
	timedEventAdd(spawn, (game.party[0], Jade), time, stopFlags=[58, (51, 0)])

def spawn(attachee, triggerer):
	game.particles( 'Orb-Summon-Fire-Elemental', triggerer )
	game.particles( 'Orb-Summon-Air-Elemental', attachee )
	game.obj_create(14025, triggerer.location-5)



"""nullSet(time) is used to demonstrate how the timedEventAdd 
can be called with no arguements for nullspawn passed and no 
stopFlags.  The only restriction is that the number and type 
of the arguements passed must match the number and type of the 
arguements required by the function passed."""

def nullSet(time):
	timedEventAdd(nullSpawn, (), time)

def nullSpawn():
	game.particles( 'Orb-Summon-Air-Elemental', game.party[0] )
	game.obj_create(14025, game.party[0].location-5)
