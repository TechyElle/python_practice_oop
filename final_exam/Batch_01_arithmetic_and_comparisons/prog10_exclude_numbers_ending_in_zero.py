class PrintExceptEndingZero:
    def run(self):
        for counter in range(101):
            if counter % 10 != 0:
                print(f"Result is {counter}")

if __name__ == "__main__":
    PrintExceptEndingZero().run()