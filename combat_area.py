import emoji


espaco = 100 * '-'

arrow_dmg = 3
fire_dmg = 5
fist_dmg = 1
firesword_dmg = 9


fire_sword = 'Espada em chamas'
arrow = 'Arco & Flecha'
fire = 'Fogo'
fist = 'Punho'

special = 1
ceu_nuvens = emoji.emojize('                                       |         :cloud:                    :cloud:                 :cloud::cloud:             |')
teto = 65*'_'
hp_hero =  10
hp_vilain =  10
eyes_normal = '                                       |               °°                                     °°       |'
arms = f'                                       |  § {special} / 3  -|-                                       -|-       |'
legs = '                                       |              | |                                     | |      |'
div = '                                       |---------------------------------------------------------------|'
floor = '                                       |_______________________________________________________________|'





'''
while 1 + 1 == 2 :
    if hp_vilain <= 0 :
        hp_vilain = 0
        print(f'                                       {teto}')
        print(ceu_nuvens)
        print(f'                                       |              {hp_hero}/10                                 {hp_vilain }/10        |')
        print(eyes_normal)
        print(arms)
        print(legs)
        print(div)
        print(f'                                       |                    V O C E   V E N C E U   ! ! !              |')        
        print(floor)
        break
    else :
        villain = randint(1,3)
        if villain == 1 :
            print(f'Voce foi atingido pelo {arrow}! hp /-{arrow_dmg}/')
            hp_hero -= arrow_dmg
            print(f'                                       {teto}')
            print(ceu_nuvens)
            print(f'                                       |              {hp_hero}/10                                 {hp_vilain}/10       |')
            print(eyes_normal)
            print(arms)
            print(legs)
            print(div)
            print(f'                                       |  {arrow} = {arrow_dmg} DMG  /  {fire} = {fire_dmg} DMG /   {fist} = {fist_dmg} DMG     |')    
            print(floor)
        if villain == 2 :
            print(f'Voce foi atingido pelo {fire}! hp /-{fire_dmg}/')
            hp_hero -= fire_dmg
            print(f'                                       {teto}')
            print(ceu_nuvens)
            print(f'                                       |              {hp_hero}/10                                 {hp_vilain}/10        |')
            print(eyes_normal)
            print(arms)
            print(legs)
            print(div)
            print(f'                                       |  {arrow} = {arrow_dmg} DMG  /  {fire} = {fire_dmg} DMG /   {fist} = {fist_dmg} DMG     |')   
            print(floor)
        if villain == 3 :
            print(f'Voce foi atingido pelo {fist} ! hp /-{fist_dmg}/')
            hp_hero -= fist_dmg
            print(f'                                       {teto}')
            print(ceu_nuvens)
            print(f'                                       |              {hp_hero}/10                                 {hp_vilain}/10        |')
            print(eyes_normal)
            print(arms)
            print(legs)
            print(div)
            print(f'                                       |  {arrow} = {arrow_dmg} DMG  /  {fire} = {fire_dmg} DMG /   {fist} = {fist_dmg} DMG     |')   
            print(floor)
    if hp_hero <= 0 :
        hp_hero = 0
        print(f'                                       {teto}')
        print(ceu_nuvens)
        print(f'                                       |              {hp_hero}/10                                 {hp_vilain }/10        |')
        print(eyes_normal)
        print(arms)
        print(legs)
        print(div)
        print(f'                                       |                    V O C E   P E R D E U   ! ! !              |')        
        print(floor)
        break
    else :
        print('Agora escolha um ataque !')
        print(f' 1 - {arrow}')
        print(f' 2 - {fire}')
        print(f' 3 - {fist}')
        sel_atk = int(input('-->  '))
        if sel_atk == 1 :
            print(f'Voce atacou com o {arrow}! hp /-{arrow_dmg}/')
            hp_vilain -= arrow_dmg
            print(f'                                       {teto}')
            print(ceu_nuvens)
            print(f'                                       |              {hp_hero}/10                                 {hp_vilain}/10        |')
            print(eyes_normal)
            print(arms)
            print(legs)
            print(div)
            print(f'                                       |  {arrow} = {arrow_dmg} DMG  /  {fire} = {fire_dmg} DMG /   {fist} = {fist_dmg} DMG     |')       
            print(floor)
        if sel_atk == 2 :
            print(f'Voce atacou com o {fire}! hp /-{fire_dmg}/')
            hp_vilain -= fire_dmg
            print(f'                                       {teto}')
            print(ceu_nuvens)
            print(f'                                       |              {hp_hero}/10                                 {hp_vilain}/10        |')
            print(eyes_normal) 
            print(arms)
            print(legs)
            print(div)
            print(f'                                       |  {arrow} = {arrow_dmg} DMG  /  {fire} = {fire_dmg} DMG /   {fist} = {fist_dmg} DMG     |')        
            print(floor)
        if sel_atk == 3 :
            print(f'Voce atacou com o {fist}! hp /-{fist_dmg}/')
            hp_vilain -= fist_dmg
            print(f'                                       {teto}')
            print(ceu_nuvens)
            print(f'                                       |              {hp_hero}/10                                 {hp_vilain}/10        |')
            print(eyes_normal)
            print(arms)
            print(legs)
            print(div)
            print(f'                                       |  {arrow} = {arrow_dmg} DMG  /  {fire} = {fire_dmg} DMG /   {fist} = {fist_dmg} DMG     |')        
            print(floor)
'''