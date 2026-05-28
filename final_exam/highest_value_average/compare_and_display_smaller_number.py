class SmallerNumber:
    def __init__(self):
        self.first_num = 0
        self.second_num = 0

    def main(self):
        # input two numbers
        self.first_num = float(input("First: "))
        self.second_num = float(input("Second: "))

        # find the smaller one
        if self.first_num < self.second_num:
            print(self.first_num)
        elif self.second_num < self.first_num:
            print(self.second_num)
        else:
            print("Equal")
    
if __name__ == "__main__":
    SmallerNumber().main()