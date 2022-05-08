YEAR_KEYS = {"14": "140052", "13": "130034", "12": "120002"}
PLAYERS_BASE_URL = "https://sofifa.com/players?set=true&col=oa&sort=desc&showCol%5B%5D=pi&showCol%5B%5D=ae&showCol%5B%5D=hi&showCol%5B%5D=wi&showCol%5B%5D=pf&showCol%5B%5D=oa&showCol%5B%5D=pt&showCol%5B%5D=bo&showCol%5B%5D=bp&showCol%5B%5D=gu&showCol%5B%5D=jt&showCol%5B%5D=le&showCol%5B%5D=vl&showCol%5B%5D=wg&showCol%5B%5D=rc&showCol%5B%5D=ta&showCol%5B%5D=cr&showCol%5B%5D=fi&showCol%5B%5D=he&showCol%5B%5D=sh&showCol%5B%5D=vo&showCol%5B%5D=ts&showCol%5B%5D=dr&showCol%5B%5D=cu&showCol%5B%5D=fr&showCol%5B%5D=lo&showCol%5B%5D=bl&showCol%5B%5D=to&showCol%5B%5D=ac&showCol%5B%5D=sp&showCol%5B%5D=ag&showCol%5B%5D=re&showCol%5B%5D=ba&showCol%5B%5D=tp&showCol%5B%5D=so&showCol%5B%5D=ju&showCol%5B%5D=st&showCol%5B%5D=sr&showCol%5B%5D=ln&showCol%5B%5D=te&showCol%5B%5D=ar&showCol%5B%5D=in&showCol%5B%5D=po&showCol%5B%5D=vi&showCol%5B%5D=pe&showCol%5B%5D=cm&showCol%5B%5D=td&showCol%5B%5D=ma&showCol%5B%5D=sa&showCol%5B%5D=sl&showCol%5B%5D=tg&showCol%5B%5D=gd&showCol%5B%5D=gh&showCol%5B%5D=gk&showCol%5B%5D=gp&showCol%5B%5D=gr&showCol%5B%5D=tt&showCol%5B%5D=bs&showCol%5B%5D=wk&showCol%5B%5D=sk&showCol%5B%5D=aw&showCol%5B%5D=dw&showCol%5B%5D=ir&showCol%5B%5D=pac&showCol%5B%5D=sho&showCol%5B%5D=pas&showCol%5B%5D=dri&showCol%5B%5D=def&showCol%5B%5D=phy"

COLUMNS_REMAPPING = {
    "weight": "weight_kg",
    "crossing": "attacking_crossing",
    "finishing": "attacking_finishing",
    "heading_accuracy": "attacking_heading_accuracy",
    "short_passing": "attacking_short_passing",
    "volleys": "attacking_volleys",
    "dribbling": "skill_dribbling",
    "curve": "skill_curve",
    "fk_accuracy": "skill_fk_accuracy",
    "long_passing": "skill_long_passing",
    "ball_control": "skill_ball_control",
    "acceleration": "movement_acceleration",
    "sprint_speed": "movement_sprint_speed",
    "agility": "movement_agility",
    "reactions": "movement_reactions",
    "balance": "movement_balance",
    "shot_power": "power_shot_power",
    "jumping": "power_jumping",
    "stamina": "power_stamina",
    "strength": "power_strength",
    "long_shots": "power_long_shots",
    "aggression": "mentality_aggression",
    "interceptions": "mentality_interceptions",
    "positioning": "mentality_positioning",
    "vision": "mentality_vision",
    "penalties": "mentality_penalties",
    "composure": "mentality_composure",
    "marking": "defending_marking",
    "standing_tackle": "defending_standing_tackle",
    "sliding_tackle": "defending_sliding_tackle",
    "gk_diving": "goalkeeping_diving",
    "gk_handling": "goalkeeping_handling",
    "gk_positioning": "goalkeeping_positioning",
    "gk_reflexes": "goalkeeping_reflexes",
    "w/f": "weak_foot",
    "a/w": "work_rate_attack",
    "d/w": "work_rate_defense",
}


def clean_string(input_str: str) -> str:
    return input_str.strip().lower().replace(" ", "_")


def rename_columns(columns: list) -> list:
    ret = []
    for col_name in columns:
        if col_name in COLUMNS_REMAPPING.keys():
            ret.append(COLUMNS_REMAPPING[col_name])
        else:
            ret.append(col_name)
    return ret
