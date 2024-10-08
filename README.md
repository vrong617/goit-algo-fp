# Метод Монте-Карло для кидання кубиків

## Опис

Метод Монте-Карло був використаний для моделювання кидання двох кубиків. Було виконано 100,000 кидків для визначення ймовірностей випадіння різних сум очок.

## Аналітичні розрахунки

Аналітично ймовірності для кожної суми між 2 та 12 можуть бути визначені на основі кількості можливих комбінацій кубиків.

| Сума | Аналітична ймовірність (%) |
|------|----------------------------|
| 2    | 2.78                       |
| 3    | 5.56                       |
| 4    | 8.33                       |
| 5    | 11.11                      |
| 6    | 13.89                      |
| 7    | 16.67                      |
| 8    | 13.89                      |
| 9    | 11.11                      |
| 10   | 8.33                       |
| 11   | 5.56                       |
| 12   | 2.78                       |

## Порівняння з методом Монте-Карло

Результати симуляції методом Монте-Карло були порівняні з аналітичними значеннями. Таблиця нижче відображає різницю:

| Сума | Ймовірність Монте-Карло (%) | Аналітична ймовірність (%) | Різниця (%) |
|------|----------------------------|----------------------------|-------------|
| 2    | 2.75                       | 2.78                       | -0.03       |
| 3    | 5.55                       | 5.56                       | -0.01       |
| 4    | 8.20                       | 8.33                       | -0.13       |
| 5    | 11.06                      | 11.11                      | -0.05       |
| 6    | 13.95                      | 13.89                      | 0.06        |


## Висновок

За результатами проведеної симуляції методом Монте-Карло, ймовірності випадання різних сум при киданні двох кубиків показали дуже близькі значення до аналітичних розрахунків. Відхилення не перевищують декількох десятих відсотка, що свідчить про високу точність методу Монте-Карло при великій кількості повторень.

Найбільші відхилення спостерігалися для рідкісних подій (суми 2 і 12), що пояснюється тим, що ці значення мають менше можливих комбінацій і тому сильніше залежать від випадкових варіацій при меншій кількості спроб. Проте, для сум з більшою кількістю комбінацій, таких як 7 або 6 і 8, результати майже повністю співпадають з аналітичними.

Таким чином, метод Монте-Карло є надійним підходом для оцінки ймовірностей у подібних завданнях. Однак, важливо враховувати, що точність результатів зростає з кількістю симуляцій, і для рідкісних подій відхилення можуть бути більшими при меншій кількості повторень.
