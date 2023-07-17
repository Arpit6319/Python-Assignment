class InputError(Exception):
    def _init_(self, message):
        self.message = message
        super()._init_(self.message)

num = None
try:
    num = int(input("Enter num: "))
except ValueError:
    try:
        if num is None:
            raise InputError("Invalid input: Wrong datatype")
    except InputError as e:
        print(e.message)