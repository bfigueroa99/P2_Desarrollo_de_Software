import json


def inner_loop(preguntas_respondidas,nivel_alumno = 5):
    umbral_racha_buenas = 2
    umbral_racha_mala = 2
    racha_buena = 0
    racha_mala = 0
    cb_tmp = 0
    cm_tmp = 0
    count_hint = 0
    for p in preguntas_respondidas:
        if p['correcta']:
            cb_tmp += 1
            cm_tmp = 0
            if cb_tmp >= umbral_racha_buenas:
                racha_buena += 1
            else:
                racha_buena = 0

        else:
            cm_tmp += 1
            cb_tmp = 0
            if cm_tmp >= umbral_racha_mala:
                racha_mala += 1
            else:
                racha_mala = 0  
        
        if p['uso_hint']:
            count_hint += 1

    puntaje = ((nivel_alumno*0.6)+(racha_buena*0.4)-(count_hint*0.1)-(racha_mala*0.3))

    # 1 2 3| 4 5 6 7 | 8 9 10
    if puntaje <= 3:
        return('baja')
    
    if  3 < puntaje <= 7:
        return('media')

    if 7 < puntaje:
        return('alta')




preguntas_respondidas = [
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "respuesta": "París",
        "correcta": True,
        "uso_hint": False
    },
    {
        "pregunta": "¿En qué año se fundó la ONU?",
        "respuesta": "1945",
        "correcta": True,
        "uso_hint": True
    },
    {
        "pregunta": "¿Cuál es el símbolo químico del oxígeno?",
        "respuesta": "O",
        "correcta": True,
        "uso_hint": False
    },
    {
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
        "respuesta": "Júpiter",
        "correcta": True,
        "uso_hint": False
    },
    {
        "pregunta": "¿Quién escribió 'Cien años de soledad'?",
        "respuesta": "Gabriel García Márquez",
        "correcta": True,
        "uso_hint": True
    },
    {
        "pregunta": "¿Cuál es el animal terrestre más grande?",
        "respuesta": "Elefante africano",
        "correcta": True,
        "uso_hint": False
    },
    {
        "pregunta": "¿En qué año se llevó a cabo la Revolución Rusa?",
        "respuesta": "1917",
        "correcta": True,
        "uso_hint": False
    },
    {
        "pregunta": "¿Cuál es el elemento más abundante en la Tierra?",
        "respuesta": "Oxígeno",
        "correcta": True,
        "uso_hint": True
    },
    {
        "pregunta": "¿Cuál es el elemento más abundante en la Tierra?",
        "respuesta": "Oxígeno",
        "correcta": True,
        "uso_hint": True
    },
    {
        "pregunta": "¿Cuál es el elemento más abundante en la Tierra?",
        "respuesta": "Oxígeno",
        "correcta": True,
        "uso_hint": True
    }
]



print(inner_loop(preguntas_respondidas))