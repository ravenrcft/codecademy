movies = {
    movie1: 1,
    movie2: 2,
    movie3: 3
}

choice = gets.chomp
puts choice

case choice
when "add"
  title = gets.chomp
  if movies[title.to_sym].nil?
    rating = gets.chomp
    movies[title.to_sym] = rating.to_i
    puts "#{title} has been added with a rating of #{rating}."
  else
    puts "That movie already exists! Its rating is #{movies[title.to_sym]}."
  end
when "update"
  puts "Updated!"
when "display"
  puts "Movies!"
when "delete"
  puts "Deleted!"
else
    puts "Error!"
end