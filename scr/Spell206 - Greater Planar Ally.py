from toee import *

from PlanarAllies import *
def OnBeginSpellCast( spell ):
    game.particles( 'sp-conjuration-conjure', spell.caster )

def OnSpellEffect( spell ):
    selection = choose_allies( spell.caster, 6, 18, 3 )

    spell.duration = 10 * spell.caster_level

    game.particles( 'sp-Summon Monster V', spell.target_loc )

    for mon in selection:
        spell.summon_monsters( 1, mon )

    # There seems to be no provision for experience costs, so
    # this is the best we can do.
    spell.caster.award_experience( -500 )

    spell.spell_end( spell.id )
