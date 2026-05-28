class ManualLower:
    def solve(self):
        text = input("Enter text: ")
        result = ""
        for char in text:
            if "A" <= char <= "Z":
                result += chr(ord(char) + 32)
            else:
                result += char
        print(f"'{text}' with uppercase letters converted to lowercase is: '{result}'") 

if __name__ == "__main__":
    manual_lower = ManualLower()
    manual_lower.solve()