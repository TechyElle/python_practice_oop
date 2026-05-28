class SubtractFromFirst:
    def __init__(self):
        self.nums = []

    def main(self):     
        for i in range(10):
            num = int(input(f"Enter a number {i+1}: "))
            self.nums.append(num)
        if self.nums:
            first_num = self.nums[0]
            for num in self.nums[1:]:
                result = first_num - num
                print(f"{first_num} - {num} = {result}")

if __name__ == "__main__":
    SubtractFromFirst().main()