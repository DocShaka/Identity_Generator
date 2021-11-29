import secrets
import string
import uuid
import os
import random
import string
import os
from faker import Faker
from faker import providers
from faker.providers import internet
from random import choice, randint
from art import *
from termcolor import colored 

fake = Faker()
fake1 = Faker(['it_IT', 'en_US', 'ja_JP', 'fr_FR'])


def main():
    
    #ascii art 
    print("="*95)
    #print(".___    .___             __  .__  __             ________                                   __                ") 
    #print("|   | __| _/____   _____/  |_|__|/  |_ ___.__.  /  _____/  ____   ____   ________________ _/  |_  ___________ ")
    #print("|   |/ __ |/ __ \ /    \   __\  \   __<   |  | /   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \")
    #print("|   / /_/ \  ___/|   |  \  | |  ||  |  \___  | \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/")
    #print("|___\____ |\___  >___|  /__| |__||__|  / ____|  \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   ")
    #print("         \/    \/     \/               \/              \/     \/     \/     \/           \/                   ")
    
    print(colored(text2art ("\t____________________\n"),'blue'))
    print(colored(text2art ("\t__Identity_Generator__"),'white'))
    print(colored(text2art ("\t______________________"),'red')) 
                         

    try:

        print("="*95)

        print("\n\t[!] Bienvenue dans le sniffer [!]\n")

        print("\t[+] En cours de Recherche d'une victime.....\n")
        
        print("\t[+] Victime Trouvé !\n")

        # generate private information

        fake1.name()
        fake.ssn()
        fake.address()
        fake.text()
        fake.add_provider(internet)
        
        for _ in range(1):
            print("Nom & Prénom =", fake1.name())
            print("Adresse =", fake.address())
            print("Numéro de Téléphone =", fake.ssn())
            print("Ipv4 =", fake.ipv4_private())

        # secure random string
        secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(20)))
        print("Mot de passe courant =", (secure_str))

        # secure password
        password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))
        print("Mot de passe interface de connection =", (password))

        # generate a random string token
        print("Adresse M.A.C =", secrets.token_hex(1),":",secrets.token_hex(1),":",secrets.token_hex(1),":",secrets.token_hex(1),":",secrets.token_hex(1),":",secrets.token_hex(1))

        # generate universally unique secure random string Id
        stringId  = uuid.uuid4()
        print("Hash identifiant active directorie =", stringId)
        
        print("\n\tVoulez vous Refaire une Génération ? (y/n)")
        choice = input("\t> ")

        if choice == 'y':
            main()
        
        elif choice == 'n':
            print("\t[!] Au Revoir !!")


    except KeyboardInterrupt:
        print("\n\t[!] Vous avez appuyé sur ctrl + C pour quitter instantanément")

main()
