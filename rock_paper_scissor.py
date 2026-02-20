import random

choices={
    "r":"  rock",
    "p":" paper",
    "s":" scissor",
}



print("Type\nr for rock\np for paper\ns for scissor")

while True:
   userchoice=input("Enter your choice:")
   comp_choice=random.choice(list(choices.keys()))
   if userchoice=="r" or userchoice=="s" or userchoice=="p":
      # condition for same choice
      if(userchoice==comp_choice):
        print("It's a draw, try again!")
        
        #condition for userchoice rock
      elif(userchoice=="r"):
         if(comp_choice=="s"):
            print("You choose rock and computer choose scissor, YOU WIN!")
            break
         else:
            print("You choose rock and computer choose paper, YOU LOSE!")
      
      #condition for paper
      elif(userchoice=="p"):
         if(comp_choice=="r"):
            print("You choose paper and computer choose rock, YOU WIN!")
            break
         else:
            print("You choose paper and computer choose scissor, YOU LOSE!")
      
      #condition for scissor
      elif(userchoice=="s"):
         if(comp_choice=="r"):
            print("You choose scissor and computer choose rock, YOU LOSE!")
         else:
            print("You choose scissor and computer choose paper, YOU WIN!")
            break
      
      else:
         break
            
         

         

   else:
      print("Invalid input, please enter your choice again!")
   


   

