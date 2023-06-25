# Моя курсовая работа

### Поставленная задача
Дано уравнение Ван-дер Поля:
 $$g''- \mu \cdot (1 - g^2) \cdot g + g = 0$$
и начальные условия:
$$g(0) = \alpha \\g'(0) = \beta$$
Необходимо реализовать программу, которая принимает начальные значения $$\alpha$$ и $$\beta$$, параметр $$\mu$$ и отображает анимацию движения фазовой траектории этого уравнения.

### Результаты

Зададим следующие начальные условия
 $$g(0) = 0\\g'(0) = 0.01$$

Посмотрим на результаты с разными значениями параметра $$\mu$$

<image src="https://imgur.com/VnsE5hx" alt="Значение параметра: 0.5">
<image src="https://imgur.com/cte925n" alt="Значение параметра: 2">
<image src="https://imgur.com/evbeURY" alt="Значение параметра: 5">
<image src="https://imgur.com/dwyrQ1i" alt="Значение параметра: 8">


### Установка 

```bash
pip install poetry
git clone https://github.com/ScorpKir/course-paper.git
cd course-paper/src
poetry install
poetry shell
python main.py
```
