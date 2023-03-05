from collections import deque

wanted_water = deque()
tank_litters = int(input())
command = input()
while True:
    if command == "Start":
        if len(wanted_water) == 0:
            print(f"{tank_litters} liters left")
            break
        litter_request = int(input())
        if tank_litters >= int(litter_request):
            print(f"{wanted_water.popleft()} got water")
            tank_litters -= litter_request
            if tank_litters > 0:
                litter_request = int(input())
                if tank_litters < litter_request:
                    print(f"{wanted_water.popleft()} must wait")
                    print(f"{tank_litters} liters left")
                    break
                print(f"{wanted_water.popleft()} got water")
                tank_litters -= litter_request
                continue

            tank_refill = input().split(" ")
            litter_request = int(input())
            tank_litters += int(tank_refill[1])

            if tank_litters >= litter_request:
                print(f"{wanted_water.popleft()} got water")
                tank_litters -= litter_request
                command = input()
            else:
                print(f"{wanted_water} must wait" )

    elif command == "End":
        print(f"{tank_litters} liters left")
        break
    else:
        wanted_water.append(command)
        command = input()

