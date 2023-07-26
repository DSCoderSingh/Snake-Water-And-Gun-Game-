import random

def swg(comp,mine):
    if(comp=='s' and mine=='g'):
        return True
    elif(comp=='w'and mine=='s'):
        return True
    elif(comp=='g' and mine=='w'):
        return True
    else:
        return False
choice = ('s','w','g')
comp  = random.randint(0, 2)
comp= choice[comp]
mine = input('choose either s ,w ,or g' )

win =swg(comp, mine)
if win:
    print("Congratulations ;you won like a professional")
else:
    print(f"you choose{mine} and the computer choose{comp}")
    print("Oohh! you loose baby ")   