# Asteroids2

A small clone of the classic arcade game *Asteroids*, written in Python with [pygame](https://www.pygame.org/). You fly a triangular ship in the middle of the screen, shoot incoming asteroids, and try not to get hit.

## Gameplay

- Asteroids drift in from a random screen edge every 0.8 seconds, in three sizes.
- Shooting an asteroid destroys it and splits it into two smaller ones, until it is too small to split.
- If an asteroid touches your ship, the game ends ("Game over!" is printed and the program exits).

## Controls

| Key     | Action                |
|---------|-----------------------|
| `W`     | Move forward          |
| `S`     | Move backward         |
| `A` / `D` | Rotate left / right |
| `Space` | Shoot (0.3 s cooldown) |

## Running

Requires Python 3 and pygame 2.6.1.

```bash
pip install -r requirements.txt
python main.py
```

## Project structure

| File               | Purpose                                                              |
|--------------------|----------------------------------------------------------------------|
| `main.py`          | Game loop, sprite groups, collision checks, drawing                  |
| `constants.py`     | Screen size, player/asteroid/shot tuning values                      |
| `circleshape.py`   | Base sprite class with position, velocity, radius and circle collision |
| `player.py`        | Player ship: input handling, movement, rotation, shooting            |
| `asteroid.py`      | Asteroid sprite and splitting logic                                  |
| `asteroidfield.py` | Spawns asteroids at random screen edges                              |
| `shot.py`          | Projectile fired by the player                                       |

## Design notes

- Everything is a `CircleShape` (a `pygame.sprite.Sprite` subclass), and collisions are simple circle-to-circle distance checks.
- Sprites register themselves into shared groups (`updatable`, `drawable`, `asteroids`, `shots`) via class-level `containers`, set up in `main.py`.
- Movement is frame-rate independent: all updates are scaled by the delta time `dt` from a 60 FPS clock.
