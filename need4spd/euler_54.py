def is_royal_flush(nums, marks):
  number="".join(str(n) for n in nums)
  mark_set = set(marks)
 
  if number == "1011121314" and len(mark_set) == 1:
    return (True, nums[4])
  else:
    return (False, nums[4])
 
def is_st_flush(nums, marks):
  mark_set = set(marks)
 
  #print (nums)
  for i in range(0,4):
    if not (int(nums[i+1]) - int(nums[i])) == 1:
      return (False, nums[4])
 
  if len(mark_set) == 1:
    return (True, nums[4])
 
  return (False, nums[4])
 
def is_fourcard(nums, marks):
    same_cnt = dict()
   
    for n in nums:
        if n in same_cnt:
            same_cnt[n] = same_cnt[n] + 1
        else:
            same_cnt[n] = 1
           
    for v in same_cnt.values():
        if v == 4:
            return (True, nums[4])
   
    return (False, nums[4])
 
def is_fullhouse(nums, marks):
    same_cnt = dict()
    nums_set = set(nums)
   
    for n in nums:
        if n in same_cnt:
            same_cnt[n] = same_cnt[n] + 1
        else:
            same_cnt[n] = 1
   
    if len(nums_set) == 2:
        for v in same_cnt.values():
            if v == 2 or v == 3:
                return (True, nums[4])
   
    return (False, nums[4])
 
def is_fulsh(nums, marks):
    mark_set = set(marks)
   
    if len(mark_set) == 1:
        return (True, nums[4])
   
    return (False, nums[4])
 
def is_st(nums, marks):
   
    for i in range(0,4):
        if not (int(nums[i+1]) - int(nums[i])) == 1:
            return (False, nums[4])
    return (True, nums[4])
 
def is_three_of_kind(nums, marks):
    same_cnt = dict()
   
    for n in nums:
        if n in same_cnt:
            same_cnt[n] = same_cnt[n] + 1
        else:
            same_cnt[n] = 1
    for v in same_cnt.values():
            if v == 3:
                return (True, nums[4])
           
    return (False, nums[4])
 
def is_two_pairs(nums, marks):
    same_cnt = dict()
    nums_set = set(nums)
   
    for n in nums:
        if n in same_cnt:
            same_cnt[n] = same_cnt[n] + 1
        else:
            same_cnt[n] = 1
   
    if len(nums_set) == 3:
        for v in same_cnt.values():
            if v == 2:
                return (True, nums[4])
   
    return (False, nums[4])
 
def is_one_pair(nums, marks):
    same_cnt = dict()
    nums_set = set(nums)
   
    #print (nums)
    for n in nums:
        if n in same_cnt:
            same_cnt[n] = same_cnt[n] + 1
        else:
            same_cnt[n] = 1
   
    if len(nums_set) == 4:
        for v in same_cnt.values():
            if v == 2:
                return (True, nums[4])
   
    return (False, nums[4])
 
def get_grade(nums, marks):
    if is_royal_flush(nums, marks)[0]:
        return (10, is_royal_flush(nums, marks)[1])
    elif is_st_flush(nums, marks)[0]:
        return (9, is_st_flush(nums, marks)[1])
    elif is_fourcard(nums, marks)[0]:
        return (8, is_fourcard(nums, marks)[1])
    elif is_fullhouse(nums, marks)[0]:
        return (7, is_fullhouse(nums, marks)[1])
    elif is_fulsh(nums, marks)[0]:
        return (6, is_fulsh(nums, marks)[1])
    elif is_st(nums, marks)[0]:
        return (5, is_st(nums, marks)[1])
    elif is_three_of_kind(nums, marks)[0]:
        return (4, is_three_of_kind(nums, marks)[1])
    elif is_two_pairs(nums, marks)[0]:
        return (3, is_two_pairs(nums, marks)[1])
    elif is_one_pair(nums, marks)[0]:
        return (2, is_one_pair(nums, marks)[1])
   
    return (1, 0)
 
#print(is_royal_flush(["10","11","12","13","14"],["D", "D", "D", "D", "D"]))
#print(is_royal_flush(["13","13","6","3","7"],["D", "C", "S", "D", "D"]))
#print(is_st_flush(["9","11","7","6","10"],["C", "D", "C", "D", "C"]))
#print(is_st_flush(["7","8","9","10","11"],["D", "D", "D", "D", "D"]))
#print(is_fourcard(["7","7","7","7","11"],["D", "D", "D", "D", "D"]))
#print(is_fourcard(["7","7","7","11","11"],["D", "D", "D", "D", "D"]))
#print(is_fullhouse(["7","7","7","7","11"],["D", "D", "D", "D", "D"]))
#print(is_fullhouse(["7","7","7","11","11"],["D", "D", "D", "D", "D"]))
#print(is_fulsh(["7","7","7","7","11"],["D", "D", "D", "D", "D"]))
#print(is_fulsh(["7","7","7","11","11"],["D", "C", "S", "D", "D"]))
#print(is_st(["7","8","9","10","11"],["D", "D", "D", "D", "D"]))
#print(is_st(["7","7","7","11","11"],["D", "C", "S", "D", "D"]))
#print(is_three_of_kind(["7","8","9","10","11"],["D", "D", "D", "D", "D"]))
#print(is_three_of_kind(["7","7","7","11","11"],["D", "C", "S", "D", "D"]))
#print(is_two_pairs(["7","7","9","9","11"],["D", "D", "D", "D", "D"]))
#print(is_two_pairs(["7","7","7","11","11"],["D", "C", "S", "D", "D"]))
#print(is_one_pair(["7","7","8","9","11"],["D", "D", "D", "D", "D"]))
#print(is_one_pair(["9","8","13","3","8"],["D", "C", "S", "D", "D"]))
 
poker_txt=open("poker.txt", "r")
mark_num_map = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
 
p1_win_cnt = 0
p2_win_cnt = 0
 
for line in poker_txt:
  line_str = line.rstrip("\n")
  game_str = line_str.split(" ")
 
 
  p1_cards_nums = []
  p1_cards_marks = []
  p2_cards_nums = []
  p2_cards_marks = []
 
  for i in range(0, 5):
    p1_num = game_str[i][0:len(game_str[i])-1]
    p1_mark = game_str[i][len(game_str[i])-1:len(game_str[i])]
   
    if p1_num in mark_num_map:
        p1_num = mark_num_map[p1_num]
   
    p1_cards_nums.append(int(p1_num))
    p1_cards_marks.append(p1_mark)
   
    p2_num = game_str[i+5][0:len(game_str[i+5])-1]
    p2_mark = game_str[i+5][len(game_str[i+5])-1:len(game_str[i+5])]
   
    if p2_num in mark_num_map:
        p2_num = mark_num_map[p2_num]
   
    p2_cards_nums.append(int(p2_num))
    p2_cards_marks.append(p2_mark)
 
  p1_cards_nums.sort()
  p2_cards_nums.sort()
 
  print ("p1_card : {0}, p1_mark : {1}, p2_card : {2}, p2_mark : {3}".format(p1_cards_nums,p1_cards_marks,p2_cards_nums,p2_cards_marks))
  print ("p1_grade : {0}, p2_grade : {1}".format(get_grade(p1_cards_nums, p1_cards_marks),get_grade(p2_cards_nums, p2_cards_marks)))
 
  if get_grade(p1_cards_nums, p1_cards_marks)[0] > get_grade(p2_cards_nums, p2_cards_marks)[0]:
    p1_win_cnt += 1
    print("p1 win 1")
  elif get_grade(p1_cards_nums, p1_cards_marks)[0] == get_grade(p2_cards_nums, p2_cards_marks)[0]:
    if get_grade(p1_cards_nums, p1_cards_marks)[1] > get_grade(p2_cards_nums, p2_cards_marks)[1]:
        p1_win_cnt += 1
        print("p1 win 2")
    elif get_grade(p1_cards_nums, p1_cards_marks)[1] == get_grade(p2_cards_nums, p2_cards_marks)[1]:
        for i in range(0, 5):
            print("a = {0}, b = {1}".format(p1_cards_nums[4-i], p2_cards_nums[4-i]))
            if p1_cards_nums[4-i] > p2_cards_nums[4-i]:
                p1_win_cnt += 1
                print("p1 win 3")
                break
            elif p1_cards_nums[4-i] == p2_cards_nums[4-i]:
                print("continue")
                continue
            else:
                p2_win_cnt += 1
                print("p2 win !!")
                break
    else:
        p2_win_cnt += 1
        print("p2 win 2")
  else:
    p2_win_cnt += 1
    print("p2 win 1")
   
  print("#################################################")
print (p1_win_cnt)
print (p2_win_cnt)