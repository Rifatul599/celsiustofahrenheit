def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius*1.8+32 #9%5 = 1.8
    print(fahrenheit)

celsius_to_fahrenheit(32)
celsius_to_fahrenheit(0)



def celsiustofahrenheit(celsius):
    fahrenheit = celsius*1.8+32
    if celsius>0:
        return fahrenheit

print(celsiustofahrenheit(45))