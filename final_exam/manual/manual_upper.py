class UpperCase:
    def __init__(self):
        self.text = ""

    def ask(self):
        # input string
        self.text = input("Text: ")

    def convert(self):
        # manual shift to upper
        res = ""
        for char in self.text:
            if "a" <= char <= "z":
                res += chr(ord(char) - 32)
            else:
                res += char
        print(res)

if __name__ == "__main__":
    app = UpperCase()
    app.ask()
    app.convert()
