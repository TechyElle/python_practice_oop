class ManualTitle:
    def solve(self):
        text = input("Enter text: ")

        word_list = text.split(" ")
        titled = []
        for word in word_list:
            if word:
                titled.append(word[0].upper() + word[1:].lower())
            else:
                titled.append(word)

        print(f"'{text}' with title case is: '{' '.join(titled)}'")

if __name__ == "__main__":
    solution = ManualTitle()
    solution.solve()