import cowsay
cowsay.fox("projet 1")

def introduire_password():
    import string
    import maskpass
    while True:
        pwd=maskpass.askpass()
        if len(pwd)==8:
            if any(char in string.digits for char in pwd):
                if any(char in string.ascii_lowercase for char in pwd):
                    if any(char in string.ascii_uppercase for char in pwd):
                        if any(char in string.punctuation for char in pwd):
                            return pwd
                            break
                        else:
                            print("il te manque un special caractere")
                    else:
                        print("il te manque une majuscule ")
                else:
                    print("il te manque une minuscule ")
            else:
                print("il te manque un chiffre ")                                    
def introduire_email():
    import re
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    def isValid(email):
        if re.fullmatch(regex, email):
            print("Valid email")
        else:
            print("Invalid email")
    while True:
        email=input("introduire votre email")
        if re.fullmatch(regex,email):
            introduire_password()
            break
        else:
            print("Invalid email")
print("enregistrement:")
print("1-Email")
print("2-password")
print("3-quitter")
choix=input("donner votre choix:")
if choix=='1':
    introduire_email()
elif choix=='2':
    introduire_password() 
def attaque_par_dictionnaire(password):
    from hashlib import sha256
    from datetime import datetime
    dict=open('dict.tct', mode='r')
    n=0
    t=datetime.now()
    for mot in dict:
        mot=mot.strip()
        n+=1
        if sha256(mot.encode).hexdigest==password():
            print("mot de passe trouvé",mot,"pensez à le changer")
            print(n,"mots testés en", (datetime.now()-t).total_seconds(), "secondes")
            dict.close()
            return True
    print()
    print("mot de passe non trouvé , aucun haché ne correspond à votre haché", password)
choix=input("faite votre choix:")
match choix:
    case'A':
        print("donner un mot a hacher")
    case'B':
        """print(decalage par CESAR) """
        Pchoix=("faite votre choix")
        match Pchoix:
            case 'a':
                print("donnez un mot à chiffrer")
                cesar=input("faite votre choix")
                match cesar:
                    case '1':
                        print("cesar avec code ASCII")
                    case '2':
                        print("cesar avec 26 lettres")
                    case _:
                        print("merci d'introduire 1 ou 2")
            case 'b':
                print("chiffrer le message (a)")
            case 'c':
                print("dechiffrer le message (b)")
            case 'd':
                quit()
            case _:
                print("merci d'introduire a, b, c ou d")
    case'C':
        """print("collecter une dataset de votre choix")"""
        pchoix=("faite votre choix")
        match pchoix:
            case 'a':
                print("afficher le dataset sous forme d'un dictionnaire")
            case 'b':
                print("afficher les courbes de votre choix")
            case 'c':
                quit()
            case _:
                print("merci d'introduire a, b, ou c")
    case _:
        print("merci d'introduire A, B, C")
        
def authentification():
    if not email != email:
        print("il faut s'enregistre avant de s'authentifier")
        print("enregistrement")
    print("Bonjour, la phase d'authentification avec email/password")
    while True:
        email=input("donner votre email:")
        if email==email:
            import hashlib
            password=sha256(mot.encode).hexdigest==password()
            if password==password:
                print("1- Tapez 1 pour vérifier la robustesse de votre mot de passe")
                print("2- Tapez 2 pour quitter")
                while True:
                    choix=input("donnez votre choix")
                    match choix :
                        case '1':
                            attaque_par_dictionnaire(password)
                        case'2' :
                            quit()
                        case _ :
                            print(" Merci d'introduire 1 ou bien 2 ")           
                break
            else:
                print("merci de verifier vote password")     
        else:
            print("merci de verifier votre email")
                 
Alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
msg=input("Donnez un message à chiffrer :")
msg=msg.upper()
key=int(input("Donnez la clé de décalage :"))
chiffrer=''
clair=''
for i in msg:
    chiffrer+=Alphabet[(Alphabet.index(i)+key)%26]
print(chiffrer)
for i in chiffrer :
    clair+=Alphabet[(Alphabet.index(i)-key)%26]  
print(clair)

message_a_code=input("entrez votre texte :")
clef=int(input("entrez votre clé:"))
message=[]
message_décodé=[]
for i in message_a_code :
    message.append(ord(i)+clef)
for i in message:
    message_décodé.append(chr(i))
final ="".join(message_décodé)
print(final) 
       
message_a_code=input("entrez votre texte :")
clef=int(input("entrez votre clé:"))
message=[]
message_décodé=[]
for i in message_a_code :
    message.append(ord(i)-clef)
for i in message:
    message_décodé.append(chr(i))
final ="".join(message_décodé)
print(final)
       
def encrypt(text,s):
    result=""
    for i in range (len(text)):
        char=text[i]
        result += chr((ord(char)+s-96)%26+96)
    return result     
text="salut"
s= 3
print(encrypt(text,s))
        
def encrypt(text,s):
    result=""
    for i in range (len(text)):
        char=text[i]
        result += chr((ord(char)-s-96)%26+96)
    return result     
text=input("entrez votre text :")
s=int(input("entrez votre clé:"))
print(encrypt(text,s))

from pylab import*
x=linspace(0,8,20)
y=x**2
plot(x,y,'r')
show()
    
