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

    # Setters

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

    # Getters

    def getID(self):
        return self.ID

    def getPrice(self):
        return self.Price

    def getQuantity(self):
        return self.Quantity

    def getProductName(self):
        return self.ProductName

    def getBrand(self):
        return self.Brand

    def getDescription(self):
        return self.Description

    def getCategory(self):
        return self.Category

    def getSupplier(self):
        return self.Supplier

    def getDate(self):
        return self.Date
