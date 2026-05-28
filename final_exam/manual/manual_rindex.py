class ManualRIndex:
    def solve(self):
        # Get the full text and the substring to locate from the right
        text = input("Enter text: ")
        sub = input("Enter substring to find: ")

        # Slide a window right to left and stop at the first match from the end
        sub_len = len(sub)
        found_at = -1
        for i in range(len(text) - sub_len, -1, -1):
            if text[i:i + sub_len] == sub:
                found_at = i
                break

        # Display the result with the index of the first match from the right, or -1 if not found
        print(f"The substring '{sub}' is found at index: {found_at}")

if __name__ == "__main__":
    ManualRIndex().solve()