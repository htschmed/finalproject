from data import get_data_frame, plot_graph

def print_btc_value(start_date, end_date, interval, min_score=100, sample_size=100):
    print('\n')
    print('Retrieving data, please wait...')
    df = get_data_frame(start_date, end_date, 'BCHAIN/MKPRU', interval, 'bitcoin', min_score, sample_size)
    print('\n')
    print('This table shows the value of bitcoin and the Reddit statistics for posts containing "bitcoin"')
    print('\n')
    print(df)
    print('\n')
    print('Press any key "Enter" to view the graph')
    input()

    plot_graph(df.loc[:,['Date','Value']], 'Date', None, ['Bitcoin worth in USD'],
               'Price of Bitcoin from {} to {}'.format(start_date, end_date))

    plot_graph(df.loc[:,['Date','posts']], 'Date', None, ['Number of Reddit Posts'],
               '\nTop {} Reddit posts with search term of "bitcoin"\n and with minimum score of {}\n from {} to {}'.format(
                   sample_size, min_score, start_date, end_date), 0.85)

    plot_graph(df.loc[:, ['Date', 'mean', 'mode', 'median']], 'Date', None,
               ['Mean Score', 'Mode Score', 'Median Score'],
               '\nTop {} Reddit posts with search term of "bitcoin"\n and with minimum score of {}\n from {} to {}'.format(
                   sample_size, min_score, start_date, end_date), 0.85)

def print_btc_difficulty(start_date, end_date, interval, min_score=100, sample_size=100):
    print('\n')
    print('Retrieving data, please wait...')
    df = get_data_frame(start_date, end_date, 'BCHAIN/DIFF', interval, 'bitcoin mining', min_score, sample_size)
    print('\n')
    print('This table shows the difficulty of verifying bitcoin blocks and the Reddit statistics for posts containing "bitcoin mining"')
    print('\n')
    print(df)
    print('\n')
    print('Press any key "Enter" to view the graph')
    input()

    plot_graph(df.loc[:, ['Date', 'Value']], 'Date', None, ['Bitcoin Difficulty'],
               'Bitcoin Difficulty from {} to {}'.format(start_date, end_date))

    plot_graph(df.loc[:, ['Date', 'posts']], 'Date', None, ['Number of Reddit Posts'],
               '\nTop {} Reddit posts with search term of "bitcoin mining"\n and with minimum score of {}\n from {} to {}'.format(
                   sample_size, min_score, start_date, end_date), 0.85)

    plot_graph(df.loc[:, ['Date', 'mean', 'mode', 'median']], 'Date', None, ['Mean Score', 'Mode Score', 'Median Score'],
               '\nTop {} Reddit posts with search term of "bitcoin mining"\n and with minimum score of {}\n from {} to {}'.format(
                   sample_size, min_score, start_date, end_date), 0.85)


def print_menu():
    print('Please select a dataset to view:')
    print('[0] Exit')
    print('[1] BTC Value')
    print('[2] BTC Difficulty')


def prompt_dataset_options():
    options = {}

    print('Enter interval: [annual][quarterly][monthly]')
    options['interval'] = input()

    print('Enter start_date: format YYYY-MM-DD')
    options['start_date'] = input()

    print('Enter end_date: format YYYY-MM-DD')
    options['end_date'] = input()

    print('OPTIONAL - Enter min_score: Default 100')
    min_score = input()
    if min_score != '':
        options['min_score'] = int(min_score)

    print('OPTIONAL - Enter sample_size: Default 100')
    sample_size = input()
    if sample_size != '':
        options['sample_size'] = int(sample_size)

    return options

def route_menu_selection(number):
    if number == 0:
        exit()
    elif number == 1:
        options = prompt_dataset_options()
        print_btc_value(**options)
    elif number == 2:
        options = prompt_dataset_options()
        print_btc_difficulty(**options)

def main():
    while True:
        print_menu()
        selection = input()
        try:
            selection = int(selection)
        except ValueError:
            print('Invalid input entered...')
            continue
        try:
            if selection == 0:
                break;
            route_menu_selection(selection)
        except:
            print('Something went wrong during your selection process, please try again')

main()