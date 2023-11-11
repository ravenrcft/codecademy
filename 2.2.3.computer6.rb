class Computer
    @@users = {}
    def initialize(username, password)
        @username = username
        @password = password
        @files = {}
        @@users[username] = password
    end
    def create(filename)
        time = Time.now
        @files[filename] = time
        puts "A file #{filename} has been created by #{@username} @ #{time}."
    end
    def Computer.get_users
        return @@users
    end
end

my_computer = Computer.new("bob",12345)