per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money =int(input("Планируемая сумма к внесению в банк:"))
deposit =[]
deposit.append(int(per_cent['ТКБ']*int(money)/100))
deposit.append(int(per_cent['СКБ']*int(money)/100))
deposit.append(int(per_cent['ВТБ']*int(money)/100))
deposit.append(int(per_cent['СБЕР']*int(money)/100))
print("Cуммы депозита с процентами за год: ",('\n'),per_cent.keys(),('\n'),deposit[:])
print("максимальная сумма депозита, которую вы можете заработать: ",max(deposit))



