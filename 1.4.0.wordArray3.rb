text = gets.chomp
puts text

words = text.split
frequencies = Hash.new(0)
words.each  {|word| frequencies[word] += 1}