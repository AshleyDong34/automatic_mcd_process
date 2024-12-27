# main.py

def get_user_code():
    """
    Prompts the user to enter a 12-digit code in the format 'xxxx-xxxx-xxxx'.
    Validates the input, capitalizes all alphabetic characters, and splits the code into three parts.
    
    Returns:
        tuple: A tuple containing the three parts of the code.
    """
    while True:
        code = input("Enter your 12-digit code (format: xxxx-xxxx-xxxx): ").strip()
        
        # Check if the code matches the required format
        parts = code.split('-')
        if len(parts) != 3:
            print("Invalid format. Please use the format 'xxxx-xxxx-xxxx'.")
            continue
        
        # Validate each part has exactly 4 characters
        if not all(len(part) == 4 for part in parts):
            print("Each part of the code must have exactly 4 characters.")
            continue
        
        # Capitalize all alphabetic characters
        capitalized_parts = [''.join([char.upper() if char.isalpha() else char for char in part]) for part in parts]
        
        # Combine back to verify the overall length (optional)
        combined_code = ''.join(capitalized_parts)
        if len(combined_code) != 12:
            print("The code must consist of exactly 12 characters (letters or numbers).")
            continue
        
        print("Code accepted.")
        return tuple(capitalized_parts)

# Example usage
if __name__ == "__main__":
    code_part1, code_part2, code_part3 = get_user_code()
    print(f"Code Parts:\nPart 1: {code_part1}\nPart 2: {code_part2}\nPart 3: {code_part3}")
