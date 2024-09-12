def palindrome_checker(word):
    return "Palindrome" if word.replace(" ", "").lower() == word[::-1].replace(" ", "").lower() else "Palindrome not"

print(palindrome_checker(input("Enter your palindrome word: ")))