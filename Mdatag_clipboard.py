import time
import sys
import pyperclip

# will paste clipboard into last_pas
last_pas = pyperclip.paste().strip()

# recursion
loop=True

print('Stop the program after completion of clipboard operation')
while loop:
    # runs every 0.1 sec
    time.sleep(0.1)
    paste = pyperclip.paste().strip()
    if paste != last_pas:
        try:
            # encoding="utf-8" To work with linux environment
            # Change clipboard.txt to insert into new file
            # Default paste destination is current working directory
            with open(r'clipboard.txt', 'a',encoding="utf-8") as f:
                # Adds "$" to every new paste
                f.write('{}\n$\n'.format(paste))
                last_pas = paste
        except Exception as e:
            sys.stderr.write("Error occured: {}".format(e))
            break





