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
  movies[title]
  rating = gets.chomp
  movies[title] = rating
  puts "#{title} has been added with a rating of #{rating}."
when "update"
  puts "Updated!"
when "display"
  puts "Movies!"
when "delete"
  puts "Deleted!"
else
    puts "Error!"
end