class ManualCenter:
    def run(self):
        text_string = input("Enter string: ")
        total_length = int(input("Enter length: "))
        padding = max(0, total_length - len(text_string))
        left_padding = padding // 2
        print(f"Result is {' ' * left_padding + text_string + ' ' * (padding - left_padding)}")

if __name__ == "__main__":
    ManualCenter().run()
    