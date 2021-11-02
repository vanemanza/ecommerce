class Carro:

    def __init__(self, request):

        self.request = request
        self.session = request.session
        carro = self.session.get('carro')

        if not carro:
            carro = self.session["carro"]={}
        self.carro = carro 
    
    def agregar(self, producto):
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad":1,
                "imagen": producto.imagen.url,
            }            
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    break 
        self.guardar()

    def guardar(self):
        self.session["carro"]=self.carro
        self.session.modified=True 

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar()

    def restar(self, producto):
        for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break 
        self.guardar() 

    def vaciar(self):
        self.session["carro"]={}
        self.session.modified=True

    def subtotal(request, producto):

        sub = 0
        if producto in request.session['carro']:
            for key, value in request.session["carro"].items():
                sub = float(value["precio"])*float(value["cantidad"])
        return sub 