class Power:
    def run(self):
        base_number = float(input("Enter base number: "))
        exponent_number = float(input("Enter exponent: "))
        print(f"Result is {base_number ** exponent_number}")
if __name__ == "__main__":
    Power().run()