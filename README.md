# Pookie Glassy Calculator ✨

A delightfully aesthetic, responsive web and CLI calculator blending **3D Pookie Claymorphism** and **Crystal Liquid Glassmorphism** aesthetics.

![Theme Preview](https://img.shields.io/badge/Aesthetic-Pookie%20Clay%20%26%20Crystal%20Glass-ff7599)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen)

---

## 🌸 Features

### 🎀 Aesthetic Design & Themes
- **Pookie Clay** *(Default)*: Soft 3D marshmallow pastel pink chassis, recessed capsule screen, and pillowy squishy keys.
- **Crystal Glass**: Liquid glassmorphism with dynamic specular gloss reflections, crystal jelly buttons, and a glowing purple `=` key.
- **Strawberry Jelly**: Glossy candy-pink jelly buttons with bright highlights.
- **Matcha Latte**: Cozy pastel sage green & cream aesthetic.
- **Lavender Dream**: Soft dreamy lilac glass & pastel violet buttons.
- **Cyber Neon Glass**: Kawaii dark mode with glowing iridescent highlights.

### 💖 Interactive Pookie Animations & Effects
- **Living Kawaii Face**:
  - Natural blinking eyelids.
  - Interactive pupil tracking that follows the mouse cursor.
  - Expressive reactions (happy smiles on numbers, winks on operators, excited expressions on results, surprised on clear).
  - Boopable face: Click the face to boop and make it giggle with sparkle bursts!
- **Squishy 3D Tactile Physics**: Keys press down with realistic depth, bevels, and springy bounce.
- **Sparkle & Confetti Engine**: Floating stars and hearts burst from the calculator upon computing results or booping the face.
- **Synthesized Sound Effects**: Built-in audio synthesizer using Web Audio API (gentle bubble pops, happy chimes, toggleable on/off with 🔊).
- **Ambient Animated Background**: Floating gradient orbs creating an ethereal backdrop.

### ⚡ Calculator Functionality
- Full basic arithmetic: Addition (`+`), Subtraction (`−`), Multiplication (`×`), Division (`÷`).
- Extended tools: Percentage (`%`), Sign toggle (`±`), Backspace (`DEL`), Clear (`C`).
- Precision formatting (no `0.1 + 0.2 = 0.30000000000000004` floating-point issues).
- Full keyboard support: Type numbers and operations directly on your keyboard with visual button feedback.
- One-click copy result to clipboard (`📋`).

---

## 🚀 How to Run

### 1. Web Calculator (`index.html`)
Simply open `index.html` in any web browser, or start a local server:
```bash
python3 -m http.server 3456
```
Then navigate to `http://localhost:3456` in your browser.

### 2. Command Line Calculator (`calculator.py`)
Run interactively:
```bash
python3 calculator.py
```
Or pass calculations directly:
```bash
python3 calculator.py 15 * 4
```
