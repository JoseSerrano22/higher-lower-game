import random 
import art
import game_data
import replit

print(art.logo)
points = 0
compareA = game_data.data[random.randint(0,len(game_data.data)-1)]
compareB = game_data.data[random.randint(0,len(game_data.data)-1)]

while True:
  print(f"Current Score: {points}")
  print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}.")
  print(art.vs)
  print(f"Against B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}.\n")

  decision = input("Who has more followers? Type 'A' or 'B' or 'SAME': ").upper()

  if(decision=='A'):
    if compareA['follower_count'] > compareB['follower_count']:
      points += 1
      compareB = game_data.data[random.randint(0,len(game_data.data)-1)]
      replit.clear()
      print(art.logo)
    else:
      print("You lose")
      break

  elif(decision=='B'):
    if compareA['follower_count'] < compareB['follower_count']:
      points += 1
      compareA = compareB
      compareB = game_data.data[random.randint(0,len(game_data.data)-1)]
      replit.clear()
      print(art.logo)
    else:
      print("You lose")
      break
  elif(decision=='SAME'):
    if compareA['follower_count'] == compareB['follower_count']:
      points += 1
      compareB = game_data.data[random.randint(0,len(game_data.data)-1)]
      replit.clear()
      print(art.logo)
    else:
      print("You lose")
      break