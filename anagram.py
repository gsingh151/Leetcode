def isAnagram(s, t):
    if len(s) != len(t):
        return False
    hashmap_1 = dict()
    hashmap_2 = dict()
    for letter in s:
        if letter not in hashmap_1:
            hashmap_1[letter] = 1
        else:
            hashmap_1[letter] += 1
    for lets in t:
        if lets not in hashmap_2:
            hashmap_2[lets] = 1
        else:
            hashmap_2[lets] += 1
        
    for key in hashmap_1:
        if key not in hashmap_2 or hashmap_2[key] != hashmap_1[key]:
            return False
    return True