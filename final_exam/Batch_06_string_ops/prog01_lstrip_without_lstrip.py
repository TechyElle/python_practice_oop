class ManualLstrip:
    def run(self):
        user_input = input("Enter string: ")
        counter = 0
        while counter < len(user_input) and user_input[counter] == ' ': counter += 1
        print(f"Result is {user_input[counter:]}")

if __name__ == "__main__":
    ManualLstrip().run()