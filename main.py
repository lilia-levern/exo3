"""
This module
"""



def isprime(p):
    """
    this function takes an int and returns True if it is prime

    Args:
        p: int
    Returns:
        boolean
    """
    premier=True
    if p in (0,1):
        premier=False

    for d in range(2,p):
        if p%d==0:
            premier=False
            break
    return premier






#### Fonction principale


def main():

    """
    description renvoyée

    """

    is_five_prime = isprime(5)

    print(is_five_prime)

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
