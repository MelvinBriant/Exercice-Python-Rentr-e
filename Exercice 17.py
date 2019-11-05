def estUnPalindrome(mot) :
    for i in range(len(mot)):
        if mot[i] != mot[-i-1]:
            return False
    return True

print(estUnPalindrome("radar"))
print(estUnPalindrome("souris"))