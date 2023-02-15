money = int(input("Введите сумму вклада:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
bank_p_c=list(per_cent.values()) # формируем список значений словаря
deposit1 = [i/100*money for i in bank_p_c] # высчитываем доход по каждому банку
deposit = [(round(a, 0)) for a in deposit1] # округляем доход по каждому банку
print("Накопленные средства за год вклада в каждом из банков -", deposit)
max_income_bank=max(deposit)
print("Максимальная сумма, которую вы можете заработать —", max_income_bank)
