print "What's your first name?"
first_name = gets.chomp.capitalize!

print "What's your last name?"
last_name = gets.chomp.capitalize!

print "What city are you from?"
city = gets.chomp.capitalize!

print "What state are you from?"
state = gets.chomp.upcase!

print "Your name is #{first_name} #{last_name} and you're from #{city}, #{state}!"
