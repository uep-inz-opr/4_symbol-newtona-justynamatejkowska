import math

el = list(map(int,input().strip().split()))

if len(el)>=3:
  print('Podałeś za dużo liczb')
elif len(el)<=1:
  print("Podałeś na mało liczb")
elif len(el)==2:
  def symbol_newton(el):   #wzór
    return math.factorial(el[0])/(math.factorial(el[1])*math.factorial(el[0]-el[1]))
  if el[0]>el[1] and el[1]>0: #tylko liczby dodatnie całkowite 
    print(math.ceil(symbol_newton(el)))
  elif el[0]==el[1] or el[1]==0:
    print('1')
  else: 
    print('Błąd-n musi być większe od k') 
