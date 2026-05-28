class Power:
    def __init__(self):
        self.base = 0
        self.exponent = 0

    def main(self):
        # input base and power
        self.base = float(input("Base: "))
        self.exponent = float(input("Power: "))

        # show final result
        print(f"Result: {self.base ** self.exponent}")

if __name__ == "__main__":
    Power().main()
