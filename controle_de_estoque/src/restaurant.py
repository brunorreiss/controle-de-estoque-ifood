from uuid import uuid4

def register_restaurant(restaurants: dict, **kwargs) -> dict:
    restaurant = {
        "name": kwargs.get('name'),
        "sales_history": kwargs.get('sales_history'),
        "requests": kwargs.get('requests'),
        "menu": kwargs.get('menu'),
    }
    
    for value in restaurants.values():
        if value.get('name') == restaurant.get('name'):
            return False
    
    return restaurant

def create_menu(restaurant: dict) -> dict:
    # peso, altura, cor, tamanho, etc. As especificações e a quantidade de especificações podem variar de acordo com o produto
    items = restaurant.get('menu')
    if not items:
        items = []
    print("Digite os itens do cardápio (digite 'sair' para terminar):")
    while True:
        """
        item_cardapio = {
            'product_name': str,
            'category': str,
            'value': float,
            'stock': int,
        }
        """
        product_name = input("Nome do produto: ")
        if product_name.lower() == "sair":
            break
        
        while True:
            category = input("Tipo do item (comida ou bebida): ").lower()
            if category in ['comida', 'bebida', 'sair']:
                break
            else:
                print("Categoria inválida")
                continue
        if category == 'sair':
            break
        
        while True:
            value = input("Informe o valor do produto: ")
            if value == 'sair':
                break
            else:
                try:
                    value = float(value)
                    if value <= 0:
                        print("Valor inválido")
                        continue
                    break
                except:
                    print("Valor inválido")
                    continue
        if value == 'sair':
            break
                
        while True:
            stock = input("Informe a quantidade em estoque: ")
            if stock == 'sair':
                break
            else:
                try:
                    stock = int(stock)
                    if stock <= 0:
                        print("Valor inválido")
                        continue
                    break
                except:
                    print("Valor inválido")
                    continue
        if stock == 'sair':
            break
                
        items.append(
            {
                "product_name": product_name,
                "category": category,
                "value": value,
                "stock": stock,
            }
        )
        
    restaurant['menu'] = items
    return restaurant

def update_stock(restaurant: dict, idx: int, amount: int) -> dict:
    restaurant['menu'][idx]['stock'] = amount
    return restaurant

def make_order(restaurant: dict, **kwargs) -> None:
    """
    'order_id': str,
    'user_name': str,
    'user_phone': str,
    'amount': int,
    'total_order': float
    """
    order_id = str(uuid4())
    user_name = kwargs.get('user_name')
    user_phone = kwargs.get('user_phone')
    product_name = kwargs.get('product_name')
    amount = kwargs.get('amount')
    total_order = round(restaurant.get('menu')[kwargs.get('index')].get('value')*amount, 2)
    restaurant.get('menu')[kwargs.get('index')]['stock'] -= amount
    restaurant['requests'] += 1 
    dict_pedido = {
        'order_id': order_id,
        'user_name': user_name,
        'user_phone': user_phone,
        'product_name': product_name,
        'amount': amount,
        'total_order': total_order
    }
    restaurant['sales_history'].append(dict_pedido)
    return restaurant