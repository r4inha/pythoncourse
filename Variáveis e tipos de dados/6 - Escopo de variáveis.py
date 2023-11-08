#Escopo de variáveis

#"Escopo" de variável é o limite, objetivo e propósito das variáveis

x = 5

def funcao():
    x = 3
    print("Valor da variável local: ", x)

funcao()
print("Valor da variável global: ",x)


#Crie variáveis com identificação, ao invés de criar assim:
y = "Gabriel" 
z = 1.74 
y = "000.000.000-00" 
l = 23 

#Crie assim:
Nome = "Gabriel" 
Altura = 1.74 
CPF = "000.000.000-00" 
Idade = 23 

