def validar_edad(edad):
    """Valida si una persona es mayor de edad."""
    if edad >= 18:
        return "La persona es mayor de edad."
    return "La persona es menor de edad."


if __name__ == "__main__":
    edad = int(input("Ingrese su edad: "))
    print(validar_edad(edad))