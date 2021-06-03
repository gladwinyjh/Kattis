from math import sqrt

while True:

    k, l, s, w = map(float, input().split())

    if k == l == s == w == 0:
        break

    #For convervation of energy, calculate GPE at top
    gravitational_energy = w * 9.81 * s

    final_velocity = sqrt((gravitational_energy/w) * 2)

    if l >= s:

        #If length of rope >= bridge height, and velocity of Bond > 10, Bond dies. Velocity <= 10, Bond survives
        #Assuming Bond starts from rest, and air resistance is negligible (no terminal velocity), no bouncing
        if final_velocity > 10:
            print("Killed by the impact.")
        else:
            print("James Bond survives.")

    else:
        #If length of rope < bridge height, elastic force will pull Bond back towards sky, slowing velocity.
        #If velocity at max rope length is already <= 10, Bond will only get slower; will not die
        if final_velocity <= 10:
            print("James Bond survives.")
        
        else:

            #Get height difference between rope length and bridge
            heightDiff = s - l

            #Conservation of energy: At bottom, total energy of Bond = 0.5kx^2 + 0.5mv^2 = mgh (at top)
            #Elastic energy
            elastic_energy = 0.5 * k * (heightDiff**2)


            #If velocity can be slowed to 10 by the time Bond reaches the bottom, Bond survives
            kinetic_energy =  gravitational_energy - elastic_energy
            botVelocity_squared = (kinetic_energy * 2) / w

            if botVelocity_squared < 0: #Velocity = 0 before even reach the bottom, so it swings back up 
                print("Stuck in the air.")
            else:
                botVelocity = sqrt(botVelocity_squared)

                if botVelocity > 10:
                    print("Killed by the impact.")
                else:
                    print("James Bond survives.")