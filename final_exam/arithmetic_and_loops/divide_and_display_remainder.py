class Divide:
    def __init__(self):
        self.first_num = 0
        self.second_num = 0

    def main(self):
        # ask inputs
        self.first_num = float(input("Enter first: "))
        self.second_num = float(input("Enter second: "))

        # display remainder
        remainder = self.first_num % self.second_num
        print(f"Remainder is {remainder}")

if __name__ == "__main__":
    Divide().main()