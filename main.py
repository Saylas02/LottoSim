import random as r

def generate_random_number(low, high) -> int:
    return r.randint(low, high)

def generate_ticket() -> list[int]:
    ticket = [0, 0, 0, 0, 0, 0]
    for i in range(0,6):
        while True:
            value:int = generate_random_number(1,49)
            if int(value) not in ticket:
                ticket[i] = int(value)
                break
    return ticket

def check_matches(con, mas)-> int:
    m = 0
    for e in con:
        if e in mas:
            m += 1
    return m

def game_process( bonus:bool ) -> None:
    ticket_amount:int = 0
    game_bonus_num:int = 0
    match_count = [0, 0, 0, 0, 0, 0]

    master_ticket = generate_ticket()

    if bonus:
        game_bonus_num = generate_random_number(1,6)

    if not bonus:
        print(f"Master ticket: {master_ticket}")
    elif bonus:
        print(f"Master ticket / Bonus Number: {master_ticket}/{game_bonus_num}")

    while True:
        ticket_amount += 1
        consumer_ticket = generate_ticket()
        matches = check_matches(consumer_ticket, master_ticket)
        if matches == 1:
            match_count[0] += 1
        elif matches == 2:
            match_count[1] += 1
        elif matches == 3:
            match_count[2] += 1
        elif matches == 4:
            match_count[3] += 1
        elif matches == 5:
            match_count[4] += 1
        elif matches == 6:
            match_count[5] += 1
            if not bonus:
                break
            else:
                ticket_bonus_num = generate_random_number(1,6)
                if game_bonus_num == ticket_bonus_num:
                    print(f"Correct bonus: {ticket_bonus_num}, master: {game_bonus_num}")
                    break
                else:
                    print(f"Wrong bonus: {ticket_bonus_num}, master: {game_bonus_num}")



    price = ticket_amount * 1.20
    price = "${:,.2f}".format(price)

    print("")
    print("")

    print("*************** S T A T S ***************")
    print(f"Total tickets bought: {ticket_amount}")
    print(f"Total matches overview: {match_count}")
    print(f"Total ticket price (1,20€): {price}")
    print("*****************************************")

if __name__ == "__main__":
    game_process( bonus = True )
