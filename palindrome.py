def isPalindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome.
    """
    s = s.replace(" ", "").lower().strip()
    return s == s[::-1]

def isPrime(n: int) -> bool:
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def run() -> None:
    """
    Runs the program.
    """
    print(isPalindrome("ANA"))
    
if __name__ == "__main__":
    run()