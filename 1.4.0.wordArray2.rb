text = gets.chomp
puts text

words = text.split
frequencies = Hash.new(0)