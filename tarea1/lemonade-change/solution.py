class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        de_cinco = 0
        de_diez = 0

        for billete in bills:

            if billete == 5:
                de_cinco = de_cinco + 1

            elif billete == 10:
                if de_cinco < 1:
                    return False

                de_cinco = de_cinco - 1
                de_diez = de_diez + 1

            elif billete == 20:
                if de_diez >= 1 and de_cinco >= 1:
                    de_diez = de_diez - 1
                    de_cinco = de_cinco - 1

                elif de_cinco >= 3:
                    de_cinco = de_cinco - 3

                else:
                    return False

        return True