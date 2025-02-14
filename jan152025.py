# 2429. Minimize XOR - Medium
# Accepted - Runtime: 1 ms. Beats 28%
# Solved it without any help. 
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Same number of set bits as num2
        # minimal xor with num1
        n2 = num2.bit_count() # answer
        n1 = num1.bit_count()
        if n2 == n1:
            return num1
       
        num1Bits = [bit for bit in "{:064b}".format(num1)]
        # num2Bits = [bit for bit in "{:064b}".format(num2)]
    
        
        if n2 > n1:
            diff = abs(n2-n1)
            for idx in range(len(num1Bits)-1, -1, -1):
                if diff < 1:
                    return int("0b" + "".join(num1Bits) ,2)
                if num1Bits[idx] == '0' and diff > 0:
                    num1Bits[idx] = '1'
                    diff -= 1
        else:
            diff = n2
            ans = ['0'] * 64
            for i in range(64):
                if diff < 1:
                    #print("ans = " + "".join(ans))
                    return int("0b" + "".join(ans) ,2)
                if num1Bits[i] == '1' and diff > 0:
                    ans[i] = '1'
                    diff -= 1
    
s = Solution()

num1 = 25
num2 = 72
print(s.minimizeXor(num1,num2)) # 24
# num1 = 3
# num2 = 5
# print(s.minimizeXor(num1,num2)) # 3



# num1 = 1
# num2 = 12
# print(s.minimizeXor(num1,num2)) # 3

# num2 = 00010101 -> 21 ... set bits = 3
# num1 = 11101101 
# answ = 11100000
# XORd = 00001101
# 1 ^ 1 = 0
# 0 ^ 0 = 0
# 0 ^ 1 = 1 
# 1 ^ 0 = 1