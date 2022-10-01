import random
from abc import ABC

import numpy as np
#from lazy.sam_knn import SAMKNNClassifier

from river import neighbors


class FGTSAMKNN(neighbors.SAMKNNClassifier, ABC):
    def __init__(self,
                 fgt=True,
                 fgt_n_instances=100,
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
        self.fgt_n_instances = fgt_n_instances
        self.fgt_from_sub_set_length = fgt_from_sub_set_length

    def delete_element_at_index(self, i):
        """ Delete element at a given index i from the sample window """
        #self._stm_samples._n_samples -= 1
        #self._stm_samples._buffer = np.delete(self._stm_samples._buffer, i, 0)
        self._stm_samples = np.delete(self._stm_samples, i, 0)
        self._stm_labels = np.delete(self._stm_labels, i, 0)
        ## Pode ser substituído pela função np.delete(self._STMLabels, i, 0), onde i é o índice
        ## e 0 indica a dimensão (0 == linha e 1 == coluna)

    def get_last_random(self, n_samples, sub_set_length):
        """ get 'n_samples' randomly from the newest 'sub_set_length' elements """
        #window_length = self.window.n_samples
        window_length = self._stm_labels.size
        print("Window_length ="+ str(window_length))
        print("STM_samples = ", self._stm_samples)
        print("STM_labels = ", self._stm_labels)
        last_random_instances = []
        last_samples_starting_position = window_length - sub_set_length
        print("last_samples_starting_position ="+str(last_samples_starting_position))
        last_samples_range = range(last_samples_starting_position, window_length) # equivalente a sub_set_length
        # !!!! POSSÍVEL PROBLEMA : se eu passar um valor não inteiro ao n_samples não funciona o random.samples!!!!!!
        # Será necessário avaliação prévia. Se n_samples menor que 1, ou seja, uma porcentagem devo aplicar essa porcentagem ao sub_set_length.
        # Objetivo: quero esquecer n_samples 0.1 do sub_set_length 1000 === quero esquecer 10% a cada 1000 elementos
        random_indexes = (random.sample(last_samples_range, n_samples))
        for i in range(n_samples):
            index = random_indexes[i]
            #random_instance = (self.window.buffer[index])
            random_instance = (self._stm_samples[index])
            last_random_instances.append(random_instance)
        return last_random_instances

    def delete_by_instance(self, instances):
        """ looks for 'instances' given in the window and deletes them """
        for i in range(len(instances)):
            for j in range(len(self._stm_samples) - 1, -1, -1):
                if np.array_equal(instances[i], self._stm_samples[j]):
                    self.delete_element_at_index(j)
                    break

    def forget_last_random(self):
        """ deletes newest random instances """
        if self.fgt_n_instances < 1 :
            n_samples = int(self.fgt_n_instances*self.fgt_from_sub_set_length)
            instances = self.get_last_random(n_samples, self.fgt_from_sub_set_length)
        else:
            instances = self.get_last_random(self.fgt_n_instances, self.fgt_from_sub_set_length)
        self.delete_by_instance(instances)
