class CheckEquality:
    def run(self):
        number_one = float(input("Enter first number: "))
        number_two = float(input("Enter second number: "))
        if number_one == number_two:
            print("Equal")
        else:
            print("Not Equal")
if __name__ == "__main__":
    CheckEquality().run()
