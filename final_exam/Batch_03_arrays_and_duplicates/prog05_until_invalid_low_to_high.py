class SortInputtedLowestToHighest:
    def run(self):
        number_list = []
        while True:
            user_input = input("Enter number: ")
            if not user_input.replace('.', '', 1).isdigit(): break
            number_list.append(float(user_input))
        number_list.sort()
        print(f"Result is {number_list}")

if __name__ == "__main__":
    SortInputtedLowestToHighest().run()