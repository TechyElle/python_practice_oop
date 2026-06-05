class DisplayFirstEntryOnly:
    def run(self):
        seen_numbers = []
        for iteration in range(10):
            user_input = input(f"Enter number {iteration + 1}: ")
            if user_input not in seen_numbers:
                print(f"Result is {user_input}")
                seen_numbers.append(user_input)
if __name__ == "__main__":
    DisplayFirstEntryOnly().run()