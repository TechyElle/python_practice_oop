class RemoveLeadingSpaces:
    def remove_leading_spaces(self):
        full_name = input("Enter your full name: ")
        print(f"Your name with leading spaces removed is: '{full_name.lstrip()}'")
        
if __name__ == "__main__":
    solution = RemoveLeadingSpaces()
    solution.remove_leading_spaces()    
