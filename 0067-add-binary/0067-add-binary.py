class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_length = max(len(a), len(b))
        a = a.zfill(max_length) 
        b = b.zfill(max_length)
        result = []
        carry = 0

        for i in range(max_length - 1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])

            total = bit_a + bit_b + carry
            result_bit = total % 2  
            carry = total // 2 

            result.append(str(result_bit))

        if carry:
            result.append(str(carry))
            
        return ''.join(reversed(result))