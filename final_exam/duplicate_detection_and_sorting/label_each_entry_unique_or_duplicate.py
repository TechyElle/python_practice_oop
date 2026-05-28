class UniqueDuplicate:
    def main(self):
        nums = []
        for line in open(0):
            try:
                nums.append(int(line))
            except ValueError:
                break
        for num in nums:
            if nums.count(num) == 1:
                print(f"{num} is unique")
            else:
                print(f"{num} is duplicate")
                
if __name__ == "__main__":
    UniqueDuplicate().main()
