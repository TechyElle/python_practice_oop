class ManualCount:
    def count_substring(self):  
        text = input("Enter text: ")
        sub = input("Enter substring to count: ")
        count = 0
        sub_len = len(sub)
        for i in range(len(text) - sub_len + 1):
            if text[i:i + sub_len] == sub:
                count += 1
        print(f"The substring '{sub}' appears {count} times in the text.")

if __name__ == "__main__":
    counter = ManualCount()
    counter.count_substring()