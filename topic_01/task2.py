#Перетворення на великі літери

text = "великі літери"
uppercase_text = text.upper()
print(uppercase_text)

#Перетворення на малі літери

text = "МАЛІ ЛІТЕРИ"
lowercase_text = text.lower()
print(lowercase_text)

#Додавання рядків

text1 = "Hello,"
text2 = "World!"
result = text1 + text2
print(result)

#Розділення рядка на слова 

text = "Робота зі словами"
words = text.split()
print(words)

#Переведення числа в рядок 
number = 63
text = str(number)
print(text)

#Повторення рядка

text = "Технології програмування"
repeated_text = text * 2
print(repeated_text)

#Визначення довжини рядка

text = "Яку довжину має рядок"
length = len(text)
print(length)

#Вилучення пробілів з початку і в кінці рядка 

text = "     Hello, World!     "
trimmed_text = text.strip()
print(trimmed_text)

#Пошук підрядка у тексті 

text = "Вивчаємо мову програмування Python"
substring = "Python"
found = substring in text
print(found)

#Переведення першої літери на велику

text = "hello!"
capitalized_text = text.capitalize()
print(capitalized_text)

#Перевірка, чи складається рядок лише з літер

text ="Рядок складається тільки з літер"
is_alpha = text.isalpha()
print(is_alpha)

#Перевірка, чи складається рядок лише з цифр

text = "16752463"
is_digit = text.isdigit()
print(is_digit)

#Перевірка, чи починається рядок з перного слова 

text = "Технології програмування - новий курс"
starts_with_word = text.startswith("Технології")
print(starts_with_word)

#Заміна тексту

text = "Необхідно замінити текст"
new_text = text.replace("текст", "вислів")
print(new_text)

#Формування рядка

age = 18
name = "Viktoria"
formatted_text = f"Мене звати {name}, мені {age} років"
print(formatted_text)