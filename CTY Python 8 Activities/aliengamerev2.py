import random

print("Welcome to Alien Game! ")
print("You have stolen a UFO to make your way across outer space. ")
print("The aliens want their UFO back and are chasing you down! ")
print("Survive and out run the aliens!")
print ("instructions: ")
print ("1. Try to get 200 miles deep into space tp win! ")
print ("2. If your thirst level gets above 6, you lose! ")
print ("2. If your tierdness level goes above 8, you lose! ")

thirst = 0
traveld = 0
tiredness = 0
alias_traveld = -20
water_left = 3

done = False


alians_moved_7_14 = random.randint(7,14)
max_speed_10_20 = random.randint(10,20)
tierdness1_2 = random.randint(1,2)
alians_moved_6_12 = random.randint(6,12)
you_moved_5_6 = random.randint(5,12)
    
print("a.  drink water")
print("b.  speed to medium")
print("c.  full speed")
print("d.  rest")
print("e.  status check")
print("q.  quit")

x = input("what do you wanna do?:  ")

if x == "e":
    print("thirst", thirst)
    print("water left", water_left)
    print("tierdness", tiredness)
    print("traveld", traveld)
    print("alien miels behind you", traveld-alias_traveld)
    
elif x == "d":
    print("You are rested but the alien have been on the move when you slepted")
    alias_traveld += alians_moved_7_14

elif x == "c":
    print("You went at full speed and went", max_speed_10_20, " miles but you got thirsty by 1 and got tired by", tierdness1_2 , "the aliens moved up", alians_moved_7_14  )
    traveld += max_speed_10_20
    thirst += 1
    alias_traveld += alians_moved_7_14
    tiredness += tierdness1_2

elif x == "b":
    print("you went at medium speed and went", you_moved_5_6 ," miels but you got thirsty by 0.5 and got tiered by 1", "and the aliens moved up", alians_moved_6_12)
    traveld += you_moved_5_6
    thirst += 0.5
    alias_traveld += alians_moved_6_12
    tiredness += 1

elif x == "a":
    if water_left >= 1 :
        print("you drank water and now your amount of water is", water_left, "but your thirst returned to 0")
    else:
        print("you will die from lack of water, such a bad way to die by thr way if you cant do common sense error")
        water_left -= 1
        thirst=0


#thirst
if thirst >= 4 and thirst <= 6:
    print ("you are thirsty")
    
else:
    print("you did not care about your self and died from thirst and the alians got the UFO")
    done = True
#tiredness

if tiredness >= 5 and tiredness <= 8:
    print ("you feel ried")
    
else:
    print("you fell asleep and the alians got the UFO back and now you are in prison")
    done = True
#alien dist

if traveld - alias_traveld < 15:
    print("the alians are less then 15 miels back")



#game quit
if x == "q":
    print("You quit the game.")
    done = True

#wincon

if traveld > 200:
    print("congrats you won! I truly thoght you would die but you proved me wrong! Now YOU can be the first human to travl space freely!")
    done = True
    
        
#backup
else: 
    print("Invalid")