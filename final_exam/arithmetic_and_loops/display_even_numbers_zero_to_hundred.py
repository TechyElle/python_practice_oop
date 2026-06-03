class EvenNumbers:
    def __init__(self, start=0, end=100):
        self.start = start
        self.end = end

    def run(self):
        for num in range(self.start, self.end + 1):
            if num % 2 == 0:
                print(f"{num} is an even number.")
    
if __name__ == "__main__":
    EvenNumbers().run()
    
