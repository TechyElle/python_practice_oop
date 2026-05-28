class UniqueNumbers:
    def main(self):
        unique_nums = []
        for i in range(10):
                num = int(input(f"Enter a number {i+1}: "))
        if num not in unique_nums:
                unique_nums.append(num)
        print("Unique numbers entered:")
        for num in unique_nums:
            print(num)

if __name__ == "__main__":
    UniqueNumbers().main()