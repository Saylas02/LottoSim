import multiprocessing as mp
import random as r
import time as t
import csv

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

def append_stats_to_csv(rt:int, ti:int, tps:int, bal:list, mt:list, bon:int = "0") -> None:
    """Built .CSV-File: RT, TI, TIS, BAL, MT, BON"""
    with open("data.csv.csv", "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([rt, ti, tps, bal, mt, bon])

def game_process( bonus:bool, silent:bool ) -> None:
    start_time = t.time()
    ticket_amount:int = 0
    game_bonus_num:int = 0
    match_count = [0, 0, 0, 0, 0, 0]

    master_ticket = generate_ticket()

    if bonus:
        game_bonus_num = generate_random_number(1,6)

    if not bonus:
        if not silent:
            print(f"Master ticket: {master_ticket}")
    elif bonus:
        if not silent:
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
                    if not silent:
                        print(f"Correct bonus: {ticket_bonus_num}, master: {game_bonus_num}")
                    break
                else:
                    if not silent:
                        print(f"Wrong bonus: {ticket_bonus_num}, master: {game_bonus_num}")

    end_time = t.time()
    runtime = round(end_time - start_time)

    tickets_per_sec =  ticket_amount // runtime

    append_stats_to_csv(runtime, ticket_amount, tickets_per_sec, match_count, master_ticket, game_bonus_num)

    price = ticket_amount * 1.20
    price = "${:,.2f}".format(price)

    if not silent:
        print("")
        print("*************** S T A T S ***************")
        print(f"Total runtime: {runtime} seconds")
        print(f"Total tickets per second: {tickets_per_sec}")
        print(f"Total tickets bought: {ticket_amount}")
        print(f"Total matches overview: {match_count}")
        print(f"Total ticket price (1,20€): {price}")
        print("*****************************************")


if __name__ == "__main__":
    """multiprocessing"""
    mp.set_start_method('spawn')
    cores:int = mp.cpu_count()
    processes:list = []
    counter:int = 0

    while True:
        processes = [p for p in processes if p.is_alive()]

        if len(processes) < cores:
            p = mp.Process(target=game_process, args=(True, True))
            p.start()
            processes.append(p)
            print(f"Process {counter} started, active: {len(processes)}")
            counter += 1

        t.sleep(0.5)
