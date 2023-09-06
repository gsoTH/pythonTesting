def bonus(x:int, y:int) -> int:
    ergebnis = 0

    if(x>0 and y>0):
        ergebnis = 30

    if(x>10 and y <10):
        ergebnis = ergebnis + 20
    else:
        ergebnis = ergebnis + 10
    return ergebnis
    
    
if __name__ == '__main__':
    bonus(5,5)
    bonus(11,5)
    bonus(11,0)
