def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Function to check String Palindrome
def is_palindrome(s):
    return s == s[::-1]

# Anagram check
    str1 = input("\nEnter the first string for Anagram check: ")
    str2 = input("Enter the second string for Anagram check: ")
    if are_anagrams(str1, str2):
        print(f"'{str1}' and '{str2}' are Anagrams.")
    else:
        print(f"'{str1}' and '{str2}' are NOT Anagrams.")