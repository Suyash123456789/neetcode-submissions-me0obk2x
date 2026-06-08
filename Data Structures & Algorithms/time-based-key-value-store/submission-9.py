class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
            self.store[key]=[]
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        keylist=self.store[key]
        l, r=0, len(keylist)-1
        res=""
        if keylist[0][1]>timestamp:
            return ""
        while l<=r:
            m=(l+r)//2
            if keylist[m][1]==timestamp:
                return keylist[m][0]
            elif keylist[m][1]<=timestamp:
                res=keylist[m][0]
                l=m+1
            else:
                r=m-1
        return res


        
