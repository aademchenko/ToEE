from toee import *

from PlanarAllies import *

def OnBeginSpellCast( spell ):
    game.particles( 'sp-conjuration-conjure', spell.caster )

def OnSpellEffect( spell ):
    spell.duration = 10 * spell.caster_level

    selection = choose_allies( spell.caster, 4, 12, 2 )

    game.particles( 'sp-Summon Monster IV', spell.target_loc )

    for n in selection:
        spell.summon_monsters( 1, n )

    spell.caster.award_experience( -250 )

    spell.spell_end( spell.id )
