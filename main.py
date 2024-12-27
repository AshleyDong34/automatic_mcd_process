# main.py

import requests

def get_user_code():
    """
    Prompts the user to enter a 12-digit code in the format 'xxxx-xxxx-xxxx'.
    Validates the input, capitalizes all alphabetic characters, and splits the code into three parts.

    Returns:
        tuple: A tuple containing the three parts of the code.
    """
    while True:
        code = input("Enter your 12-digit code (format: xxxx-xxxx-xxxx): ").strip()
        
        # Split the code by hyphens
        parts = code.split('-')
        if len(parts) != 3:
            print("Invalid format. Please use the format 'xxxx-xxxx-xxxx'.")
            continue
        
        # Validate each part has exactly 4 characters
        if not all(len(part) == 4 for part in parts):
            print("Each part of the code must have exactly 4 characters.")
            continue
        
        # Capitalize all alphabetic characters in each part
        capitalized_parts = [
            ''.join([char.upper() if char.isalpha() else char for char in part])
            for part in parts
        ]
        
        # Verify the combined length is 12 and alphanumeric
        combined_code = ''.join(capitalized_parts)
        if len(combined_code) != 12 or not combined_code.isalnum():
            print("The code must consist of exactly 12 alphanumeric characters.")
            continue
        
        print("Code accepted.")
        return tuple(capitalized_parts)

def submit_initial_survey(session, code_parts):
    """
    Submits the initial survey form with the provided code parts and fixed price values.

    Args:
        session (requests.Session): The active session object.
        code_parts (tuple): A tuple containing the three parts of the code.

    Returns:
        requests.Response: The HTTP response object.
    """
    survey_url = "https://www.mcdfoodforthoughts.com/"  # Main survey page URL

    # Prepare the payload with form data
    payload = {
        'CN1': code_parts[0],             # First part of the code
        'CN2': code_parts[1],             # Second part of the code
        'CN3': code_parts[2],             # Third part of the code
        'AmountSpent1': '2',               # Fixed value for pounds
        'AmountSpent2': '99',              # Fixed value for pence
        'NextButton': 'Next'               # Simulating the "Next" button press
    }

    # Headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Referer': survey_url
    }

    try:
        # Submit the form via POST request
        response = session.post(survey_url, data=payload, headers=headers)

        if response.status_code == 200:
            print("Initial survey submitted successfully.")
        else:
            print(f"Failed to submit initial survey. Status Code: {response.status_code}")

        return response

    except Exception as e:
        print(f"An error occurred while submitting the initial survey: {e}")
        return None

def answer_question(session, question_name, selected_value):
    """
    Submits an answer to a survey question by selecting a radio button option and pressing "Next".

    Args:
        session (requests.Session): The active session object.
        question_name (str): The 'name' attribute of the radio input field.
        selected_value (str): The 'value' attribute of the selected radio option.

    Returns:
        requests.Response: The HTTP response object.
    """
    survey_url = "https://www.mcdfoodforthoughts.com/"  # Main survey page URL

    # Prepare the payload with form data
    payload = {
        question_name: selected_value,    # Selected option for the question
        'NextButton': 'Next'               # Simulating the "Next" button press
    }

    # Headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Referer': survey_url
    }

    try:
        # Submit the form via POST request
        response = session.post(survey_url, data=payload, headers=headers)

        if response.status_code == 200:
            print(f"Answered question '{question_name}' with value '{selected_value}'.")
        else:
            print(f"Failed to answer question '{question_name}'. Status Code: {response.status_code}")

        return response

    except Exception as e:
        print(f"An error occurred while answering question '{question_name}': {e}")
        return None

def main():
    # Step 1: Get and parse the user code
    code_parts = get_user_code()
    print(f"Code Parts:\nPart 1: {code_parts[0]}\nPart 2: {code_parts[1]}\nPart 3: {code_parts[2]}")

    # Step 2: Initialize a session
    session = requests.Session()

    # Step 3: Submit the initial survey
    response = submit_initial_survey(session, code_parts)

    # Step 4: Answer subsequent questions
    if response:
        # Example list of questions to answer
        # Each tuple contains (question_name, selected_value)
        # Add more questions as needed based on the survey flow
        questions = [
            ('R000005', '2'),  # Select value '2' for question 'R000005'
            # ('NextQuestionName', 'SelectedValue'),
            # Add more as required
        ]

        for question_name, selected_value in questions:
            response = answer_question(session, question_name, selected_value)
            if not response:
                print("Stopping due to an error in answering the question.")
                break

        # Continue adding more questions as needed

if __name__ == "__main__":
    main()
