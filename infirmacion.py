SUMA = 1
MULTIPLICACION = 2

def operacion(dato, op =SUMA):
    print(f"srv: recibido: {dato} y {op}")
    if op == SUMA:
        return dato + 1
    if op == MUKTIPLICACION:
        return dato + 2
       
def cli():
    print("cli: begin")
   operacion(22)
   operacion(33)
    print("cli: end")
# main --------------------------------
cli()
