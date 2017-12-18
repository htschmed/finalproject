from data import get_data_frame, plot_graph


print('\n')
print('Retrieving data, please wait...')
df = get_data_frame('2009-1-1', '2017-12-1', 'BCHAIN/MKPRU', 'annual', 'bitcoin', 100, 100)
print('\n')
print('This table shows the value of bitcoin and the Reddit statistics for posts containing "bitcoin"')
print('\n')
print(df)
print('\n')
print('Press any key "Enter" to view the graph')
input()

plot_graph(df, 'Bitcoin worth in USD', 'Price of Bitcoin from 1/1/2009 to 12/1/2017')