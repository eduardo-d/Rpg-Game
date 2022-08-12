
# for sleep function
from time import sleep
# for level
from level import easy,medium,hard
#for heros
from heros import wizard,warrior,giant

#nickname interation

cor_espaço = 70* '-'
print(f'\033[1;90m {cor_espaço}')
nick_name = (str(input('\033[1;31m Nickname ->\033[1;32m ')))
sleep(0.3)

print(f'\033[1;90m {cor_espaço}')
print(f'\033[1;37m Seja bem vindo \033[1;32m"{nick_name}" \033[1;37ma essa jornada')
sleep(1)

#hero choice

print(f'\033[1;90m {cor_espaço}')
print('\033[1;37m Selecione seu heroi')
sleep(1)

print(f'\033[1;90m {cor_espaço}')
print( wizard)
sleep(0.5)

print(f'\033[1;90m {cor_espaço}')
print( warrior)
sleep(0.5)

print(f'\033[1;90m {cor_espaço}')
print( giant)
sleep(0.5)

print(f'\033[1;90m {cor_espaço}') 
select_hero = (int(input('\033[1;37m Numero do seu heroi! -> ')))

#hero condition

if select_hero == 1:
    print(f'\033[1;90m {cor_espaço}')
    print(f'\033[1;37m Parabens \033[1;32m{nick_name}\033[1;37m! Agora voce e um \033[1;93mMago')

if select_hero == 2:
    print(f'\033[1;90m {cor_espaço}')
    print(f'\033[1;37m Parabens \033[1;32m{nick_name}\033[1;37m!  Agora voce e um \033[1;93mGuerreiro')

if select_hero == 3:
    print(f'\033[1;90m {cor_espaço}')
    print(f'\033[1;37m Parabens \033[1;32m{nick_name}\033[1;37m!  Agora voce e um \033[1;93mGigante')

#difficulty choice

sleep(0.5)
print(f'\033[1;90m {cor_espaço}')
print('\033[1;37m Escolha sua dificuldade: ')
sleep(1)

print(f'\033[1;90m {cor_espaço}')
print( f'\n {easy} \n {medium} \n {hard}\n')
print(f'\033[1;90m {cor_espaço}')
sleep(0.5)

#difficulty condition

select_difficulty = (int(input(' ->\033[1;97m ')))
if select_difficulty == 1:
    sleep(0.5)
    print(f'\033[1;90m {cor_espaço}')
    print(f'\033[1;92m Parece que e a sua primeira vez.. Boa Sorte!')
sleep(0.5)

if select_difficulty == 2:
    sleep(0.5)
    print(f'\033[1;90m {cor_espaço}')
    print(f'\033[1;93mHum ja sabe um pouco... Boa Sorte!')
sleep(0.5)

if select_difficulty == 3:
    sleep(0.5)
    print(f'\033[1;90m {cor_espaço}')
    print(f'\033[1;31m Parece que voce e o manda-chuva por aqui... Boa Sorte!')
print(f'\033[1;90m {cor_espaço}')

#loading...

for c in range(1,3):
    sleep(0.5)
    print('\033[1;90m Carregando.')
    sleep(0.5)
    print('\033[1;90m Carregando..')
    sleep(0.5)
    print('\033[1;90m Carregando...')
    sleep(1)

#start

print = input('\033[1;94m------S T A R T------')


#python game_ini.py