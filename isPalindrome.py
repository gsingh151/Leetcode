def isPalindrome(s):
        print("Starting")
        t = ""
        for char in s:
            if char.isalnum():
                t += char.lower()
        p1 = 0
        p2 = len(t) - 1
        while (p1 < p2):
            if t[p1] != t[p2]:
                print("False")
                return
            p1 += 1
            p2 -= 1
        print("True")
        return
    

def main():
    s = "race a car"
    # s = "A man, a plan, a canal: Panama"
    isPalindrome(s)

if __name__ == '__main__':
    main()