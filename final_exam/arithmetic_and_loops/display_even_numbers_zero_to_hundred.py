class EvenNumbers:
    def __init__(self):
        self.start = 0
        self.end = 100

    def main(self):
        even_nums = []
        for num in range(self.start, self.end + 1):
            if num % 2 == 0:
                even_nums.append(num)
                print(f"Even number: {num}")
    
if __name__ == "__main__":
    even_nums = EvenNumbers()
    even_nums.main()