class Averager:
    def __init__(self):
        self.nums = []

    def main(self):
        # ask inputs
        value = float(input("Enter number: "))
        self.nums.append(value)

        # calculate average
        result = sum(self.nums) / len(self.nums)
        print(f"Average: {result}")

if __name__ == "__main__":
    Averager().main()