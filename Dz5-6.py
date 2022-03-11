rev = float(input('Введите значение выручки вашей фирмы: '))
costs = float(input('Введите ваши издержки: '))
workers = int(input('Сколько сотрудников работает у вас? '))

if rev > costs:
    print(f'Ваша прибыль: {rev - costs:.2f} рублей')
    print(f'Рентабельность фирмы: {rev/costs:.1f} %')
    print(f'Прибыль на одного сотрудника составляет: {(rev - costs) / workers:.2f} рублей')
elif rev == costs:
    print('Вы работаете в ноль!')
else:
    print(f'Вы работаете себе в убыток: {rev - costs:.2f} рублей')
