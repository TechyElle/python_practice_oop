class CheckDuplicateStatus:
    def run(self):
        nums = []
        while True:
            user_input = input("Enter number: ")
            if not user_input.replace('.', '', 1).isdigit(): break
            if user_input in nums:
                print("Result is Duplicate")
            else:
                print("Result is Unique")
                nums.append(user_input)
if __name__ == "__main__":
    CheckDuplicateStatus().run()