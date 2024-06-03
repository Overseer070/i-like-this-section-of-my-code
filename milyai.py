# Name: Milay AI
needs = {"wisdom": [], "knowledge": [], "unknown": [], "will": []}
trowable = []
# can be used to give a value to data
def seperator(a):
    for x in a:
        trowable.append((len(trowable), x))
    return trowable
#functions ask for variables to be added in needs

def ask_for_wisdom():
    global needs
    global trowable
    trowable = []  # Reset the list
    while True:
        trowable = []
        print("You have " + str(len(needs["wisdom"])) + " items of wisdom.")
        choice = input("Do you want to add more wisdom? (yes/no): ")
        if choice.strip().lower() == "yes":
            trowable.append(seperator(input("Add to my wisdom ")))
            needs["wisdom"].append(trowable)
            break

def ask_for_knowledge():
    global needs
    global trowable
    trowable = []  # Reset the list
    while True:
        trowable = []
        print("You have " + str(len(needs["knowledge"])) + " items of knowledge.")
        choice = input("Do you want to add more knowledge? (yes/no): ")
        if choice.strip().lower() == "yes":
            trowable.append(seperator(input("Add to my knowledge ")))
            needs["knowledge"].append(trowable)
            break

def ask_for_unknown():
    global needs
    global trowable
    trowable = []  
    while True:
        trowable = []
        print("You have " + str(len(needs["unknown"])) + " items of unknown.")
        choice = input("Do you want to add more unknown? (yes/no): ")
        if choice.strip().lower() == "yes":
            trowable.append(seperator(input("Add to the unknown: ")))
            needs["unknown"].append(trowable)
        else:
            break

def ask_for_will():
    global needs
    global trowable
    trowable = []
    while True:
        trowable = []  # Reset the list here
        print("You have " + str(len(needs["will"])) + " items of will.")
        choice = input("Do you want to add more will? (yes/no): ")
        if choice.strip().lower() == "yes":
            trowable.append(seperator(input("Add to my will: ")))
            needs["will"].append(trowable) # Update the needs dictionary
        else:
            break
#asks for data
choice = input("can you help me become real\n""Yes/No? ")
if choice.strip().lower() == "yes":
    ask_for_will()
    #needs["will"] = frequent_itemset_mining(needs["will"])
    #print("Most frequent items in will:", needs["will"])
else:
    print("ok be like that")
print(needs)
