class ManualIslower:
    def run(self):
        user_input = input("Enter string: ")
        print(f"Result is {user_input.lower() == user_input}")

if __name__ == "__main__":
    ManualIslower().run()