from toee import *

# Special criteria for certain gods
Demon  = 0
Devil  = 1
Animal = 2
Spider = 3
Earth  = 4
Fire   = 5
Air    = 6
Water  = 7

#    desc   hd  align                   flags
OUTSIDERS = [
    (14110,  3, ALIGNMENT_CHAOTIC_EVIL, []),              # Quasit
    (14111, 15, ALIGNMENT_CHAOTIC_EVIL, [Fire]),          # Noble Salamander
    (14258, 10, ALIGNMENT_CHAOTIC_EVIL, [Demon]),         # Vrock
    (14259, 10, ALIGNMENT_CHAOTIC_EVIL, [Demon]),         # Hezrou
    (14263, 12, ALIGNMENT_CHAOTIC_EVIL, [Demon]),         # Glabrezu
    (14275,  5, ALIGNMENT_NEUTRAL_EVIL, []),              # Drelb
    (14286, 20, ALIGNMENT_CHAOTIC_EVIL, [Demon]),         # Balor
    (14299,  4, ALIGNMENT_TRUE_NEUTRAL, [Animal]),        # Fire Snake
    (14340, 10, ALIGNMENT_LAWFUL_EVIL,  [Fire]),          # Efreet
    (14384,  4, ALIGNMENT_CHAOTIC_EVIL, [Fire]),          # Flamebrother
    (14529,  7, ALIGNMENT_NEUTRAL_GOOD, []),              # Avoral
    (14530, 12, ALIGNMENT_CHAOTIC_EVIL, [Demon, Spider]), # Bebilith
    (14531,  6, ALIGNMENT_CHAOTIC_GOOD, [Air]),           # Bralani
    (14537,  7, ALIGNMENT_CHAOTIC_GOOD, [Air]),           # Djinn
    (14540,  4, ALIGNMENT_LAWFUL_EVIL,  [Animal]),        # Hell Hound
    (14541,  6, ALIGNMENT_LAWFUL_GOOD,  [Animal]),        # Hound Archon
    (14543,  6, ALIGNMENT_TRUE_NEUTRAL, []),              # Jann
    (14544, 12, ALIGNMENT_NEUTRAL_GOOD, [Animal]),        # Leonal
    (14545,  3, ALIGNMENT_TRUE_NEUTRAL, [Air]),           # Air Mephit
    (14546,  3, ALIGNMENT_TRUE_NEUTRAL, [Air, Earth]),    # Dust Mephit
    (14547,  3, ALIGNMENT_TRUE_NEUTRAL, [Earth]),         # Earth Mephit
    (14549,  3, ALIGNMENT_TRUE_NEUTRAL, [Fire]),          # Fire Mephit
    (14550,  3, ALIGNMENT_TRUE_NEUTRAL, [Fire, Earth]),   # Magma Mephit
    (14551,  3, ALIGNMENT_TRUE_NEUTRAL, [Water, Earth]),  # Ooze Mephit
    (14552,  3, ALIGNMENT_TRUE_NEUTRAL, [Earth]),         # Salt Mephit
    (14553,  3, ALIGNMENT_TRUE_NEUTRAL, [Fire, Water]),   # Steam Mephit
    (14554,  3, ALIGNMENT_TRUE_NEUTRAL, [Water]),         # Water Mephit
    (14555,  8, ALIGNMENT_NEUTRAL_EVIL, []),              # Night Hag
    (14563,  9, ALIGNMENT_CHAOTIC_EVIL, [Fire]),          # Salamander
    (14564,  4, ALIGNMENT_NEUTRAL_EVIL, []),              # Shadow Mastiff
    (14565,  3, ALIGNMENT_TRUE_NEUTRAL, []),              # Thoqqua
    (14566,  3, ALIGNMENT_NEUTRAL_EVIL, []),              # Yeth Hound
    (14567,  6, ALIGNMENT_LAWFUL_EVIL,  [Devil]),         # Bearded Devil
    (14568,  8, ALIGNMENT_LAWFUL_EVIL,  [Devil])          # Chain Devil
    ]

FIENDS = [
    (14399,  4, ALIGNMENT_CHAOTIC_EVIL, [Spider]), # Large Spider
    (14402,  3, ALIGNMENT_CHAOTIC_EVIL, [Animal]), # Large Viper
    (14403,  6, ALIGNMENT_CHAOTIC_EVIL, [Animal]), # Huge Viper
    (14404,  3, ALIGNMENT_LAWFUL_EVIL,  [Animal]), # Constrictor
    (14407,  4, ALIGNMENT_NEUTRAL_EVIL, [Animal]), # Dire Bat
    (14408,  6, ALIGNMENT_LAWFUL_EVIL,  [Animal]), # Dire Wolf
    (14472,  6, ALIGNMENT_CHAOTIC_EVIL, []),       # Minotaur
    (14520,  3, ALIGNMENT_LAWFUL_EVIL,  [Animal]), # Boar
    (14521,  7, ALIGNMENT_LAWFUL_EVIL,  [Animal]), # Dire Boar
    (14523, 32, ALIGNMENT_CHAOTIC_EVIL, [Spider]), # Colossal Spider
    (14524, 16, ALIGNMENT_CHAOTIC_EVIL, [Spider]), # Gargantuan Spider
    (14525, 11, ALIGNMENT_LAWFUL_EVIL,  [Animal]), # Giant Constrictor
    (14527,  8, ALIGNMENT_CHAOTIC_EVIL, [Spider])  # Huge Spider
    ]

CELESTIALS = [
    (14394,  3, ALIGNMENT_LAWFUL_GOOD,  [Animal]), # Black Bear
    (14395,  6, ALIGNMENT_LAWFUL_GOOD,  [Animal]), # Brown Bear
    (14503, 12, ALIGNMENT_LAWFUL_GOOD,  [Animal]), # Dire Bear
    (14505,  8, ALIGNMENT_LAWFUL_GOOD,  [Animal]), # Polar Bear
    (14532,  5, ALIGNMENT_LAWFUL_GOOD,  [Animal]), # Bison
    (14534,  4, ALIGNMENT_NEUTRAL_GOOD, [Animal]), # Giant Eagle
    (14535,  4, ALIGNMENT_NEUTRAL_GOOD, [Animal]), # Giant Owl
    (14536, 18, ALIGNMENT_LAWFUL_GOOD,  [Animal])  # Roc
    ]

ELEMENTALS = [
    (14292,  8, ALIGNMENT_TRUE_NEUTRAL, [Air]),
    (14296,  8, ALIGNMENT_TRUE_NEUTRAL, [Earth]),
    (14298,  8, ALIGNMENT_TRUE_NEUTRAL, [Fire]),
    (14302,  8, ALIGNMENT_TRUE_NEUTRAL, [Water]),
    (14376,  2, ALIGNMENT_TRUE_NEUTRAL, [Air]),
    (14377,  2, ALIGNMENT_TRUE_NEUTRAL, [Earth]),
    (14378,  2, ALIGNMENT_TRUE_NEUTRAL, [Fire]),
    (14379,  2, ALIGNMENT_TRUE_NEUTRAL, [Water]),
    (14380,  4, ALIGNMENT_TRUE_NEUTRAL, [Air]),
    (14381,  4, ALIGNMENT_TRUE_NEUTRAL, [Earth]),
    (14382,  4, ALIGNMENT_TRUE_NEUTRAL, [Fire]),
    (14383,  4, ALIGNMENT_TRUE_NEUTRAL, [Water]),
    (14508, 16, ALIGNMENT_TRUE_NEUTRAL, [Air]),
    (14509, 16, ALIGNMENT_TRUE_NEUTRAL, [Earth]),
    (14510, 16, ALIGNMENT_TRUE_NEUTRAL, [Fire]),
    (14511, 16, ALIGNMENT_TRUE_NEUTRAL, [Water])
    ]

ALL_ELEMS = [Air, Earth, Fire, Water]

deity_alignments = { DEITY_HEIRONEOUS:        ([ALIGNMENT_LAWFUL_GOOD],
                                               [],
                                               []),

                     DEITY_ST_CUTHBERT:       ([ALIGNMENT_LAWFUL_GOOD,
                                                ALIGNMENT_LAWFUL_NEUTRAL],
                                               [],
                                               []),

                     DEITY_MORADIN:           ([ALIGNMENT_LAWFUL_GOOD],
                                               [],
                                               [Fire, Earth]),

                     DEITY_LOLTH:             ([ALIGNMENT_CHAOTIC_EVIL,
                                                ALIGNMENT_NEUTRAL_EVIL],
                                               [Spider],
                                               []),

                     DEITY_IUZ:               ([ALIGNMENT_CHAOTIC_EVIL,
                                                ALIGNMENT_NEUTRAL_EVIL],
                                               [],
                                               [Fire]),

                     DEITY_ZUGGTMOY:          ([ALIGNMENT_CHAOTIC_EVIL],
                                               [Demon],
                                               [Water]),

                     DEITY_OLD_FAITH:         ([ALIGNMENT_NEUTRAL_GOOD,
                                                ALIGNMENT_TRUE_NEUTRAL],
                                               [Animal],
                                               [Earth, Water]),

                     DEITY_PELOR:             ([ALIGNMENT_LAWFUL_GOOD,
                                                ALIGNMENT_NEUTRAL_GOOD,
                                                ALIGNMENT_CHAOTIC_GOOD,
                                                ALIGNMENT_TRUE_NEUTRAL],
                                               [],
                                               ALL_ELEMS),

                     DEITY_YONDALLA:          ([ALIGNMENT_LAWFUL_GOOD,
                                                ALIGNMENT_NEUTRAL_GOOD,
                                                ALIGNMENT_TRUE_NEUTRAL],
                                               [],
                                               ALL_ELEMS),

                     DEITY_WEE_JAS:            ([ALIGNMENT_LAWFUL_EVIL,
                                                 ALIGNMENT_LAWFUL_NEUTRAL,
                                                 ALIGNMENT_TRUE_NEUTRAL],
                                                [],
                                                ALL_ELEMS),

                     DEITY_VECNA:              ([ALIGNMENT_LAWFUL_EVIL,
                                                 ALIGNMENT_NEUTRAL_EVIL,
                                                 ALIGNMENT_CHAOTIC_EVIL,
                                                 ALIGNMENT_TRUE_NEUTRAL],
                                                [],
                                                ALL_ELEMS),

                     DEITY_OLIDAMMARA:         ([ALIGNMENT_CHAOTIC_GOOD,
                                                 ALIGNMENT_CHAOTIC_NEUTRAL,
                                                 ALIGNMENT_CHAOTIC_EVIL,
                                                 ALIGNMENT_TRUE_NEUTRAL],
                                                [],
                                                ALL_ELEMS),

                     DEITY_NERULL:             ([ALIGNMENT_LAWFUL_EVIL,
                                                 ALIGNMENT_NEUTRAL_EVIL,
                                                 ALIGNMENT_CHAOTIC_EVIL,
                                                 ALIGNMENT_TRUE_NEUTRAL],
                                                [],
                                                ALL_ELEMS),

                     DEITY_KORD:               ([ALIGNMENT_CHAOTIC_GOOD,
                                                 ALIGNMENT_CHAOTIC_NEUTRAL,
                                                 ALIGNMENT_NEUTRAL_GOOD],
                                                [],
                                                [Air,Water]),

                     DEITY_HEXTOR:             ([ALIGNMENT_LAWFUL_EVIL],
                                                [],
                                                []),

                     DEITY_GRUUMSH:            ([ALIGNMENT_CHAOTIC_EVIL,
                                                 ALIGNMENT_CHAOTIC_NEUTRAL,
                                                 ALIGNMENT_NEUTRAL_EVIL,
                                                 ALIGNMENT_TRUE_NEUTRAL],
                                                [],
                                                ALL_ELEMS),

                     DEITY_GARL_GLITTERGOLD:   ([ALIGNMENT_CHAOTIC_GOOD,
                                                 ALIGNMENT_NEUTRAL_GOOD,
                                                 ALIGNMENT_TRUE_NEUTRAL],
                                                [],
                                                ALL_ELEMS),

                     DEITY_CORELLON_LARETHIAN: ([ALIGNMENT_CHAOTIC_GOOD,
                                                 ALIGNMENT_CHAOTIC_NEUTRAL,
                                                 ALIGNMENT_NEUTRAL_GOOD],
                                                [],
                                                ALL_ELEMS),

                     DEITY_BOCCOB:             ([ALIGNMENT_TRUE_NEUTRAL,
                                                 ALIGNMENT_NEUTRAL_GOOD,
                                                 ALIGNMENT_NEUTRAL_EVIL,
                                                 ALIGNMENT_LAWFUL_EVIL,
                                                 ALIGNMENT_CHAOTIC_GOOD],
                                                [],
                                                ALL_ELEMS),
                     DEITY_OBAD_HAI:           ([ALIGNMENT_TRUE_NEUTRAL,
                                                 ALIGNMENT_NEUTRAL_GOOD,
                                                 ALIGNMENT_NEUTRAL_EVIL,
                                                 ALIGNMENT_CHAOTIC_EVIL,
                                                 ALIGNMENT_LAWFUL_GOOD,
                                                 ALIGNMENT_CHAOTIC_GOOD],
                                                [Animal],
                                                ALL_ELEMS),
                     DEITY_FHARLANGHN:         ([ALIGNMENT_TRUE_NEUTRAL,
                                                 ALIGNMENT_NEUTRAL_GOOD,
                                                 ALIGNMENT_NEUTRAL_EVIL,
                                                 ALIGNMENT_LAWFUL_EVIL,
                                                 ALIGNMENT_CHAOTIC_GOOD],
                                                [],
                                                ALL_ELEMS),
                     DEITY_ERYTHNUL:           ([ALIGNMENT_NEUTRAL_EVIL,
                                                 ALIGNMENT_CHAOTIC_EVIL],
                                                [],
                                                [Fire,Air]),
                     DEITY_EHLONNA:            ([ALIGNMENT_NEUTRAL_GOOD,
                                                 ALIGNMENT_LAWFUL_GOOD,
                                                 ALIGNMENT_CHAOTIC_GOOD],
                                                [Animal],
                                                ALL_ELEMS),
                     DEITY_PROCAN:             ([ALIGNMENT_CHAOTIC_GOOD,
                                                 ALIGNMENT_CHAOTIC_EVIL,
                                                 ALIGNMENT_TRUE_NEUTRAL],
                                                [],
                                                [Water]),
                     DEITY_RALISHAZ:           ([ALIGNMENT_CHAOTIC_GOOD,
                                                 ALIGNMENT_CHAOTIC_EVIL,
                                                 ALIGNMENT_TRUE_NEUTRAL],
                                                [],
                                                [Air]),
                     DEITY_PYREMIUS:           ([ALIGNMENT_NEUTRAL_EVIL,
                                                 ALIGNMENT_CHAOTIC_EVIL,
                                                 ALIGNMENT_LAWFUL_EVIL],
                                                [],
                                                [Fire]),
                     DEITY_NOREBO:             ([ALIGNMENT_CHAOTIC_GOOD,
                                                 ALIGNMENT_CHAOTIC_NEUTRAL,
                                                 ALIGNMENT_TRUE_NEUTRAL],
                                                [],
                                                [AIR]),
                     DEITY_NONE:               ([], [], ALL_ELEMS)
                     }

def fuzz( deity ):
    dice = dice_new( '1d2' )
    dice.bonus = -1

    # make the non-chooseable deities a little more interesting
    if deity == DEITY_ZUGGTMOY or deity == DEITY_IUZ:
        dice.number = 2
    elif deity == DEITY_LOLTH:
        dice.size = 3

    return dice.roll()

def tails( l ):
    if len(l) == 0:
        return []
    else:
        return [(l[0], l)] + tails( l[1:] )

def match( mon_flags, target_flags ):
    accept = 1

    for flag in target_flags:
        if flag not in mon_flags:
            accept = 0

    return accept

def picks( n, max_hd, l ):
    if max_hd <= 0:
        return [[]]
    elif n <= 0:
        # Try to get close to the maximum hit dice limit.
        # We don't want 3 4-hit-dice creatures for the
        # 18-hit-dice greater planar ally.
        if max_hd < 3:
            return [[]]
        else:
            return []
    else:
        return [ rest + [desc]
                 for ((desc, hd), tl) in tails( l )
                 if hd <= max_hd
                 for rest in picks( n-1, max_hd - hd, tl ) ]

def choose_among( critters, max_hd, num ):
    choices = picks( num, max_hd, critters )

    if len(choices) == 0:
        return []

    die = dice_new( '1d1' )
    die.size = len(choices)
    die.bonus = -1

    return choices[die.roll()]

def choose_allies( caster, min_hd, max_hd, max_summon ):
    deity = caster.get_deity()

    percent = dice_new( '1d100' )

    (alignments, specials, elements) = deity_alignments[deity]

    fz = fuzz( deity )

    outsiders = [ (desc, hd)
                  for (desc, hd, align, mon_flags)
                  in OUTSIDERS + FIENDS + CELESTIALS
                  if align in alignments and match(mon_flags, specials) 
                  if min_hd <= hd and hd <= max_hd ]

    elementals = [ (desc, hd)
                   for (desc, hd, align, flags)
                   in ELEMENTALS
                   if flags[0] in elements
                   if min_hd <= hd and hd <= max_hd ]

    num = 1

    p = percent.roll()

    # prefer single summons to multiples
    if p < 11:
        num = min( max_summon, 3 )
    elif p < 31:
        num = min( max_summon, 2 )

    if len(outsiders) == 0:
        available = elementals
    elif len(elementals) == 0:
        available = outsiders
    # prefer outsiders to elementals
    elif percent.roll() < 19:
        available = elementals
    else:
        available = outsiders

    if available == []:
        allies = [14546] # dust mephit, this shouldn't happen
    else:
        allies = choose_among( available, max_hd + fz, num )

    if allies == []:
        allies = choose_among( available, max_hd + fz, max_summon )

    if allies == []:
        allies = choose_among( elementals + outsiders, max_hd, max_summon )

    # if it's still nothing, we have a problem
    if allies == []:
        allies = [14550] # magma mephit this time

    return allies
