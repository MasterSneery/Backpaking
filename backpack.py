import cvxpy as cvx

a= [5,8,7,4,8,4,5,6] #peso
b= [3,4,5,2,1,2,6,5] #beneficio
q= 25 #capacidad
n= len(a) #numero de objetos

x= cvx.Variable(n, boolean = True) #variables de decision (binarias)

#restricciones
peso=0
for i in range(n):
    peso= peso+a[i]*x[i]

cst=[]
cst.append(peso<=q) #construccion de la lista de restricciones

beneficio=0
for j in range(n):
    beneficio= beneficio+b[j]*x[j] #contruccion de la funcion objetivo
    
mochila= cvx.Problem(cvx.Maximize(beneficio), cst) #definicion del problema
Rp= mochila.solve(solver=cvx.GLPK_MI) #resolucion del problema



binario=[]
for i in range(n):
    if (x.value[i]>0):
        binario.append(1)
    else:
        binario.append(0)
        
print("Mejor decision: ", binario)
print("valor optimo de la mochila: ", mochila.value)

