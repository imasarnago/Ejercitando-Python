"""

Escribir un programa para un negocio. De cada venta ingresa el importe total y un código que indica la forma de pago.
Los códigos puede ser:

C: cheque, 20% de recargo.
E: efectivo, 10% de descuento.
T: con tarjeta, 12% de recargo.

Se debe ingresar una F para finalizar el día de venta y arrojar los totales.

"""


RECARGO_CHEQUE = 20/100
DESCUENTO_EFECTIVO  = 10/100
RECARGO_TARJETA = 12/100

CHEQUE = 'C'
EFECTIVO = 'E'
TARJETA = 'T'

recargo = 0
descuento = 0

total_cheque = 0
total_efectivo = 0
total_tarjeta = 0

final = 0

codigo = input("Ingrese un codigo : <<< C (cheque) , E (efectivo) , T (tarjeta) , F (termina el programa) >>> : ").upper()

while codigo != 'F':
    importe = int (input("Ingrese el monto : "))
    if codigo == CHEQUE:
        suma_cheque = importe + importe*RECARGO_CHEQUE
        total_cheque += suma_cheque
        final += suma_cheque
    elif codigo == EFECTIVO:
        suma_efectivo = importe - importe*DESCUENTO_EFECTIVO
        total_efectivo += suma_efectivo
        final += suma_efectivo
    elif codigo == TARJETA:
        suma_tarjeta = importe + importe*RECARGO_TARJETA
        total_tarjeta += suma_tarjeta
        final += suma_tarjeta
    codigo = input("Ingrese un codigo : <<< C , E , T , F (termina el programa) >>> : ").upper()


str_totales = f""" 
| Forma de Pago    | Total |
| **************** | ******** | 
| Efectivo en Caja | {total_efectivo} |
| Tarjeta/Crédito  | {total_tarjeta}  |
| Cheques          | {total_cheque}   |
| TotaldeVenta     | {final}  |

"""
print (str_totales)

