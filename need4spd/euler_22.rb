
def getNameAndIndex(dataList)
            
    for index in (0..dataList.length-1)
        name = dataList[index]
        
        puts "name=#{name}, index=#{index}"
        
        yield name, index+1
    end
end

alphaList=Array.new
('A'..'Z').each {|c| alphaList.push(c)}

def getNameScore(name)
    sum=0    
    
    name.each_char do
      |c| sum = 1
      puts "c=#{c}, score=#{alphaList.index(c)+1}, namescore=#{sum}"
    end
    
    return sum
end

namesStr=""
File.open("names.txt") do |file|
  while line = file.gets
    namesStr=line
  end
end

namesStr = namesStr.gsub(/\"/, "")
namesList = namesStr.split(",")
namesList.sort!

puts namesList

totalScore = 0

getNameAndIndex(namesList) do
  |name, index|
  
  nameScore = 0
  name.rstrip!
  name.each_char do
      |c|
      puts "c : #{c}, name : #{name}"      
      nameScore = nameScore + alphaList.index(c) + 1
      puts "total score : #{totalScore}, al : #{alphaList.index(c)}, c : #{c}"
  end
  totalScore = totalScore + (nameScore * index)
  puts "total score : #{totalScore}, name score : #{nameScore}, name index : #{index}"
end

puts "total score : #{totalScore}"