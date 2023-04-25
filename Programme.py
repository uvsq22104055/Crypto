#Chiffrement par substitution mono-alphabétique. MARIE-MICHELE1
import random
import tkinter as tk

#création de l'alphabet
liste_a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("alphabet original:",liste_a)

#cle de substitution 
clef = list(liste_a)
random.shuffle(clef)
#clef = list("AZERTYUIOPQSDFGHJKLMWXCVBN")
print("nouvel alphabet:",clef)
message_en_clair = input("entrez votre message :")

#création de la fonction qui va chiffrer notre message
def chiffré_message(message_en_clair):
    #on créé une variable qui contiendra notre texte chiffré 
    message_chiffré = ""
    #on vérifie que chaque lettre ou caractere est dans l'alphabaet pré-définie.
    #on determine la position de la lettre dans la liste alphabet grace a index().on uttilise la position de la lettre dans la liste pour trouver la lettre correspondante dans l'alphabet de substitution
    #si la lettre ou le caractere n'est pas definie, celui ci est directemet renvoyer dans le message chiffré tels quel.
    #la fonction renvoie la variable message chiffre.
    for lettre in message_en_clair:
        if lettre in liste_a:
            indice = liste_a.index(lettre)
            lettre_chiffré = clef[indice]
            message_chiffré += lettre_chiffré
        else:
            message_chiffré += lettre
    return message_chiffré
#on appelle la fonction dans notre variable
message_chiffré = chiffré_message(message_en_clair)
print("message original:",message_en_clair)
print("message chiffré:",message_chiffré)

#décriptage MARIE-MICHELE2 
list_a = list("ABCDEFGHIJQLMNOPQRSTUVWXYZ")
#définir la clef de substitution 
clef = list(input("entrez votre clef:"))
#clef = list("AZERTYUIOPQSDFGHJKLMWXCVBN")
print(clef)

#définir une fonction pour déchiffrer un message 
def dechiffre_message(message_chiffre) : 
    message_dechiffré = ""
    #dechiffrer chaque caractere du message 
    for lettre_chiffre in message_chiffre: 
        if lettre_chiffre in clef : 
            indice = clef.index(lettre_chiffre)
            lettre_dechiffre = list_a[indice]
            message_dechiffré += lettre_dechiffre
        else:
            message_dechiffré += lettre_chiffre 
    return message_dechiffré

message_chiffre = input("entrez le message à dechiffrer : ")
message_dechiffré = dechiffre_message(message_chiffre)
print("message chiffré:", message_chiffre)
print("message déchiffré:",message_dechiffré)
#clef de substitution : AZERTYUIOPQSDFGHJKLMWXCVBN
#message à dechiffrer : ZGFPGWK EGDDTFM EA XA 
    

def cryptage_scytale(plaintext, key):
    key = int(key)
    ciphertext = [''] * key
    index = 0
    for letter in plaintext:
        ciphertext[index] += letter
        index = (index + 1) % key
    return ''.join(ciphertext)

# Fonction de déchiffrement de Scytale
def decryptage_scytale(ciphertext, key):
    key = int(key)
    plaintext = [''] * len(ciphertext)
    index = 0
    for i in range(len(ciphertext)):
        plaintext[i] = ciphertext[index]
        index = (index + 1) % key
    return ''.join(plaintext)

def vigenere_cryptage(c, cle):
    indice_cle = 0
    msg_code =""

    for i in range(0, len (c)):
        if 'A'<= c[i]<='Z':
            msg_code +=chr((((ord(c[i])-ord('A'))+(ord(cle[indice_cle])-ord('A')))%26)+ord('A'))
            indice_cle = (indice_cle + 1) % len(cle)
    else:
        msg_code +=c[i]
    return msg_code

print(vigenere('BONDOUR. A TOUS', 'PYTHON'))

def vigenere_decryptage(c, cle):
    indice_cle = 0
    msg_code =""

    for i in range(0, len (c)):
        if 'A'<= c[i]<='Z':
            msg_code +=chr((((ord(c[i])-ord('A'))-(ord(cle[indice_cle])-ord('A')))%26)+ord('A'))
            indice_cle = (indice_cle + 1) % len(cle)
    else:
        msg_code +=c[i]
    return msg_code


#CodeCesarTessaCryptage
def cryptage(message, cle) : 
    message_resultat = ""
    #Si la lettre est en majuscule on utilise la méthode ord() ce qui donne la table des lettres ASCII
    for i in range(len(message)):
        lettre = message[i]
        if 65 <= ord(lettre) <= 90 :
            lettre_chiffree = chr(65 + (ord(lettre) - 65 + cle)%26) #%26 permet de se balader dans l'alphabet, -65 permet de donner la position de la lettre
                                                     #cle permet le décalage de la lettre, +65 permet de trouver le décalage de la lettre dans la table
    #Si la lettre est en minuscule
        elif 97 <= ord(lettre) <= 122 :
            lettre_chiffree = chr(97 + (ord(lettre) - 97 + cle)% 26)
        else :
            lettre_chiffree = lettre
        message_resultat += lettre_chiffree
    return message_resultat

message = "Salut, moi c'est Tessa"
cle = 1
message_resultat = cryptage(message, cle)
print("Message chiffré:", message_resultat)

#CodeCesarTessaDecryptage
def decrypt_cesar(messagecode, cle):
    message = ""
    for lettre in messagecode:
        if 65 <= ord(lettre) <= 90:
            # Décale la lettre en fonction de la clé de chiffrement
            message += chr(65 + (ord(lettre) - cle - 65) % 26)
        elif 97 <= ord(lettre) <= 122 :
            message += chr(97 + (ord(lettre) - cle - 97)% 26)
        
        else:
            message += lettre
    return message

messagecode = "Cpotpjs, kf n'bqqfmmf Ufttb."
cle = 1
message = decrypt_cesar(messagecode, cle)
print(message)

#CommencementInterphaceTessa
# L'importation de l’ensemble des éléments du paquet tkinter :
from tkinter import *

# Création d'une fenêtre avec la classe Tk :
fenetre = Tk()
# Ajout d'un titre à la fenêtre principale :
fenetre.title("Cryptanalyse")
# Définir les dimensions par défaut la fenêtre principale :
fenetre.geometry("640x480")
 # = fenetre pas redimensionnable dans longeur et largeur, figer les dimenssions
fenetre.resizable(height=False, width=False)  
# Ajout d'un texte dans la fenêtre :
texte1 = Label (fenetre, text = "Veuillez choisir votre cryptage")
texte1.pack()




# Fonction pour gérer le clic sur le bouton de cryptage
def cryptage_cesar(message, key) : 
    message_resultat = ""
    #Si la lettre est en majuscule on utilise la méthode ord() ce qui donne la table des lettres ASCII
    for i in range(len(message)):
        lettre = message[i]
        if 65 <= ord(lettre) <= 90 :
            lettre_chiffree = chr(65 + (ord(lettre) - 65 + key)%26) #%26 permet de se balader dans l'alphabet, -65 permet de donner la position de la lettre
                                                     #cle permet le décalage de la lettre, +65 permet de trouver le décalage de la lettre dans la table
    #Si la lettre est en minuscule
        elif 97 <= ord(lettre) <= 122 :
            lettre_chiffree = chr(97 + (ord(lettre) - 97 + key)% 26)
        else :
            lettre_chiffree = lettre
        message_resultat += lettre_chiffree
    return message_resultat

def decrypt_cesar(messagecode, cle):
    message = ""
    for lettre in messagecode:
        if 65 <= ord(lettre) <= 90:
            # Décale la lettre en fonction de la clé de chiffrement
            message += chr(65 + (ord(lettre) - cle - 65) % 26)
        elif 97 <= ord(lettre) <= 122 :
            message += chr(97 + (ord(lettre) - cle - 97)% 26)
        
        else:
            message += lettre
    return message

def create_Cesar ():  
    def encrypt_message():
        message = message_text.get("1.0", END).strip()
        key = int(key_text.get("1.0", END).strip())
        encrypted_message = cryptage_cesar(message, key)
        result_text.delete("1.0", END)
        result_text.insert(END, encrypted_message)
    
    def decrypt_message():
        message1 = message_text1.get("1.0", END).strip()
        key1 = int(key_text1.get("1.0", END).strip())
        decrypted_message = decrypt_cesar(message1, key1)
        result1_text.delete("1.0", END)
        result1_text.insert(END, decrypted_message)
    
    # Créer la fenêtre
    window = Toplevel()
    window.title("Chiffrement de César")

    # Ajouter les widgets
    message_label = Label(window, text="Message à crypter:")
    message_label.pack()

    message_text = Text(window, height=5)
    message_text.pack()

    key_label = Label(window, text="Clé de cryptage:")
    key_label.pack()

    key_text = Text(window, height=1)
    key_text.pack()

    encrypt_button = Button(window, text="Crypter", command=encrypt_message)
    encrypt_button.pack()

    result_label = Label(window, text="Résultat:")
    result_label.pack()
    
    result_text = Text(window, height=5)
    result_text.pack()
    
    message_label1 = Label(window, text="Message à décrypter:")
    message_label1.pack()

    message_text1 = Text(window, height=5)
    message_text1.pack()

    key_label1 = Label(window, text="Clé de décryptage:")
    key_label1.pack()

    key_text1 = Text(window, height=1)
    key_text1.pack()

    decrypt_button = Button(window,text ="Décryptage", command=decrypt_message)
    decrypt_button.pack()

    result_label1 = Label(window, text="Résultat:")
    result_label1.pack()
    
    result1_text = Text(window, height=5)
    result1_text.pack()

def vigenere_cryptage(messageV, keyV):
    ciphertext = ""
    keyV_index = 0
    for char in messageV:
        if char.isalpha():
            shift = ord((keyV[keyV_index % len(keyV)].upper()) - 65)
            cipher_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)
            ciphertext += cipher_char
            keyV_index += 1
        else:
            ciphertext += char
    return ciphertext

def create_Vigenere ():  
    def encrypt_message_Vigenere():
        messageV = message_textV.get("1.0", END).strip()
        keyV = int(key_textV.get("1.0", END).strip())
        encrypt_message_Vigenere = vigenere_cryptage(messageV, keyV)
        result_textV.delete("1.0", END)
        result_textV.insert(END, encrypt_message_Vigenere)
    
    def decrypt_message_Vigenere():
        message1V = message_text1V.get("1.0", END).strip()
        key1V = int(key_text1V.get("1.0", END).strip())
        decrypted_message_Vigenere = decrypt_cesar(message1V, key1V)
        result1_text1V.delete("1.0", END)
        result1_text1V.insert(END, decrypted_message_Vigenere)
    
    # Créer la fenêtre
    window_Vigenere = Toplevel()
    window_Vigenere.title("Chiffrement de César")

    # Ajouter les widgets
    message_labelV = Label(window_Vigenere, text="Message à crypter:")
    message_labelV.pack()

    message_textV = Text(window_Vigenere, height=5)
    message_textV.pack()

    key_labelV = Label(window_Vigenere, text="Clé de cryptage:")
    key_labelV.pack()

    key_textV = Text(window_Vigenere, height=1)
    key_textV.pack()

    encrypt_buttonV = Button(window_Vigenere, text="Crypter", command=encrypt_message_Vigenere)
    encrypt_buttonV.pack()

    result_labelV = Label(window_Vigenere, text="Résultat:")
    result_labelV.pack()
    
    result_textV = Text(window_Vigenere, height=5)
    result_textV.pack()
    
    message_label1V = Label(window_Vigenere, text="Message à décrypter:")
    message_label1V.pack()

    message_text1V = Text(window_Vigenere, height=5)
    message_text1V.pack()

    key_label1V = Label(window_Vigenere, text="Clé de décryptage:")
    key_label1V.pack()

    key_text1V = Text(window_Vigenere, height=1)
    key_text1V.pack()

    decrypt_buttonV = Button(window_Vigenere,text ="Décryptage", command=decrypt_message_Vigenere)
    decrypt_buttonV.pack()

    result_label1V = Label(window_Vigenere, text="Résultat:")
    result_label1V.pack()
    
    result1_text1V = Text(window_Vigenere, height=5)
    result1_text1V.pack()

#encryption function
def encryptScytal(message, key):
    num_columns = len(key)
    num_rows = len(message) // num_columns
    if len(message) % num_columns:
        num_rows += 1
    nulls = (num_rows * num_columns) - len(message)
    message += '_' * nulls
    cipher = ''
    for r in range(num_rows):
        for c in range(num_columns):
            cipher += message[c*num_rows + r]
    key_order = [i[0] for i in sorted(enumerate(key), key=lambda x:x[1])]
    return ''.join([cipher[key_order.index(i)] for i in range(num_columns)])

#decryption function
def decryptSvytal(cipher, key):
    num_columns = len(key)
    num_rows = len(cipher) // num_columns
    key_order = [i[0] for i in sorted(enumerate(key), key=lambda x:x[1])]
    plain = [''] * num_rows
    col = 0
    for key_idx in key_order:
        for row in range(num_rows):
            plain[row] += cipher[col]
            col += 1
    return ''.join(plain).rstrip('_')


def create_Scytal ():  


    root = Toplevel()
    root.title("Scytal Encryption/Decryption")

    def encrypt_message_Scytal():
        message = message_entry.get()
        key = key_entry.get()
        cipher = encryptScytal(message, key)
        result_text.set(cipher)

    def decrypt_message_Scytal():
        cipher = message_entry.get()
        key = key_entry.get()
        plain = decryptSvytal(cipher, key)
        result_text.set(plain)

    message_label = Label(root, text="Message:")
    message_label.grid(row=0, column=0)

    message_entry = Entry(root)
    message_entry.grid(row=0, column=1)

    key_label = Label(root, text="Key:")
    key_label.grid(row=1, column=0)

    key_entry = Entry(root)
    key_entry.grid(row=1, column=1)

    encrypt_button = Button(root, text="Encrypt", command=encrypt_message_Scytal)
    encrypt_button.grid(row=2, column=0)

    decrypt_button = Button(root, text="Decrypt", command=decrypt_message_Scytal)
    decrypt_button.grid(row=2, column=1)

    result_text = StringVar()
    result_label = Label(root, textvariable=result_text)
    result_label.grid(row=3, column=0, columnspan=2)






def create_Submonoalpha ():  
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 'qwertyuiopasdfghjklzxcvbnm'

    def encrypt_Submonoalpha (message):
        # Fonction pour chiffrer le message
        result = ''
        for letter in message:
            if letter in alphabet:
                index = alphabet.index(letter)
                result += key[index]
            else:
                result += letter
        return result

    def decrypt_Submonoalpha (message):
    # Fonction pour déchiffrer le message
        result = ''
        for letter in message:
            if letter in key:
                index = key.index(letter)
                result += alphabet[index]
            else:
                result += letter
            return result

    def encrypt_message_Submonoalpha ():
        # Fonction pour chiffrer le message saisi
        message = message_var.get()
        encrypted_message = encrypt_Submonoalpha (message)
        result_var.set(encrypted_message)

    def decrypt_message_Submonoalpha ():
        # Fonction pour déchiffrer le message saisi
        message = message_var.get()
        decrypted_message = decrypt_Submonoalpha (message)
        result_var.set(decrypted_message)

    # Créer la fenêtre principale
    root = Toplevel()
    root.title('Chiffrement par substitution alphabétique')

    # Créer les widgets
    message_label=Label(root, text='Message:')
    message_var = StringVar()
    message_entry = Entry(root, textvariable=message_var)
    encrypt_button = Button(root, text='Chiffrer', command=encrypt_message_Submonoalpha )
    decrypt_button =Button(root, text='Déchiffrer', command=decrypt_message_Submonoalpha )
    result_label = Label(root, text='Résultat:')
    result_var = StringVar()
    result_entry = Entry(root, textvariable=result_var, state='readonly')

    # Placer les widgets dans la fenêtre
    message_label.grid(row=0, column=0)
    message_entry.grid(row=0, column=1)
    encrypt_button.grid(row=1, column=0)
    decrypt_button.grid(row=1, column=1)
    result_label.grid(row=2, column=0)
    result_entry.grid(row=2, column=1)

    # Afficher la fenêtre

    
# Ajout d'un bouton dans la fenêtre :
bouton_Cesar = Button (fenetre, text = "Code Cesar", command = create_Cesar)
bouton_Cesar.pack()
bouton_Vigenere = Button (fenetre, text = "Chiffre Vigenere", command= create_Vigenere)
bouton_Vigenere.pack()
bouton_Scytal = Button (fenetre, text = "Scytal", command = create_Scytal)
bouton_Scytal.pack()
bouton_Submonoalpha = Button (fenetre, text = "Substituion Monoalphabetique", command = create_Submonoalpha)
bouton_Submonoalpha.pack()

#def create():
    #newfenetre = Toplevel(fenetre)
    #newfenetre.pack()
    #labelExample = Label(fenetre, text = "New Window")
    #labelExample.pack()
    #buttonExample = Button(fenetre, text = "New Window button")
    #buttonExample.pack()
    #labelExample.grid(column= 0, row = 0)

# Affichage de la fenêtre créée : 
fenetre.mainloop()
#FIN iNTERFACE TESSA
# L'importation de l’ensemble des éléments du paquet tkinter :
from tkinter import *

# Création d'une fenêtre avec la classe Tk :
fenetre = Tk()
# Ajout d'un titre à la fenêtre principale :
fenetre.title("Cryptanalyse")
# Définir les dimensions par défaut la fenêtre principale :
fenetre.geometry("640x480")
 # = fenetre pas redimensionnable dans longeur et largeur, figer les dimenssions
fenetre.resizable(height=False, width=False)  
# Ajout d'un texte dans la fenêtre :
texte1 = Label (fenetre, text = "Veuillez choisir votre cryptage")
texte1.pack()




# Fonction pour gérer le clic sur le bouton de cryptage
def cryptage_cesar(message, key) : 
    message_resultat = ""
    #Si la lettre est en majuscule on utilise la méthode ord() ce qui donne la table des lettres ASCII
    for i in range(len(message)):
        lettre = message[i]
        if 65 <= ord(lettre) <= 90 :
            lettre_chiffree = chr(65 + (ord(lettre) - 65 + key)%26) #%26 permet de se balader dans l'alphabet, -65 permet de donner la position de la lettre
                                                     #cle permet le décalage de la lettre, +65 permet de trouver le décalage de la lettre dans la table
    #Si la lettre est en minuscule
        elif 97 <= ord(lettre) <= 122 :
            lettre_chiffree = chr(97 + (ord(lettre) - 97 + key)% 26)
        else :
            lettre_chiffree = lettre
        message_resultat += lettre_chiffree
    return message_resultat

def decrypt_cesar(messagecode, cle):
    message = ""
    for lettre in messagecode:
        if 65 <= ord(lettre) <= 90:
            # Décale la lettre en fonction de la clé de chiffrement
            message += chr(65 + (ord(lettre) - cle - 65) % 26)
        elif 97 <= ord(lettre) <= 122 :
            message += chr(97 + (ord(lettre) - cle - 97)% 26)
        
        else:
            message += lettre
    return message

def create_Cesar ():  
    def encrypt_message():
        message = message_text.get("1.0", END).strip()
        key = int(key_text.get("1.0", END).strip())
        encrypted_message = cryptage_cesar(message, key)
        result_text.delete("1.0", END)
        result_text.insert(END, encrypted_message)
    
    def decrypt_message():
        message1 = message_text1.get("1.0", END).strip()
        key1 = int(key_text1.get("1.0", END).strip())
        decrypted_message = decrypt_cesar(message1, key1)
        result1_text.delete("1.0", END)
        result1_text.insert(END, decrypted_message)
    
    # Créer la fenêtre
    window = Toplevel()
    window.title("Chiffrement de César")

    # Ajouter les widgets
    message_label = Label(window, text="Message à crypter:")
    message_label.pack()

    message_text = Text(window, height=5)
    message_text.pack()

    key_label = Label(window, text="Clé de cryptage:")
    key_label.pack()

    key_text = Text(window, height=1)
    key_text.pack()

    encrypt_button = Button(window, text="Crypter", command=encrypt_message)
    encrypt_button.pack()

    result_label = Label(window, text="Résultat:")
    result_label.pack()
    
    result_text = Text(window, height=5)
    result_text.pack()
    
    message_label1 = Label(window, text="Message à décrypter:")
    message_label1.pack()

    message_text1 = Text(window, height=5)
    message_text1.pack()

    key_label1 = Label(window, text="Clé de décryptage:")
    key_label1.pack()

    key_text1 = Text(window, height=1)
    key_text1.pack()

    decrypt_button = Button(window,text ="Décryptage", command=decrypt_message)
    decrypt_button.pack()

    result_label1 = Label(window, text="Résultat:")
    result_label1.pack()
    
    result1_text = Text(window, height=5)
    result1_text.pack()

def vigenere_cryptage(messageV, keyV):
    ciphertext = ""
    keyV_index = 0
    for char in messageV:
        if char.isalpha():
            shift = ord((keyV[keyV_index % len(keyV)].upper()) - 65)
            cipher_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)
            ciphertext += cipher_char
            keyV_index += 1
        else:
            ciphertext += char
    return ciphertext

def create_Vigenere ():  
    def encrypt_message_Vigenere():
        messageV = message_textV.get("1.0", END).strip()
        keyV = int(key_textV.get("1.0", END).strip())
        encrypt_message_Vigenere = vigenere_cryptage(messageV, keyV)
        result_textV.delete("1.0", END)
        result_textV.insert(END, encrypt_message_Vigenere)
    
    def decrypt_message_Vigenere():
        message1V = message_text1V.get("1.0", END).strip()
        key1V = int(key_text1V.get("1.0", END).strip())
        decrypted_message_Vigenere = decrypt_cesar(message1V, key1V)
        result1_text1V.delete("1.0", END)
        result1_text1V.insert(END, decrypted_message_Vigenere)
    
    # Créer la fenêtre
    window_Vigenere = Toplevel()
    window_Vigenere.title("Chiffrement de César")

    # Ajouter les widgets
    message_labelV = Label(window_Vigenere, text="Message à crypter:")
    message_labelV.pack()

    message_textV = Text(window_Vigenere, height=5)
    message_textV.pack()

    key_labelV = Label(window_Vigenere, text="Clé de cryptage:")
    key_labelV.pack()

    key_textV = Text(window_Vigenere, height=1)
    key_textV.pack()

    encrypt_buttonV = Button(window_Vigenere, text="Crypter", command=encrypt_message_Vigenere)
    encrypt_buttonV.pack()

    result_labelV = Label(window_Vigenere, text="Résultat:")
    result_labelV.pack()
    
    result_textV = Text(window_Vigenere, height=5)
    result_textV.pack()
    
    message_label1V = Label(window_Vigenere, text="Message à décrypter:")
    message_label1V.pack()

    message_text1V = Text(window_Vigenere, height=5)
    message_text1V.pack()

    key_label1V = Label(window_Vigenere, text="Clé de décryptage:")
    key_label1V.pack()

    key_text1V = Text(window_Vigenere, height=1)
    key_text1V.pack()

    decrypt_buttonV = Button(window_Vigenere,text ="Décryptage", command=decrypt_message_Vigenere)
    decrypt_buttonV.pack()

    result_label1V = Label(window_Vigenere, text="Résultat:")
    result_label1V.pack()
    
    result1_text1V = Text(window_Vigenere, height=5)
    result1_text1V.pack()

#encryption function
def encryptScytal(message, key):
    num_columns = len(key)
    num_rows = len(message) // num_columns
    if len(message) % num_columns:
        num_rows += 1
    nulls = (num_rows * num_columns) - len(message)
    message += '_' * nulls
    cipher = ''
    for r in range(num_rows):
        for c in range(num_columns):
            cipher += message[c*num_rows + r]
    key_order = [i[0] for i in sorted(enumerate(key), key=lambda x:x[1])]
    return ''.join([cipher[key_order.index(i)] for i in range(num_columns)])

#decryption function
def decryptSvytal(cipher, key):
    num_columns = len(key)
    num_rows = len(cipher) // num_columns
    key_order = [i[0] for i in sorted(enumerate(key), key=lambda x:x[1])]
    plain = [''] * num_rows
    col = 0
    for key_idx in key_order:
        for row in range(num_rows):
            plain[row] += cipher[col]
            col += 1
    return ''.join(plain).rstrip('_')


def create_Scytal ():  


    root = Toplevel()
    root.title("Scytal Encryption/Decryption")

    def encrypt_message_Scytal():
        message = message_entry.get()
        key = key_entry.get()
        cipher = encryptScytal(message, key)
        result_text.set(cipher)

    def decrypt_message_Scytal():
        cipher = message_entry.get()
        key = key_entry.get()
        plain = decryptSvytal(cipher, key)
        result_text.set(plain)

    message_label = Label(root, text="Message:")
    message_label.grid(row=0, column=0)

    message_entry = Entry(root)
    message_entry.grid(row=0, column=1)

    key_label = Label(root, text="Key:")
    key_label.grid(row=1, column=0)

    key_entry = Entry(root)
    key_entry.grid(row=1, column=1)

    encrypt_button = Button(root, text="Encrypt", command=encrypt_message_Scytal)
    encrypt_button.grid(row=2, column=0)

    decrypt_button = Button(root, text="Decrypt", command=decrypt_message_Scytal)
    decrypt_button.grid(row=2, column=1)

    result_text = StringVar()
    result_label = Label(root, textvariable=result_text)
    result_label.grid(row=3, column=0, columnspan=2)






def create_Submonoalpha ():  
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 'qwertyuiopasdfghjklzxcvbnm'
    #création de la fonction qui va chiffrer notre message

    def encrypt_Submonoalpha (message):
        # Fonction pour chiffrer le message
        result = ''
        for letter in message:
            if letter in alphabet:
                index = alphabet.index(letter)
                result += key[index]
            else:
                result += letter
        return result

    def decrypt_Submonoalpha (message):
    # Fonction pour déchiffrer le message
        result = ''
        for letter in message:
            if letter in key:
                index = key.index(letter)
                result += alphabet[index]
            else:
                result += letter
            return result

    def encrypt_message_Submonoalpha ():
        # Fonction pour chiffrer le message saisi
        message = message_var.get()
        encrypted_message = encrypt_Submonoalpha (message)
        result_var.set(encrypted_message)

    def decrypt_message_Submonoalpha ():
        # Fonction pour déchiffrer le message saisi
        message = message_var.get()
        decrypted_message = decrypt_Submonoalpha (message)
        result_var.set(decrypted_message)

    # Créer la fenêtre principale
    root = Toplevel()
    root.title('Chiffrement par substitution alphabétique')

    # Créer les widgets
    message_label=Label(root, text='Message:')
    message_var = StringVar()
    message_entry = Entry(root, textvariable=message_var)
    encrypt_button = Button(root, text='Chiffrer', command=encrypt_message_Submonoalpha )
    decrypt_button =Button(root, text='Déchiffrer', command=decrypt_message_Submonoalpha )
    result_label = Label(root, text='Résultat:')
    result_var = StringVar()
    result_entry = Entry(root, textvariable=result_var, state='readonly')

    # Placer les widgets dans la fenêtre
    message_label.grid(row=0, column=0)
    message_entry.grid(row=0, column=1)
    encrypt_button.grid(row=1, column=0)
    decrypt_button.grid(row=1, column=1)
    result_label.grid(row=2, column=0)
    result_entry.grid(row=2, column=1)

    # Afficher la fenêtre

    
# Ajout d'un bouton dans la fenêtre :
bouton_Cesar = Button (fenetre, text = "Code Cesar", command = create_Cesar)
bouton_Cesar.pack()
bouton_Vigenere = Button (fenetre, text = "Chiffre Vigenere", command= create_Vigenere)
bouton_Vigenere.pack()
bouton_Scytal = Button (fenetre, text = "Scytal", command = create_Scytal)
bouton_Scytal.pack()
bouton_Submonoalpha = Button (fenetre, text = "Substituion Monoalphabetique", command = create_Submonoalpha)
bouton_Submonoalpha.pack()

#def create():
    #newfenetre = Toplevel(fenetre)
    #newfenetre.pack()
    #labelExample = Label(fenetre, text = "New Window")
    #labelExample.pack()
    #buttonExample = Button(fenetre, text = "New Window button")
    #buttonExample.pack()
    #labelExample.grid(column= 0, row = 0)

# Affichage de la fenêtre créée : 
fenetre.mainloop()

