class FirstOccurrence:
    def main(self):
        nums = []
        for i in range(10):
            num = int(input(f"Enter a number {i+1}: "))
            if num not in nums:
                nums.append(num)
        for num in nums:
            print(num)

if __name__ == "__main__":
    FirstOccurrence().main()
