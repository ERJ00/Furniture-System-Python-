class Product:
    attribute_names = ["ID", "Price", "Quantity", "ProductName", "Brand", "Description", "Category", "Supplier", "Date"]

    def __init__(self, other=None):
        self.ID = None
        self.Price = None
        self.Quantity = None
        self.ProductName = None
        self.Brand = None
        self.Description = None
        self.Category = None
        self.Supplier = None
        self.Date = None


    # def __init__(self, other):
    #     self.key = other.key
    #     self.ID = other.ID
    #     self.price = other.price
    #     self.quantity = other.quantity
    #     self.productName = other.productName
    #     self.brand = other.brand
    #     self.description = other.description
    #     self.category = other.category
    #     self.supplier = other.supplier
    #     self.date = other.date

    # Getters and Setters

    # def getKey(self):
    #     return self.key
    #
    # def getID(self):
    #     return self.ID
    #
    # def setID(self, ID):
    #     self.ID = ID
    #
    # def getPrice(self):
    #     return self.price
    #
    # def setPrice(self, price):
    #     self.price = price
    #
    # def getQuantity(self):
    #     return self.quantity
    #
    # def setQuantity(self, quantity):
    #     self.quantity = quantity
    #
    # def getProductName(self):
    #     return self.productName
    #
    # def setProductName(self, productName):
    #     self.productName = productName
    #
    # def getBrand(self):
    #     return self.brand
    #
    # def setBrand(self, brand):
    #     self.brand = brand
    #
    # def getDescription(self):
    #     return self.description
    #
    # def setDescription(self, description):
    #     self.description = description
    #
    # def getCategory(self):
    #     return self.category
    #
    # def setCategory(self, category):
    #     self.category = category
    #
    # def getSupplier(self):
    #     return self.supplier
    #
    # def setSupplier(self, supplier):
    #     self.supplier = supplier
    #
    # def getDate(self):
    #     return self.date
    #
    # def setDate(self, date):
    #     self.date = date

    def setID(self, ID):
        self.ID = ID

    def setPrice(self, Price):
        self.Price = Price

    def setQuantity(self, Quantity):
        self.Quantity = Quantity

    def setProductName(self, ProductName):
        self.ProductName = ProductName

    def setBrand(self, Brand):
        self.Brand = Brand

    def setDescription(self, Description):
        self.Description = Description

    def setCategory(self, Category):
        self.Category = Category

    def setSupplier(self, Supplier):
        self.Supplier = Supplier

    def setDate(self, Date):
        self.Date = Date
