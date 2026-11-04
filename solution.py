# You can create any variables here to store state within a run (but not between runs)
import numpy as np
history = []
turns_left = 125

def play(reward: float, lockout: int, t: int, T: int, your_score: float, other_scores: list[tuple[float, bool]], is_locked: bool) -> bool:

	k = 10 * np.log10(t + 1) + 10 * np.log10(T - t + 1) + 10 * np.log10(your_score + 1) + 10 * np.log10(sum(score for score, _ in other_scores) + 1)

	if reward >= k and not is_locked and turns_left > 0: 
		return True
		turns_left -= 1 
	else: 
		return False
