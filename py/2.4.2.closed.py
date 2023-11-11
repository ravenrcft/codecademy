with open("text.txt","w") as write_file:
    write_file.write("This should work")

if write_file != write_file.closed:
    write_file.close()

print my_file.closed