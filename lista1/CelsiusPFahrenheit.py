def converterParaCelsius():
  F= float(input('Digite os graus Fahrenheit:'))
  C=(5/9)*(F-32)
  return C

def converterParaFahrenheit():
  C=float(input('Digite os graus Celsius:'))
  F=(9*C+160)/5
  return F
escolha=input('Converter para graus Celsius ou Fahrenheit: ')

if escolha == "celsius":
  Celsius=converterParaCelsius()
  print('%.1f'% Celsius)

elif escolha == "fahrenheit":
    Fahrenheit = converterParaFahrenheit()
    print('%.1f'% Fahrenheit)