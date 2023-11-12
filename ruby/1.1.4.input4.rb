print "gvie me your input!"
user_input = gets.chomp.downcase!

if user_input.include? "s"
    user_input.gsub (/s/, "th")
end
