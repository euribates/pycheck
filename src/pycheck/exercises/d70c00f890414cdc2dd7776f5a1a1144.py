DESCRIPTION = '''
Dado un nombre y apellidos en formato "apellidos, nombre", obtenga las iniciales de dicha
persona pasadas a mayúsculas y con punto al final.
'''

ENTRYPOINT = {
    'PARAMS': [
        ['fullname', str],
    ],
    'RETURN': [
        ['initials', str],
    ],
}

CHECK_CASES = [
    [['Delgado Quintero, sergio'], ['S.D.Q.']],
    [['sánchez, María'], ['M.S.']],
    [['Prado López, Ana Belén'], ['A.P.L.']],
]

SOURCE = 'https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3'
