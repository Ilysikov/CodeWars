
Directions Reduction
-------------------
Смотреть на платформе CodeWars:
* [Задачу](https://www.codewars.com/kata/550f22f4d758534c1100025a)
* [Мое решение](https://www.codewars.com/kata/reviews/5512f1242b34d80e9a00020e/groups/64ef8c6c6861c10001c934b6)

Условия задачи:
---------------
Однажды, путешествуя по дикому горному западу,…

… человеку дали указания идти из одной точки в другую. 
Направления были «СЕВЕР», «ЮГ», «ЗАПАД», «ВОСТОК». Очевидно, что «СЕВЕР» и «ЮГ» противоположны, «ЗАПАД» и «ВОСТОК» тоже.
Идти в одном направлении и тут же возвращаться в противоположном направлении — бесполезное усилие. 
Поскольку это Дикий Запад, с ужасной погодой и нехваткой воды, важно сохранить немного энергии, иначе вы можете умереть от жажды!
Как я хитро пересёк горную пустыню.
Указания, данные мужчине, могут быть, например, следующими (в зависимости от языка):

`["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]`

Сразу видно, что идти "НА СЕВЕР" и сразу "НА ЮГ" не разумно, лучше остаться на том же месте! 
Так что задача - дать человеку упрощенный вариант плана. Лучший план в данном случае просто:

`["WEST"]
or
{ "WEST" }
or
[West]`

Другие примеры:
* В `["NORTH", "SOUTH", "EAST", "WEST"]`, направление "NORTH" + "SOUTH"идет на север и тут же возвращается обратно .
Путь становится `["EAST", "WEST"]`, теперь "EAST"и "WEST"уничтожают друг друга, поэтому конечный результат равен `[]` (ноль в Clojure).

* В `["СЕВЕР", "ВОСТОК", "ЗАПАД", "ЮГ", "ЗАПАД", "ЗАПАД"]` "СЕВЕР" и "ЮГ" не являются прямо противоположными, но они становятся прямо противоположными после сокращения "ВОСТОК" и "ЗАПАД", поэтому весь путь сводится к `["ЗАПАД", "ЗАПАД"]`.

Задача

Напишите функцию dirReduc, которая будет принимать массив строк и возвращать массив строк, в котором удалены ненужные направления (W<->E или S<->N рядом).

Примечания
Не все пути можно упростить. Путь `["СЕВЕР", "ЗАПАД", "ЮГ", "ВОСТОК"]` не является редуцируемым. "СЕВЕР" и "ЗАПАД", "ЗАПАД" и "ЮГ", "ЮГ" и "ВОСТОК" не являются прямо противоположными друг другу и не могут стать таковыми. 
Следовательно, результирующий путь сам по себе: `["СЕВЕР", "ЗАПАД", "ЮГ", "ВОСТОК"]`.
Если вы хотите перевести, пожалуйста, спросите перед переводом.
