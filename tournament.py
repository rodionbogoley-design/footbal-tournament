import random

team1 = input('Введите первую команду: ')
team2 = input('Введите вторую команду: ')
def play_match(team1, team2):
    score1 = 0
    score2 = 0
    yc = 0
    print(f'⚽ СЕГОДНЯ НА СТАДИОНЕ: {team1} vs {team2}')
    print(f'Матч между {team1} и {team2} начался!')
    for i in range(1, 91):
        if random.randint(1, 100) <= 3:
            if random.choice([team1, team2]) == team1:
                score1 += 1
                print(f"{i}' ГООООООЛ! {team1} забивает!")
            else:
                score2 += 1
                print(f"{i}' ГООООООЛ! {team2} забивает!")
            print(f'Счет: {score1}-{score2}')
        
        if random.randint(1, 100) <= 5:
                if random.choice([team1, team2]) == team1:
                    print(f"{i}' 🟨 Жёлтая карточка, {team1}.")
                else:
                    print(f"{i}' 🟨 Жёлтая карточка, {team2}.")
                yc += 1
        
        if i == 45:
            print(f'Перерыв! Счет: {score1}-{score2}')

    print('Матч окончен!')

    print(f'Финальный счёт: {score1}:{score2}')
    print(f'Жёлтых карточек: {yc}')
    print(f'Всего голов: {score1 + score2}')

    if score1 > score2:
        print(f'Выиграла команда {team1}!')
        winner = team1
        looser = team2
    elif score1 < score2:
        print(f'Выиграла команда {team2}!')
        winner = team2
        looser = team1
    else:
        print('Ничья! Серия пенальти!')
        pen1 = 0
        pen2 = 0
        for k in range(5):
            if random.randint(1, 100) <= 75:
                pen1 += 1
                print(f'{team1} — ГОЛ ⚽')
            else:
                print("Не забил!")
            print(f'Счет: {pen1}-{pen2}')
            
            if random.randint(1, 100) <= 75:
                pen2 += 1
                print(f'{team2} — ГОЛ ⚽')
            else:
                print("Не забил!")
            print(f'Счет: {pen1}-{pen2}')
        
        if pen1 > pen2:
            print(f'Выиграла команда {team1}!')
            winner = team1
            loser = team2
        elif pen1 < pen2:
            print(f'Выиграла команда {team2}!')
            winner = team2
            loser = team1
        else:
            print('Дополнительные пенальти!')
            while pen1 == pen2:
                if random.randint(1, 100) <= 75:
                    pen1 += 1
                    print(f'{team1} — ГОЛ ⚽')
                else:
                    print("Не забил!")
                print(f'Счет: {pen1}-{pen2}')
                        
                if random.randint(1, 100) <= 75:
                    pen2 += 1
                    print(f'{team2} — ГОЛ ⚽')
                else:
                    print("Не забил!")
                print(f'Счет: {pen1}-{pen2}')
            if pen1 > pen2:
                print(f'Выиграла команда {team1}!')
                winner = team1
                loser = team2
            else:
                print(f'Выиграла команда {team2}!')
                winner = team2
                loser = team1
    return winner, loser

team3 = input('Введите третью команду: ')
team4 = input('Введите четвертую команду: ')
print('Первый матч полуфинала!')
w1, l1 = play_match(team1, team2)
print('Второй матч полуфинала!')
w2, l2 = play_match(team3, team4)
print('Матч за третье место!')
place3, l = play_match(l1, l2)
print(f'Поздравляем! Третье место заняла команда {place3}!')
print('Финал!')
win, l = play_match(w1, w2)
print(f'Поздравляем! Турнир выиграла команда {win}!')

            
