import barcode
from barcode.writer import ImageWriter

# Генерация штрих-кода EAN-13
ean = barcode.get_barcode_class('ean13')
ean_barcode = ean('2020492456329', writer=ImageWriter())
filename = ean_barcode.save('ean13_barcode')

# Генерация штрих-кода Code 128
code128 = barcode.get_barcode_class('code128')
code128_barcode = code128('2020492456329', writer=ImageWriter())
filename = code128_barcode.save('code128_barcode')

