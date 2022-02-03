# Wordle Cheater
Quick script to help cheat wordle puzzles with minimal extra input.

## Installation
```
pip install wordfreq
pip install keyboard
```
Word list is from [here](https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b)

## Usage
To start, in the terminal run 
```
python main.py
```
The script will automatically detect keyboard input as you play wordle. When you press the Enter key to submit a word, the script will prompt you to type in the response from wordle. For each letter in order, press the following:
```
GREEN (correct letter and position): Press 1
YELLOW (correct letter wrong position): Press 2
GREY (wrong letter wrong position): Press Space
```
and submit the entry by pressing '3'. You can also press 3 before inputting all 5 responses to restart.

Pressing Escape will exit the script

## Notes
As recommendations are given based on the most common English word that is still valid, it is recommended to use some opener to start of the puzzle before using the recommendations (e.g. ADIEU then STORY).