import math

g = -9.81


def height(time, ht, vel):
    return g / 2 * (time**2) + vel * time + ht


def veloc(time, vel):
    return g * time + vel


def top_time(vel):
    return -1 * vel / g


def top_height(ht, vel):
    return ht - (vel**2) / 2 * g


def time_air(ht, vel):
    return - (vel + math.sqrt((vel ** 2) - 2 * g * ht)) / g


def main():
    while 1:
        inp = input('Press any key to continue or "q" to quit: ')
        if inp == "q":
            break
        init_height = int(input("Enter initial height: "))
        velocity = int(input("Enter velocity: "))
        print(f'''
Air time = {round(time_air(init_height, velocity), 2)}
Time to top = {round(top_time(velocity), 2)}
Top height = {round(top_height(init_height, velocity), 2)}
''')
        air_time = int(time_air(init_height, velocity))
        time = float(input(f'Enter a time value between 0 and {round(top_time(velocity), 2)}: '))
        if time < 0 or air_time < time:
            print('Time is out of range.')
        else:
            print(f'''
Height at time: {time} = {round(height(time, init_height, velocity), 2)}
Velocity at time = {round(veloc(time, velocity), 2)}''')


main()






