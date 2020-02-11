# Shopping Cart

## Installation

Fork this repo, then clone your fork to download it locally onto your computer.  Then navigate there from the command line.

```sh
cd ~/Documents/OPIM-243/GitHub/shopping-cart
```
## Setup

### Environment Setup

Setup a virtual enviorment called something like "shopping-env" and from within it install gspread & dotenv packages

```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env

pip install gspread oauth2client

pip install python-dotenv
```
## Usage

Run the Shopping Cart Program

```sh
python shopping_cart.py
```
