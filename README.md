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

$$\mu=0.5$$ 
![image](https://github.com/ScorpKir/course-paper/assets/77200268/772bc10b-6037-4a33-b206-bb84e6594c96)
$$\mu=2$$ 
![image](https://github.com/ScorpKir/course-paper/assets/77200268/777f7625-55c7-405e-b8ef-0c2424663720)
$$\mu=5$$ 
![image](https://github.com/ScorpKir/course-paper/assets/77200268/644ca227-32bb-4a7e-bf70-f4497bb1989f)
$$\mu=8$$ 
![image](https://github.com/ScorpKir/course-paper/assets/77200268/cd6427ff-b04b-459b-b091-bc55e087dc61)

### Установка 

```bash
pip install poetry
git clone https://github.com/ScorpKir/course-paper.git
cd course-paper/src
poetry install
poetry shell
python main.py
```
