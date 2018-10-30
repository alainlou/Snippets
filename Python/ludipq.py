import sys

flag = False

while True:
    if flag:
        break
    for i in range(3):
        print(i+1)
        sys.stdout.flush()
        x = input()
        if x == "DONE":
            flag = True
            break
