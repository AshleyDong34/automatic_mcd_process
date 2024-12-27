# main.py
import requests
from bs4 import BeautifulSoup

def get_user_code():
    while True:
        code = input("Enter your 12-digit McDonald's Food for Thoughts code: ").strip()
        if code.isdigit() and len(code) == 12:
            return code
        else:
            print("Invalid code. Please ensure it is exactly 12 digits.")

# Example usage
if __name__ == "__main__":
    user_code = get_user_code()
    print(f"Code entered: {user_code}")
