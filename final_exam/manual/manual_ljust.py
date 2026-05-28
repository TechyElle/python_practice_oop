class ManualLjust:
    def solve(self):
        text = input("Enter text: ")
        target_width = int(input("Enter total width: "))
        result = text
        while len(result) < target_width:
            result += " "
        print(f"'{text}' left-justified to width {target_width} is: '{result}'")    

if __name__ == "__main__":
    ManualLjust().solve()