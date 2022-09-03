import pyautogui
import time


time.sleep(5)

with open("./song.txt") as file:

	wordList = file.read().split(" ")


for word in wordList:
	word = word.replace("\n", "")
	pyautogui.typewrite(word)
	pyautogui.press("enter")



