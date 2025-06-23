def get_oldest(ages: dict) -> str:
    cur_old_name = ''
    cur_old_age = -float('inf')
    for name, age in ages.items():
        if age > cur_old_age:
            cur_old_age = age
            cur_old_name = name
        elif age == cur_old_age:
            cur_old_name = min(name, cur_old_name)
    return cur_old_name


# assert get_oldest({'Пантелеймон': 34, 'Нина': 34, 'Любовь': 25, 'Станислав': 34}) == 'Нина'
# assert get_oldest({'Павел': 43, 'Нифонт': 38, 'Юлия': 21, 'Сергей': 45, 'Осип': 30}) == 'Сергей'
