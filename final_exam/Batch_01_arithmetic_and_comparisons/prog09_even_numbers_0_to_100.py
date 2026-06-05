class PrintEvenRange:
    def run(self):
        for even_number in range(0, 101, 2):
            print(f"Result is {even_number}")
            
if __name__ == "__main__":
    PrintEvenRange().run()