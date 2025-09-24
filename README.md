# 🕹️ Pygame Platformer

A 2D platformer game built with **Pygame**, featuring:
- Player movement and animations (idle, run, jump, launch).
- Level loading from saved data files.
- Collision with lava, flags, and exit portals.
- Level progression system.

## 📸 Preview
![](https://github.com/Undeacl/Simple-Platformer/blob/main/Preview.gif)

---

## 🚀 Table of Contents
- [Features](#-features)
- [Gameplay](#-gameplay)
- [What I Learned](#-what-i-learned)
- [Credit](#-credit)  

---

## 🚀 Features
- **Smooth Movement & Animations**  
  Includes idle, running, jumping, and launch animations.

- **Level System**  
  Levels are loaded dynamically from `.pkl` files stored in `levels/`.

- **Environment**  
  - Sky background  
  - Lava hazards  
  - Flag checkpoints  
  - Exit portals  

- **Physics & Gameplay**  
  - Jump charging system (hold space to charge higher jumps).  
  - Collision detection with world tiles.  
  - Level reset when completed.  

## 🎮 Gameplay

In this game, the player controls a character navigating through 2D platformer levels filled with obstacles and challenges. The main goal is to reach the level exit while avoiding hazards.  

### Controls
- **Move Left:** `A` or `Left Arrow`  
- **Move Right:** `D` or `Right Arrow`  
- **Jump:** `Spacebar`
- **Charged Jump:** `Hold Spacebar` 

### Mechanics
- **Running & Jumping:** The player can move left and right and perform jumps. The jump height increases the longer the jump button is held, up to a maximum height.  
- **Animations:** Player animations change dynamically based on actions:
  - Idle when standing still
  - Run when moving on the ground
  - Jumping when in the air
  - Special animation when reaching max jump height  
- **Hazards:** Falling into lava will cause the player to die and respawn at their previous checkpoint.  
- **Level Progression:** Reach the exit portal to complete a level. On completion, the player is transported to the next level with their position reset.  
- **Multiple Levels:** The game currently supports multiple levels, each loaded from saved data using `pickle`.  

The game focuses on timing, precise jumping, and navigating through platforming challenges to progress through each level.

## 📝 What I Learned

While building this Pygame project, I gained hands-on experience in several areas of game development:

- **Pygame Basics:** Learned how to initialize Pygame, create a game window, handle the game loop, and control the frame rate using `pygame.time.Clock()`.
- **Player Movement & Animations:** Implemented smooth player movement, including running, jumping, and idle states. Learned to update animations dynamically based on player actions.
- **Collision Detection & Physics:** Managed player-environment interactions, such as jumping mechanics, in-air movement, and detecting when the player falls or reaches the level exit.
- **Tile-Based World:** Learned to construct a grid-based game world using tile sizes and implemented drawing functions for both debugging (grid lines) and game visuals.
- **Level Management:** Used `pickle` to save and load level data, allowing easy level resets and transitions when the player reaches the end of a level.
- **Event Handling:** Gained experience with Pygame events, including detecting key presses/releases and quitting the game.
- **Code Organization:** Practiced modularizing code with functions and external classes (`Player`, `World`), improving readability and maintainability.

Overall, this project strengthened my understanding of 2D game development concepts and how to implement them in Python with Pygame.

## 🎨 Credit
- **Animation and Level System:** Developed with guidance from [YouTube tutorial series](https://www.youtube.com/watch?v=Ongc4EVqRjo&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu) by the original creator.
- **Character Sprites:** [Tiny Hero Sprites](https://craftpix.net/freebies/free-pixel-art-tiny-hero-sprites/) by CraftPix (royalty-free)
- **Portal Sprites:** [Portal](https://actuallykron.itch.io/32x32-2d-portal-asset-pack) by actuallyKron
- **Flag Sprites:** [Flag Animation](https://ankousse26.itch.io/free-flag-with-animation) by ankousse26

