from base_conocimiento import autos

def tiene_sintoma(auto, sintoma):
    for sistema, sintomas in autos[auto]['sintomas'].items():
        if sintoma in sintomas:
            return True
    return False

def falla_sistema_refrigeracion(auto):
    if tiene_sintoma(auto, 'humo blanco'):
        return 'fuga de refrigerante'
    return None

def falla_empaque(auto):
    if tiene_sintoma(auto, 'humo blanco') and tiene_sintoma(auto, 'no arranca'):
        return 'empaque dañado'
    return None

def falla_transmision(auto):
    if tiene_sintoma(auto, 'ruido metálico') and tiene_sintoma(auto, 'no avanza'):
        return 'desgaste de engranajes'
    return None

def resolver_fallas(auto):

    posibles_fallas = []

    reglas = [falla_sistema_refrigeracion, falla_empaque, falla_transmision]

    for regla in reglas:
        resultado = regla(auto)
        if resultado:
            posibles_fallas.append(resultado)

    if posibles_fallas:
        print(f"{auto} tiene las siguientes posibles fallas: {posibles_fallas}")
    else:
        print('El auto no tiene fallas')
    return posibles_fallas

resolver_fallas('Nissan Sentra')
resolver_fallas('Subaru Crosstrek')