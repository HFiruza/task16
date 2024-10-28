calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    pieces = len(string) # длина строки
    word_text = string.upper() # нижний регистр, буквы маленькие
    word_text_1 = string.lower() # верхний регистр, заглавные буквы
    return f'{pieces,word_text,word_text_1}'

# Регистром строки при проверке пренебречь: UrbaN ~ URBAN
# False - если отсутствует
# True - если строка находится в этом списке
def is_contains(string,list_to_search):
    count_calls()
    result = any(item in string for item in list_to_search)
    return result

print(string_info('Capybara')) #Capybara и Armageddon
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN','urBAN '] ))
print(is_contains('cycle',['recycling', 'cyclic']))
print(calls)