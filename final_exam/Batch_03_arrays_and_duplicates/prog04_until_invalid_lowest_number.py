class FindLowestInputted:
    def run(self):
        nums = []
        while True:
            num = input("Enter number: ")
            if not num.replace('.', '', 1).isdigit(): break
            nums.append(float(num))
        print(f"Result is {min(nums)}")

if __name__ == "__main__":
    FindLowestInputted().run()