# C-Battle

### Игровая модель

**C-Battle** - консольная игра в карточном стиле. Игрок собирает свою команду  управленцев (5 человек). Каждому управленцу соотетсвтует ***карточка*** с *именем(name), репутацией(reputation), профессиональным навыком (managerial or tech), лидерством (leadership) и должностью(position).*  Управленцы бывают двух типов: менеджеры (managers) и технари (tech). Менеджеров в качестве проф. скилла идут менеджерские способности, а у технарей технические. Игрок играет против "рынка" (market). Рынок имеет два ключевых показателя: Рост (Growth) и Технологии (Technologies). Игрок отдает каждому управленцу комманду: саморазвиваться (Develop) или выполнять рабочую функцию (для менеджеров это Collaborate, а для технарей Research). Саморазвитие с опр. вероятностью повышает один из 3 скиллов, а выполнение рабочей функции  оказывает влияние на рынок. Если игрок правильно отдал команды нужным управленцам, и система посчитала, что команда управленцев работает достаточно эффективно, то рыночная стоимость  компании (market valuation) повышается. В противном случае она либо слегка понижается, либо проседает. Цель игрока -- добиваться оптимальной рыночной стоимости через мудрое управление своей командой.

### Архитектура

#### Создание колоды

Команда управленцев суть колода карт, а каждый управленец суть карта с показателями (см. **Игровую модель**).  Все классы персонажей наследуются от класса `AbsCharater`. Для менеджерских классов от него отнаследован `AbsManager`, а для технарей `AbsTech`. Далее от них наследуются классы, которые соответствуют конкретным профессиям. 

Для создания персонажей создан класс `AbsBuilder`. От него наследуются `AbsManagerBuilder` и `AbsTechBuilder`. Билдеры обоих типов умеют производить экземпляры конкретных классов. Класс создаваемого объекта передается в конструктор билдера.

Директором для билдера служит статическая функция класса `Pool`, котороая генерирует для игрока некий пул случайных карт.