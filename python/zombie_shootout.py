#https://www.codewars.com/kata/5deeb1cc0d5bc9000f70aa74/train/python

def zombie_shootout(zombies, distance, ammo):

    kills = 0
    distance_walked = 0
    is_dead = False

    if zombies == 0:
        return("You shot all "  + str(kills) + " zombies.")

    elif ammo == 0:
        return("You shot " + str(kills) + " zombies before being eaten: ran out of ammo.")

    elif distance == 0:
        return("You shot " + str(kills) + " zombies before being eaten: overwhelmed.")

    while is_dead == False:
        distance_walked += 0.5
        zombies -= 1
        kills += 1
        ammo -= 1

        if zombies == 0:
            is_dead = True
            return("You shot all "  + str(kills) + " zombies.")

        elif distance_walked == distance:
            is_dead = True
            return("You shot " + str(kills) + " zombies before being eaten: overwhelmed.")

        elif ammo == 0:
            is_dead = True
            return("You shot " + str(kills) + " zombies before being eaten: ran out of ammo.")


