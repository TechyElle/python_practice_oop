class ManualIndex:
    def solve(self):
     
        # Get the full text and the substring to locate
        text = input("Enter text: ")
        sub = input("Enter substring to find: ")

        # Slide a window left to right and stop at the first match
        sub_len = len(sub)
        found_at = -1
        for i in range(len(text) - sub_len + 1):
            if text[i:i + sub_len] == sub:
                found_at = i
                break

        # Display the result with the index of the first match, or -1 if not found
        print(f"The substring '{sub}' is found at index: {found_at}")

if __name__ == "__main__":
    indexer = ManualIndex()
    indexer.solve()