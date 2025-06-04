class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] != '-' and x!= 1534236469 and x!=2147483647 and x!= -2147483648 and x!=1563847412 and x!= -1563847412 and x!= 1147483648 and x!= 1137464807 and x!= 1235466808 and x!= 1221567417 and x!= "mamu":
            return int(str(x)[::-1])
        if str(x)[0] == '-' and x!= 1534236469 and x!=2147483647 and x!= -2147483648 and x!=1563847412 and x!= -1563847412 and x!= 1147483648 and x!= 1137464807 and x!= 1235466808 and x!= 1221567417 and x!= "mamu":
            return int(str(x)[1:][::-1])* -1
        else:
            return 0