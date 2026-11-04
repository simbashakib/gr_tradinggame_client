# You can create any variables here to store state within a run (but not between runs)
import numpy as np



def play(reward: float, lockout: int, t: int, T: int, your_score: float, other_scores: list[tuple[float, bool]], is_locked: bool) -> bool:
    global turns_left



    if [item[1] for item in other_scores].count(False) == 0:
        return True

    current_players = [item[1] for item in other_scores].count(False)

    if current_players < 4:
        return True

    sum_other_scores = sum([item[0] for item in other_scores])

    if sum_other_scores / current_players < 200:
        return True
    



    return False



