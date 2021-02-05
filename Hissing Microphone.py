txt = input()
if len(txt) > 30 or len(txt) < 1:
    print ("Error!")
    txt = input()
else:
    for i in txt:
        if "ss" in txt:
            print("hiss")
            break
        else:
            print('no hiss')
            break
