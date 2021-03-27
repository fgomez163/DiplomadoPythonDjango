direcciones = {
    'casa': 'Calle falsa 123',
    'Odontólogo': 'P Sherman calle Wallaby 42 Sydney',
    'Toretto House': ' 724 de East Kensington Road',
}
print('Sus direcciones guardadas son:')
for key in direcciones.keys():
    print(key , ' ubicada en ', direcciones.get(key))
