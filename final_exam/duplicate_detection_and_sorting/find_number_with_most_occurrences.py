class MostOccurrences:
    def main(self):
        nums = []
        while True:
            try:
                num = float(input("Enter a number (or 'q' to quit): "))
                nums.append(num)
            except ValueError:
                break
      
        num_counts = {}
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1
        most_occurred = max(num_counts, key=num_counts.get)
        print(f"The number with the most occurrences is: {most_occurred}")

if __name__ == "__main__":
    MostOccurrences().main()