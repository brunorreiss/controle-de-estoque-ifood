import sys
import platform

if platform.system() == 'Windows':
    sys.path.append(sys.path[0] + '\\src')
else:
    sys.path.append(sys.path[0] + '/src')

from Menu import *
from restaurant import *
from json_manipulation import *

def menu():
    clear()
    
    while True:
        option = set_menu(
            title = ['Bem-vindo ao iFood !\n'
                     'Use as setas para navegar e pressione ENTER para selecionar uma opção:'],
            items = [
                "Acessar como parceiro",
                "Acessar como usuário",
                "Sair"
            ]
        )

        if option == '1':
            partner_menu()
        elif option == '2':
            user_menu()
        elif option == '3':
            input('Obrigado pelo seu acesso!')
            break
        else:
            print('Opção inválida!')

def partner_menu():
    while True:
        
        option = set_menu(
            title = ["Escolha uma opção: "],
            items = [
                "Cadastrar novo restaurante",
                "Cadastrar produto no cardápio",
                "Listar restaurantes",
                "Listar produtos",
                "Excluir restaurante",
                "Ver histórico de vendas",
                "Atualizar quantia no estoque",
                "Retornar",
                "Sair"
            ]
        )
        restaurants = load_data()

        if not restaurants and option not in ['1', '8', '9']:
            input('Não há restaurantes cadastrados !\nDigite qualquer tecla para continuar ...')
            continue
        
        # Cadastrar novo restaurante
        if option == "1":
            clear()
            
            while True:
                name = input("Nome do restaurante: ")
                if not name:
                    print('Nome inválido, tente novamente!')
                    continue
                break
            
            restaurant = register_restaurant(
                restaurants,
                **{
                    'name': name,
                    'sales_history': [],
                    'requests': 0,
                    'menu': []
                }
            )
            
            if restaurant:
                input('Restaurante cadastrado com sucesso !')
                restaurant_save(**restaurant)
            else:
                input('Restaurante já cadastrado !')

        # Cadastrar produto no cardápio
        elif option == "2":
            clear()
            print('Restaurantes cadastrados:')
            
            print('\n'.join([restaurant.get('name') for _, restaurant in restaurants.items()]))
            
            name = input("Nome do restaurante: ")
            
            try:
                id = [key for key in restaurants if restaurants[key].get('name') == name][0]
            except:
                input("Restaurante não encontrado ...")
                clear()
                id = None
            
            if id:
                restaurant = restaurants[id]
                restaurant = create_menu(restaurant)
                restaurant['id'] = id
                restaurant_save(**restaurant)

        # Listar restaurantes
        elif option == '3':
            clear()
            print('Restaurantes cadastrados:')
            
            print('\n'.join([restaurant.get('name') for _, restaurant in restaurants.items()]))
            
            input('\nDigite qualquer tecla para continuar ...')
        
        # Listar produtos
        elif option == "4":
            clear()
            for id, restaurant in restaurants.items():
                clear()
                for key, value in restaurant.items():
                    if key == 'menu':
                        if not value:
                            print('Não há produtos no cardápio !')
                        else:
                            print("Cardápio:")
                            for item in value:
                                for new_key, new_value in item.items():
                                    if new_key == 'product_name':
                                        print(f'\tNome: {new_value}')
                                    elif new_key == 'category':
                                        print(f"\tCategoria: {new_value}")
                                    elif new_key == 'value':
                                        print(f"\tValor: {new_value}")
                                    elif new_key == 'stock':
                                        print(f"\tQuantidade em estoque: {new_value}")
                    elif key in ['id', 'requests', 'sales_history' ]:
                        continue
                    elif key == 'name':
                        print(f"Nome do restaurante: {value}")
                    elif key == 'requests':
                        print(f"Quantidade de pedidos: {value}")
                        
                input('\nDigite qualquer tecla para continuar ...')

        # Excluir restaurante
        elif option == "5":
            clear()
            
            print('Restaurantes cadastrados:')
            print('\n'.join([restaurant.get('name') for _, restaurant in restaurants.items()]))
                
            name = input("Nome do restaurante que deseja descadastrar: ")
            
            try:
                id = [key for key in restaurants if restaurants[key].get('name') == name][0]
            except:
                input("Restaurante não encontrado ...")
                clear()
                id = None
            
            if id:
                restaurants.pop(id)
                save_data(restaurants)

        # Ver histórico de vendas
        elif option == "6":
            clear()
            for id, restaurant in restaurants.items():
                clear()
                print(f"Restaurante: {restaurant.get('name')}")
                for key, value in restaurant.items():
                    if key == 'sales_history':
                        if value :
                            for item in value:
                                for new_key, new_value in item.items():
                                    if new_key == 'user_name':
                                        print(f'\tNome do usuário: {new_value}')
                                    elif new_key == 'product_name':
                                        print(f'\tNome do produto: {new_value}')
                                    elif new_key == 'amount':
                                        print(f'\tQuantidade: {new_value}')
                                    elif new_key == 'total_order':
                                        print(f'\tValor total: {new_value}')
                                print()
                        else:
                            print('Não há histórico de compras para o restaurante !')           
                    else:
                        continue
                input('\nDigite qualquer tecla para continuar ...')

        # Atualizar quantia no estoque
        elif option == "7":
            clear()
            
            print('Restaurantes:')
            print('\n'.join([restaurant.get('name') for _, restaurant in restaurants.items()]))
                
            name = input("\nNome do restaurante que deseja selecionar: ")
            
            try:
                id = [key for key in restaurants if restaurants[key].get('name') == name][0]
            except:
                input("Restaurante não encontrado ...")
                clear()
                id = None
            
            if id:
                selected_restaurant = restaurants.get(id)
                
                if not selected_restaurant['menu']:
                    clear()
                    input('Não há produtos no cardápio !')
                    continue
                else:
                    print()
                    for item in selected_restaurant['menu']:
                        print(f"Produto: {item.get('product_name')}, em estoque: {item.get('stock')}")
                        
                    product_name = input('Qual o nome do produto que deseja atualizar: ')
                    if not product_name:
                        print('Nome inválido, tente novamente!')
                        continue
                    
                    while True:
                        amount = input(f'Qual nova quantidade do produto {product_name}: ')
                        try:
                            amount = int(amount)
                            if amount <= 0:
                                print('Valor inválido, tente novamente!')
                                continue
                            break
                        except:
                            print('Valor inválido, tente novamente!')
                    
                    for idx, item in enumerate(selected_restaurant['menu']):
                        if item.get('product_name') == product_name:
                            restaurante_atualizado = update_stock(selected_restaurant, idx, amount)
                            restaurante_atualizado['id'] = id          
                            restaurant_save(**restaurante_atualizado)
                            break
                        else:
                            print('Produto não existe no cardápio !') 
                    input('\nDigite qualquer tecla para continuar ...')

        # Retornar
        elif option == "8":
            clear(); break
        
        # Sair
        elif option == "9":
            clear(); input('Obrigado pelo seu acesso!'); exit()

        else:
            input("Opção inválida!")

def user_menu():
    clear()
    while True:
        user_name = input('Insira seu nome: ')
        if not user_name:
            print('Nome inválido, tente novamente!')
            continue
        break
    
    while True:
        user_phone = input('Insira seu número de telefone: ')
        if not user_phone:
            print('Telefone inválido, tente novamente!')
            continue
        break
    
    restaurants = load_data()
    while True:
        option = set_menu(
            title = ['Escolha uma opção: '],
            items = [
                "Realizar pedido",
                "Retornar",
                "Sair"
            ]
        )
        
        if option == '1':
            clear()
            
            print('Restaurantes:')
            print('\n'.join([restaurant.get('name') for _, restaurant in restaurants.items()]))
                
            name = input("\nNome do restaurante realizar um pedido: ")
            
            try:
                id = [key for key in restaurants if restaurants[key].get('name') == name][0]
            except:
                input("Restaurante não encontrado ...")
                clear()
                id = None
            
            if id:
                selected_restaurant = restaurants.get(id)
                if not selected_restaurant['menu']:
                    clear()
                    input('Não há produtos no cardápio!')
                    continue
                
                for item in selected_restaurant['menu']:
                  for key, value in item.items():
                        print(f"{key}: {value}")
                product_name = input('Qual o name do produto que deseja comprar: ')
                
                while True:
                    amount = input('Qual a quantidade que deseja comprar: ')
                    try:
                        amount = int(amount)
                        break
                    except:
                        print('Valor inválido, tente novamente!')
                        continue
                
                idx = [i for i, item in enumerate(selected_restaurant['menu']) if item.get('product_name') == product_name]
                
                if idx:
                    if selected_restaurant['menu'][idx[0]]['stock'] >= amount:
                        dicionario = {
                            'index': idx[0],                        
                            'user_name': user_name,
                            'user_phone': user_phone,
                            'product_name': product_name,
                            'amount': amount,
                        }
                        selected_restaurant = make_order(selected_restaurant, **dicionario)
                        selected_restaurant['id'] = id
                        restaurant_save(**selected_restaurant)
                        print('Pedido realizado com sucesso!')
                    else:
                        print('Quantidade não disponível em estoque!')
                else:
                    print('Produto não existe no cardápio !')
                
                input('\nDigite qualquer tecla para continuar ...')
                            
        elif option == '2':
            clear(); break
        
        elif option == '3':
            clear(); input('Obrigado pelo seu acesso!'); exit()

if __name__ == "__main__":
    menu()
