# Final-Project--Online-shopping-cart
Final submission online shopping cart csc500

## Overview 
This is my final project for CSC500: Principles of Programming. Throughout the course we built smaller milestones, and this project combines everything into a full Online Shopping Cart program. It uses python classes, objects, loops, and a menu system so the user can manage a shopping cart.

The program lets the user add items, remove them, change quantities, and print descriptions or totals. It's basically an expanded version of the earlier Moving Shopping Cart assignment, but now with all the required features from the final module.

---

## Features 

#### ItesmTPurchase Class
Stores: 
- name
- price
- quantity
- description

Includes a method to print the item's cost based on quantity. 

## ShoppingCart Class 
Stores 
- customer name
- current date
- list of cart items

Includes methods to: 
- add items
- remove items
- modify quantities
- count total items
- calculate total cost
- print descriptions
- print the full cart

- --- 

#Interactive Menu 
The program runs a loop until the user chooses to quit. 
Menu options: 

| Command | What it does |
|--------|---------------|
| `a` | Add an item |
| `r` | Remove an item |
| `c` | Change item quantity |
| `i` | Print item descriptions |
| `o` | Print the full cart with totals |
| `q` | Quit |

---

## How to Run
1. Make sure Python 3 is installed.  
2. Clone the repo:
