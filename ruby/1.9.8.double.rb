def double(dub)
    yield(dub)
end

double(2) { |n| n * 2 }