import openpyxl

wb = openpyxl.load_workbook("12612645.xlsx", data_only=True)
ws = wb["Daily_Log"]



records = []

for row in ws.iter_rows(min_row=6, max_row=41, values_only=False):

    record = {
        "date": row[0].value,
        "sleep": row[1].value,
        "fitness": row[2].value,
        "study": row[3].value,
        "coding": row[4].value,
        "class": row[5].value,
        "classes_attended": row[6].value,
        "other": row[7].value,
        "total_tracked": row[8].value,
        "free_time": row[9].value,
        "feeling": row[10].value,
        "satisfaction": row[11].value,
        "energy": row[12].value,
    }

    records.append(record)

valid_days = len(records)

print("Number of records:", valid_days)



#Function for TPi
def tpi():
    print("\n")
    total_cod = 0

    for record in records:
        total_cod = total_cod + record["coding"]

    valid_d = len(records)

    TPI = total_cod / valid_d

    print("Total coding time:", total_cod, "minutes")
    print("Valid days:", valid_d)
    print("TPI:", TPI, "minutes/day\n")
    return TPI

#function for AII
def aii():
    total_academic = 0

    for record in records:
        total_academic = total_academic + record["study"] + record["class"]

    valid_days = len(records)
    AII = total_academic / valid_days

    print("Total academic time:", total_academic, "minutes")
    print("AAI:", AII, "minutes/day\n")
    return AII

#Function for PhAI
def phai():
    total_fitness = 0

    for record in records:
        total_fitness = total_fitness + record["fitness"]

    valid_days = len(records)
    PhAI = total_fitness / valid_days

    print("Total fitness time: ", total_fitness, "minutes")
    print("PhAI: ", PhAI, "minutes/day\n")
    return PhAI

#Function for sleep recovery index
def sri():
    total_sleep = 0
    for record in records:
        total_sleep = total_sleep + record["sleep"]

    valid_days = len(records)
    SRI = total_sleep / valid_days

    print("Total sleep time: ", total_sleep, "minutes")
    print("SRI: ", SRI, "minutes/day\n")
    return SRI


#Function for Abi
def abi():
    total_uncountedt = 0
    for record in records:
        total_uncountedt = total_uncountedt + record["free_time"]

    valid_days = len(records)
    ABI = total_uncountedt / valid_days

    print("Total Free/Uncounted time: ", total_uncountedt, "minutes")
    print("ABI: ", ABI, "minutes/day\n")
    return ABI

#Function for TUI
def tui():
    total_utilizedt = 0
    for record in records:
        total_utilizedt = total_utilizedt + record["total_tracked"]
    valid_days = len(records)
    TUI = total_utilizedt / valid_days

    print("Total tracked time: ", total_utilizedt, "minutes")
    print("TUI: ", TUI, "minutes/day\n")
    return TUI


#We are scalling the 3 columns which are in the form of text. 
feeling_values = {
    "Excellent": 5,
    "Good": 4,
    "Neutral": 3,
    "Low": 2,
    "Stressed": 1
}

satisfaction_values = {
    "Very Satisfied": 5,
    "Satisfied": 4,
    "Neutral": 3,
    "Unsatisfied": 2,
    "Very Unsatisfied": 1
}

energy_values = {
    "High": 5,
    "Medium": 3,
    "Low": 1
}


#Function for EI
def ei():
    total_experience = 0

    for record in records:
        feeling = feeling_values[record["feeling"]]
        satisfaction = satisfaction_values[record["satisfaction"]]
        energy = energy_values[record["energy"]]

        total_experience = total_experience + feeling + satisfaction + energy

    EI = total_experience / (3 * valid_days)

    print("EI:", round(EI, 2))
    return EI


#Function for DCI
def dci():
    from datetime import datetime

    start_date = datetime(2026, 8, 17)
    end_date = datetime(2026, 9, 21)

    expected_days = (end_date - start_date).days + 1

    DCI = (valid_days / expected_days) * 100

    print("Valid recorded days:", valid_days)
    print("Expected days:", expected_days)
    print("DCI:", DCI, "%\n")
    return DCI


#Correlation between Coding and Energy
def coding_energy():
    x = []
    y = []

    for record in records:
        x.append(record["coding"])
        y.append(energy_values[record["energy"]])


    n = len(x)

    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0

    for i in range(n):
        sum_x = sum_x + x[i]
        sum_y = sum_y + y[i]
        sum_xy = sum_xy + x[i] * y[i]
        sum_x2 = sum_x2 + x[i] * x[i]
        sum_y2 = sum_y2 + y[i] * y[i]

    numerator = n * sum_xy - sum_x * sum_y

    denominator = ((n * sum_x2 - sum_x * sum_x) *
                (n * sum_y2 - sum_y * sum_y)) ** 0.5

    coding_energy = numerator / denominator

    print("Coding-Energy correlation:", round(coding_energy, 2))



#Correlation between Sleep and Energy
def sleep_energy():
    x = []
    y = []

    for record in records:
        x.append(record["sleep"])
        y.append(energy_values[record["energy"]])

    n = len(x)

    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0

    for i in range(n):
        sum_x = sum_x + x[i]
        sum_y = sum_y + y[i]
        sum_xy = sum_xy + x[i] * y[i]
        sum_x2 = sum_x2 + x[i] * x[i]
        sum_y2 = sum_y2 + y[i] * y[i]

    numerator = n * sum_xy - sum_x * sum_y

    denominator = ((n * sum_x2 - sum_x * sum_x) *
                (n * sum_y2 - sum_y * sum_y)) ** 0.5

    sleep_energy = numerator / denominator

    print("Sleep-Energy correlation:", round(sleep_energy, 2))


#Correlation between Study and Satisfaction
def study_satisfaction():
    x = []
    y = []

    for record in records:
        x.append(record["study"])
        y.append(satisfaction_values[record["satisfaction"]])

    n = len(x)

    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0

    for i in range(n):
        sum_x = sum_x + x[i]
        sum_y = sum_y + y[i]
        sum_xy = sum_xy + x[i] * y[i]
        sum_x2 = sum_x2 + x[i] * x[i]
        sum_y2 = sum_y2 + y[i] * y[i]

    numerator = n * sum_xy - sum_x * sum_y

    denominator = ((n * sum_x2 - sum_x * sum_x) *
                (n * sum_y2 - sum_y * sum_y)) ** 0.5

    study_satisfaction = numerator / denominator

    print("Study-Satisfaction correlation:", round(study_satisfaction, 2))


#Correlation between class and Energy
def class_energy(): 
    x = []
    y = []

    for record in records:
        x.append(record["class"])
        y.append(energy_values[record["energy"]])


    n = len(x)

    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0

    for i in range(n):
        sum_x = sum_x + x[i]
        sum_y = sum_y + y[i]
        sum_xy = sum_xy + x[i] * y[i]
        sum_x2 = sum_x2 + x[i] * x[i]
        sum_y2 = sum_y2 + y[i] * y[i]

    numerator = n * sum_xy - sum_x * sum_y

    denominator = ((n * sum_x2 - sum_x * sum_x) *
                (n * sum_y2 - sum_y * sum_y)) ** 0.5

    class_energy = numerator / denominator

    print("Class-Energy correlation:", round(class_energy, 2))


def average_class():
    total_class = 0
    for record in records:
        total_class = total_class + record["class"]

    print("Average class/day: ", total_class/valid_days)

def average_other():
    oat = 0
    for record in records:
        oat = oat + record["other"]

    print("Average Other Activity/dahy: ", oat/valid_days)

def average_free_time():
    free_time = 0
    for record in records:
        free_time = free_time + record["free_time"]

    print("Average Free/Uncounted time/day: ", free_time/valid_days)

#Function for PAI

#Function for PAI
def pai():
    tpi_value = tpi()
    aai_value = aii()
    phai_value = phai()
    sri_value = sri()
    tui_value = tui()
    ei_value = ei()
    dci_value = dci()

    PAI = (0.15 * tpi_value) + (0.20 * aai_value) + (0.15 * phai_value) + (0.20 * sri_value) + (0.15 * tui_value) + (0.10 * ei_value) + (0.05 * dci_value)

    print("PAI:", round(PAI, 2))

tpi()
aii()
phai()
sri()
abi()
tui()
ei()
dci()
coding_energy()
sleep_energy()
study_satisfaction()
class_energy()
average_class()
average_other()
average_free_time()
pai()