AK = 120
EK = 700
t = 30

def cagr_berechnung(AK, EK, t):
    cagr = ((EK/AK)**(1/t)-1)*100
    return cagr

print(cagr_berechnung())
