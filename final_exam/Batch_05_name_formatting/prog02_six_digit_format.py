class FormatSixDigits:
    def run(self): 
        print(f"Result is {input('Enter number: ').zfill(6)}")

if __name__ == "__main__":
    FormatSixDigits().run()