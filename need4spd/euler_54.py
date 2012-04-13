def is_royal_flush(nums, marks):
  number="".join(str(n) for n in nums)
  mark_set = set(marks)
 
  if number == "1011121314" and len(mark_set) == 1:
    return (True, nums[4])
  else:
    return (False, nums[4])
 
def is_st_flush(nums, marks):
  mark_set = set(marks)
 
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
           
    for k in same_cnt:
        if same_cnt[k] == 4:
            return (True, k)
   
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
        for k in same_cnt:
            if same_cnt[k] == 2 or same_cnt[k] == 3:
                return (True, k)
   
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
    for k in same_cnt:
            if same_cnt[k] == 3:
                return (True, k)
           
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
        for k in same_cnt:
            if same_cnt[k] == 2:
                return (True, k)
    
    return (False, nums[4])
 
def is_one_pair(nums, marks):
    same_cnt = dict()
    nums_set = set(nums)
   
    for n in nums:
        if n in same_cnt:
            same_cnt[n] = same_cnt[n] + 1
        else:
            same_cnt[n] = 1
   
    if len(nums_set) == 4:
        for k in same_cnt:
            if same_cnt[k] == 2:
                return (True, k)
   
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
 
  if get_grade(p1_cards_nums, p1_cards_marks)[0] > get_grade(p2_cards_nums, p2_cards_marks)[0]:
    p1_win_cnt += 1
  elif get_grade(p1_cards_nums, p1_cards_marks)[0] == get_grade(p2_cards_nums, p2_cards_marks)[0]:
    if get_grade(p1_cards_nums, p1_cards_marks)[1] > get_grade(p2_cards_nums, p2_cards_marks)[1]:
        p1_win_cnt += 1
    elif get_grade(p1_cards_nums, p1_cards_marks)[1] == get_grade(p2_cards_nums, p2_cards_marks)[1]:
        for i in range(0, 5):
            if p1_cards_nums[4-i] > p2_cards_nums[4-i]:
                p1_win_cnt += 1
                break
            elif p1_cards_nums[4-i] == p2_cards_nums[4-i]:
                continue
            else:
                p2_win_cnt += 1
                break
    else:
        p2_win_cnt += 1
  else:
    p2_win_cnt += 1
   
print (p1_win_cnt)
print (p2_win_cnt)
print (t)