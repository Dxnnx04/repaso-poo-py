from account import Account
from accountAdmin import Admin
from accountDelivery import Delivery
from accoountUser import User
from pedido import PedidoPizzaEstandar
from pizzaEstandar import PizzaEstandar
from pago import Pago

if __name__ == "__main__":
    
    mateo = Admin(1,"Mateo Navas", "mateo@gmail.com",[658,698],989480227,True )
    #print(vars(mateo))
    
    sebastian = User (2,"Sebastian Vaca", "sebas@gmail.com",[5874,2589], 321456987)
    #print(vars(sebastian))
    
    charlie = Delivery (3,"Alexander Zapata",987456321,"licencia1234","PCC-1725","motocicleta" )
    #print(vars(charlie))
    
    pizzaEstandar1= PizzaEstandar (1,"Pizza estandar", "Pizza de 2 ingredientes", 9, True, ["peperoni", "jamon"])
    
    pedido1 = PedidoPizzaEstandar(1, Admin(1,"Mateo Navas", "mateo@gmail.com",[658,698],989480227,True ), User (2,"Sebastian Vaca", "sebas@gmail.com",[5874,2589], 321456987), False, PizzaEstandar(1,"Pizza estandar", "Pizza de 2 ingredientes", 9, True, ["peperoni", "jamon"]), 1700, 1740)
    # print(vars(pedido1))
    # print(pedido1.cliente)
    
    pedido2 = PedidoPizzaEstandar(2,mateo, sebastian, charlie,pizzaEstandar1, 1800, 1850)
    # print(vars(pedido2))
    
    pago1= Pago (1, "efectivo",12012023, PedidoPizzaEstandar(1, Admin(1,"Mateo Navas", "mateo@gmail.com",[658,698],989480227,True ), User (2,"Sebastian Vaca", "sebas@gmail.com",[5874,2589], 321456987), False, PizzaEstandar(1,"Pizza estandar", "Pizza de 2 ingredientes", 9, True, ["peperoni", "jamon"]),1750, 1820))
    # print(vars(pago1))
    # print(vars(pago1.pedido))
    # print(vars(pago1.pedido.cliente))    
    
    pago2 = Pago(2, "efectivo",1262023,pedido2)
    # print(vars(pago2))
    print((pago2))
    
    
    