class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers or len(numbers) <= 0:
            return
        # 若存在则该数出现次数比其他所有数字出现次数之和还要多，则要找的数字肯定是最后一次把次数设为1时对应的数字
        res = numbers[0]
        times = 1
        for i in range(len(numbers)):
            if times == 0:
                res = numbers[i]
                times = 1
            elif numbers[i] == res:
                times += 1
            else:
                times -= 1
        t = 0
        for i in range(len(numbers)):
            if numbers[i] == res:
                t += 1
        if t*2 > len(numbers):
            return res
        else:
            return

if __name__ == '__main__':
    a = [1, 3, 3, 3, 2, 3, 5, 3, 2]
    b = Solution()
    print(b.MoreThanHalfNum_Solution(a))