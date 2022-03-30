import random
#Guess the cases in which this code doesn't work!!
l_dealer = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
l1=[]
l2=[]

def sum_l1(l1):
    l1_sum = l1.copy()
    for i in l1:
        if(i=="K"):
            l1_sum.remove("K")
            l1_sum.append(10)
    for i in l1:
        if(i=="Q"):
            l1_sum.remove("Q")
            l1_sum.append(10)
    for i in l1:
        if(i=="J"):
            l1_sum.remove("J")
            l1_sum.append(10)
    countt = 0
    for i in l1:
        if(i=="A"):
            countt=countt+1
    for i in l1:
        if(i=="A"):
            l1_sum.remove("A")
    
    if(countt>1):
        for t in range(0,countt):
            n = sum(l1_sum)
            if(n==10 or n<10):
                l1_sum.append(11)
            elif(n>10):
                l1_sum.append(1)
              
    elif(countt==1):
        n = sum(l1_sum)
        if(n==10 or n<10):
            l1_sum.append(11)
        elif(n>10):
            l1_sum.append(1)
        
                    
   
    
    '''if(n==10 or n<10):
        l1_sum.append(11)
    elif(n>10 or countt>1):
        l1_sum.append(1)
    print("222:",l1_sum)'''
    
    m = sum(l1_sum)
    return m
            


def hit(l1):
    l1.append(random.choice(l_dealer))
    return l1
 
def stand(a,b):
    if(a<21 and b<21):
        if(a>b):
            print("You win! You stood with a higher score", a," than the dealer",b,"\n")
        elif(a<b):
            print("You lost :( You stood with a lower score", a," than the dealer", b,"\n") 
        else:
            print("Draw. You tied with the dealer.\n")
    elif(a==21):
        print("You win! You got to 21.\n")
    elif(b==21):
        print("You lost :( The dealer got to 21 before you.\n")
    elif(a<21 and b>21):
        print("You win! The dealer went over 21 and busted.\n")

def display():
    print("\n|YOU \n|Cards : ",l1,"\n|Total : ",sum_l1(l1),"\n")
    print("|Dealer \n|Cards : ",l2[0],"?","\n|Total : ??","\n")

def display_final():
    print("\n🆁🅴🆂🆄🅻🆃")
    print("\n|YOU \n|Cards : ",l1,"\n|Total : ",sum_l1(l1),"\n")
    print("|Dealer \n|Cards : ",l2,"\n|Total : ",sum_l1(l2),"\n")
    
    
for i in range(0,1000): 
    s = input("Type BJ to start a new game \nor END to end the game     :")
    if(s=="BJ"):
        l1.append(random.choice(l_dealer))
        #l1.append("A")
        l2.append(random.choice(l_dealer))
        l1.append(random.choice(l_dealer))
        #l1.append("A")
        #l1.append("A")
        l2.append(random.choice(l_dealer))
        display()
        if(sum_l1(l1)==21):
            display_final()
            print("You win! You got to 21.\n")
            l1.clear()
            l2.clear()
            continue
        elif(sum_l1(l2)==21):
            display_final()
            print("You lost :( The dealer got to 21 before you.\n")
            l1.clear()
            l2.clear()
            continue
        elif(sum_l1(l2)==21 and sum_l1(l1)==21):
            display_final()
            print("Oof!! It's a tie\n")
            l1.clear()
            l2.clear()
            continue
        hit_count = 0
        hit_dealer = 0
        for j in range(0,1000):
            choice = input("\nHIT / STAND / END : ")
            if(choice=="HIT"):
                hit_count = hit_count+1
                l1.append(random.choice(l_dealer))
                if(sum_l1(l2)==18 or sum_l1(l2)==19 or sum_l1(l2)==20 or sum_l1(l2)==21 ):
                    l2=l2
                elif(sum_l1(l1)>21):
                    l2=l2
                else:
                    l2.append(random.choice(l_dealer))
                    hit_dealer = hit_dealer + 1
                display()
                if(sum_l1(l1)==21):
                   display_final()
                   print("You win! You got to 21.\n")
                   break
                elif(sum_l1(l1)>21):
                   display_final()
                   print("You lost :( You went over 21 and busted.\n")
                   break
                elif(sum_l1(l2)==21):
                    display_final()
                    print("You lost :( The dealer got to 21 before you.\n")
                    break
                elif(sum_l1(l2)>21 and sum_l1(l1)<21):
                    display_final()
                    print("You win! The dealer went over 21 and busted.\n")
                    break
                elif(hit_count == 3 and sum_l1(l1)<21):
                    print("You win! You took 5 cards without going over 21.\n")
                    break
                
            
            elif(choice=="STAND"):
                if(sum_l1(l2)==18 or sum_l1(l2)==19 or sum_l1(l2)==20 or sum_l1(l2)==21 ):
                    l2=l2
                else:
                    while(sum_l1(l2)!=21 and sum_l1(l2)<17 ):
                        l2.append(random.choice(l_dealer))
                        hit_dealer = hit_dealer + 1
                        if(hit_dealer==3 and sum_l1(l2)<21):
                            print("You Lost :( Dealer took 5 cards without going over 21.\n")
                            continue 
                display_final()
                stand(sum_l1(l1),sum_l1(l2))
                break
        l1.clear()
        l2.clear()
    elif(s=="END"):
        break
    else:
        print("Enter a valid input!!")
        continue
