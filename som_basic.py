import sys
import pandas as pd
import SimpSOM as som
import numpy as np


def base_func(file_path: str) -> None:
    """
    Basic SOM function: creates maps and weight matrixes
    
    Args:
    =====
    file_path: str
    a path to a data file (.xlsx)
    """
    
    MY_HEADER = ['ВА', 'ВА*', 'ОА',
           'ОА*','КиР','КиР*',
           'КО', 'КО*', 'КЗ',
           'КЗ*', 'Б', 'Б*',
           'В', 'В*', 'СС'
           'СС*', 'ПП', 'ПП*',
           'ПДН', 'ПДН*', 'ЧП'
           'ЧП*', 'ТНП', 'НМА',
           'НМА*', 'НДС', 'НДС*',
           'ПОА', 'МЗ', 'СЧРС',
           'ФОТ', 'И', 'А', 'А-Б']
    
    df = pd.read_excel(file_path, skiprows=3)
    df.drop([1, 2, 3], inplace=True)
    
    data_arr = df.to_numpy()
    
    SOM_NET = som.somNet(25, 25, data_arr, PBC=True)
    SOM_NET.train(0.01, 100)
    SOM_NET.save('test_weights')
    SOM_NET.nodes_graph(colnum=0)
    
    SOM_NET.diff_graph()
    
    
    
