def passwordCracker(passwords, attempt):

    l = len(attempt)
    composition = ""

    passwords = passwords.split()

    c = 0
    for i in range(l+1):
       
        if attempt[c:i] in passwords:
            composition += attempt[c:i] + " "
            c = i           

    if len(composition.replace(" ", "")) == len(attempt):
        return composition.strip()
    else:
        return "WRONG PASSWORD"


print passwordCracker("ab abcd cd", "abcd")
