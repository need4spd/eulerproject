
def getNameScore(name)
  alphaList=Array.new
  ('A'..'Z').each {|c| alphaList.push(c)}

    nameScore=0   
     
    name.each_char do
      |c|
      nameScore = nameScore + alphaList.index(c) + 1
      #puts "c=#{c}, score=#{alphaList.index(c)+1}, namescore=#{sum}"
    end
     
    return nameScore
end

namesStr=""
File.open("euler_42_words.txt") do |file|
  while line = file.gets
    namesStr=line
  end
end
 
namesStr = namesStr.gsub(/\"/, "")
namesList = namesStr.split(",")

def isTriangelNumber(n)
  temp_n = n * 2
  start_num = (Math.sqrt(temp_n) - 1).to_i
  
  while (true)
    s = start_num**2 + start_num
    if temp_n == s
      return true
    end
    
    if temp_n < s
      return false
    end
    
    start_num += 1
  end
end
 
cnt_of_result = 0

namesList.each do |name|
  name_score = getNameScore(name)
  
  if isTriangelNumber(name_score)
    cnt_of_result += 1
  end
end

puts cnt_of_result