class SkipZeroFiveEnding:
    def run(self):
        for counter in range(101):
            if counter % 10 != 0 and counter % 5 != 0:
                print(f"Result is {counter}")
if __name__ == "__main__":
    SkipZeroFiveEnding().run()