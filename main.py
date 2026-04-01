e = { 1, 2, 3, 4, 5, 6, 7, 8, 9 }
a = { 1, 2, 3, 6, 8, 9 }
b = { 3, 5, 7 }

aBar = e-a
bBar = e-b

union = a|b
intersection = a&b
inclus = a<=b

aUbBar = e - (a | b)
aIbBar = e - (a & b)

aBarIbBar = aBar & bBar
aBarUbBar = aBar | bBar

print(aBar)
print(union)
print(intersection)
print(inclus)
print(aUbBar == aBarIbBar)
print(aIbBar == aBarUbBar)

def ens_parties(e):
    res = [[]]
  
    for i in e:
      # Pour chaque élément, on crée de nouveaux sous-ensembles 
      # en l'ajoutant à ceux déjà existants
      new_parties = [actuel + [i] for actuel in res]
      res.extend(new_parties)
    
    return res

print(ens_parties(e))

def henry_theoreme(e):
    n = len(e)
    # Calcul manuel de 2^n
    valeur_theorique = 2**n
    
    # Génération de l'ensemble des parties
    p_e = ens_parties(e)
    cardinal_reel = len(p_e)
    
    is_valid = (cardinal_reel == valeur_theorique)
    
    print(f"--- Vérification pour n = {n} ---")
    print(f"Nombre d'éléments : {cardinal_reel}")
    print(f"Calcul 2^{n} : {valeur_theorique}")
    print(f"Théorème vérifié : {is_valid}")
    
henry_theoreme(e)

def image(f, x):
    """Retourne l'image de x par la fonction f"""
    return f.get(x, None)

f = {1: 'A', 2: 'B', 3: 'C'}
print(image(f, 1))

def composer(f, g):
    """Retourne une nouvelle fonction (dictionnaire) résultant de f o g"""
    h = {}
    for x, image_g in g.items():
        if image_g in f:
            h[x] = f[image_g]
    return h
  
def verifier_proprietes(f, codomaine):
    images = list(f.values())
    domaine = list(f.keys())
    
    # Injectivité : Chaque image est unique (pas de doublons dans les valeurs)
    est_injective = len(set(images)) == len(domaine)
    
    # Surjectivité : Toutes les valeurs du codomaine sont atteintes
    est_surjective = set(images) == set(codomaine)
    
    # Bijectivité : Les deux conditions sont remplies
    est_bijective = est_injective and est_surjective
    
    return est_injective, est_surjective, est_bijective
    
def image_directe(f, sous_ensemble_a):
    """f(A) = {f(x) | x ∈ A}"""
    return {f[x] for x in sous_ensemble_a if x in f}

def image_reciproque(f, sous_ensemble_b):
    """f⁻¹(B) = {x | f(x) ∈ B}"""
    return {x for x, image in f.items() if image in sous_ensemble_b}

def verifier_image_union(f, a, b):
    # Membre de gauche : f(A U B)
    gauche = image_directe(f, a | b)
    
    # Membre de droite : f(A) U f(B)
    droite = image_directe(f, a) | image_directe(f, b)
    
    return gauche == droite, gauche

def verifier_image_intersection(f, a, b):
    # f(A n B)
    gauche = image_directe(f, a & b)
    
    # f(A) n f(B)
    droite = image_directe(f, a) & image_directe(f, b)
    
    # Vérification de l'inclusion (gauche est inclus dans droite)
    est_inclus = gauche.issubset(droite)
    est_egal = (gauche == droite)
    
    return est_inclus, est_egal
    
def verifier_reciproque_lois(f, part_a, part_b):
    """Vérifie f⁻¹(A U B) = f⁻¹(A) U f⁻¹(B) et f⁻¹(A n B) = f⁻¹(A) n f⁻¹(B)"""
    
    # Union
    inv_union_globale = image_reciproque(f, part_a | part_b)
    inv_union_separee = image_reciproque(f, part_a) | image_reciproque(f, part_b)
    
    # Intersection
    inv_inter_globale = image_reciproque(f, part_a & part_b)
    inv_inter_separee = image_reciproque(f, part_a) & image_reciproque(f, part_b)
    
    return (inv_union_globale == inv_union_separee), (inv_inter_globale == inv_inter_separee)

def ens(ens_a, ens_b):
  res = set()
  
  for i in ens_a:
    for j in ens_b:
      res.add((i,j))
      
  return res

ab = ens(a,b)

print(ab)
#print("len:",len(ab))

def premier(n):
  if n<=1:
    return False
  
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
    
  return True
  
print(premier(1333))

def pgcd(a, b):
  div_a=set()
  div_b=set()
  
  for i in (1, a+1):
    if a%i==0:
      div_a.add(i)
      
  for i in (1, b+1):
    if b%i==0:
      div_b.add(i)
  
  com=div_a.intersection(div_b)
  return max(com)
  
#print(pgcd(24,101))

def premier_ee(x,y):
  return pgcd(x,y)==1
  
#print(premier_ee(12,1333))

def ens_premier_ee(ens):
  res=set()
  for e in ens:
    if premier_ee(e[0],e[1]):
      res.add(e)
        
  return res
  
print(ens_premier_ee(ab))

def classe_equivalence(x, n, limite):
    """
    Trouve tous les y dans [0, limite] tels que x - y est un multiple de n.
    Relation : y ≡ x [n]
    """
    res = set()
    # Le reste standard de x modulo n
    reste_x = x % n
    
    for y in range(limite + 1):
        if y % n == reste_x:
            res.add(y)
            
    return res

# Paramètres
n = 5
x = 2
limite = 20

# Calcul
classe_de_x = classe_equivalence(x, n, limite)

print(f"Classe d'équivalence de {x} modulo {n} (jusqu'à {limite}) :")
print(classe_de_x)

def chiffrer_messages(messages, decalages):
    # On s'assure de ne pas dépasser la taille de la liste de décalages
    messages_chiffres = []
    
    for i in range(len(messages)):
        msg = messages[i]
        # On utilise le modulo % pour boucler sur les décalages si M1 est plus long que M2
        n = decalages[i % len(decalages)]
        
        msg_code = ""
        for caractere in msg:
            # ord(caractere) donne le code ASCII (ex: 'A' -> 65)
            # On ajoute le décalage n
            nouveau_code = ord(caractere) + n
            # chr() transforme le nouveau code en caractère
            msg_code += chr(nouveau_code)
            
        messages_chiffres.append(msg_code)
    
    return messages_chiffres

# --- Test ---
M1 = ["Hello !", "Python 3", "Gemini beta 4.5"]
M2 = [1, 3, 5]

resultat = chiffrer_messages(M1, M2)
print(f"Messages originaux : {M1}")
print(f"Messages chiffrés : {resultat}")

import base64

def chiffrer_base64(message):
    # 1. Convertir le texte en octets
    message_bytes = message.encode('utf-8')
    
    # 2. Encoder en Base64
    base64_bytes = base64.b64encode(message_bytes)
    
    # 3. Reconvertir les octets en texte lisible
    return base64_bytes.decode('utf-8')

# Exemple d'utilisation
msg = "Bonjour !"
resultat = chiffrer_base64(msg)
print(resultat)

def dechiffrer_base64(message_code):
    base64_bytes = message_code.encode('utf-8')
    
    message_bytes = base64.b64decode(base64_bytes)
    
    return message_bytes.decode('utf-8')

# Exemple :
code = "Qm9uam91ciAh"
message_original = dechiffrer_base64(code)
print(message_original)

def chiffrer(message, decalage):
    resultat = ""
    
    for caractere in message:
        if caractere.isupper():
            index = (ord(caractere) - ord('A') + decalage) % 26
            resultat += chr(index + ord('A'))
            
        elif caractere.islower():
            index = (ord(caractere) - ord('a') + decalage) % 26
            resultat += chr(index + ord('a'))
            
        else:
            resultat += caractere
            
    return resultat

msg = "Hello tout le monde !"
code = chiffrer(msg, 3)
print(f"Original : {msg}")
print(f"Chiffré  : {code}")

def message_en_ascii(message):
    codes = [ord(caractere) for caractere in message]
    return codes

# Test
msg = "Hello"
resultat = message_en_ascii(msg)
print(resultat)

def chiffrer_rsa(message_entier, cle_publique):
    """
    message_entier : le message converti en nombre
    cle_publique : un tuple (e, n)
    """
    e, n = cle_publique
    # On utilise pow(base, exp, mod) pour l'efficacité (exponentiation modulaire)
    message_chiffre = pow(message_entier, e, n)
    return message_chiffre
    
def dechiffrer_rsa(message_chiffre, cle_privee):
    """
    message_chiffre : le nombre chiffré
    cle_privee : un tuple (d, n)
    """
    d, n = cle_privee
    message_original = pow(message_chiffre, d, n)
    return message_original
    
# 1. Choisir deux nombres premiers p et q
p = 61
q = 53

# 2. Calculer n (le module)
n = p * q  # 3233

# 3. Calculer l'indicateur d'Euler phi(n)
phi = (p - 1) * (q - 1) # 3120

# 4. Choisir e (exposant public) tel que 1 < e < phi et pgcd(e, phi) = 1
e = 17

# 5. Calculer d (exposant privé) : l'inverse de e modulo phi
# d * e = 1 (mod phi)
d = pow(e, -1, phi) # En Python 3.8+, pow peut calculer l'inverse modulaire

cle_publique = (e, n)
cle_privee = (d, n)

# Message original
texte = "A"
m_nombre = ord(texte) # 65

# Chiffrement
c = chiffrer_rsa(m_nombre, cle_publique)
print(f"Message chiffré : {c}")

# Déchiffrement
m_recupere = dechiffrer_rsa(c, cle_privee)
print(f"Message déchiffré (ASCII) : {m_recupere}")
print(f"Lettre finale : {chr(m_recupere)}")
    
import base64

def encoder_base64(message):
    return base64.b64encode(message.encode()).decode()

def decoder_base64(message_code):
    return base64.b64decode(message_code.encode()).decode()

def cesar(message, decalage):
    res = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            res += chr((ord(char) - base + decalage) % 26 + base)
        else:
            res += char
    return res 
    
def texte_vers_entier(message):
    """Transforme un texte en un seul très grand nombre."""
    return int.from_bytes(message.encode('utf-8'), byteorder='big')

def entier_vers_texte(nombre):
    """Transforme un grand nombre en texte clair."""
    # Calcule combien d'octets sont nécessaires pour représenter le nombre
    taille = (nombre.bit_length() + 7) // 8
    return nombre.to_bytes(taille, byteorder='big').decode('utf-8')
    
def generer_cles_rsa(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    while pgcd(e, phi) != 1:
        e += 2
    # pow(e, -1, phi) calcule l'inverse modulaire (la clé d)
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def rsa_chiffrer(message_texte, cle_publique):
    e, n = cle_publique
    m_nombre = texte_vers_entier(message_texte)
    # Vérification de sécurité pour éviter l'erreur "Message trop long"
    if m_nombre >= n:
        raise ValueError(f"Message trop grand pour n={n}. Utilisez des p et q plus grands.")
    return pow(m_nombre, e, n)

def rsa_dechiffrer(message_chiffre, cle_privee):
    d, n = cle_privee
    m_nombre = pow(message_chiffre, d, n)
    return entier_vers_texte(m_nombre)
    
# 1. On choisit deux nombres premiers assez grands
p = 1000003  # Un nombre premier proche de 1 million
q = 1000033  # Un autre

# 2. Génération des clés
publique, privee = generer_cles_rsa(p, q)
# Ici n vaudra environ 1 000 000 000 000 (10^12)

# 3. Test de chiffrement
msg = "Test" # Avec ces p et q, on peut chiffrer environ 4-5 caractères d'un coup
crypte = rsa_chiffrer(msg, publique)
print(f"Chiffré : {crypte}")

# 4. Déchiffrement
clair = rsa_dechiffrer(crypte, privee)
print(f"Retrouvé : {clair}")