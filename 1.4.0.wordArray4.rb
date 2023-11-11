#text = gets.chomp
text = "Fredolf fred fred fred fredolf"
#puts text

words = text.split
frequencies = Hash.new(0)
words.each  do |word| 
    frequencies[word] += 1
end
frequencies = frequencies.sort_by do |word, count|
    count
end
p frequencies.reverse!