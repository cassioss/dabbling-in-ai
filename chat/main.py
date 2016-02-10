class Main():
    def __init__(self):
        self.user_input = str()

    def state_machine(self):
        self.input_state()
        while not self.end_state():
            self.reply_state()
            self.input_state()

    def input_state(self):
        self.user_input = str(raw_input('>>> '))

    def reply_state(self):
        self.reply_according_to(self.user_input)

    def end_state(self):
        return self.user_input.lower() == 'quit'

    @staticmethod
    def reply_according_to(user_input):
        if user_input.lower() == 'hi':
            print 'Hello!'
        else:
            print 'ERROR!'


def main():
    main_class = Main()
    main_class.state_machine()


if __name__ == "__main__":
    main()
