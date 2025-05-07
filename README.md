#  Ultimate Quiz Showdown

A modular, text-based Python quiz game with difficulty scaling, timed scoring, and multiple categories. Designed for educational use and built according to a structured project plan.

---

##  Project Overview

This program allows players to select a quiz category (Math, Science, or History), answer questions of increasing difficulty, and receive scores based on both accuracy and response time. Final rankings are saved in a text file with a timestamp for each session.

---

##  Features

- Single or multi-player support (text-based)
- 3 categories: Math, Science, and History
- Easy, Medium, Hard questions per round
- Timed bonus/malus scoring:
  - +5 bonus if answered in ≤5 sec
  - -5 penalty if answered in >10 sec
- Final rankings sorted and displayed
- Scores saved to `top_scores.txt` with session metadata
- Modular code with full inline documentation
- External data file (`quiz_data.py`) for clean separation


Open a terminal in the project folder and run:

```bash
python quiz_game.py