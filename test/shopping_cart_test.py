
import pytest
import datetime

from app.shopping_cart import to_usd, human_friendly_timestamp, find_product

def test_to_usd():
    # it should apply USD formatting
    assert to_usd(4.50) == "$4.50"

    # it should display two decimal places
    assert to_usd(4.5) == "$4.50"

    # it should round to two places
    assert to_usd(4.55555) == "$4.56"

    # it should display thousands separators
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"

def test_human_friendly_timestamp():
    time = datetime.datetime(1776,7,4,11,36,42)
    time2 = datetime.datetime(1776,7,4,14,32,17)
    result = human_friendly_timestamp(time)
    result2 = human_friendly_timestamp(time2)
    # it should display a properly formatted time
    assert result == "11:36 AM"
    # it should properly display AM/PM
    assert result2 == "02:32 PM"

def test_find_product():
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    ]

    # if there is a match, it should find and return a product
    matching_product = find_product("3", products)
    assert matching_product["price"] == 2.49

    # if there is no match, it should raise an IndexError
    with pytest.raises(IndexError):
        find_product("2222", products)