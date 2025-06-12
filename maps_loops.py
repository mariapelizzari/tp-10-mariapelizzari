def find_max_value(d):
    if len(d) == 0:
        return ""
    valor_mayor = max(d.values())
    for student, value in d.items():
        if value == valor_mayor:
            return student
    pass


def reverse_dict(d):
    diccionario_revertido = dict()
    for key, value in d.items():
        if value in diccionario_revertido:
            diccionario_revertido[value] = diccionario_revertido[value] + key
        else:
            diccionario_revertido[value] = key
    return diccionario_revertido 

    pass


def word_freq_counter(words):
    diccionario = dict()
    for word in words:
        if word in diccionario:
            diccionario[word] = diccionario[word] + 1
        else:
            diccionario[word] = 1
    return diccionario
    pass


def find_biggest_expense(dicta):
    if len(dicta) == 0:
        return ""
    promedios = dict()
    for categoria, costos in dicta.items():
        suma = sum(costos)
        largo = len(costos)
        promedio = suma/largo
        promedios[categoria] = promedio 
    promedio_mas_alto = max(promedios.values())
    for categoria, promedio in promedios.items():
        if promedio == promedio_mas_alto:
            return categoria 


def sum_of_expenses(expenses):
    diccionario_suma = dict()
    for categoria, costo in expenses.items():
        diccionario_suma[categoria] = sum(costo)
    return diccionario_suma
    pass


def sum_of_expenses_by_type(expenses):
    diccionario_nuevo = dict()
    for categoria in expenses:
        for tipo, valor in expenses[categoria]:
            if tipo in diccionario_nuevo:
                diccionario_nuevo[tipo] = diccionario_nuevo[tipo] + valor 
            else: 
                diccionario_nuevo[tipo] = valor 
    return diccionario_nuevo

    pass
