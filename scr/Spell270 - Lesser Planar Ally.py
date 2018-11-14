from toee import *

from PlanarAllies import *
def OnBeginSpellCast( spell ):
    game.particles( 'sp-conjuration-conjure', spell.caster )

def OnSpellEffect( spell ):
    selection = choose_allies( spell.caster, 3, 6, 1 )

    spell.duration = 10 * spell.caster_level

    game.particles( 'sp-Summon Monster III', spell.target_loc )

    spell.summon_monsters( 1, selection[0] )

    # There seems to be no provision for experience costs, so
    # this is the best we can do.
    spell.caster.award_experience( -100 )

    spell.spell_end( spell.id )
