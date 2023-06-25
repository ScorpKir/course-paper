# Моя курсовая работа

### Поставленная задача
Дано уравнение Ван-дер Поля:
 $$g''- \mu \cdot (1 - g^2) \cdot g + g = 0$$
 
Необходимо реализовать программу, которая принимает начальные значения `g(0)` и `g'(0)`, параметр $\mu$ и отображает анимацию движения фазовой траектории этого уравнения.

### Результаты

Зададим следующие начальные условия
```
 g(0) = 0
 g'(0) = 0.01
```

Посмотрим на результаты с разными значениями параметра $\mu$

![Imgur](https://i.imgur.com/VnsE5hx.png)
![Imgur](https://i.imgur.com/cte925n.png)
![Imgur](https://i.imgur.com/evbeURY.png)
![Imgur](https://i.imgur.com/dwyrQ1i.png)

### Установка 

```bash
pip install poetry
git clone https://github.com/ScorpKir/course-paper.git
cd course-paper/src
poetry install
poetry shell
python main.py
```
