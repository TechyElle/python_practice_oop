class CountWordsInInputStatement:
    def count_words(self):
        statement = input("Enter a statement: ")
        word_count = len(statement.split())
        print(f"Word count: {word_count}")

if __name__ == "__main__":
    count_words = CountWordsInInputStatement()
    count_words.count_words()
