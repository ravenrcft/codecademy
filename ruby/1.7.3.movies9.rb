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
  puts "What movie do you want to update?"
  title = gets.chomp
  if movies[title.to_sym].nil?
    puts "#{title} NOT FOUND! Please add it to the list with 'add'"
  else
    puts "Update the rating (1-5)"
    rating = gets.chomp
    movies[title.to_sym] = rating.to_i
    puts "#{title} has been updated with new rating of #{rating}."
  end
when "display"
  movies.each do |movie, rating|
      puts "#{movie}: #{rating}"
  end
when "delete"
  puts "What movie do you want deleted?"
  title = gets.chomp
  if movie[title.to_sym].nil?
      puts "#{title} is not in the list. Use 'display' to list all known movies"
  else
      movie.delete(title.to_sym)
      puts "#{title} has been removed"
  end
else
    puts "Error! Please use one of following commands: 'add' 'update' 'display' or 'delete'"
end