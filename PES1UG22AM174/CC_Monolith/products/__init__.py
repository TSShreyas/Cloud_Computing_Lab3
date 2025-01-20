from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    """
    Retrieve all products from the database and convert them into Product objects.
    """
    # Use list comprehension for faster iteration and object creation
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """
    Retrieve a single product by ID and return it as a Product object.
    """
    # Directly load the product using the DAO call
    return Product.load(dao.get_product(product_id))


def add_product(product: dict):
    """
    Add a new product to the database.
    """
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """
    Update the quantity of a product. Raises an error if qty is negative.
    """
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
