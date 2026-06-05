class StripLeadingSpaces:
    def run(self): 
        print(f"Result is {input('Enter fullname: ').lstrip()}.")

if __name__ == "__main__":
    StripLeadingSpaces().run()