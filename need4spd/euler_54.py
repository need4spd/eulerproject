def is_royal_flush(cards):
  numbers=[]
  marks=[]
  number=""
  mark=""
  for card in cards:
    numbers.append(card[0:1])
    if not card[1:2] in marks:
      marks.append(card[1:2])
    
    number = number + card[0:1]
    mark = mark + card[1:2]
  
  if number == "10JQKA" and len(marks) == 1:
    return True
  else:
    return False

def is_st_flush(cards):
  numbers=[]
  marks=[]
  number=""
  for card in cards:
    numbers.append(card[0:1])
    if not card[1:2] in marks:
      marks.append(card[1:2])
    
    for i in range(0,3):
      if not (int(numbers[i+1]) - int(numbers[i])) == 1:
        return False
    
    if len(marks) == 1:
      return True
  
  return False
      
print(is_royal_flush(["KD", "KC", "6S", "3D", "7D"]))
print(is_royal_flush(["10C", "JC", "QC", "KC", "AC"]))
"""      
poker_txt=open("poker.txt", "r")

player_1_cards = []
player_2_cards = []

for line in poker_txt:
  line_str = line.rstrip("\n")
  game_str = line_str.split(" ")
  
  for i in range(0, 5):
    player_1_cards.append(game_str[i])
    player_2_cards.append(game_str[i+5])
    
    

print (player_1)
print (player_2)
"""
