class CountWords:
    def run(self): 
        print(f"Result is {len(input('Enter statement: ').split())}")

if __name__ == "__main__":
    CountWords().run()