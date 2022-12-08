import csv

import matplotlib.pyplot as plt
save_location='visualization/'

""" 1000-RECENT"""
save_location+='1000-recent/'

""" chessboard """
save_location+='chessboard/'

plt.title("K = 3 , 1000-recent")
save_location+='k=3'

plt.ylabel("accuracy")
save_location+='_acc.png'
files = ['results/1000-recent/chessboard/results_k=3_fgt=0_acuracia.csv',
         'results/1000-recent/chessboard/results_k=3_fgt=50_acuracia.csv',
         'results/1000-recent/chessboard/results_k=3_fgt=125_acuracia.csv',
         'results/1000-recent/chessboard/results_k=3_fgt=250_acuracia.csv',
         'results/1000-recent/chessboard/results_k=3_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/1000-recent/chessboard/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 1000-recent")
# save_location+='k=5'

# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/1000-recent/chessboard/results_k=5_fgt=0_acuracia.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=50_acuracia.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=125_acuracia.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=250_acuracia.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/1000-recent/chessboard/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/chessboard/results_k=5_fgt=375_acuracia_balanceada.csv']

""" INTERCHANGING-RBF """
# save_location+='interchanging-rbf/'

# plt.title("K = 3 , 1000-recent")
# save_location+='k=3'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/1000-recent/interchanging-rbf/results_k=3_fgt=0_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=50_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=125_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=250_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=375_acuracia.csv']
# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/1000-recent/interchanging-rbf/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 1000-recent")
# save_location+='k=5'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/1000-recent/interchanging-rbf/results_k=5_fgt=0_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=50_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=125_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=250_acuracia.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=375_acuracia.csv']
# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/1000-recent/interchanging-rbf/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/interchanging-rbf/results_k=5_fgt=375_acuracia_balanceada.csv']

""" MOVING-SQUARES """
# save_location+='moving_squares/'

# plt.title("K = 3 , 1000-recent")
# save_location+='k=3'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/1000-recent/moving_squares/results_k=3_fgt=0_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=50_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=125_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=250_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=375_acuracia.csv']
# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/1000-recent/moving_squares/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 1000-recent")
# save_location+='k=5'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/1000-recent/moving_squares/results_k=5_fgt=0_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=50_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=125_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=250_acuracia.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/1000-recent/moving_squares/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/moving_squares/results_k=5_fgt=375_acuracia_balanceada.csv']

""" POKER """
# save_location+='poker/'

# plt.title("K = 3 , 1000-recent")
# save_location+='k=3'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/1000-recent/poker/results_k=3_fgt=0_acuracia.csv',
#          'results/1000-recent/poker/results_k=3_fgt=50_acuracia.csv',
#          'results/1000-recent/poker/results_k=3_fgt=125_acuracia.csv',
#          'results/1000-recent/poker/results_k=3_fgt=250_acuracia.csv',
#          'results/1000-recent/poker/results_k=3_fgt=375_acuracia.csv']
# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/1000-recent/poker/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 1000-recent")
# save_location+='k=5'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/1000-recent/poker/results_k=5_fgt=0_acuracia.csv',
#          'results/1000-recent/poker/results_k=5_fgt=50_acuracia.csv',
#          'results/1000-recent/poker/results_k=5_fgt=125_acuracia.csv',
#          'results/1000-recent/poker/results_k=5_fgt=250_acuracia.csv',
#          'results/1000-recent/poker/results_k=5_fgt=375_acuracia.csv']
# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/1000-recent/poker/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/1000-recent/poker/results_k=5_fgt=375_acuracia_balanceada.csv']


##########################################################################################
""" 5000-RECENT"""
# save_location+='5000-recent/'

""" chessboard """
# save_location+='chessboard/'

# plt.title("K = 3 , 5000-recent")
# save_location+='k=3'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/5000-recent/chessboard/results_k=3_fgt=0_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=50_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=125_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=250_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=375_acuracia.csv']
# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/5000-recent/chessboard/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 5000-recent")
# save_location+='k=5'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/5000-recent/chessboard/results_k=5_fgt=0_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=50_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=125_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=250_acuracia.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/5000-recent/chessboard/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/chessboard/results_k=5_fgt=375_acuracia_balanceada.csv']

""" INTERCHANGING-RBF """
# save_location+='interchanging-rbf/'

# plt.title("K = 3 , 5000-recent")
# save_location+='k=3'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/5000-recent/interchanging-rbf/results_k=3_fgt=0_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=50_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=125_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=250_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/5000-recent/interchanging-rbf/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 5000-recent")
# save_location+='k=5'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/5000-recent/interchanging-rbf/results_k=5_fgt=0_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=50_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=125_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=250_acuracia.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/5000-recent/interchanging-rbf/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/interchanging-rbf/results_k=5_fgt=375_acuracia_balanceada.csv']

""" MOVING-SQUARES """
# save_location+='moving_squares/'

# plt.title("K = 3 , 5000-recent")
# save_location+='k=3'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/5000-recent/moving_squares/results_k=3_fgt=0_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=50_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=125_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=250_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/5000-recent/moving_squares/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 5000-recent")
# save_location+='k=5'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/5000-recent/moving_squares/results_k=5_fgt=0_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=50_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=125_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=250_acuracia.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/5000-recent/moving_squares/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/moving_squares/results_k=5_fgt=375_acuracia_balanceada.csv']

""" POKER """
# save_location+='poker/'

# plt.title("K = 3 , 5000-recent")
# save_location+='k=3'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/5000-recent/poker/results_k=3_fgt=0_acuracia.csv',
#          'results/5000-recent/poker/results_k=3_fgt=50_acuracia.csv',
#          'results/5000-recent/poker/results_k=3_fgt=125_acuracia.csv',
#          'results/5000-recent/poker/results_k=3_fgt=250_acuracia.csv',
#          'results/5000-recent/poker/results_k=3_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/5000-recent/poker/results_k=3_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=3_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=3_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=3_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=3_fgt=375_acuracia_balanceada.csv']

# plt.title("K = 5 , 5000-recent")
# save_location+='k=5'
# plt.ylabel("accuracy")
# save_location+='_acc.png'
# files = ['results/5000-recent/poker/results_k=5_fgt=0_acuracia.csv',
#          'results/5000-recent/poker/results_k=5_fgt=50_acuracia.csv',
#          'results/5000-recent/poker/results_k=5_fgt=125_acuracia.csv',
#          'results/5000-recent/poker/results_k=5_fgt=250_acuracia.csv',
#          'results/5000-recent/poker/results_k=5_fgt=375_acuracia.csv']

# plt.ylabel("mean accuracy")
# save_location+='_mean_acc.png'
# files = ['results/5000-recent/poker/results_k=5_fgt=0_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=5_fgt=50_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=5_fgt=125_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=5_fgt=250_acuracia_balanceada.csv',
#          'results/5000-recent/poker/results_k=5_fgt=375_acuracia_balanceada.csv']



data_for_plot = []

for file in files:
    try:
        reader = open(file, 'r')
        dicti = dict()
        dicti['n_answers'] = []
        dicti['metric'] = []
        dicti['percentage'] = []
        Lines = reader.readlines()
        for row in Lines:
            colunas = row.split()
            dicti['n_answers'].append(float(colunas[0].strip("[]").replace(',','')))
            dicti['metric'].append(colunas[1].strip(":"))
            dicti['percentage'].append(float(colunas[2].strip("%")))
        data_for_plot.append(dicti)
    except OSError:
        print ("Could not open/read file:", file)
        exit()

for data in data_for_plot:
    plt.plot(data['n_answers'], data['percentage'])
    if (data['metric'][1] == 'Accuracy'):
        plt.yticks(range(65,100,5))
    else:
        plt.yticks(range(0, 100, 10))
        # plt.locator_params(axis='y', nbins=10)
    plt.locator_params(axis='x', nbins=10)



plt.xlabel('total dados lidos')

plt.legend(['Upper Bound', '0.1', '0.25', '0.5', '0.75'])

plt.savefig(save_location)
plt.show()



