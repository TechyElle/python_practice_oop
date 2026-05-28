class DuplicateNumbers:
    def main(self):
        nums = []
        for i in range(10):
            num = int(input(f"Enter a number {i+1}: "))
            nums.append(num)
        
        duplicates = set()
        seen = set()
        
        for num in nums:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        
        if duplicates:
            print("Duplicate numbers entered:", ", ".join(map(str, duplicates)))
        else:
            print("No duplicate numbers entered.")

if __name__ == "__main__":
    DuplicateNumbers().main()