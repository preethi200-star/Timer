# Timer
# ⏳ Countdown Timer

A simple Python-based countdown timer that takes input in seconds and displays the remaining time in **MM:SS** format until it reaches zero. At the end, it displays a fun explosion message.

---

## 📜 Features
- Accepts user input for countdown time in seconds.
- Formats time in **minutes:seconds** (`MM:SS`) format.
- Overwrites the timer on the same line for a clean look.
- Pauses for exactly 1 second between updates.
- Handles invalid (non-numeric) input gracefully.
- Displays a final "💥 Fire in the hole!! 💥" message when finished.

---

## 🛠 Requirements
- Python 3.x

---

## ▶️ How to Run
1. **Clone or download** this repository.
2. Open a terminal in the project directory.
3. Run the script:
   ```bash
   python countdown_timer.py
4. Enter the time (in seconds) when prompted.
**💡 Example Output**
Enter the time in seconds: 10
Countdown starting...

00:10
00:09
00:08
...
00:02
00:01
💥 Fire in the hole!! 💥

**📂 Project Structure**
countdown-timer/<br>
│<br>
├── countdown_timer.py  # Main script<br>
└── README.md           # Project documentation <br> 
