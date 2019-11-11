class Solution:
    def reOrderArray(self, array):
        n = len(array)
        if array == None or n == 0:
            return
        first = 0
        last = n - 1
        while first < last:
            while first < last and self.pd(array[first]):
                first += 1
            while first < last and not self.pd(array[last]):
                last -= 1
            if first < last:
                t = array[first]
                array[first] = array[last]
                array[last] = t
        return array

    def pd(self, s):
        return s % 2 == 1

    def reOrderArray1(self, array):
        res1 = []
        res2 = []
        for i in array:
            if i % 2 != 0:
                res1.append(i)
            else:
                res2.append(i)
        return res1 + res2

if __name__ == '__main__':
    s = [1, 2, 3, 4, 5, 6]
    print(Solution().reOrderArray(s))

