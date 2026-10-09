def obtener_opcion():
    print("\n" + "=" * 35)
    print("      SISTEMA DE BLOG (POO + JSON)      ")
    print("=" * 35)
    print("1) Ver todos los posts")
    print("2) Buscar post por título")
    print("3) Filtrar posts por tag")
    print("4) Crear nuevo post")
    print("5) Salir")
    try:
        return int(input("\nElegí una opción (1-5): ").strip())
    except ValueError:
        print(" Error: ingresá un número entero válido.")
        return None
