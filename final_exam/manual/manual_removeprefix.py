class ManualRemovePrefix:
    def solve(self):
        # Get the full text and the prefix to strip
        text = input("Enter text: ")
        prefix = input("Enter prefix to remove: ")
        # If the text starts with that prefix, cut it off
        if text.startswith(prefix):
            print(f"'{text}' with prefix '{prefix}' removed is: '{text[len(prefix):]}'")
        else:
            print(f"'{text}' does not start with prefix '{prefix}'")

if __name__ == "__main__":
    solution = ManualRemovePrefix()
    solution.solve()