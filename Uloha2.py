import sys
import os
import re
from collections import defaultdict

"""
    Skript načíta všetky txt súbory z priečinka pomenovaného Subory,
    alebo načíta len vybrané súbory zadané ako argument pri spustení.
    Vytvorí tabuľku, ktorú zapíše do súboru vystup.txt.
    
"""

folder_of_logs = "Subory"

# Zistenie zoznamu súborov
if len(sys.argv) < 2:
    print("Nezadal si názvy súborov, načítavam obsah priečinka Subory...")
    sorted_list_of_files = sorted([f for f in os.listdir(folder_of_logs) if f.endswith(".txt")])
else:
    sorted_list_of_files = sorted(sys.argv[1:])

# Overím, či priečinok súbory obsahuje txt súbory
if not sorted_list_of_files:
    print("Priečinok Subory neobsahuje textové súbory.")
    sys.exit(1)

# Filtrovanie prázdnych súborov
non_empty_files = []
for i, file_name in enumerate(sorted_list_of_files):
    file_path = os.path.join(folder_of_logs, file_name)
    if os.path.getsize(file_path) > 0:
        non_empty_files.append(file_name)
    else:
        print(f"{file_name} (index {i}) je prázdny súbor.")

FILES_COUNT = len(non_empty_files)

if FILES_COUNT == 0:
    print("Všetky súbory sú prázdne. Ukončujem program.")
    sys.exit(1)

# Inicializácia dátovej štruktúry
logs_by_time = defaultdict(lambda: [" "] * FILES_COUNT)

# Funkcia na parsovanie riadku logu
def split_line_to_time_and_text(line):
    parts = line.strip().split(None, 1)  # rozdelí podľa prvej medzery (1 alebo viac)
    if len(parts) < 2:
        return parts[0], ""
    return parts[0], parts[1]

# Regex na kontrolu času v tvare hh:mm:ss alebo hh:mm:ss.xxx
TIME_PATTERN = re.compile(r"^\d{2}:\d{2}:\d{2}(\.\d+)?$")

# Funkcia na načítanie súboru do logs_by_time
def load_file(path_to_file, index_of_file):
    with open(path_to_file, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, 1):
            time, text = split_line_to_time_and_text(line)

            # Kontrola správneho formátu časovej značky
            if not TIME_PATTERN.match(time):
                print(f"Chybný formát času v súbore {path_to_file}, riadok {line_number}: '{line.strip()}'")
                continue  # tento riadok preskočíme

            if time and logs_by_time[time][index_of_file] == " ":
                logs_by_time[time][index_of_file] = text

# Načítanie dát z neprázdnych súborov
for i, file_name in enumerate(non_empty_files):
    file_path = os.path.join(folder_of_logs, file_name)
    load_file(file_path, i)

# Výpočet maximálnej šírky stĺpcov
max_leng_in_column = [len("Čas")] + [len(f) for f in non_empty_files]

for time, log_text in logs_by_time.items():
    max_leng_in_column[0] = max(max_leng_in_column[0], len(time))
    for i, value in enumerate(log_text):
        max_leng_in_column[i + 1] = max(max_leng_in_column[i + 1], len(value))

# Funkcia na formátovanie riadkov do tabuľky
def format_row(values):
    return " | ".join(str(h).ljust(max_leng_in_column[i]) for i, h in enumerate(values))

# Vytvorenie výstupného súboru
with open("vystup.txt", "w", encoding="utf-8") as output:
    # Hlavička
    header = ["Čas"] + non_empty_files
    output.write(format_row(header) + "\n")

    # Oddelovacia čiara
    full_width = sum(max_leng_in_column) + 3 * FILES_COUNT  # 3 znaky na každý " | "
    output.write("-" * full_width + "\n")

    # Údaje podľa časov
    for time in sorted(logs_by_time):
        raw = [time] + logs_by_time[time]
        output.write(format_row(raw) + "\n")

print("Tabuľka bola zapísaná do súboru 'vystup.txt'")
