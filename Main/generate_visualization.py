import csv

import matplotlib.pyplot as plt

""" CHESSBOARD """

plt.title("K = 3 , 1000-recent")

plt.ylabel("accuracy")
files = ['results/1000-recent/chessboard/results_k=3_fgt=0_acuracia.csv',
         'results/1000-recent/chessboard/results_k=3_fgt=50_acuracia.csv',
         'results/1000-recent/chessboard/results_k=3_fgt=125_acuracia.csv',
         'results/1000-recent/chessboard/results_k=3_fgt=250_acuracia.csv',
         'results/1000-recent/chessboard/results_k=3_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/1000-recent/chessboard/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 1000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/1000-recent/chessboard/results_k=5_fgt=0_acuracia.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=50_acuracia.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=125_acuracia.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=250_acuracia.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/1000-recent/chessboard/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 3 , 5000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/5000-recent/chessboard/results_k=3_fgt=0_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=50_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=125_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=250_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/5000-recent/chessboard/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 5000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/5000-recent/chessboard/results_k=5_fgt=0_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=50_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=125_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=250_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/5000-recent/chessboard/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=375_acuracia_balanceada.csv']

""" INTERCHANGING-RBF """
#
# plt.title("K = 3 , 1000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/1000-recent/interchanging-rbf/results_k=3_fgt=0_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=50_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=125_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=250_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/1000-recent/interchanging-rbf/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 1000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/1000-recent/interchanging-rbf/results_k=5_fgt=0_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=50_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=125_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=250_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/1000-recent/interchanging-rbf/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 3 , 5000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/5000-recent/interchanging-rbf/results_k=3_fgt=0_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=50_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=125_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=250_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/5000-recent/interchanging-rbf/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 5000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/5000-recent/interchanging-rbf/results_k=5_fgt=0_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=50_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=125_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=250_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/5000-recent/interchanging-rbf/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=375_acuracia_balanceada.csv']

""" MOVING-SQUARES """

# plt.title("K = 3 , 1000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/1000-recent/moving_squares/results_k=3_fgt=0_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=50_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=125_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=250_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/1000-recent/moving_squares/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 1000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/1000-recent/moving_squares/results_k=5_fgt=0_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=50_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=125_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=250_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/1000-recent/moving_squares/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 3 , 5000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/5000-recent/moving_squares/results_k=3_fgt=0_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=50_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=125_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=250_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/5000-recent/moving_squares/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 5000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/5000-recent/moving_squares/results_k=5_fgt=0_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=50_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=125_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=250_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/5000-recent/moving_squares/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=375_acuracia_balanceada.csv']

""" POKER """

# plt.title("K = 3 , 1000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/1000-recent/poker/results_k=3_fgt=0_acuracia.csv',
#          'results/1000-recent/poker/results_k=3_fgt=50_acuracia.csv',
#          'results/1000-recent/poker/results_k=3_fgt=125_acuracia.csv',
#          'results/1000-recent/poker/results_k=3_fgt=250_acuracia.csv',
#          'results/1000-recent/poker/results_k=3_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/1000-recent/poker/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 1000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/1000-recent/poker/results_k=5_fgt=0_acuracia.csv',
#          'results/1000-recent/poker/results_k=5_fgt=50_acuracia.csv',
#          'results/1000-recent/poker/results_k=5_fgt=125_acuracia.csv',
#          'results/1000-recent/poker/results_k=5_fgt=250_acuracia.csv',
#          'results/1000-recent/poker/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/1000-recent/poker/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=5_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 3 , 5000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/5000-recent/poker/results_k=3_fgt=0_acuracia.csv',
#          'results/5000-recent/poker/results_k=3_fgt=50_acuracia.csv',
#          'results/5000-recent/poker/results_k=3_fgt=125_acuracia.csv',
#          'results/5000-recent/poker/results_k=3_fgt=250_acuracia.csv',
#          'results/5000-recent/poker/results_k=3_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/5000-recent/poker/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 5000-recent")
#
# plt.ylabel("accuracy")
# files = ['results/5000-recent/poker/results_k=5_fgt=0_acuracia.csv',
#          'results/5000-recent/poker/results_k=5_fgt=50_acuracia.csv',
#          'results/5000-recent/poker/results_k=5_fgt=125_acuracia.csv',
#          'results/5000-recent/poker/results_k=5_fgt=250_acuracia.csv',
#          'results/5000-recent/poker/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# files = ['results/5000-recent/poker/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=5_fgt=375_acuracia_balanceada.csv']



data_for_plot = []

for file in files:
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        dicti = dict()
        dicti['n_answers'] = []
        dicti['metric'] = []
        dicti['percentage'] = []
        for rows in csv_reader:
            if len(rows)>1:
                rows[0] = rows[0]+rows[1]
                rows.pop(1)
            for row in rows:
                colunas = row.split()
                for i in range(len(colunas)):
                    if (i == 0):
                        dicti['n_answers'].append(colunas[i].strip("[]:%"))
                    elif (i == 1):
                        dicti['metric'].append(colunas[i].strip("[]:%"))
                    else:
                        dicti['percentage'].append(colunas[i].strip("[]:%"))
        data_for_plot.append(dicti)

for data in data_for_plot:
    plt.plot(data['n_answers'], data['percentage'])


plt.xlabel('total dados lidos')

plt.legend(['Upper Bound', '0.1', '0.25', '0.5', '0.75'])

# plt.tight_layout()
plt.show()



