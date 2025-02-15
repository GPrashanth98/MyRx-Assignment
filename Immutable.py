from collections import OrderedDict
from datetime import datetime
from typing import List
from dataclasses import dataclass, field
from copy import deepcopy

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    zip_code: str

@dataclass(frozen=True)
class Employee:
    name: str
    id: str
    date_of_joining: datetime
    addresses: List[Address] = field(default_factory=list)
    
    def get_addresses(self):
        return deepcopy(self.addresses)

# Example usage
name = input("Name: ")
id = input("Id: ")
date_of_joining = datetime.strptime(input("DateOfJoining: "), "%Y-%m-%d")
num_addresses = int(input("Number of addresses: "))
addresses = [Address(input("Street: "), input("City: "), input("Zip code: ")) for _ in range(num_addresses)]

employee = Employee(name, id, date_of_joining, addresses)
print(employee)