from toee import *

def OnBeginSpellCast( spell ):
    game.particles( 'sp-enchantment-conjure', spell.caster )

def OnSpellEffect( spell ):
    target = spell.target_list[0]

    spell.duration = 14400 * spell.caster_level

    if target.obj.is_friendly( spell.caster ):
        # can't dominate friendlies
        game.particles( 'Fizzle', target.obj )
        spell.target_list.remove_target( target.obj )
    elif target.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE,
                                        spell.caster, spell.id ):
        # success
        target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
        game.particles( 'Fizzle', target.obj )
        spell.target_list.remove_target( target.obj )
    else:
        # failure
        target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
        target.partsys_id = game.particles( 'sp-Dominate Person', target.obj )
        target.obj.condition_add_with_args( 'sp-Dominate Person', spell.id,
                                            spell.duration, 0 )

        target.obj.add_to_initiative()
        game.update_combat_ui()

    spell.spell_end( spell.id )
