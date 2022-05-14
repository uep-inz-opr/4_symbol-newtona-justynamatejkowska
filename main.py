import math

print('Witaj w kalkulatorze obliczającym dwumian Newtona')


el = list(map(int,input("Wprowadź najpierw n później k oddzielając je spacją: ").strip().split()))

if len(el)>=3:
  print('Podałeś za dużo liczb')
elif len(el)<=1:
  print("Podałeś na mało liczb")
elif len(el)==2:
  def symbol_newton(el):   #wzór
    return math.factorial(el[0])/(math.factorial(el[1])*math.factorial(el[0]-el[1]))
  if el[0]>el[1] and el[1]>0: #tylko liczby dodatnie całkowite 
    print(symbol_newton(el))
  else: 
    print('Błąd-n musi być większe od k') 
