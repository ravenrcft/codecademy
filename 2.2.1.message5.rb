class Message
    @@messages_sent = 0
    def initialize(from, to)
        @@messages_sent += 1
        @from = from
        @to = to
    end
end

my_message = Message.new("bob","fred")

class Email < Message
    def initialize(from, to)
        super
    end
end