print "gvie me your input!"
user_input = gets.chomp.downcase!

if user_input.include? "s"
  user_input.gsub!(/s/, "th")
else
  puts "Your string doesn't contain 's'"
end

puts "Your string is: #{user_input}"