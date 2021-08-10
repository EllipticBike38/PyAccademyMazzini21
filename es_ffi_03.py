
class Automaton():
    def read_commands(self,lista:list):
        el='q1'

        for a in lista:
                print(el)
                if el=='q1' and a=='1':
                    el='q2'
                elif el=='q2' and a=='0':
                    el='q3'
                elif el=='q3':
                    el='q2'
        ans=el=='q2'
        return ans

a=Automaton()
print(a.read_commands(list('10010')))