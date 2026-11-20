from pyscript import document, display

#Dictionary of all nonmetals
nonmetals= {
    "H": ("H", "Hydrogen", 1, 1.008),
    "C": ("C", "Carbon", 6, 12.011),
    "N": ("N", "Nitrogen", 7, 14.007),
    "O": ("O", "Oxygen", 8, 15.999),
    "F": ("F", "Fluorine", 9, 18.998),
    "P": ("P", "Phosphorus", 15, 30.974),
    "S": ("S", "Sulfur", 16, 32.06),
    "Se": ("Se", "Selenium", 34, 78.971),
    "Cl": ("Cl", "Chlorine", 17, 35.45),
    "Br": ("Br", "Bromine", 35, 79.904),
    "I": ("I", "Iodine", 53, 126.904),
    "He": ("He", "Helium", 2, 4.003),
    "Ne": ("Ne", "Neon", 10, 20.180),
    "Ar": ("Ar", "Argon", 18, 39.948),
    "Kr": ("Kr", "Krypton", 36, 83.798),
    "Xe": ("Xe", "Xenon", 54, 131.293),
    "Rn": ("Rn", "Radon", 86, 222)
}
# Values, Non metal code, Non metal symbol, Name, Atomic Number, Atomic Mass

#function to search for a planet
def find_nonmetal(e):

    #Get the input FROM HTML
    nonmetal = document.getElementById("nonmetal").value.strip().capitalize()

    
    lookup = nonmetals.get(nonmetal, ("Nonmetal cannot be found", "-", "-", "-"))

    #display the properties
    
    document.getElementById("nonmetalcode").innerText = nonmetal
    document.getElementById("symbol").innerText = lookup[0]
    document.getElementById("element").innerText = lookup[1]
    document.getElementById("atomic number").innerText = lookup[2]
    document.getElementById("atomic mass").innerText = lookup[3]

###############################################################################

def add_name(e):

    first = document.getElementById('first').value  #first name
    last = document.getElementById('last').value    #last name
    full = first + ' ' + last + '(The newest member), ' #full name

    document.getElementById("output1").innerHTML = "" #clears the response after answering

    #list of all the members
    g10 = {"Logan Anaque, ", "Jacob Minguillo, ", "Gavin Ruiz, "}
    g9 = {"Robert Junior, ", "Boberto Junior, ", "Robertido Junior, "}
    g8 = {"Rick Grayson, ", "Bruce Wayne, ", "Clark Kent, "}  
    g7 = {"Wally West, ", "Barry Allen, ", "Oliver Queen, "}

    #combined the list of all the members
    all_members = g10.union(g9, g8, g7)
    all_members.add(full)

    #number of members
    combined_members = len(all_members)

    #the variable of the message
    message = full + ", you are officially a new member of ICT Club, joined by, "

    #it displays the message
    display(message + "".join(sorted(all_members)) + f" Total Members: {combined_members}", target = 'output1')

################################################################################

    names = ['Logan Anaque', 'Gavin Ruiz', 'Jacob Minguillo', 'Jhoanna Evnag    elista']

def check_name(e):

    #list of people in the club
    names = ['Logan Anaque', 'Gavin Ruiz', 'Jacob Minguillo', 'Jhoanna Evnagelista']

    #clears result
    document.getElementById("output1").innerHTML=" "

    #assiigns the first and last values
    first = document.getElementById('first').value
    last = document.getElementById('last').value

    full = first + " " + last
    realname = full in names

    #determines whether or not the member is in the club
    message = {

        True: "Your name is part of ICT club!",
        False: "Your name is not on the list of members"

    }

    #displays the message
    display(message[realname], target="output1")