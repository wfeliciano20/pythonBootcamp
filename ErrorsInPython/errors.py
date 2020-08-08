class MyCustomError(Exception):
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code


raise MyCustomError("And error occured", 500)
