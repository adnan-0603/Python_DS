### author Md-Adnan chowdhury

def Towers_Of_Hanoi(numbersOfDisks,startPeg=1,endPeg =3):
    if numberOfDisks:
        TowersOfHanoi(NumberOfDisks-1,startPeg,6-startPeg-endPeg)
        print("Move disk %d from peg %d to peg %d " %(numbersOfDisks,startPeg,endPeg))
        Towers_Of_Hanoi(numbersOfDisks-1,6-startPeg-endPeg,endPeg)

Towers_Of_Hanoi(numbersOfDisks=4)
