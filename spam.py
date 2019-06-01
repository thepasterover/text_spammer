# !python3
# Text Spammer - A scrip to spam posts.

"""
WARNING: I'm not responsible for any damage that may happen to your account! Proceed at your own risk!
Author: Boobalan R Shettiyar
Built with: PYTHON 3.6.7
github: github.com/thepasterover
"""

import pyautogui, time

# Ask user for message and spam count
print("WARNING: I'm not responsible for any damage that may happen to your account! Proceed at your own risk!\n" +
	"To be on the safe side make a fake account for sites like FB.")
print("-" * 100)
message = input("Enter a message to spam?: ")
count = input("How many times do you want to spam?: ")
count = int(count)


# Warn the user for more than 50 entered.
if count > 50:
	print("For your own well-being, please enter a number less than 50. ")

else:
	# Give user time to kill the script.
	print("-" * 100)
	print(">>>PRESS CTRL + C TO STOP THE SCRIPT;\n" + 
		"Place the cursor on the text bar, the spamming will start in 10 secs.")

	time.sleep(10)

	# Run the loop according to count given.
	for i in range(count):
		
		pyautogui.typewrite(message)
		pyautogui.press('enter')
		time.sleep(0.5)
	print("Target has been spmmed successfully! Thanks for using have fun!! ;)")