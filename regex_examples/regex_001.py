# https://regex101.com/
# https://www.youtube.com/watch?v=_pLpx6btq6U

"""
Регулярные выражения!
. - любой одиночный символ
[ ] - любой из них, диапазоны
$ - конец строки
^ - начало строки
\ - экранирование
\d - любую цифру
\D - все что угодно, кроме цифр
\s - пробелы
\S - все кроме пробелов
\w - буква
\W - все кроме букв
\b - граница слова
\B - не границ

Квантификация
n{4} - искать n подряд 4 раза
n{4,6} - искать n от 4 до 6
* от нуля и выше
+ от 1 и выше
? - нуль или 1 раз

"""
import re

text = "one two name.001 other name1_other.002 another"

# blender names
ex = r"\b(\S+)\.\d+\b"
matches = re.findall(ex, text)
if matches:
    print(matches)
    for match in matches:
        m = re.match(r"(\w+)", match)
        print(m.groups()[0])

else:
    print("NO MATCHES!")

names = set()
for name in text.split(" "):
    m = re.match(r"(\w+).\d{3}", name)
    # print(m.groups()[0])
    if m:
        print(m.groups()[0])
        names.add(m.groups()[0])
    else:
        print(name)
        names.add(name)

print("names:", names)

