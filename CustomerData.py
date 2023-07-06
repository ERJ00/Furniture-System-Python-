class CustomerData:
    attribute_names = [
        "id", "quantity", "totalPayment", "paymentReceived", "balance", "change",
        "category", "productName", "status", "name", "birthday", "contactNumber",
        "address", "date"
    ]


    def __init__(self):
        self.id = None
        self.quantity = None
        self.totalPayment = None
        self.paymentReceived = None
        self.balance = None
        self.change = None
        self.category = None
        self.productName = None
        self.status = None
        self.name = None
        self.birthday = None
        self.contactNumber = None
        self.address = None
        self.date = None

    def __init__(self, other=None):
        if other is not None:
            self.id = other.id
            self.quantity = other.quantity
            self.productName = other.productName
            self.category = other.category
            self.date = other.date
            self.totalPayment = other.totalPayment
            self.paymentReceived = other.paymentReceived
            self.balance = other.balance
            self.change = other.change
            self.status = other.status
            self.name = other.name
            self.birthday = other.birthday
            self.contactNumber = other.contactNumber
            self.address = other.address

    # Getters and Setters

    def getID(self):
        return self.id

    def setID(self, id):
        self.id = id

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def getProductName(self):
        return self.productName

    def setProductName(self, productName):
        self.productName = productName

    def getCategory(self):
        return self.category

    def setCategory(self, category):
        self.category = category

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    def getTotalPayment(self):
        return self.totalPayment

    def setTotalPayment(self, totalPayment):
        self.totalPayment = totalPayment

    def getPaymentReceived(self):
        return self.paymentReceived

    def setPaymentReceived(self, paymentReceived):
        self.paymentReceived = paymentReceived

    def getBalance(self):
        return self.balance

    def setBalance(self, balance):
        self.balance = balance

    def getChange(self):
        return self.change

    def setChange(self, change):
        self.change = change

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getBirthday(self):
        return self.birthday

    def setBirthday(self, birthday):
        self.birthday = birthday

    def getContactNumber(self):
        return self.contactNumber

    def setContactNumber(self, contactNumber):
        self.contactNumber = contactNumber

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address
