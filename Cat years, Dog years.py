def human_years_cat_years_dog_years(human_years):
    if human_years >= 1 and type(human_years) == int: 
        if human_years == 1:
            return [1, 15, 15]
        elif human_years == 2:
            return [2, 24, 24]
        else:
            cat_years = ((human_years - 2) * 4) + 24
            dog_years = ((human_years - 2) * 5) + 24
            return [human_years, cat_years, dog_years]
    else:
        return 'Недопустимое значение'
    
print(human_years_cat_years_dog_years(25))