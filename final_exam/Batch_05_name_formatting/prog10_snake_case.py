class ConvertToSnakeCase:
    def run(self): 
        print(f"Result is {input('Enter fullname: ').lower().replace(' ', '_')}")

if __name__ == "__main__":
    ConvertToSnakeCase().run()
