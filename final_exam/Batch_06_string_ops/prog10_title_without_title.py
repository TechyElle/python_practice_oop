class ManualTitle:
    def run(self):
        user_input = input("Enter string: ")
        output = ' '.join(word.capitalize() for word in user_input.split())
        print(f"Result is {output}")

if __name__ == "__main__":
    ManualTitle().run()