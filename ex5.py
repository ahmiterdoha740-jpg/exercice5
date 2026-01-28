def trouver_maximum(liste):
    if len(liste) == 0:
        return None  # ou tu peux lever une erreur

    max_nombre = liste[0]

    for nombre in liste:
        if nombre > max_nombre:
            max_nombre = nombre

    return max_nombre
