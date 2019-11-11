class Solution:
    def minnumberinrotatearray(self, rotatearray):
        n = len(rotatearray)
        first = 0
        mid = 0
        last = n - 1
        if n <= 0:
            return 0
        while rotatearray[first] >= rotatearray[last]:
            if last - first == 1:
                mid = last
                break
            mid = (last + first) // 2

            # 如果 first, mid, last相等，只能采用顺序查找
            if (rotatearray[first] == rotatearray[last]) and (rotatearray[mid] == rotatearray[first]):
                return self.minvalue(rotatearray, first, last)

            if rotatearray[mid] >= rotatearray[first]:
                first = mid
            elif rotatearray[mid] <= rotatearray[last]:
                last = mid

        return rotatearray[mid]

    # 顺序查找
    def minvalue(self, rotatearry, first, last):
        res  = rotatearry[first]
        for i in range(first+1, last+1):
            if res > rotatearry[i]:
                res = rotatearry[i]
        return res

if __name__ == '__main__':
    a = [3, 4, 5, 1, 2]
    b = [1, 0, 1, 1, 1]
    c = [1, 1, 1, 0, 1]
    d = [1, 2, 3, 4, 5]
    print(Solution().minnumberinrotatearray(a))
    print(Solution().minnumberinrotatearray(b))
    print(Solution().minnumberinrotatearray(c))
    print(Solution().minnumberinrotatearray(d))