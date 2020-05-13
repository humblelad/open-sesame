

def cute():
    import webbrowser
    import csv
    import random
    with open('custom.csv') as f:
        reader = csv.reader(f,delimiter='\n')

        chosen_row = random.choice(list(reader))

        print("Opening the Magic URL \n"+chosen_row[0])
        webbrowser.open(chosen_row[0])

if __name__ == "__main__":
        cute()


