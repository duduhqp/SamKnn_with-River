import os
import sys

from river import stream
from fgt_sam_river import FGTSAMKNN
from fgt_progessive_val_score import FGTProgressive_val_score

cwd = os.getcwd()
sys.path.insert(0, cwd)



"""
This is a python program to generate evaluation results for 4 datasets with forgetting feature.
The aim is to compare models with the same k value and maximum window size
that forget different number of samples every 1000 samples seen.
For that purpose there are 5 forgetting values for each model: 0, 0.1, 0.25, 0.50, 0.75
"""

"""
Esse é um programa python para gerar resultados para avaliação de 4 datasets com possibilidade de esquecimento.
O objetivo é compara modelos com mesmo valor de k and tamanho máximo de janela que esquecem
diferentes valores de dados a cada 1000/5000 valores vistos.
Para esse propósito exitem 5 valores de esquecimento para cada modelo: 0, 0.1, 0.25, 0.5, 0.75.
"""


"""
Inicializando streams a partir dos arquivos csv dos datasets, especificando tipagem dos dados e os alvos.
"""
converters_interchanging = {'1': float, '2': float,'3':int}
target_interchanging = '3'

converters_chessboard = {'1': float, '2': float,'3':int}
target_chessboard = '3'

converters_squares = {'feat_1': float, 'feat_2': float,'target':int}
target_squares = 'target'

converters_poker = {'1':int, '2':int, '3':int, '4':int, '5':int, '6':int, '7':int, '8':int, '9':int, '10':int, '11':int}
target_poker = '11'



def generate_samknn_models(k, wind_size):
    # Lista com porcentagem dos dados a serem excluídos (esquecidos)
    n_samples_fgt = [0.1, 0.25, 0.50, 0.75]
    # Inicialização do modelo Upper Bound, que não haverá esqueicmento
    samknn_models = [FGTSAMKNN(n_neighbors=k, max_window_size=wind_size, fgt=False)]
    # Loop inicializando modelos com as taxas de esquecimento diferentes
    for i in range(4):
        samknn_models.append(FGTSAMKNN(n_neighbors=k,max_window_size=wind_size, fgt_n_instances=n_samples_fgt[i]))
    return samknn_models


def generate_different_k_values_sam_knn_models(starting_k_value):
    # Lista que irá conter as listas com as diferentes instâncias do modelo FGT-SAM-KNN
    samknn_models_nested = []
    # Loop para instânciar os modelos de FGT-SAM-KNN com diferentes valore de k, default k = [3, 5]
    for j in range(starting_k_value, 6, 2):
        samknn_models_nested.append(generate_samknn_models(j, 5000))
    #No final terá 10 modelos, cinco deles com k=3 e taxa de esquecimento de [0%, 10%, 25%, 50%, 75%] e cinco deles com k=5 e taxa de esquecimento de [0%, 10%, 25%, 50%, 75%]
    return samknn_models_nested


def evaluated(dataset_name,converters, target, metricas, nomes_metricas, starting_k_value=3, fgt_freq=1000):
    samknn_list = generate_different_k_values_sam_knn_models(starting_k_value)

    for i in samknn_list:
        for j in i:
            for p in range(len(metricas)):
                # Tanto a stream do dataset quanto a métrica são objetos pela biblioteca River então tenho de reinstânciá-los ou ter um array com vários objetos
                streamed = stream.iter_csv(dataset_name, converters=converters, target=target)
                metrica = metricas[p].clone()
                file_directory = dataset_name.split("/")
                # Gerando resultados para as métricas
                # file_name = 'results/'+file_directory[1]+'/'+file_directory[2]+'/'+'results_k='+ str(j.n_neighbors) + '_fgt=' + str(j.fgt_n_instances) + str(nomes_metricas[p]) + '.csv'
                # f = open(file_name, 'w')
                # print("Abriu arquivo:"+str(file_name))
                # FGTProgressive_val_score.progressive_val_score(dataset=streamed,
                #                                            model=j,
                #                                            fgt_freq=fgt_freq,
                #                                            metric=metrica,
                #                                            print_every=200,
                #                                            file=f)

                # Avaliando tempo e memória
                # file_name = 'time_and_memory_interchanging-rbf_results_k='+ str(j.n_neighbors) + '_fgt=' + str(j.fgt_n_instances) + str(nomes_metricas[p]) + '.log'
                file_name = 'time_and_memory/' + file_directory[1] + '/' + file_directory[2] + '/' + 'results_k=' + str(j.n_neighbors) + '_fgt=' + str(j.fgt_n_instances) + str(nomes_metricas[p]) + '.csv'
                f = open(file_name, 'w')
                print("Abriu arquivo:" + str(file_name))
                FGTProgressive_val_score.progressive_val_score(dataset=streamed,
                                                               model=j,
                                                               fgt_freq=fgt_freq,
                                                               metric=metrica,
                                                               print_every=20000,
                                                               file=f,
                                                               show_memory=True,
                                                               show_time=True)
                f.close()



# DEFINIR A MÉTRICA
from river import metrics

# metric = metrics.Accuracy()
# metric = metrics.BalancedAccuracy()
# metric = metrics.F1()
metricas=[metrics.Accuracy(), metrics.BalancedAccuracy()]

# Nomes das métricas para criação dos arquivos
nome_metricas=['_acuracia', '_acuracia_balanceada']

# Valor inicial de k
valor_ini_k = 3

"""
Gerar resultados para cada dataset (1000-recent)
"""
freq_esquecimento = 1000

# evaluated('datasets/1000-recent/interchanging-rbf/interchanging.csv', converters_interchanging, target_interchanging, metricas, nome_metricas, valor_ini_k, freq_esquecimento)
# evaluated('datasets/1000-recent/moving_squares/squares.csv', converters_squares, target_squares,  metricas, nome_metricas, valor_ini_k, freq_esquecimento)
# evaluated("datasets/1000-recent/chessboard/chessboard.csv",converters_chessboard, target_chessboard, metricas, nome_metricas, valor_ini_k, freq_esquecimento)
# evaluated('datasets/1000-recent/poker/poker.csv', converters_poker, target_poker,  metricas, nome_metricas, valor_ini_k, freq_esquecimento)

"""
Gerar resultados para cada dataset (5000-recent)
"""
freq_esquecimento = 5000

# evaluated('datasets/5000-recent/interchanging-rbf/interchanging.csv', converters_interchanging, target_interchanging,  metricas, nome_metricas, valor_ini_k, freq_esquecimento)
# evaluated('datasets/5000-recent/moving_squares/squares.csv', converters_squares, target_squares,  metricas, nome_metricas, valor_ini_k, freq_esquecimento)
# evaluated("datasets/5000-recent/chessboard/chessboard.csv",converters_chessboard, target_chessboard, metricas, nome_metricas, valor_ini_k, freq_esquecimento)
evaluated('datasets/5000-recent/poker/poker.csv', converters_poker, target_poker,  metricas, nome_metricas, valor_ini_k, freq_esquecimento)