print "1 or 0?"
user_input = Integer(gets.chomp)

if user_input == 0
    puts "Your answer was 0"
elsif user_input == 1
    puts "Your answer was 1"
else
    puts "Your answer was greater than 1"
end
