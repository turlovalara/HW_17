error = 'ПЕРЕЗАПУСТИТЕ ПРОГРАММУ'
sum_result = input('Введите несколько целых чисел через пробел: ')
rand_digit = int(input('И ещё одно целое число: '))

# Проверяем на цифры в строке

def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

# Проверяем на соответствие указанному в условии ввода данных.

if " " not in sum_result:
    print("\nНЕ ЗАБУДЬТЕ ПРО ПРОБЕЛЫ! (введите ЧИСЛА, согласно условиям ввода.)")
    sum_result = input('Введите ЦЕЛЫЕ числа через пробел: ')
if not is_int(sum_result):
    print('\nВ ВВОДЕ СОДЕРЖАТСЯ НЕ ЦИФРЫ ЛИБО НЕ ЦЕЛЫЕ ЧИСЛА (введите ЧИСЛА, согласно условиям ввода.)\n')
    print(error)
else:
    sum_result = sum_result.split()

list_sum_result = [int(item) for item in sum_result]

# Сортируем список

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_sum_result = merge_sort(list_sum_result)

# Установливаем позицию элемента

def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число превышает диапазон списка, введите меньшее число.'

print(f'Упорядоченный по возрастанию список: {list_sum_result}')

if not binary_search(list_sum_result, rand_digit, 0, len(list_sum_result)):
    rI = min(list_sum_result, key=lambda x: (abs(x - rand_digit), x))
    ind = list_sum_result.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < rand_digit:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {list_sum_result[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_sum_result.index(rI)}
В списке нет меньшего элемента''')
    elif rI > rand_digit:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_sum_result.index(rI)}
Ближайший меньший элемент: {list_sum_result[min_ind]} его индекс: {min_ind}''')
    elif list_sum_result.index(rI) == 0:
        print(f'Индекс введенного элемента: {list_sum_result.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_sum_result, rand_digit, 0, len(list_sum_result))}')
