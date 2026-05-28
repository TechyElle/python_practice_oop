class NameCounter:
    def __init__(self):
        self.name = ""

    def ask(self):
        # get name from user
        self.name = input("Enter name: ")

    def show(self):
        # print the length
        print(f"Length: {len(self.name)}")

if __name__ == "__main__":
    app = NameCounter()
    app.ask()
    app.show()