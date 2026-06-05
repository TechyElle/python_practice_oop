class FindMostFrequentDuplicate:
    def run(self):
        nums = []
        while True:
            user_input = input("Enter number: ")
            if not user_input.replace('.', '', 1).isdigit(): break
            nums.append(user_input)

        most_frequent = max(set(nums), key=nums.count)
        print(f"Result is {most_frequent}")
if __name__ == "__main__":
    FindMostFrequentDuplicate().run()
