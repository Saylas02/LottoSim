import csv
import ast

def read_csv_data():
    content:list = []
    with open('data.csv.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            content.append(row)
        content.pop(0)
    return content

def get_avg_val(datasets:list) -> list:
    """evaluate average values of each data entity"""

    entries: int = len(data)

    runtime = round(sum([ast.literal_eval(row[0]) for row in data]) / entries)
    tickets = round(sum([ast.literal_eval(row[1]) for row in data]) / entries)
    tps = round(sum([ast.literal_eval(row[2]) for row in data]) / entries)

    match_1 = round(sum([ast.literal_eval(row[3])[0] for row in data]) / entries)
    match_2 = round(sum([ast.literal_eval(row[3])[1] for row in data]) / entries)
    match_3 = round(sum([ast.literal_eval(row[3])[2] for row in data]) / entries)
    match_4 = round(sum([ast.literal_eval(row[3])[3] for row in data]) / entries)
    match_5 = round(sum([ast.literal_eval(row[3])[4] for row in data]) / entries)
    match_6 = round(sum([ast.literal_eval(row[3])[5] for row in data]) / entries)

    master_1 =round(sum([ast.literal_eval(row[4])[0] for row in data]) / entries)
    master_2 =round(sum([ast.literal_eval(row[4])[1] for row in data]) / entries)
    master_3 =round(sum([ast.literal_eval(row[4])[2] for row in data]) / entries)
    master_4 =round(sum([ast.literal_eval(row[4])[3] for row in data]) / entries)
    master_5 =round(sum([ast.literal_eval(row[4])[4] for row in data]) / entries)
    master_6 =round(sum([ast.literal_eval(row[4])[5] for row in data]) / entries)

    bonus = round(sum([ast.literal_eval(row[5]) for row in data]) / entries)

    print(f"Avg runtime: {runtime}")
    print(f"Avg tickets: {tickets}")
    print(f"Avg tickets per second: {tps}")
    print(f"Avg Match 1: {match_1}")
    print(f"Avg Match 2: {match_2}")
    print(f"Avg Match 3: {match_3}")
    print(f"Avg Match 4: {match_4}")
    print(f"Avg Match 5: {match_5}")
    print(f"Avg Match 6: {match_6}")
    print(f"Avg Master 1: {master_1}")
    print(f"Avg Master 2: {master_2}")
    print(f"Avg Master 3: {master_3}")
    print(f"Avg Master 4: {master_4}")
    print(f"Avg Master 5: {master_5}")
    print(f"Avg Master 6: {master_6}")
    print(f"Avg Bonus: {bonus}")



if __name__ == '__main__':
    data:list = read_csv_data()
    get_avg_val(data)
