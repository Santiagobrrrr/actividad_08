product_list = []

while True:
    print(f"=== MENÚ ===")
    print(f"1. Agregar producto a la lista")
    print(f"2. Modificar un producto existente")
    print(f"3. Eliminar un producto")
    print(f"4. Ver todos los productos")
    print(f"5. Salir del programa")
    option = input(f"Ingrese la opción a la que desea ingresar (1-5): ")

    match option:
        case "1":
            product_user = input(f"Ingrese el nombre del producto: ")
            product_list.append(product_user)

        case "2":
            print(f"Lista de productos actuales: {product_list}")
            index_product = int(input(f"Ingrese el índice del producto a modificar (empieza desde 0): "))
            new_product = input(f"Ingrese el nombre del nuevo producto: ")
            product_list[index_product] = new_product
            print(f"Producto modificado exitosamente")

        case "3":
            print(f"Lista de productos actuales: {product_list}")
            remove_product = input(f"Ingrese el producto que desea eliminar: ")
            if remove_product in product_list:
                product_list.remove(remove_product)
                print(f"Producto eliminado exitosamente")
            else:
                print("Producto no existente, intentelo nuevamente")

        case "4":
            print(f"Productos: {product_list}")

        case "5":
            print(f"Graciar por visitarnos, salio del programa.")
            break

        case _:
            print(f"Valor inválido, intente de nuevo")