import random
gnum = random.randint(1,10)
win = True
count =0 
while win != False:
    count = count + 1
    pnum = int(input("Enter your choice = "))
    if pnum > gnum:
        print("To high Guess some Less")
    elif pnum < gnum:
        print("To low Guess some high")
    elif pnum == gnum:
        print("You Win!!! in ",count," Time")
        win = False
