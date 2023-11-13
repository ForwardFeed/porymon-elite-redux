'''
this file contains formated string that are a little more complicated
to not clutter the PokemonData class even more
'''

def formatSpeciesInfo(name, species_info):
    formated_species_info = f'''
    [SPECIES_{name.upper()}] =
    {{
        .baseHP        = {species_info["baseStats"]["baseHP"]},
        .baseAttack    = {species_info["baseStats"]["baseAttack"]},
        .baseDefense   = {species_info["baseStats"]["baseDefense"]},
        .baseSpeed     = {species_info["baseStats"]["baseSpeed"]},
        .baseSpAttack  = {species_info["baseStats"]["baseSpAttack"]},
        .baseSpDefense = {species_info["baseStats"]["baseSpDefense"]},
        .type1 = {species_info["types"]["type1"]},
        .type2 = {species_info["types"]["type2"]},
        .catchRate = {species_info["catchRate"]},
        .expYield = {species_info["expYield"]},
        .evYield_HP        = {species_info["evYield"]["evYield_HP"]},
        .evYield_Attack    = {species_info["evYield"]["evYield_Attack"]},
        .evYield_Defense   = {species_info["evYield"]["evYield_Defense"]},
        .evYield_SpAttack  = {species_info["evYield"]["evYield_SpAttack"]},
        .evYield_SpDefense = {species_info["evYield"]["evYield_SpDefense"]},
        .evYield_Speed     = {species_info["evYield"]["evYield_Speed"]},
        .item1 = {species_info["items"]["itemCommon"]},
        .item2 = {species_info["items"]["itemRare"]},
        .genderRatio = {species_info["genderRatio"]},
        .eggCycles = {species_info["eggCycles"]},
        .friendship = {species_info["friendship"]},
        .growthRate = {species_info["growthRate"]},
        .eggGroup1 = {species_info["eggGroups"]["eggGroup1"]},
        .eggGroup2 = {species_info["eggGroups"]["eggGroup2"]},
        .abilities = {{ {species_info["abilities"]["ability1"]}, {species_info["abilities"]["ability2"]}, {species_info["abilities"]["abilityHidden"]} }},
        .innates = {{ {species_info["innates"]["innates1"]}, {species_info["innates"]["innates2"]}, {species_info["innates"]["innates3"]} }},
        .bodyColor = {species_info["bodyColor"]},
        .noFlip = {str(species_info["noFlip"]).upper()},
    }},
'''
    return formated_species_info

def formatPokedexData(name, pokedex_data):
    formated_pokedex_data = f'''
    [NATIONAL_DEX_{name.upper()}] =
    {{
        .categoryName = _("{name.title()}"),
        .height = {pokedex_data["height"]},
        .weight = {pokedex_data["weight"]},
        .description = g{name.title()}PokedexText,
        .pokemonScale = {pokedex_data["pokemonScale"]},
        .pokemonOffset = {pokedex_data["pokemonOffset"]},
        .trainerScale = {pokedex_data["trainerScale"]},
        .trainerOffset = {pokedex_data["trainerOffset"]},
    }},
'''
    return formated_pokedex_data

def formatPokedexText(name, pokedex_text):
    formated_pokedex_text = f'''
const u8 g{name.title()}PokedexText[] = _(
    \"{pokedex_text["descLine1"]}\\n\"
    \"{pokedex_text["descLine2"]}\\n\"
    \"{pokedex_text["descLine3"]}\\n\"
    \"{pokedex_text["descLine4"]}\");
'''
    return formated_pokedex_text

def formatEvolutionData(name, evolution_data):
    if len(evolution_data) <= 0: #safety
        return ""

    formated_evolution_data = f'    [SPECIES_{name.upper()}]'.ljust(36) + '= {' + f'{{{evolution_data[0]["method"]}, {evolution_data[0]["param"]}, {evolution_data[0]["targetSpecies"]}}}'
    if len(evolution_data) > 1:
        formated_evolution_data += ",\n"
    for i in range(1, len(evolution_data)):
        formated_evolution_data += "".ljust(39) + f'{{{evolution_data[i]["method"]}, {evolution_data[i]["param"]}, {evolution_data[i]["targetSpecies"]}}}'
        if i < len(evolution_data)-1:
            formated_evolution_data += ",\n"
    formated_evolution_data += '},\n'
    return formated_evolution_data

def formatLevelUplearnset(name, level_up_learnset):
    formated_level_up_learnset = f'\nstatic const struct LevelUpMove s{name.title()}LevelUpLearnset[]'+' = {\n'
    for move in level_up_learnset:
        formated_level_up_learnset += f'    LEVEL_UP_MOVE({" " if move["level"] < 10 else ""}{move["level"]}, {move["move"]}),\n'
    formated_level_up_learnset += f'    LEVEL_UP_END\n'+'};\n'
    return formated_level_up_learnset

def formatTeachablelearnset(name, teachable_learnset):
    foramted_teachable_learnset = f'    [SPECIES_{name.upper()}]   = TMHM_LEARNSET ('
    noOr = True
    for move in teachable_learnset["TMHM1"]:
        if noOr:
            foramted_teachable_learnset += f'TMHM1({move})'
            noOr = False
        else:
            foramted_teachable_learnset += f'\n                                        | TMHM1({move})'
    foramted_teachable_learnset += ","
    noOr = True
    for move in teachable_learnset["TMHM2"]:
        if noOr:
            foramted_teachable_learnset += f'\n                                          TMHM2({move})'
            noOr = False
        else:
            foramted_teachable_learnset += f'\n                                        | TMHM2({move})'
    foramted_teachable_learnset += "),\n"
    return foramted_teachable_learnset

def formatTutorPointers(name, tutor_pointers):
    formated_tutor_pointer = f'	[SPECIES_{name.upper()}] = ' + "{"
    for pointer in tutor_pointers:
        formated_tutor_pointer += pointer + ","
    formated_tutor_pointer += "},\n";
    return formated_tutor_pointer
    
def formatTutorMoves(name, tutor_moves):
    formated_tutor_moves = f'	[SPECIES_{name.upper()}] = ' + "{\n"
    for move in tutor_moves:
        formated_tutor_moves += f'		{move},\n'
    formated_tutor_moves += "	},\n"
    return formated_tutor_moves
        
    
def formatEgglearnset(name, egg_learnset):
    i = 1
    formated_egg_learnset = f'    egg_moves({name.upper()},'
    for move in egg_learnset:
        formated_egg_learnset += f'\n        {move["move"]}'
        formated_egg_learnset += ',' if i < len(egg_learnset) else ""
        i += 1
    formated_egg_learnset += '),\n'
    return formated_egg_learnset

def formatPicCoordinates(name, pic_coordinates):
    formated_pic_coordinates = f'    [SPECIES_{name.upper()}] =\n' + f'    {{\n        .size = {pic_coordinates["size"]},\n        .y_offset = {" " if pic_coordinates["y_offset"] < 10 else ""}{pic_coordinates["y_offset"]}\n    }},\n'
    return formated_pic_coordinates

def formatFrontPicAnim(name):
    formated_front_pic_anim = f'''static const union AnimCmd sAnim_{name.upper()}_1[] =
{{
    ANIMCMD_FRAME(0, 1),
    ANIMCMD_END,
}};
'''
    return formated_front_pic_anim

def formatFormsTable(name, otherForms):
    if not len(otherForms):
        return ''
    formated_forms_table = f'static const u16 s{otherForms[0].title()}FormSpeciesIdTable[] = ' + "{\n"
    for form in otherForms:
        formated_forms_table += f'    SPECIES_{form.upper()},\n'
    formated_forms_table += "    FORM_SPECIES_END,\n};"
    return formated_forms_table

def formatFormsTablePointers(name, otherForms):
    if not len(otherForms):
        return ''
    formated_forms_table_pointers = f'    [SPECIES_{name.upper()}] = s{otherForms[0].title()}FormSpeciesIdTable,\n'
    return formated_forms_table_pointers
