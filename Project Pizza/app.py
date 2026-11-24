import sqlite3
import time
import os
import bcrypt
import sys
# 1. Connect to a database (creates the file if it doesn't exist)
conn = sqlite3.connect("restaurant.db")
cursor = conn.cursor()

# 2. Execute the CREATE TABLE query
cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu (
        foodID INTEGER PRIMARY KEY AUTOINCREMENT,
        categoryid INTEGER,
        Food TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sizes (
        sizeID INTEGER PRIMARY KEY AUTOINCREMENT,
        size TEXT,
        price REAL NOT NULL
    );
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS category (
        categoryid INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT
    );
""")
cursor.execute("""
SELECT * FROM Menu; """)

all_menu_items = cursor.fetchall()

categories = cursor.execute("""
SELECT * FROM category""")
categories = cursor.fetchall()
sizee = cursor.execute("""
SELECT * FROM sizes""")
sizee = cursor.fetchall()

lirli = cursor.execute("""
SELECT foodid FROM menu""")
lirli = cursor.fetchall()

sizee2 = cursor.execute("SELECT sizeID FROM sizes")
sizee2 = cursor.fetchall()


employeename = cursor.execute("SELECT employeeusername FROM employee")
employeename = cursor.fetchall()
employeeidd = cursor.execute("SELECT employeeid FROM employee")
employeeidd = cursor.fetchall()
employeepass = cursor.execute("SELECT password FROM employee")
employeepass = cursor.fetchall()
descri = cursor.execute("SELECT description FROM employee")
descri = cursor.fetchall()


Answer = 'Flowey'
pricee = cursor.execute("SELECT Price FROM menu")
pricee = cursor.fetchall()
Price0 = 0
Price2 = 0
Price1 = 0
Deathrow = None
C = 0
Size1 = []
Choose = 0
Order = []
TPrice = 0
Select = None
Cart = []
Select2 = None
Select3 = None
Choose2 = 0
User = None
Choose3 = 0
hehe = -1000




import time


RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

def idiot():
    hehe = -1000
    
    while True:
        print(f"Flowey's menacing Appearance in The Underground{RESET}")
        time.sleep(0.0001)
        
        print(f"{BOLD}YOU CANNOT ESCAPE! HAAHAHAHAAHAHHAAAAAAAAAAAAAA!{RESET}")
        hehe += 1
        
        if hehe == 0:
            print("Oh nvm... Heres a break!")
            time.sleep(5)
            print("Your gonna escape...")
            time.sleep(5)
            print(f"{RED}NOT! HAHAHAAHAHAHAHHA~{RESET}")
            time.sleep(2)
            continue
            
        if hehe == 150000:
            print(f"{YELLOW}You know What? I feel bad for you.{RESET}")
            time.sleep(2)
            
            Question = input("What is my Name? ")
            
            if Question.strip().lower() == "asriel dreemur or flowey":
                print(f"Alright, your ccorrect!{RESET}")
                break
            else:
                fake_flowey_uninstall()
def fake_flowey_uninstall():
    print(f"{RED}{BOLD}I'M COMING FOR YOU.{RESET}")
    time.sleep(1.5)
    
    print(f"\n{YELLOW}[SYSTEM ERROR] Flowey acquired root privileges.{RESET}")
    time.sleep(1)
    
    fake_files = [
        "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
        "Deleting extensions: ms-python.python...",
        "Wiping user settings and keybindings...",
        "Clearing workspace cache...",
        "Uninstalling Visual Studio Code core package..."
    ]
    
    for item in fake_files:
        print(f"{RED}[DELETING] {item}{RESET}")
        time.sleep(0.8)
        
    print(f"\n{RED}{BOLD}VS CODE HAS BEEN UNINSTALLED. GOODBYE!{RESET}")
    time.sleep(1.5)
    
    # Just kill VS Code normally so they think it got deleted
    os.system("taskkill /F /IM Code.exe")
    sys.exit()






sans_lines = [
    r"██████████▀▀▀▀▀▀▀▀▀▀▀▀▀██████████",
    r"█████▀▀░░░░░░░░░░░░░░░░░░░▀▀█████",
    r"███▀░░░░░░░░░░░░░░░░░░░░░░░░░▀███",
    r"██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██",
    r"█░░░░░░▄▄▄▄▄▄░░░░░░░░▄▄▄▄▄▄░░░░░█",
    r"█░░░▄██▀░░░▀██░░░░░░██▀░░░▀██▄░░█",
    r"█░░░██▄░░▀░░▄█░░░░░░█▄░░▀░░▄██░░█",
    r"██░░░▀▀█▄▄▄██░░░██░░░██▄▄▄█▀▀░░██",
    r"███░░░░░░▄▄▀░░░████░░░▀▄▄░░░░░███",
    r"██░░░░░█▄░░░░░░▀▀▀▀░░░░░░░█▄░░░██",
    r"██░░░▀▀█░█▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀██▀▀░░██",
    r"███░░░░░▀█▄░░█░░█░░░█░░█▄▀░░░░███",
    r"████▄░░░░░░▀▀█▄▄█▄▄▄█▄▀▀░░░░▄████",
    r"███████▄▄▄▄░░░░░░░░░░░░▄▄▄███████"
]

def print_sans():
    for line in sans_lines:
        print(line)
        time.sleep(0.02)





while True:
    try:
        Choose2 = int (input("Who are You? 1. Admin 2. Customer 3. Exit"))
    except ValueError:
        print("Today I will show you a piece of Info about a Character. Enjoy!"
        "Thic [WAIT WAIT CHILL HERE, don't put that K- NONO]k Thighs [GOOOSH]"
        "Thick Stomach [Tf does that mean]"
        "Thick Brain [Only Normal One]")
        continue

    if Choose2 == 2:
            while True:
                try:
                    Choose = int (input("1. Order 2. See Menu 3. Shopping Cart 4. Exit [P.S Sometimes the system can say weird things]: "))
                except ValueError:
                    print("Hello, I'm Verity! Your personal helper friend. Ask me anything, I know Everything!")
                    continue
                if Choose == 1:
                    for category in categories:
                        print(f"{category[0]} - {category[1]}\n")
                    Select = input("What Category? ")
                # 1. Parameterized query (safe from SQL injection)
                    cursor.execute("SELECT * FROM Menu WHERE categoryid = ?;", (Select,))
                    Pick = cursor.fetchall()
                # 2. Your loop displaying the filtered items
                    if Pick:
                        print("\n--- Items Available ---")
                        for picks in Pick:
                            print(f" FoodId: {picks[0]} - CatgId: {picks[1]} - Food: {picks[2]} - Price: ${picks[3]}\n")
                    else:
                        print("Invalid category selected.\n")
                        continue
                    cursor.execute("SELECT * FROM sizes")
                    Size1 = cursor.fetchall()
                # 2. Your loop displaying the filtered items
                    if Size1:
                        print("\n--- Sizes Available ---")
                        for Sizs in Size1:
                            print(f"{Sizs[0]} - {Sizs[1]} - %{Sizs[2]}\n")
                    else:
                        print("This does not exist")
                    print(Select)
                    while True:
                        try:
                            Select2 = int (input("What Item? "))
                        except ValueError:
                            print("SO STOP BEING SO DAMN ANNOYING! NGAHHHHHHHH")
                            continue
                        if Select2:
                            break
                    for id in lirli:
                        if Select2 in id:
                            print("Noted")
                            C = 1
                            break
                        else:
                            print("It's KILL or BE killed -A tiny Talking Flower")
                            C = 0
                    while True:
                        try:
                            C = int (input("Did you choose Correctly? 1. Yes 2. No "))
                        except ValueError:
                            print("You Sneaky little brat-")
                            continue
                        if C:
                            break
                    if C == 1:
                        while True:
                            try:
                                Select3 = int (input("What Size? "))
                            except ValueError:
                                print("Hello there mate I'm a Genderless child.")
                                continue
                            if Select3:
                                break
                        for id2 in sizee2:
                            if Select3 in id2:
                                cursor.execute("SELECT Food FROM menu WHERE foodID = ? AND categoryid = ?", (Select2, Select,))
                                Order = cursor.fetchall()
                                Sizeorder = cursor.execute("SELECT size FROM sizes WHERE sizeID = ?;", (Select3,))
                                Sizeorder = cursor.fetchall()
                                Cart.append("Food: ")
                                Cart.append(Order[0][0])
                                Cart.append("Size: ")
                                Cart.append(Sizeorder[0][0])
                                Price1 = cursor.execute("SELECT price FROM menu WHERE foodID = ?;", (Select2,))
                                row = cursor.fetchone() 
                                Price2 = cursor.execute("SELECT price FROM sizes WHERE sizeID = ?", (Select3,))
                                Price2 = cursor.fetchone()
                                if row:
                                    Price0 += row[0] * (Price2[0] / 100)
                                print("Order Successful!")
                                break
                            else:
                                print("[BLANK] will happen in 7 Days")
                elif Choose == 3:
                    print("Your Shopping Cart:", Cart)
                    while True:
                        try:
                            Choose2 = int (input("1. Go back 2. Check out 3. Remove Items 4. Clear Cart "))
                            if Choose2 == 1:
                                break
                            elif Choose2 == 2:
                                while True:
                                    try:
                                        Choose3 = int (input("Are you sure? 1. Yes 2. No "))
                                    except ValueError:
                                        print("Interstellar Retribution")
                                        continue
                                    if Choose3:
                                        break
                                if Choose3 == 1:
                                    print("Please press 4 in the main Menu to Exit.")
                                    break
                                elif Choose3 == 2:
                                    print("...")
                                    continue
                                else:
                                    print("Skibidi Toilet dob dob yes yes")
                            elif Choose2 == 3:
                                # FIX #3 (Part 2): Safely check and remove item without crashing
                                if Cart:
                                    Deathrow = input("What Items would you like to Remove? ")
                                    for trili in Cart:
                                        if Deathrow in trili:
                                            Cart.remove(Deathrow)
                                            print(Deathrow, " Removed.")
                                            break
                                        else:
                                            print(f"A Human, A Monster, and a Prince of the Dark")
                                            print(trili)
                                else:
                                    print("Blud your not Einstein you don't have Items Mr. Ein and stein")
                            elif Choose2 == 4:
                                Cart = []
                                print("Cart Cleared!")
                            else:
                                print("NO! I, THE GREAT PAPYRUS, MUST CAPTURE A HUMAN!")
                            
                        except ValueError:
                            print("David Baszucki is your Dad!")
                elif Choose == 2:
                    print(all_menu_items)
                    print(categories)
                    print(sizee)
                elif Choose == 4:
                    print("Bye!")
                else:
                    print("It's Either Spanish or Vaaanish")
    elif Choose2 == 3:
        break

    elif Choose2 == 1:
        User = input("What User are you?")
        passi = input("What's the Password?")
        while True:
            try:
                ImnamingthisUndynecuzIlikeAlphysrahh = int (input("Is your password Correct? If you forgot, press 2., if not, press 1."))
            except ValueError:
                print("Sheepy you are so Silly, dirin dirin")
                continue
            if ImnamingthisUndynecuzIlikeAlphysrahh:
                break
        if ImnamingthisUndynecuzIlikeAlphysrahh == 1:
            
            # --- FIXED: Fetch stored password hash from DB ---
            cursor.execute("SELECT password FROM employee WHERE employeeusername = ?", (User,))
            row = cursor.fetchone()
            
            # --- FIXED: Verify plaintext 'passi' against the bcrypt hash ---
            if row and bcrypt.checkpw(passi.encode('utf-8'), row[0].encode('utf-8')):
                print("Wow log-in")
                while True:
                    try:
                        Choose3 = int (input("1. Profile 2. Manage The Menu 3. View the Database 4. Change your Password 5. Hire/Fire Employees 6. Exit: "))
                    except ValueError:
                        print("OH MY GOD, THE MOBILE TASK FORCE SQUAD, THAT NO ONE STOPS, IT IS THE NINE-TAILED-FOX")
                        continue
                    if Choose3 == 1:
                        print("User:", User)
                        # --- FIXED: Removed password query check since user is logged in ---
                        cursor.execute("SELECT Rank FROM employee WHERE employeeusername = ?", (User,))
                        ran = cursor.fetchall()
                        print("Rank:", ran)
                        print("Description:", descri)
                        continue
                    elif Choose3 == 2:
                        while True:
                            try:
                                Choose4 =  int(input("1. Add new Food 2. Overwrite Price 3. Remove Food: "))
                            except ValueError:
                                print("if you mess with my brother, your gonna have a bad time.")
                                continue
                            if Choose4:
                                break
                        if Choose4 == 1:
                            foodie = input("What Food? ")
                            
                            # Check if foodie is not empty AND contains only letters
                            if foodie:
                                print("")
                            else:
                                print("....YOU... YOU IDIOT. YOU THINK I'M STUPID? HAHHHAHA")
                                time.sleep(2)
                                print("I feel bad for you, try again.")
                            while True:
                                try:
                                    catty = int (input("What Category is it in? 1. Pizza 2. Appetizer 3. Burger 4. Drink 5. Pasta 6. Salad: "))
                                except ValueError:
                                    idiot()
                                    continue
                                if catty:
                                    break
                            while True:
                                try:
                                    pice = int(input("Price [Only include the Number]: "))
                                except ValueError:
                                    print("Two possibilities exist: either we are alone in the Universe or we are not. Both are equally terrifying")
                                    continue
                                if pice:
                                    break
                            while True:
                                try:
                                    Yes = int(input("Now, do you want to do this? 1. Yes 2. No"))
                                except ValueError:
                                    print("Dog please stop spamming wrong shi.")
                                    continue
                                if Yes:
                                    if Yes == 1:
                                        cursor.execute("INSERT INTO Menu VALUES (NULL, ?, ?, ?)", (catty, foodie, pice,))
                                        conn.commit()
                                        break
                                    if Yes == 2:
                                        print("Okay")
                                        foodie = None
                                        catty = 0
                                        pice = 0
                                        break
                                    else:
                                        print("I'M IN THE THICK OF IT EVERYBODY KNOWS!")
                                        continue
                        elif Choose4 == 2:
                            while True:
                                try:
                                    Choose3 = int (input("Please give the FoodID."))
                                except ValueError:
                                    print("El cucuy is coming to your house")
                                    continue
                                if Choose3:
                                    break
                            while True:
                                try:
                                    pice = int (input("New Price: "))
                                except ValueError:
                                    print("Cause I'm happy, clap your hands if you see a room without a roof")
                                    continue
                                if pice:
                                    break
                            cursor.execute("UPDATE menu SET price = ? WHERE foodID = ?", (pice, Choose3,))
                            conn.commit()
                        elif Choose4 == 3:
                            while True:
                                try:
                                    Choose3 = int (input("Please give the FoodID."))
                                except ValueError:
                                    print("You don't want to delete it aren'tchya")
                                    continue
                                if Choose3:
                                    break
                            while True:
                                try:
                                    Choose5 = int (input("ARE YOU SURE? 1. yes 2. no"))
                                except ValueError:
                                    print("When the balance of Dark and light are broken, Earth will take her last breath.")
                                    continue
                                if Choose5:
                                    break
                            if Choose5 == 1:
                                cursor.execute("DELETE FROM menu WHERE foodID = ?", (Choose3,))
                                conn.commit()
                            else:
                                continue
                        else:
                            print_sans()
                    elif Choose3 == 3:
                        Choose3 = input("What Table?")
                        cursor.execute(f"SELECT * FROM {Choose3}")
                        cam = cursor.fetchall()
                        print(cam)
                    elif Choose3 == 4:
                        while True:
                            try:
                                Choose3 = int (input("Are you Sure? 1. Yes 2. No "))
                            except ValueError:
                                print("Ah Shi, here we go again.")
                            if Choose3:
                                break
                        if Choose3 == 1:
                            User = input("User: ")
                            Pass1 = input("Pervious Password: ")
                            Pass2 = input("New Password: ")
                            
                            # Hey it's me Verity
                            cursor.execute("SELECT password FROM employee WHERE employeeusername = ?;", (User,))
                            row = cursor.fetchone()
                            
                            if row and bcrypt.checkpw(Pass1.encode('utf-8'), row[0].encode('utf-8')):
                                new_hash = bcrypt.hashpw(Pass2.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                                cursor.execute("UPDATE employee SET password = ? WHERE employeeusername = ?", (new_hash, User,))
                                conn.commit()
                            else:
                                print("What's this diddy blud doing on the calculator?")
                        else:
                            print("Oh I am a Gummibar, yes I'm a Gummibar, oh I'm a Lucky Funny Jelly Gummy Bear")

                    elif Choose3 == 6:
                        print("Byaaaa!")
                        break
                    elif Choose3 == 5:
                        cursor.execute("SELECT Rank FROM employee WHERE employeeusername = ?;", (User,))
                        ran = cursor.fetchall()
                        for rni in ran[0]:
                            if ran[0][0] == 'Head Manager':
                                while True:
                                    try:
                                        Choose3 = int (input("1. Add Employee 2. Remove Employee"))
                                    except ValueError:
                                        print("DIE FACHEN HOCH!1 HER WASSELD DANE SCHWEZER HESCH WASSERLAD")
                                    if Choose3 == 1:
                                        print("Please fill in their Details:")
                                        passi = input("Password: ")
                                        User = input("Username: ")
                                        Ranka = input("Rank: ")
                                        Description = input("Description: ")
                                        cursor.execute("INSERT INTO employee VALUES NULL,?, ?, ?, ?", (User, Description, passi, Ranka,))
                                        conn.commit()
                                        print("Employee added!")
                                    elif Choose3 == 2:
                                        print("PEN PINEAPPLE APPLE PEN")
                                    else:
                                        print("Vengaboys are back in town!")
                            else:
                                print("CAN YOU TWO SMOOCH ALREADY? THE AUDIENCE IS DYING FOR SOME ROMANCE!")
                    else:
                        print("Uh.. Yeah, T-to make Mettaton more entertaining I-I made him a Human Killer Machine.")
            else:
                print("SCREW IT, WHY SHOULD I TELL THE HUMAN THE INFO WHEN THEY'RE GONNA DIE ANYWAY? NGAHHHHHHHHHHHHHH!")
        elif ImnamingthisUndynecuzIlikeAlphysrahh == 2:
                User = input("User: ")
                Pass2 = input("New Password: ")
                
                # Hey it's me Verity
                cursor.execute("SELECT password FROM employee WHERE employeeusername = ?;", (User,))
                row = cursor.fetchone()
                new_hash = bcrypt.hashpw(Pass2.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                cursor.execute("UPDATE employee SET password = ? WHERE employeeusername = ?", (new_hash, User,))
                conn.commit()
    elif Choose2 == "flowey":
        idiot()
    else:
        print("DRIVING IN MY CAR RIGHT AFTER A BEER, HEY THAT BUMP [Frisk] IS SHAPED LIKE A DEER, D-U-I HOW ABOUT YOU DIE I'LL GO A HUNDRED MILES... IN AN HOUR")
# 3. Save (commit) changes and close the connection
conn.commit()
conn.close()
print("Your Order: ", Cart)
print("Price:", Price0)


