salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(months):
    delta = salary - spend
    need_money += delta
    spend = spend * (1 + increase)
need_money *= -1  # TODO Оформить решение

print(round(need_money))
