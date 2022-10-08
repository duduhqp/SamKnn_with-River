import os
import sys

from river import stream
from river import evaluate
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
initializing streams by passing csv datasets to stream constructor,with specific casting and target
"""
converters_interchanging = {'1': float, '2': float,'3':int}
target_interchanging = '3'
# stream_interchanging = stream.iter_csv("C:/Users/Pichau/Documents/GitHub/research-project-stream-learning/lazy/fgt-sam-knn-tests/1000-recent/interchanging-rbf/interchanging.csv", converters=converters_interchanging, target= target_interchanging)

converters_chessboard = {'1': float, '2': float,'3':int}
target_chessboard = '3'
# stream_chessboard = stream.iter_csv("C:/Users/Pichau/Documents/GitHub/research-project-stream-learning/lazy/fgt-sam-knn-tests/1000-recent/chessboard/chessboard.csv", converters=converters_chessboard, target= target_chessboard)

converters_squares = {'feat_1': float, 'feat_2': float,'target':int}
target_squares = 'target'
# stream_squares = stream.iter_csv("C:/Users/Pichau/Documents/GitHub/research-project-stream-learning/lazy/fgt-sam-knn-tests/1000-recent/moving_squares/squares.csv", converters=converters_squares, target= target_squares)

converters_poker = {'1':int, '2':int, '3':int, '4':int, '5':int, '6':int, '7':int, '8':int, '9':int, '10':int, '11':int}
target_poker = '11'
# stream_poker = stream.iter_csv("C:/Users/Pichau/Documents/GitHub/research-project-stream-learning/lazy/fgt-sam-knn-tests/1000-recent/poker/poker.csv", converters=converters_poker, target= target_poker)



def generate_samknn_models(k, wind_size):
    # list with number of samples to be forgotten
    n_samples_fgt = [0.1, 0.25, 0.50, 0.75]
    # initialize list of SAMKNN with model which won't have data forgotten - 25% not forget
    samknn_models = [FGTSAMKNN(n_neighbors=k, max_window_size=wind_size, fgt=False)]
    # loop to add samknn's that will have data forgotten
    for i in range(4):
        samknn_models.append(FGTSAMKNN(n_neighbors=k,max_window_size=wind_size, fgt_n_instances=n_samples_fgt[i]))
    return samknn_models


def generate_different_k_values_sam_knn_models(starting_k_value):
    # list that will contain lists with samknn models, each with its own 'k' values
    samknn_models_nested = []
    # loop to append to samknn_models_nested samknn models with k = [3, 5]
    for j in range(starting_k_value, 4, 2):
        # print('k='+str(j))
        samknn_models_nested.append(generate_samknn_models(j, 5000))
    #No final terá 10 modelos, cinco deles com k=3 e taxa de esquecimento de [0%, 10%, 25%, 50%, 75%] e cinco deles com k=5 e taxa de esquecimento de [0%, 10%, 25%, 50%, 75%]
    return samknn_models_nested


def evaluated(dataset_name,converters, target, metrics, starting_k_value=3):
    samknn_list = generate_different_k_values_sam_knn_models(starting_k_value)

    for i in samknn_list:
        # file_name = 'fgt-sam-knn-tests/1000-recent/' + dataset_name + '/results_k=' + str(samknn_list[i][0].n_neighbors) + '_ws=' + str(samknn_list[i][0].window_size) + '.log'
        for j in i:
            streamed = stream.iter_csv(dataset_name, converters=converters, target=target)
            file_name = 'results_k='+ str(j.n_neighbors) + '_ws=' + str(j.window_size) + '_fgt=' + str(j.fgt_n_instances) + '.log'
            f = open(file_name, 'w')
            # f2 = open(file_name+'x','w')
            print('abri arquivo '+ file_name)
            FGTProgressive_val_score.progressive_val_score(dataset=streamed,
                                                       model=j,
                                                       metric=metrics,
                                                       print_every=200,
                                                       file=f)
            # evaluate.progressive_val_score(dataset=stream, model=samknn_list[i][j], metric=metrics, print_every=200, file =f2)
            f.close()
            # f2.close()
            print('fechei arquivo')


from river import metrics

metric = metrics.Accuracy()

"""
generate results for each dataset
"""
# evaluate('datasets/1000-recent/interchanging-rbf/interchanging.csv', converters_interchanging, target_interchanging, metric)
# evaluate('datasets/1000-recent/moving_squares/squares.csv', converters_squares, target_squares, metric)
evaluated("datasets/1000-recent/chessboard/chessboard.csv",converters_chessboard, target_chessboard, metric)
# evaluate('datasets/1000-recent/poker/poker.csv', converters_poker, target_poker, metric)
