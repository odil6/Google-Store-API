import matplotlib.pyplot as plt
import csv
from collections import Counter


# Get the number of apps for each category
def get_categories(categories):
    with open('googleplaystore.csv', 'rt', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader):
            category = format(row['Category'])
            if not (category in categories.keys()):
                categories[category] = 1
            else:
                categories[category] += 1


# Counts the number of free apps vs. the paid apps.
# It returns the average price for an app
def count_free_paid(free_paid):
    price_av = 0
    app_count = 0
    free_paid['Free'] = 0
    free_paid['Paid'] = 0
    with open('googleplaystore.csv', 'rt', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader):
            is_free = format(row['Type'])
            if is_free == 'Free':
                free_paid['Free'] += 1
            elif is_free == 'Paid':
                free_paid['Paid'] += 1
                price_av += float(format(row['Price'])[1:])
            app_count += 1
    return price_av / app_count


# Get the number of apps for each rating score
def get_ratings():
    rating_list = []
    with open('googleplaystore.csv', 'rt', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader):
            if format(row['Rating']) != 'NaN':
                rating_list.append(format(row['Rating']))
    counts = Counter(rating_list)
    return counts


# shows only 3.0 rating and above!
# Creates and shows the number of apps per rating score.
# Those are sorted in order to make sense
def plt_ratings(ratings):
    keys = ratings.keys()
    scores = []
    counts = []
    for key in sorted(keys):
        if format(key) != 'NaN' and float(format(key)) >= 3.0:
            scores.append(key)
            counts.append(ratings[key])
    plt.scatter(scores, counts)
    plt.xlabel('Rating Scores')
    plt.ylabel('Number Of Apps For Score')
    plt.show()


# Creates and shows the table that compares free and paid apps.
# It also shows the average price for an app for the entire database.
def plt_free(average):
    keys = free_paid.keys()
    count = 0
    number_of_apps = []
    amount = []
    f_p = []
    for k in keys:
        f_p.append(k)
        amount.append(free_paid[k])
        count += 1
        number_of_apps.append(count)
    plt.ylabel('Number Of Apps')
    plt.bar(number_of_apps, amount, tick_label=f_p,
            width=0.1, color=['blue', 'brown'])
    plt.text(1.2, 9000, f'Average Price For App: \n{average}',
             fontsize=18, bbox=dict(facecolor='red', alpha=0.5))
    plt.ylabel('Number Of Apps')
    plt.show()


# Creates and shows apps per genre.
def plt_genres(categories):
    keys = categories.keys()
    count = 0
    number_of_apps = []
    amount = []
    genre = []
    for k in keys:
        genre.append(k)
        amount.append(categories[k])
        count += 1
        number_of_apps.append(count)
    plt.ylabel('Number Of Apps')
    plt.gcf().autofmt_xdate()
    plt.subplots_adjust(right=2)

    plt.bar(number_of_apps, amount, tick_label=genre,
            width=0.2, color=['blue', 'brown'])

    plt.ylabel('Number Of Apps')
    plt.show()


# Creates a new file that holds the apps of a specific genre selected by the user.
# The user chose with 0, 1 or 2 for both, free or paid (correspondingly)
# The file is saved as 'special genre.txt'.
def special_list(categories):
    print('Now we will make a file which will hold all the apps of the selected genre')
    l_genres = []
    for i in categories.keys():
        l_genres.append(i)

    print(f'Choose one of the following: {l_genres}')
    genre = input('choose genre:\n').upper()
    while not (genre in l_genres):
        print('Your choice is not on the list. Try again')
        genre = input('choose genre:\n').upper()

    price = int(input('Want only free or paid?\n(0 - for both,1 - for free, 2- for paid\n'))
    while int(price) != 1 and int(price) != 2 and int(price) != 0:
        print('Chose only 0, 1 or 2!')
        price = int(input('Want only free or paid?\n(0 - for both,1 - for free, 2- for paid\n'))

    file_list = []
    with open('googleplaystore.csv', 'rt', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader):
            if format(row['Category']) == genre:
                if price == 1 and format(row['Type']) == 'Free':
                    file_list.append(format(row['App']) + '\n')
                elif price == 2 and format(row['Type']) == 'Paid':
                    file_list.append(format(row['App']) + '\n')
                else:
                    file_list.append(format(row['App']) + '\n')
    with open('special genre.txt', 'w') as f:
        f.writelines(file_list)


if __name__ == '__main__':
    categories = {}
    get_categories(categories)
    free_paid = {}
    averaged_price = count_free_paid(free_paid)
    ratings = get_ratings()
    plt_ratings(ratings)
    plt_free(averaged_price)
    plt_genres(categories)
    special_list(categories)

