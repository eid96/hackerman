from attacks.attack1.main import solve_password
from attacks.attack4.main import overflow

if __name__ == "__main__":
    print("Initiating attack..")
    print("Attack one initiated")
    solve_password()
    print("Attack 2 was an sql injection, see report")
    print("Attack 3 was an xss attack, see report")
    print("Initiating attack 4..")
    print("Attack 4 Initiated")
    overflow()
    print("Attack 5 is done with burp terminal, see report")