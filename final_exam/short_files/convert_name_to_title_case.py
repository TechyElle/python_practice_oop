class ConvertNameToTitleCase:
    def run(self):
        name = input("Enter your name: ")
        title_case_name = name.title()
        print(f"Your name in title case is: {title_case_name}")

if __name__ == "__main__":
    converter = ConvertNameToTitleCase()
    converter.run()
