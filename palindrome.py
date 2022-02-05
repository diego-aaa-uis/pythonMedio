"""palindrome = lambda string: string == string[::-1]

print(palindrome('ana'))"""

"""def palindrome(string):
    return string == string[::-1]
try:
    print(palindrome(1))
except TypeError:
    print("Solo se pueden ingresar strings")"""


def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacía")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False
try:
    print(palindrome(""))
except TypeError:
    print("Solo se pueden ingresar strings")