import pandas as pd
from decimal import Decimal, InvalidOperation
from numbers import Number


# Funcion para validar el beneficiario
def validar_beneficiario(beneficiario):
    if pd.isna(beneficiario) or not str(beneficiario).strip():
        return "El beneficiario está vacío"

    return None

# Funcion para validar la CLABE
def validar_clabe(clabe):
    if pd.isna(clabe):
        return "La CLABE está vacía"

    if isinstance(clabe, Number) and not isinstance(clabe, bool):
        try:
            numero = Decimal(str(clabe))
        except (InvalidOperation, ValueError):
            return "La CLABE no tiene un formato numérico válido"

        # Revisar si es un número entero y no tiene decimales
        if not numero.is_finite() or numero != numero.to_integral_value():
            return "La CLABE no debe contener decimales"

        clabe_texto = str(int(numero))
    else:
        clabe_texto = "".join(str(clabe).split())

    if not clabe_texto.isdigit():
        return "La CLABE contiene caracteres no numéricos"
    
    # Recuperar el cero inicial si se perdió
    if len(clabe_texto) == 17:
        clabe_texto = "0" + clabe_texto    

    if len(clabe_texto) != 18:
        return f"La CLABE tiene {len(clabe_texto)} dígitos; debe tener 18"   
    return None

# Funcion para validar el importe
def validar_importe(importe):
    if pd.isna(importe):
        return "El importe está vacío"
    try:
        numero = Decimal(str(importe))
    except (InvalidOperation, ValueError):
        return "El importe no es numérico"
    
    if not numero.is_finite() or numero <= 0:
        return "El importe debe ser un número positivo"

    if numero != numero.quantize(Decimal("0.01")):
        return "El importe no puede tener más de 2 decimales"        
    return None