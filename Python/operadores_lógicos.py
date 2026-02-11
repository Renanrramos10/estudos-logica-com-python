#AND para ser True tudo tem que ser True
#OR para ser True apenas um tem que ser True

print (True and True)
print (True and False)
print (False and False)
print (True or True)
print (True or False)
print(False or False)
saldo = 1000
saque = 250
limite = 200
conta_especial = True


x= saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(x)
y=(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(y)
