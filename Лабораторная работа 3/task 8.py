money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital >= 0:
    money_capital -= spend
    if month >= 1:  # в нулевой месяц нет зарплаты
        money_capital += salary
    spend = spend * (1 + increase)
    if money_capital < 0:
        break  # 4 месяц не смогли прожить полностью, поэтому вышли из цикла
    month += 1  # TODO Оформить решение

print(month)
