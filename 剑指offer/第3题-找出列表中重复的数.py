class solution:
    def duplicate(self,list,number = []):
        n = len(list)
        if list == None or n <= 1:
            return False

        for i in range(len(list)):
            if list[i] < 0 or list[i] > n - 1:
                return False
            a = list[i] in number
            if list.count(list[i]) > 1 and a == False:
                number.append(list[i])
        return number


class solution1:
    def duplicate(self,list,number = []):
        n = len(list)
        if list == None or n <= 1:
            return False
        for i in range(len(list)):
            if list[i] < 0 or list[i] > n - 1:
                return False
        for i in range(len(list)):
            while list[i] != i:
                if list[i] == list[list[i]]:
                    number.append(list[i])
                    return number
                else:
                    temp = list[i]
                    list[i] = list[temp]
                    list[temp] = temp
        return False







if __name__== "__main__":
    print(solution().duplicate([2, 3, 1, 0, 2, 5, 3]))
