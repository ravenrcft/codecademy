puts "Please give atleast 2 search terms"
text = gets.chomp
puts "Search terms to block"
redact = gets.chomp

words = text.split(" ")

words.each do |word|
    if word == redact
        print "REDACTED "
    else
        print "#{word} "
    end
end