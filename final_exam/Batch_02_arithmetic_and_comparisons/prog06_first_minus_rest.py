class SubtractAllFromFirst:
    def run(self):
        nums = [float(input(f"Enter number {i + 1}: ")) 
                for i in range(10)]
        result = nums[0] - sum(nums[1:])
        print(f"Result is {result}")

if __name__ == "__main__":
    SubtractAllFromFirst().run()