def calculate_IMC(weigth,height):
	imc = weigth/(height*height)
	return imc

height = float(input("Please,inform your height in meters:"))
weight = float(input("PLease,input your weight in kilograms:"))

imc = calculate_IMC(weight, height)
print(f'Your IMC is {imc}')