class ManualRemoveSuffix:
    def solve(self):
        # Get the full text and the suffix to strip
        text = input("Enter text: ")
        suffix = input("Enter suffix to remove: ")

        # Store suffix length then check and remove from the right
        suffix_len = len(suffix)
        if suffix and text[-suffix_len:] == suffix:
            print(f"'{text}' with suffix '{suffix}' removed is: '{text[:-suffix_len]}'")
        else:
            print(f"'{text}' does not end with '{suffix}'")

if __name__ == "__main__":
    ManualRemoveSuffix().solve()