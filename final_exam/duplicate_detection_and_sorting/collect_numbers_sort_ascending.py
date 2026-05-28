class AscendingSort:
    def main(self):
        nums = []
        while True:
            try:
                num = float(input("Enter a number (or 'q' to quit): "))
                nums.append(num)
            except ValueError:
                break
        nums.sort()
        print("Numbers in ascending order:")
        for num in nums:
            print(num)

if __name__ == "__main__":
    AscendingSort().main()