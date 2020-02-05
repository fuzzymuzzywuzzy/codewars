#https://www.codewars.com/kata/592a5f9fa3df0a28730000e7/train/python

def souls(character, build):

    import pandas as pd

    l_Warrior = ['warrior', 4, 11, 8, 12, 13, 13, 11, 9, 9]
    l_Knight = ['knight', 5, 14, 10, 10, 11, 11, 10, 9, 11]
    l_Wanderer = ['wanderer', 3, 10, 11, 10, 10, 14, 12, 11, 8]
    l_Thief = ['thief', 5, 9, 11, 9, 9, 15, 10, 12, 11]
    l_Bandit = ['bandit', 4, 12, 8, 14, 14, 9, 11, 8, 10]
    l_Hunter = ['hunter', 4, 11, 9, 11, 12, 14, 11, 9, 9]
    l_Sorcerer = ['sorcerer', 3, 8, 15, 8, 9, 11, 8, 15, 8]
    l_Pyromancer = ['pyromancer', 1, 10, 12, 11, 12, 9, 12, 10, 8]
    l_Cleric = ['cleric', 2, 11, 11, 9, 12, 8, 11, 8, 14]
    l_Deprived = ['deprived', 6, 11, 11, 11, 11, 11, 11, 11, 11]
    l_full = [l_Warrior, l_Knight, l_Wanderer, l_Thief, l_Bandit, l_Hunter, l_Sorcerer, l_Pyromancer, l_Cleric, l_Deprived]

    df_classes = pd.DataFrame(l_full, columns = ['class','starting_level','stat_1','stat_2','stat_3','stat_4','stat_5','stat_6','stat_7','stat_8'])
    df_classes = df_classes.set_index('class')

    exp_1 = [673, 690, 707, 724, 741, 758, 775, 793, 811, 829]
    exp_2 = []

    temp = list(df_classes.loc[character])
    difference = sum(build) - sum(temp[1:9])
    target_level = temp[0] + difference

    if target_level < 12:
        target_exp = sum(exp_1[temp[0]-1:target_level-1])

    else:
        start = 11
        levels = list(range(11+1,target_level+1))

        for x in levels:
            exp_x = round(pow(x,3)*0.02+pow(x,2)*3.06+105.6*x-895)
            exp_2.append(exp_x)

        target_exp = sum(exp_1[temp[0]-1:target_level-1]) + sum(exp_2)

    return str('Starting as a ' + character + ', level ' + str(target_level) + ' will require ' + str(target_exp) + ' souls.')
