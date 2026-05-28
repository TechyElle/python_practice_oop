class IsUpper:
    def solve(self):
        text = input("Enter text: ")
        has_letter = False
        all_upper = True        
        for char in text:
            if char.isalpha():
                has_letter = True
                if "a" <= char <= "z":
                    all_upper = False
        print(f"Is '{text}' all uppercase? {has_letter and all_upper}")
        
if __name__ == "__main__":
    solution = IsUpper()
    solution.solve()
