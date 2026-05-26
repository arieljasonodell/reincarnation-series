from .episode_1 import load_episode_1

__version__ = "0.1.0"

def load_episode(n: int):
    if n == 1:
        return load_episode_1()
    raise ValueError(f"Episode {n} not yet implemented")
