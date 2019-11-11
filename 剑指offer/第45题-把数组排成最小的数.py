# 比较规则：'a' > 'b'  'ab' > 'ba' ab > ba
class Soluton:
    def PrintMinNumber(self, arr):
        if not arr or len(arr) <= 0:
            return
        strarr = [str(i) for i in arr]
        for i in range(1, len(strarr)):
            for j in range(0, len(strarr) - i):
                if strarr[j] > strarr[j + 1]:
                    strarr[j], strarr[j + 1] = strarr[j + 1], strarr[j]
        return ''.join(strarr)
if __name__ == '__main__':
    a = [12, 4, 31, 4]
    print(Soluton().PrintMinNumber(a))