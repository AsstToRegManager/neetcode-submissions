class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        d = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for ch in s:
                arr[ord(ch) - ord('a')] += 1
            d[tuple(arr)].append(s)
        
        for v in d.values():
            l.append(v)
        
        print(d)
        return l


        

