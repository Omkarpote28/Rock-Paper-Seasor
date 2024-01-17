import random
def check(comp,user):
    if comp==user:
        return 0
    if (comp==1 and user==0):
        return -1
    if (comp==2 and user==1):
        return -1
    if (comp==0 and user==2):
        return -1
    return 1
comp=random.randint(0,2)     
user=int(input("0 for Shinju (stone) , 1 for Kami (paper) ,2 for Hasami (Scissors)\n" ))
print("you",user)
print("computer",comp)
score=check(comp,user)
if(score==0):
    print("match draw")
elif(score==1):
    print("match won")  
else:
    print("match lost")   
