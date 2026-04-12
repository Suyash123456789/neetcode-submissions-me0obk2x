class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0

        def totres(l,r,count):
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1

            return count
        for i in range(len(s)):
            res+=totres(i,i,0) + totres(i,i+1,0)
            # l=r=i
            # while l>=0 and r<len(s) and s[l]!=s[r]:
            #     res+=1
            #     l-=1
            #     r+=1

            # l,r=i,i+1
            # while l>=0 and r<len(s) and s[l]!=s[r]:
            #     res+=1
            #     l-=1
            #     r+=1


        return res

        