"""
Diccionarios que contienen preguntas y respuestas categorizadas por nivel de dificultad.

Diccionarios
------------
preguntas_basicas : dict
    Contiene preguntas de nivel básico. Cada clave es un identificador de pregunta 
    (por ejemplo, 'pregunta_1'), y su valor es un diccionario que incluye:
    - 'enunciado': Una lista con el texto de la pregunta.
    - 'alternativas': Una lista de listas, donde cada lista interna contiene el texto de una alternativa y 
      un valor (0 o 1) que indica si la alternativa es incorrecta (0) o correcta (1).

preguntas_intermedias : dict
    Contiene preguntas de nivel intermedio, con la misma estructura que `preguntas_basicas`.

preguntas_avanzadas : dict
    Contiene preguntas de nivel avanzado, con la misma estructura que `preguntas_basicas`.

pool_preguntas : dict
    Diccionario que agrupa las preguntas según el nivel de dificultad. Las claves son:
    - 'basicas': Referencia a `preguntas_basicas`.
    - 'intermedias': Referencia a `preguntas_intermedias`.
    - 'avanzadas': Referencia a `preguntas_avanzadas`.
"""
preguntas_basicas = {
    'pregunta_1': {'enunciado':['¿En qué año comenzó la Guerra de Independencia de Chile?'],
    'alternativas': [['1820', 0], 
                     ['1810', 1], 
                     ['1800', 0], 
                     ['1830', 0]]},
    'pregunta_2': {'enunciado':['¿En qué año rescataron a los 33 mineros de la mina San José?'],
    'alternativas': [['2012', 0], 
                     ['2010', 1], 
                     ['2008', 0], 
                     ['2007', 0]]},
    
'pregunta_3': {'enunciado':['¿Quién ganó el premio Nobel de Literatura en 1945?'],
    'alternativas': [['Pablo Neruda', 0], 
                     ['Gabriela Mistral', 1], 
                     ['Nicanor Parra', 0], 
                     ['Isabel Allende', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado':['¿Qué deportista chileno ganó la medalla de oro en tenis en los Juegos Olímpicos de Atenas 2004?'],
    'alternativas': [['Fernando Gonzalez', 0], 
                     ['Nicolás Massú', 1], 
                     ['Marcelo Rios', 0], 
                     ['Alejandro Tabilo', 0]]},
    'pregunta_2': {'enunciado':['¿Quién compuso e interpretó la canción "Gracias a la vida"?'],
    'alternativas': [['Francisca Valenzuela', 0], 
                     ['Violeta Parra', 1], 
                     ['Mon Laferte', 0], 
                     ['Yuri', 0]]},
    
'pregunta_3': {'enunciado':['¿De qué ciudad proviene la agrupación chilena Los Bunkers?'],
    'alternativas': [['Valdivia', 0], 
                     ['Concepción', 1], 
                     ['Temuco', 0], 
                     ['Coquimbo', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['¿Qué se celebra el 8 de diciembre en Chile?'],
    'alternativas': [['La Asunción de la Virgen de Lourdes', 0], 
                     ['La Inmaculada Concepción', 1], 
                     ['Santa Teresa de los Andes', 0], 
                     ['La Asunción de la Virgen María', 0]]},
    'pregunta_2': {'enunciado':['Ciudad chilena que limita con Tacna, Perú '],
    'alternativas': [['Iquique', 0], 
                     ['Arica', 1], 
                     ['Antofagasta', 0], 
                     ['Calama', 0]]},
    
'pregunta_3': {'enunciado':['Nombre del principal puerto de Chile'],
    'alternativas': [['San Antonio', 0], 
                     ['Valparaíso ', 1], 
                     ['Valdivia', 0], 
                     ['Calama', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}

