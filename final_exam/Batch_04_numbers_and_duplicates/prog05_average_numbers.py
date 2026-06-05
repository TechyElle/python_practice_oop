class CalculateAverage:
    def run(self):
        nums = []
        while True:
            user_input = input("Enter number (q to quit): ")
            if not user_input.replace('.', '', 1).isdigit(): break
            nums.append(float(user_input))
        print(f"Result is {sum(nums) / len(nums)}")

if __name__ == "__main__":
    CalculateAverage().run()