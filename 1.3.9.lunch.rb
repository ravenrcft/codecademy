lunch_order = {
  "Ryan" => "wonton soup",
  "Eric" => "hamburger",
  "Jimmy" => "sandwich",
  "Sasha" => "salad",
  "Cole" => "taco"
}

#puts lunch_order["Ryan"]
lunch_order.each do |x|
   puts "#{x[1]}" 
end