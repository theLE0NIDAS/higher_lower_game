import art
import game_data
import random
from replit import clear

def selector():
  p=random.choice(game_data.data)
  selection=""
  for n in p:
    if n=="name":
      selection=selection + p[n] + ", "
    elif n=="description":
      selection= selection + "a " +  p[n] + ", "
    elif n=="country":
      selection= selection + "from " + p[n] + " "
    elif n=="follower_count":
      followers=p[n]
  details=[selection,followers]
  return details

def compare_followers(s1,s2):
  print(s1)
  print(s2)
  if s1>s2:
    return s1
  else:
    return s2

play="yes"
score=0
while play=="yes":
  clear()
  print(art.logo)
  
  selection1=selector()
  selection2=selector()
  if selection1!=selection2:  
    
    if score>0:
      print(f"You made a correct choice, your current score is: {score}")
    print(f"Compare A: {selection1[0]}")
    print(art.vs)
    print(f"Compare B: {selection2[0]}")
    trial=input("Enter you choice, which one has greater number of followers? 'A' or 'B': ")
    
    if trial=="A":
      num_foll=selection1[1]
    else:
      num_foll=selection2[1]
    
    big=compare_followers(selection1[1], selection2[1])
    
    if(big==num_foll):
      score+=1
    else:
      clear()
      print("You made an incorrect choice")
      print(f"Your final score: {score}")
      play="no"
      
