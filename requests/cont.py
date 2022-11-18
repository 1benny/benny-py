from time import sleep

def write_file():
    with open("write_out.txt", "w") as f:
        f.write(ans)
        f.close()
    return

def read_file():
    with open("write_out.txt", "r") as f:
        print(f.read())
        f.close()
    return




ans = "hey it wrote out. nice!"

key_entry = key_entry.get()


def write_key():
    global ans
    with open("write_out.txt", "w") as f:
        f.write(ans)
        f.close()
    return


def read_key():
    global keyval
    with open("write_out.txt", "r") as f:
        keyval = f.read()
        f.close()
    return

write_key()

read_key()

print(keyval)