class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for asteriod in asteroids:

            while stk and stk[-1] >0 and asteriod < 0 :

                if stk[-1] < abs(asteriod):
                    stk.pop()
                    continue
                elif stk[-1] == abs(asteriod):
                    stk.pop()

                break
            else:
                stk.append(asteriod)

        return stk
        