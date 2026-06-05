class ManualCount:
    def run(self):
        text_string = input("Enter string: ")
        substring = input("Enter substring: ")
        count = 0
        for index in range(len(text_string) - len(substring) + 1):
            if text_string[index:index + len(substring)] == substring: count += 1
        print(f"Result is {count}")

if __name__ == "__main__":
    ManualCount().run()