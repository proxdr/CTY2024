# 7/3/2024 - Python Activity 1 Adventure Game

# --- story customization ---
name = input("What is the name of the main character of this story?\n") # \n tells python to print what's next on a new line
friend = input("What is the name of the main character's friend?\n")
enemy = input("What is the name of the enemy whom your main character must defeat?\n")
weapon = input("What weapon will you wield on your quest?\n")

# --- begin the story ---
print("\nYou awaken in a dark cave. Your friend " + friend + " sits beside you.")
print(friend + ": You're finally awake! You missed it, " + name + ". The Evil Wizard " + enemy + " has taken over the kingdom!")
print("You grab your " + weapon + " and find a way to exit the cave")

# --- begin decisions ---
print("There are two paths in front of you. The one on the left has a large spikes hanging above. The one on the right has thousands of bats hanging above.")

path = input("Do you go left or right? ")
while path != "left" and path != "right":
    # if you give answer other than left or right, it'll keep asking
    path = input("That was not one of the options. Do you go left or right? ")
  
if path == "left":
    print("As you slowly make your way down the left path, you begin to hear a rumble. You cautiously continue as the spikes above begin to shake")
    print("*CRACK* A spike breaks from the caves ceiling and falls down onto you. You can't save the kingdom with a spike in your head")
    print("YOU LOSE!")
  
elif path == "right":
    print("As you walk down the cavern the bats begin to shake their wings. A few steps later they all take off in unison, flying away. You follow them and find yourself at he exit of the cave.")
    print("And they all lived happily ever after, the end.")


