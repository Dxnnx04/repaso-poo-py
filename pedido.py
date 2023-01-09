from accountAdmin import Admin
from accountDelivery import Delivery
from accoountUser import User
from pizzaEstandar import PizzaEstandar
from pizzaPremium import PizzaPremium
from pizzaSuperPremium import PizzaSuperPremium

class PedidoPizzaEstandar(Admin, Delivery, User, PizzaEstandar, PizzaPremium, PizzaSuperPremium):
    id                  = int
    vendedor            = Admin("","","","","","")
    cliente             = User ("","","","","")
    delivery            = bool
    pizzaEstandar       = PizzaEstandar("","","","","","")
    horaPedido          = int
    horaEntrega         = int    
    
    def __init__(self, id, vendedor, cliente, delivery, pizzaEstandar, horaPedido,  horaEntrega):
        self.id             = id
        self.vendedor       = vendedor
        self.cliente        = cliente
        self.pizzaEstandar  = pizzaEstandar
        self.horaPedido     = horaPedido
        self.horaEntrega    = horaEntrega
        self.delivery       = delivery
 
#  PizzaPremium   
class PedidoPizzaPremium(Admin, Delivery, User, PizzaEstandar, PizzaPremium, PizzaSuperPremium):
    id                  = int
    vendedor            = Admin("","","","","","")
    cliente             = User ("","","","","")
    delivery            = bool
    pizzaPremium        = PizzaPremium("","","","","","")
    horaPedido          = int
    horaEntrega         = int    
    
    def __init__(self, id, vendedor, cliente, delivery, pizaaPremium, horaPedido,  horaEntrega):
        self.id             = id
        self.vendedor       = vendedor
        self.cliente        = cliente
        self.pizzaPremium   = pizaaPremium 
        self.horaPedido     = horaPedido
        self.horaEntrega    = horaEntrega
        self.delivery       = delivery
        