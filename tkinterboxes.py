from time import sleep

# Show the spinning animation 3 times
print('Downloading...  ', end='', flush=True)
for x in range(10):
    for frame in r'-\|/-\|/':
        # Back up one character then print our next frame in the animation
        print('\b', frame, sep='', end='', flush=True)
        sleep(0.2)

# Back up one character, print a space to erase the spinner, then a newline
# so that the prompt after the program exits isn't on the same line as our
# message
print('\b ')
print()



# chars = ('|' ,'\\', '~', '/', '|', '\\', '~', '/')

#def animation(event):
#    ani_lbl = tk.Label(canvas1, text="Downloading... ")
#    
#    dl_text = print('Downloading...  ', end='', flush=True)
#    for x in range(3):
#        for frame in r'-\|/-\|/':
            # Back up one character then print our next frame in the animation
#            Text('\b', frame, sep='', end='', flush=True)
#            sleep(0.2)
#    print('\b ')
#    return