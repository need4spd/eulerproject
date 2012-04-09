def is_royal_flush(cards):
  numbers=[]
  marks=[]
  for card in cards:
    numbers.append(card[0:1])
    if not card[1:2] in mark:
      marks.append(card[1:2])
      
    
    number = number + card[0:1]
    mark = mark + card[1:2]
  
  if number == "10JQKA" and 
    
poker_txt=open("poker.txt", "r")

player_1 = []
player_2 = []

for line in poker_txt:
  line_str = line.rstrip("\n")
  game_str = line_str.split(" ")
  
  for i in range(0, 5):
    player_1.append(game_str[i])
    player_2.append(game_str[i+5])
    
    

print (player_1)
print (player_2)
