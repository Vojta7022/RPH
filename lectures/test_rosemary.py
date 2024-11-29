from rosemary import Item, update
import random

def test_name_change_normal_item():
    item = Item('Bread', days_left=3, quality=5)
    update(item)
    return item.name == 'Bread'

def test_name_change_brie():
    item = Item('Aged Brie', days_left=3, quality=5)
    update(item)
    return item.name == 'Aged Brie'

def test_name_change_diamond():
    item = Item('Diamond', days_left=3, quality=5)
    update(item)
    return item.name == 'Diamond'

def test_name_change_tickets():
    item = Item('Tickets', days_left=3, quality=5)
    update(item)
    return item.name == 'Tickets'

def test_normal_item_decreases_days_left():
    item = Item('Bread', days_left=3, quality=5)
    update(item)
    return item.days_left == 2

def test_normal_item_decreases_days_left_after_day_0():
    item = Item('Bread', days_left=-1, quality=5)
    update(item)
    return item.days_left == -2

def test_diamond_decreases_days_left_after_day_0():
    item = Item('Diamond', days_left=-1, quality=5)
    update(item)
    return item.days_left == -1

def test_brie_decreases_days_left_after_day_0():
    item = Item('Aged Brie', days_left=-1, quality=5)
    update(item)
    return item.days_left == -2

def test_tickets_decreases_days_left_after_day_0():
    item = Item('Tickets', days_left=-1, quality=5)
    update(item)
    return item.days_left == -2

def test_normal_item_decreases_quality():
    item = Item('Bread', days_left=3, quality=5)
    update(item)
    return item.quality == 4

def test_normal_item_decreases_quality_after_day_0():
    item = Item('Bread', days_left=-1, quality=5)
    update(item)
    return item.quality == 3

def test_lower_quality_range():
    item = Item('Bread', days_left=3, quality=0)
    update(item)
    return item.quality == 0

def test_upper_quality_range_brie():
    item = Item('Aged Brie', days_left=3, quality=50)
    update(item)
    return item.quality == 50

def test_upper_quality_range_tickets():
    item = Item('Tickets', days_left=3, quality=50)
    update(item)
    return item.quality == 50

def test_no_days_left_decrease():
    item = Item('Bread', days_left=0, quality=5)
    update(item)
    return item.quality == 3

def test_diamonds_quality():
    item = Item('Diamond', days_left=5, quality=100)
    update(item)
    return item.quality == 100

def test_diamonds_days_left():
    item = Item('Diamond', days_left=5, quality=100)
    update(item)
    return item.days_left == 5

def test_brie_days_left():
    item = Item('Aged Brie', days_left=3, quality=5)
    update(item)
    return item.days_left == 2

def test_brie_quality():
    item = Item('Aged Brie', days_left=3, quality=5)
    update(item)
    return item.quality == 6

def test_brie_quality_after_day_0():
    item = Item('Aged Brie', days_left=-1, quality=5)
    update(item)
    return item.quality == 6

def test_tickets_days_left():
    item = Item('Tickets', days_left=3, quality=5)
    update(item)
    return item.days_left == 2

def test_tickets_days_left_after_0():
    item = Item('Tickets', days_left=-1, quality=5)
    update(item)
    return item.days_left == -2

def test_tickets_quality_more_than_10():
    item = Item('Tickets', days_left=11, quality=5)
    update(item)
    return item.quality == 6

def test_tickets_quality_6_10():
    item = Item('Tickets', days_left=6, quality=5)
    update(item)
    return item.quality == 7

def test_tickets_quality_6_10_2():
    item = Item('Tickets', days_left=10, quality=5)
    update(item)
    return item.quality == 7

def test_tickets_quality_1_5():
    item = Item('Tickets', days_left=1, quality=5)
    update(item)
    return item.quality == 8

def test_tickets_quality_1_5_2():
    item = Item('Tickets', days_left=5, quality=5)
    update(item)
    return item.quality == 8

def test_tickets_quality_day_0():
    item = Item('Tickets', days_left=0, quality=5)
    update(item)
    return item.quality == 0

def test_tickets_quality_day_after_0():
    item = Item('Tickets', days_left=-1, quality=5)
    update(item)
    return item.quality == 0

def test_tickets_quality_over_50_day_more_than_10():
    item = Item('Tickets', days_left=11, quality=50)
    update(item)
    return item.quality == 50

def test_tickets_quality_over_50_day_6_10():
    item = Item('Tickets', days_left=6, quality=50)
    update(item)
    return item.quality == 50

def test_tickets_quality_over_50_day_1_5():
    item = Item('Tickets', days_left=1, quality=50)
    update(item)
    return item.quality == 50

# def test_random():
#     return random.choice([True, False])
