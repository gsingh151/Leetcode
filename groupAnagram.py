def groupAnagrams(strs):
        if (len(strs)==0):
            return []
        hashmap = dict()
        for item in strs:
            sorted_word = ''.join(sorted(item))
            if sorted_word not in hashmap:
                hashmap[sorted_word] = [item]
            else:
                hashmap[sorted_word].append(item)
        final_ans = list()
        for key in hashmap:
            final_ans.append(hashmap[key])
        final_ans.sort()
        print(final_ans)
    
def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    strs = [""]
    groupAnagrams(strs)
if __name__ == '__main__':
    main()