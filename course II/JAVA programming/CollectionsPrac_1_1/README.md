## Задание

1. Реализуйте метод, который на вход получает любую коллекцию и возвращает коллекцию
уже без дубликатов.
2. Реализовать метод, который добавляет 1 000 000 случайных элементов в ArrayList и
LinkedList. Реализовать второй метод, который выбирает из списка элемент наугад 100 000
раз. Замерьте время и скажите кто быстрее.
3. Реализовать частотный словарь слов русского языка (на вход принимается текст любой
размерности)


## Демонстрация

```
Удаление дупликатов:

Исходный ArrayList:
[str, str, str, string, uniq, primary]
ArrayList (HashSet<String>) после удаления дупликатов:
[str, string, uniq, primary]


Сравнение ArrayList и LinkedList:

Тест: добавление элементов
ArrayList: 34 ms
LinkedList: 152 ms

Тест: вставка элементов
ArrayList: 1331 ms
LinkedList: 16216 ms

Тест: извлечение элементов
ArrayList: 1 ms
LinkedList: 16028 ms


Частотный словарь слов:

ut: 3
in: 3
dolor: 2
dolore: 2
mollit: 1
culpa: 1
incididunt: 1
tempor: 1
est: 1
...
```