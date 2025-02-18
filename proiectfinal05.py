from abc import ABC, abstractmethod

# Clasa abstractă Person
class Person(ABC):
    def __init__(self, name, email, address, password):
        self.name = name
        self._email = email
        self.__password = password
        self._address = address
        self.__login = False

    def check_email(self):
        return '@' in self._email
    
    def check_login(self, email, password):
        if self._email == email and self.__password == password:
            self.__login = True
            return True
        return False

    @abstractmethod
    def display_info(self):
        pass

# Clasa Employee moștenește Person
class Employee(Person):
    def __init__(self, name, email, address, password, salary):
        super().__init__(name, email, address, password)
        self.__salary = salary
        self._working_hours = 0

    def increase_salary(self, percentage):
        self.__salary += self.__salary * (percentage / 100)
    
    def checkin(self):
        print(f"{self.name} a început lucrul.")
    
    def checkout(self, hours):
        self._working_hours += hours
        print(f"{self.name} a terminat lucrul și a lucrat {hours} ore.")
    
    def display_info(self):
        return f"Employee: {self.name}, Email: {self._email}, Salary: {self.__salary}, Address: {self._address}, Working Hours: {self._working_hours}"

# Subclasa ContractEmployee
class ContractEmployee(Employee):
    def __init__(self, name, email, address, password, salary, contract_expiration):
        super().__init__(name, email, address, password, salary)
        self.contract_expiration = contract_expiration
    
    def display_info(self):
        return super().display_info() + f", Contract Expiration: {self.contract_expiration}"

# Subclasa Freelancer
class Freelancer(Employee):
    def __init__(self, name, email, address, password, salary, projects):
        super().__init__(name, email, address, password, salary)
        self.projects = projects
    
    def display_info(self):
        return super().display_info() + f", Projects: {self.projects}"

# Clasa User moștenește Person
class User(Person):
    def __init__(self, name, email, address, password, phone):
        super().__init__(name, email, address, password)
        self.phone = phone
        self.shopping_history = {}
    
    def add_product(self, product, quantity):
        if product.name in self.shopping_history:
            self.shopping_history[product.name] += quantity
        else:
            self.shopping_history[product.name] = quantity
    
    def total_spent(self):
        return sum(product.get_price() * quantity for product, quantity in self.shopping_history.items())
    
    def display_info(self):
        return f"User: {self.name}, Email: {self._email}, Phone: {self.phone}, Address: {self._address}"

# Subclasa StandardUser
class StandardUser(User):
    def calculate_discount(self):
        total = self.total_spent()
        return total * 0.1 if total > 10000 else total * 0.05

# Clasa Product
class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.__price = price
        self.quantity = quantity
        self._description = description
    
    def get_price(self):
        return self.__price
    
    def check_quantity(self):
        return self.quantity > 10

# main.py
products = [
    Product("Laptop", 3500.99, 15, "Laptop performant"),
    Product("Mouse", 150.50, 5, "Mouse wireless"),
    Product("Tastatura", 200.00, 25, "Tastatura mecanica"),
    Product("Monitor", 1200.75, 8, "Monitor Full HD"),
    Product("Casti", 300.90, 12, "Casti cu noise cancelling")
]

employees = {
    Employee("Alex Pop", "alex.pop@example.com", "Strada Libertății 12", "pass123", 4500),
    ContractEmployee("Maria Ionescu", "maria.ionescu@example.com", "Bulevardul Unirii 45", "pass456", 5200, "2025-12-31"),
    Freelancer("Ion Georgescu", "ion.geo@example.com", "Strada Victoriei 5", "pass789", 3000, 5)
}

users = {
    StandardUser("Elena Dobre", "elena.dobre@example.com", "Strada Mihai Eminescu 10", "userpass", "0744556677"),
    StandardUser("Radu Dumitru", "radu.d@example.com", "Bulevardul Carol 25", "pass999", "0733667788")
}

print("\nInformatii utilizatori:")
for user in users:
    print(user.display_info())

print("\nInformatii angajati:")
for employee in employees:
    print(employee.display_info())
