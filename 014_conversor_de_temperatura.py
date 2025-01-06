c = float(input('Informe a temperatura em °C: '))
f = (c*1.8+32)
k = (c+(-273.15))
print('A temperatura de {:.1f}°C, equivale a:\nFahrenheit: {:.1f}°F\nKelvin: {:.1f}°K'.format(c,f,k))