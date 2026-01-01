import math
print(2+3)
print(4-2)
print(type(3))
print(type((3,5)))
print(type(1+3j))
print(type(3j))
print(type('amoungs'))
print(type([2,3,4,5]))
print(type({'nome':'exemplo'}))
print(type({2.4,5.6,4}))

print('Day 2 of 30 days learning python')
skills= ['HTML','CSS','Japonse','phyton','blah']
is_married=True

city = 'JF'
person_info={
    'nome':'Enzo',
    'curso':'Comp',
    'idade':'26',
}
print(skills)
print (is_married)
print(person_info)
print(len(skills))
print(len(person_info))
print('tamnanhp da palavra JF ',len(city))
idade=input('Qual sua idade: ')
print(idade)
print(len(person_info['curso']))
print(len(person_info['idade']))
print((len(person_info['curso'])>len(person_info['idade'])))
num_one = 5
num_two = 4
total = num_one + num_two
sub = num_one - num_two
radius = 30
area_of_circle = math.pi*(radius**2)
print('Área do círculo: ',area_of_circle)
circunfarence_of_circle =2*math.pi*radius
print('Circuferencia do circulo: ',circunfarence_of_circle)
raio = input('Escreva o raio do círculo que voce quer calcular a área: ')
raioint =int(raio)
areadociculo = math.pi*(raioint**2)
print('Area do ciculo do raio fornecido: ',areadociculo)
nome=input('Diga seu nome: ')
lastname = input('Diga um de seus sobrenomes: ')
pais = input('Diga seu país de origem: ')
idade = input('Diga sua idade: ')
primeiro,segundo,terceiro='primeiro','2',3
usuario = {
    'nome':nome,
    'sobrenome':lastname,
    'pais':pais,
    'idade':idade,
}
print(usuario)
print(1<2 and 1<3)
#base=int(input('Qual é a base do triangulo: '))
#altura= int(input('Qual é a altura do triangulo: '))
#area_triangulo= (base*altura)/2
#print(area_triangulo)
lado1=int(input('Escreva o valor do lado 1: '))
lado2=int(input('Escreva o valor do lado 2: '))
lado3=int(input('Escreva o valor do lado 3: '))
perimetro_triangulo=lado1+lado2+lado3
print('O perimetro é: ',perimetro_triangulo)
#equação = mx+ b
m=2
b=-2
slope = m
x_intercept = (0,b)
y_intercept = (-b/m,0)
print('O slope é: ',slope,'\n A interseção no X é no ponto: ',x_intercept,'\n A interseção no Y é no ponto: ',y_intercept)
x1=2
y1=2
x2=6
y2=10
preview =((x2-x1)**2+(y2-y1)**2)
resultado =preview**(1/2)
print('Distancia euclidiana de (2,2) e (6,10): ',resultado)
slope2 = (y2-y1)/(x2-x1)
print('Slope de (2,2) e (6,10): ',slope2)
x=int(input('Escreva o valor de X: '))
y=x**2 + 6*x +9
print('Valor de Y tendo X como ',x,": ",y)
print(len('Python')==len('dragon'))
print('on' in 'Python' and 'on' in 'Dragon')
print('jargon' in ' BLAh bwafwa blah jargon da silva')
print(type(str(float(len('python')))))
number=int(input('Escreva o numero para ver se é impar ou par: '))
if number%2==0 :
    print(number,' é par')
else :
    print(number, " é impar")
print(7/3)
print (int(2.7))
print( 'verifica tipos: ',type('10') == type(10))
print('Verifica 9.8: ',int(9.8),10,int(9.8)==10)
horas_trab = int(input('Horas trabalhas: '))
dinheiro_por_hora = int(input('Ganho por hora: '))
print('Voce recebe ',horas_trab*dinheiro_por_hora*7,' reais por semana')
anos_vividos = int(input('quantos anos você viveu: '))
print('Você ainda tem ',(100-anos_vividos)*365*24*60*60, 'segundos de vida')
print(' 1 1 1 1 1 \n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125')
