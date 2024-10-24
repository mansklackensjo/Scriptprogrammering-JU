def weWish():
    for _ in range(2):
        print("We wish you a Merry Christmas")
    
    print("We wish you a Merry Christmas and a Happy New Year")
    print()

def goodTidings():
    print("Good tidings we bring to you and your kin")
    print("We wish you a Merry Christmas and a Happy New Year")
    print()

def stick(stick):
    if stick == "now":
        for _ in range(2):
            print("Now bring us some figgy pudding")
    
        print("Now bring us some figgy pudding, now bring some out here")
        print() 

    elif stick == "we":
        for _ in range(2):
            print("We won't go until we get some")
    
        print("We won't go until we get some, so bring some out here")
        print() 


weWish()
goodTidings()
stick("now")
goodTidings()
stick("we")
goodTidings()
weWish()
