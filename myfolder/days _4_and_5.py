multiline_string = """Ola 
Opa
EAE"""
print(multiline_string)
#Forma antiga
first_name = "Enzo"
last_name = "Sales"
pais ="Brasil"
string_completa ="Olá, meu nome é %s %s, moro no %s" %(first_name,last_name,pais)
print(string_completa)
nuemro_inteiro = 100
numero_foat = 20.343566575
string_numeros = "Quero viver até os %d, e já possuo %.2f anos" %(nuemro_inteiro,numero_foat)
print(string_numeros)
lista_amigo=['Pietro','TOledo','Amanda','Enzo']
string_amigos ="Esses são meus amigos %s" %(lista_amigo)
print(string_amigos)
#forma mais nova
string_completa_nova = "Ola meu nome E {} {}, moro no {}".format(first_name,last_name,pais)
print(string_completa_nova)
string_numeros_nova = "Quero viver até os {}, e ja possuo {:.2f} anos, que é {:.2f} % do total".format(nuemro_inteiro,numero_foat,numero_foat/nuemro_inteiro*100)
print(string_numeros_nova)
#interpolação
num1 = 3
num2 = 5
print(f'{num1} + {num2} = {num1 +num2}')
print(f'{num1} / {num2} = {num1/num2:.2f}')
language = "portuguesoo"
a,b,c,d,e,f,g,h,i,j,k= language
print(a,b,c,d,e,f,g)
print(i)
primeira = language[0]
ultima = language[-1]
print(primeira,ultima)
port = language [0:4]
last3 = language [3:]
print(port)
print(last3)
print(language[::-1])
pulando2 = language[0::3]
print(pulando2)
print(language.capitalize())
print(language.count('o',2,))
print("termina vdd",language.endswith('oo'))
print("termina falso",language.endswith("nop"))
textotab=("tem\tmto\ttab\t")
print(textotab)
print(textotab.expandtabs(12))
print(textotab.find('e'))
print(textotab.rfind('t'))
#index é quase igual a find, a diferença, que se não achar, o find retorna -1, o index se n acha retorna valueError
#.isallnum() verifica se tudo é alfabeto ou numero retornando v ou f.se tiver espaço retorna f tbm
#.isalpha() verifica só se é alfabeto
#.isdecimal se é decimal
#isdigit - se é decimal e uns otro trem
#isnumeric - aceita mais trem
#isidentifier - verifica se essa palavra pode se tornar o nome de uma variavel
#islower - verifica se tudo no minusculo
#issupper - verifica se tudo ta no maiusculo
teste_join = ['Eu','voce','dois filhos','e um cachorro']
print("teste".join(teste_join))
print(string_completa_nova.strip('lisO'))
print(textotab.replace("\t"," "))
print(string_completa_nova.split())
print(string_numeros_nova.title())
#swapecase() troca maiusculo e minusculo
#startwith verifica se começa com oq ta dentro do ()

#Exercicios
frase_conc = "eu"+" sei"+ " concatenar lol"
print(frase_conc)
print(frase_conc.strip('eu'))
print(frase_conc.find('se'))
print(frase_conc.replace('eu','voce'))
frase_grande_ex = 'frase, grande, para, teste'
print(frase_grande_ex.split(', '))
print(frase_grande_ex[0])
print(frase_grande_ex[-1])
print(frase_grande_ex[9])
print(frase_grande_ex.index('e'))
print(frase_grande_ex.rindex('e'))
print(frase_grande_ex.replace('grande',""))
print('Começa com eu? ',frase_grande_ex.startswith('eu'))
print('termina com teste? ',frase_grande_ex.endswith('teste'))
frase_com_espaco = '   espaco no inicio e no fim    '
print(frase_com_espaco.strip()) 
lista_exercicio = ['djangp','livre','e','afins']
frasejoindasilva = " ".join(lista_exercicio)
print(frasejoindasilva)
print("I am enjoying this challenge\nI wonder what is the next one")
print('opa\teae\tpessoal\nbora\nprozbar')
print('**')
print('%')
print('//')
