class ConvertToPascalCase:
    def run(self): 
        print(f"Result is {''.join(word.capitalize() for word in input('Enter fullname: ').split())}")

if __name__ == "__main__":
    ConvertToPascalCase().run()