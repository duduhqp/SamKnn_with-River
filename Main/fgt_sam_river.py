import random
from abc import ABC

import numpy as np
from river import neighbors


class FGTSAMKNN(neighbors.SAMKNNClassifier, ABC):
    def __init__(self,
                 fgt=True,
                 fgt_n_instances=0,
                 fgt_from_sub_set_length=500,
                 n_neighbors=5,
                 weighting='distance',
                 max_window_size=5000,
                 ltm_size=0.4,
                 min_stm_size=50,
                 stm_aprox_adaption=True,
                 use_ltm=True):
        super().__init__(n_neighbors=n_neighbors,
                         distance_weighting=weighting,
                         window_size=max_window_size,
                         ltm_size=ltm_size,
                         min_stm_size=min_stm_size,
                         stm_aprox_adaption=stm_aprox_adaption,
                         use_ltm=use_ltm)

        self.fgt = fgt
        if fgt_n_instances < 1 :
            fgt_n_instances = int(fgt_n_instances * fgt_from_sub_set_length)
        if fgt_from_sub_set_length < min_stm_size:
            print("O número de instâncias a serem esquecidas (fgt_n_instances) não pode ser  inferior ao tamanho mínimo da STM (min_stm_size)")
            print(fgt_n_instances)
        else :
            self.fgt_n_instances = fgt_n_instances
        self.fgt_from_sub_set_length = fgt_from_sub_set_length

    def delete_element_at_index(self, i):
        """ Deleta elemento num dado índice i da janela de amostras """
        self._stm_samples = np.delete(self._stm_samples, i, 0)
        self._stm_labels = np.delete(self._stm_labels, i, 0)

    def get_last_random(self, n_samples, sub_set_length):
        """ Seleciona 'n_samples' aleatoriamente dos elementos dentro do 'sub_set_length' mais recente """
        window_length = self._stm_labels.size
        last_random_instances = []
        last_samples_starting_position = window_length - sub_set_length
        if (last_samples_starting_position < 0):
            last_samples_starting_position = 0
        last_samples_range = range(last_samples_starting_position, window_length)
        if n_samples >  max(last_samples_range) :
            n_samples = max(last_samples_range)
        random_indexes = (random.sample(last_samples_range, n_samples))
        for i in range(n_samples):
            index = random_indexes[i]
            random_instance = (self._stm_samples[index])
            last_random_instances.append(random_instance)
        return last_random_instances

    def delete_by_instance(self, instances):
        """ Busca por 'instâncias' dadas dentro da janela e as deleta"""
        for i in range(len(instances)):
            for j in range(len(self._stm_samples) - 1, -1, -1):
                if np.array_equal(instances[i], self._stm_samples[j]):
                    self.delete_element_at_index(j)
                    break

    def forget_last_random(self):
        """ Deleta instâncias mais novas aleatoriamente"""
        if self.fgt_n_instances < 1 :
            n_samples = int(self.fgt_n_instances*self.fgt_from_sub_set_length)
            instances = self.get_last_random(n_samples, self.fgt_from_sub_set_length)
        else:
            instances = self.get_last_random(self.fgt_n_instances, self.fgt_from_sub_set_length)
        self.delete_by_instance(instances)
