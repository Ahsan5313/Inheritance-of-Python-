class phone:
    def call(self):
        print('You can call')

    def message(self):
        print('You can message')

class samsung(phone):


    def print(self):
        print('You can print')


print(issubclass( samsung, phone))

q = samsung()

q.call()
q.message()
q.print()
