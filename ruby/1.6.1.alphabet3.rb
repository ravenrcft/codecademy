def alphabetize(arr, rev=false)
    arr.sort!
    if rev == true
        arr.reverse
    else
        arr
    end
end
numbers = [5, 1, 3, 8]

puts "Sort: #{alphabetize(numbers, true)}"