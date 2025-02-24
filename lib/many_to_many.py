class Author:
    all =[]
    def __init__(self,name):
        if isinstance(name,str):
            self._name = name
    
    @property
    def name(self):
        return self._name
    def contracts(self):
        return [contracts for contracts in Contract.all if contracts.author == self ]
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    def sign_contract(self,book, date, royalties): 
        if isinstance(book,Book) and isinstance(date,str) and isinstance(royalties,int):
            contract = Contract(self,book,date,royalties)
            return contract
        else:
            raise Exception("Book must be an instance of Book class, the date must be a string and royalties must be integers")
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
    


class Book:
    all=[]
    def __init__(self,title):
        if isinstance(title,str):
            self._title = title.title()
        else:
            raise Exception("The title must be a string")
    @property
    def title(self):
        return self._title
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all =[]
    def __init__(self,author,book,date,royalties):
        if isinstance(author,Author):
            self.author = author
        else:
            raise Exception("The author must be an instance of the Author class")
        if isinstance(book,Book):
            self.book = book
        else:
            raise Exception("The book must be an instance of the Book class")
        if isinstance(date,str):
            self.date = date
        else:
            raise Exception("The date must be a string")
        if isinstance(royalties,int):
            self.royalties =royalties
        else:
            raise Exception("The royalties must be integers")
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        if isinstance(date,str):
            return [contract for contract in cls.all if contract.date == date]
        else:
            raise Excepion("Date must be a string")
        