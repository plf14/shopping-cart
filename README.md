# Shopping Cart Project

## Installation

Fork this repo, then clone your fork to download it locally onto your computer.  Then navigate there from the command line.

```sh
cd ~/Documents/OPIM-243/GitHub/shopping-cart
```
## Setup

### Environment Setup

Setup a virtual enviorment called something like "shopping-env" and from within it install gspread & dotenv packages

gspread:  https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/gspread.md

dotenv:  https://github.com/prof-rossetti/intro-to-python/blob/master/projects/shopping-cart/challenges.md#integrating-with-a-google-sheets-datastore

```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env

pip install gspread oauth2client

pip install python-dotenv
```
### .env Setup

Use your text editor or the command-line to create a file in that repo called ".env", and then place the following contents inside:

```sh
GOOGLE_SHEET_ID = "1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI"
SHEET_NAME = "products-custom"
Tax = ".0875"
```
Optionally you can customize these variables to apply to your own product list or local tax rate.

## Usage

Run the Shopping Cart Program

```sh
python shopping_cart.py
```
