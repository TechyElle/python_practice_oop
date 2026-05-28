class ReverseCaseOfEachCharacter:
    def reverse_case(self):
        full_name = input("Enter your full name: ")
        print(f"Your name with the case of each character reversed is: {full_name.swapcase()}") 

if __name__ == "__main__":
    reverse_case = ReverseCaseOfEachCharacter()
    reverse_case.reverse_case()