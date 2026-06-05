class ManualCapitalize:
    def run(self):
        user_input = input("Enter string: ")
        print(f"Result is {user_input[:1].upper() + user_input[1:].lower()}")

if __name__ == "__main__":
    ManualCapitalize().run()