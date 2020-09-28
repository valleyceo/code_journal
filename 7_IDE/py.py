class Solution:
    def lemonadeChange(self, bills) -> bool:
        change = list([])
        
        for b in bills:
            pay = b - 5
            change.append(b)
            change.sort()
            print(b)

            if pay == 0:
                continue
                
            while pay != 0:
                print(change)
                
                for ch in reversed(change):
                    if ch <= pay:
                        pay -= ch
                        change.remove(ch)
                        
                        if pay == 0:
                            break

                if pay > 0:
                    return False
                else:
                    break

        return True


x = Solution()
assert(x.lemonadeChange([5,5,10,5,20,5,5,5,5,5,20,5,10,5,5,5,5,20,20,5]), True)