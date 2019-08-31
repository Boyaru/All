product = { 'city': 'Москва', 'temperature': 20}
print(product['city'])
product['temperature'] -= 5   #Изменение значения ключа
print(product.get('country')) #Проверить есть ли елемент в словаре.
print(product.get('country', 'Россия')) #Добавляет новый ключ со значением
product['date'] = '27.05.2019' #Добавляет новый ключ к словарю
print(len(product)) #Проверка длины словаря
print(product)

#Здесь был текст