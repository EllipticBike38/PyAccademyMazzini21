from EsempioClasse1 import Student
def test():
    s1=Student("andrea", "ndr",'4648')
    s2=Student("andrea", "ndr",'4648')
    print(s1.getName)
    
    Student.albero='tiglio'
    # si può attribuire una nuova variabile di classe
    # a una classe già madrea di oggetti senza errori 
    # e modificando tali oggetti
    print(s1.albero)

    s1.cognome='mazzini'
    # si può attribuire una nuova variabile di istanza
    # a oggetto già istanziato senza errori
    print(s1.cognome)
test()