class HighestNumber:
    def run(self):
        nums = []
        while True:
            user_input = input("Enter number: ")
            if not user_input.replace('.', '', 1).isdigit(): break
            nums.append(float(user_input))
        print(f"Result is {max(nums)}")

if __name__ == "__main__":
    HighestNumber().run()
