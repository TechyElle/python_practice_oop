class OddNumber:
    def __init__(self):
        self.start = 0
        self.end = 100

    def main(self):
        # Find odd ones and display
        for num in range(self.start, self.end + 1):
            if num % 2 != 0:
                print(f"{num} is an odd number.")

if __name__ == "__main__":
    OddNumber().main()