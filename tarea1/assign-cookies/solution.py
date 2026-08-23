class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        posicion_nino = 0
        posicion_galleta = 0
        atendidos = 0

        while posicion_nino < len(g) and posicion_galleta < len(s):

            necesita = g[posicion_nino]
            tamano = s[posicion_galleta]

            if tamano >= necesita:
                atendidos = atendidos + 1
                posicion_nino = posicion_nino + 1
                posicion_galleta = posicion_galleta + 1

            else:
                posicion_galleta = posicion_galleta + 1

        return atendidos