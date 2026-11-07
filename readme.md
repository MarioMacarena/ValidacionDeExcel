# Prueba técnica: Validación de pagos

## Descripción

Proyecto desarrollado en Python para procesar un archivo Excel con información de beneficiarios y validar sus datos.

Se realizan las siguientes validaciones:

- **Beneficiario:** no debe estar vacío.
- **CLABE:** debe contener exactamente 18 dígitos numéricos. Se eliminan los espacios y se recupera un cero inicial cuando se reciben 17 dígitos.
- **Importe:** debe ser numérico, positivo y tener como máximo dos decimales.

El programa genera un archivo `resultado.xlsx` que conserva las columnas originales y agrega dos columnas:

- `estado`: indica si el registro es válido o inválido.
- `motivo_error`: describe los errores encontrados en cada registro.

## Tecnologías utilizadas

- Python 3
- Pandas
- OpenPyXL
- Tabulate
- Decimal

## Requisitos

Python 3.11 o superior.

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/MarioMacarena/ValidacionDeExcel.git
cd ValidacionDeExcel
```

2. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

3. Colocar el archivo `DatosEntrada.xlsx` en la carpeta principal del proyecto.

4. Ejecutar el programa:

```bash
python main.py
```

5. El archivo `resultado.xlsx` se generará automáticamente en la misma carpeta.

## Estructura del proyecto

```text
├── main.py
├── validators.py
├── requirements.txt
├── DatosEntrada.xlsx
├── resultado.xlsx
└── README.md
```

## ¿Qué fue lo más difícil del reto y cómo lo resolviste?

Lo más difícil fue manejar los distintos formatos en los que podían venir las CLABE, ya que algunas estaban almacenadas como números, otras contenían espacios y algunas no tenian el 0 inicial.
Lo resolví creando una función específica para validar las CLABE, normalizando temporalmente los valores antes de comprobar su longitud y contenido numérico.
Finalmente, trabajé sobre una copia de los datos originales para conservar intacta la información de entrada y generar un archivo independiente con los resultados.