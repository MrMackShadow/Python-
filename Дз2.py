user_time = int(input('Enter time in seconds: '))
print('Вы ввели: ', user_time, 'секунд')
hours = user_time // 3600
minutes = (user_time - hours * 3600) // 60
seconds = user_time - (hours * 3600 + minutes * 60)
print("Время в формате чч:мм:сс   {} : {} : {}".format(hours, minutes, seconds))