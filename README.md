# COMP9001-FinalProject
# High Diving Game 🕹️

A 2D arcade-style High Diving Game built using Python and the **Pygame** framework. This project was developed as the Final Project. It features custom physics for high diving, an interactive multi-stage platform animation, fluid aerial rotation mechanics, dynamic background cycles, and automated unit testing.

---

## 📂 Project Structure

```text
COMP9001-FinalProject/
│
├── Main.py            # Game entry point and core rendering loop
├── Diver.py           # Diver class handles physics, gravity, and states
├── Platform.py        # Platform class handles the multi-stage bending animation
├── Splash.py          # Splash class handles water entry visual effects
├── settings.py        # Configuration file for screen size, FPS, paths, and constants
├── README.md          # Project documentation (this file)
└── pictures/          # Asset folder containing all game sprites and graphics
    ├── background.png, background2.png, background3.png
    ├── stand.png, ready.png, jump.png
    ├── stage1.png, stage2.png, stage3.png
    └── waterSplash1.png, waterSplash2.png, waterSplash3.png
```
## 🎮 Game Controls
【SPACE (Spacebar)】 on Ground: Transition from standing pose to ready pose.

【SPACE (Spacebar)】 on Platform: Execute the formal jump and trigger the diving board animation.

【HOLD SPACE】 in Air: Continuously rotate and perform flips while falling.

【R Key】 after Water Entry: Instantly restart the game and try for a better jump!

## 📦 Installation & Execution
Prerequisites
Make sure you have Python installed on your local computer. This project relies on the Pygame package.
# 1. Clone the Repository
open in terminal: 
```
git clone [https://github.com/zzpSimon/COMP9001-FinalProject.git]
cd COMP9001-FinalProject
```
# 2. Install Dependencies
Install the required graphics library via pip:
```
pip install pygame
```
# 3. Run the Game
Execute the main entry script to play the game:
```
python Main.py
```

## FINALLY
Enjoy the game, hopefully this will bring some joy for u.
