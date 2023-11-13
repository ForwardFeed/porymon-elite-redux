
`src/data/pokemon/form_species_table_pointers.h`
[SPECIES_SKARMORY] = sSkarmoryFormSpeciesIdTable,
[SPECIES_SKARMORY_MEGA] = sSkarmoryFormSpeciesIdTable,

`src/data/pokemon/form_species_tables.h`
static const u16 sSkarmoryFormSpeciesIdTable[] = {
    SPECIES_SKARMORY,
    SPECIES_SKARMORY_MEGA,
    FORM_SPECIES_END,
};

BOTH OF THESE FOLLOWING ARE FOR ITEM TRANSFORMATION LIKE ARCEUS OR GENESECT
OR LIKE UNUSUAL TRANSFORMATION
`src/data/pokemon/form_change_table_pointers.h`

`src/data/pokemon/form_change_tables.h`

otherFormes = [
    "SPECIES_NAME"
    "SPECIES_NAME"
]




## POTENTIAL MISS

```
 grep -r "SPECIES_POTATO"

data/pokemon/tmhm_learnsets.h:    [SPECIES_POTATO]   = TMHM_LEARNSET (TMHM1(TM24_THUNDERBOLT)
data/pokemon/tutor_learnsets.h:	[SPECIES_POTATO] = {
data/pokemon/evolution.h:    [SPECIES_POTATO]                = {{EVO_LEVEL, 20, SPECIES_BULBASAUR}},
data/pokemon/level_up_learnset_pointers.h:    [SPECIES_POTATO] = sPotatoLevelUpLearnset,
data/pokemon/base_stats.h:    [SPECIES_POTATO] =
pokemon.c:    [SPECIES_POTATO - 1]        = ANIM_V_SQUISH_AND_BOUNCE,
pokemon_animation.c:    [SPECIES_POTATO]                       = BACK_ANIM_NONE,



 grep -r "SPECIES_SKARMORY_MEGA"
data/text/species_names.h:    [SPECIES_SKARMORY_MEGA]      = _("Skarmory"),
data/pokemon_graphics/front_pic_coordinates.h:    [SPECIES_SKARMORY_MEGA] =
data/pokemon_graphics/back_pic_coordinates.h:    [SPECIES_SKARMORY_MEGA] =
data/pokemon/evolution.h:    [SPECIES_SKARMORY]	 = {{EVO_MEGA_EVOLUTION, ITEM_SKARMORITE,  SPECIES_SKARMORY_MEGA}},
data/pokemon/level_up_learnset_pointers.h:    [SPECIES_SKARMORY_MEGA]     = sSkarmoryLevelUpLearnset,
data/pokemon/form_species_table_pointers.h:    [SPECIES_SKARMORY_MEGA] = sSkarmoryFormSpeciesIdTable,
data/pokemon/base_stats.h:[SPECIES_SKARMORY_MEGA] =
data/pokemon/form_species_tables.h:    SPECIES_SKARMORY_MEGA,
battle_util.c:        case SPECIES_SKARMORY_MEGA:
hall_of_fame.c:                return SPECIES_SKARMORY_MEGA;
battle_interface.c:        case SPECIES_SKARMORY_MEGA:
pokemon.c:    [SPECIES_SKARMORY_MEGA - 1] = NATIONAL_DEX_SKARMORY,



 grep -r "SPECIES_BULBASAUR"
pokemon_jump.c:    { .species = SPECIES_BULBASAUR,  .jumpType = JUMP_TYPE_SLOW, },
data/bard_music/pokemon.h:    [SPECIES_BULBASAUR] = {
data/battle_frontier/battle_frontier_mons.h:        .species = SPECIES_BULBASAUR,
data/contest_opponents.h:        .species = SPECIES_BULBASAUR,

data/text/species_names.h:    [SPECIES_BULBASAUR] = _("Bulbasaur"),
data/trainer_parties.h:    .species = SPECIES_BULBASAUR,

data/wild_encounters.json:                "species": "SPECIES_BULBASAUR"
data/wild_encounters.json:                "species": "SPECIES_BULBASAUR"
data/wild_encounters.json:                "species": "SPECIES_BULBASAUR"
data/wild_encounters.json:                "species": "SPECIES_BULBASAUR"


data/pokemon/evolution.h:    [SPECIES_BULBASAUR]	 = {{EVO_LEVEL, 16, SPECIES_IVYSAUR}},
data/pokemon/evolution.h:    [SPECIES_POTATO]                = {{EVO_LEVEL, 20, SPECIES_BULBASAUR}},
data/pokemon/level_up_learnset_pointers.h:    [SPECIES_BULBASAUR] = sBulbasaurLevelUpLearnset,
data/pokemon/base_stats.h:[SPECIES_BULBASAUR] =
data/easy_chat/easy_chat_group_pokemon2.h:	SPECIES_BULBASAUR,
data/wild_encounters.h:    { 5, 5, SPECIES_BULBASAUR },
data/wild_encounters.h:    { 5, 5, SPECIES_BULBASAUR },
data/wild_encounters.h:    { 5, 5, SPECIES_BULBASAUR },
data/wild_encounters.h:    { 5, 5, SPECIES_BULBASAUR },
mail_data.c:    mail->species = SPECIES_BULBASAUR;
pokemon.c:    [SPECIES_BULBASAUR - 1]     = ANIM_V_JUMPS_H_JUMPS,
starter_choose.c:    SPECIES_BULBASAUR,
pokemon_animation.c:    [SPECIES_BULBASAUR]  = BACK_ANIM_DIP_RIGHT_SIDE,
debug.c:                 SPECIES_BULBASAUR,
```

