import os
import tarfile
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
from helpers import print_b

NUMBER_OF_DASH = 30
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    """
    fetch_housing_data download and extract data from tgz file

    :param housing_url: url of tgz data file
    :param housing_path: path to save and extract tgz data file
    :return:
    """
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    if tarfile.is_tarfile(tgz_path):
        housing_tgz = tarfile.open(tgz_path)
        housing_tgz.extractall(path=housing_path)
        housing_tgz.close()
    else:
        print(f'{tgz_path} n\'est pas un fichier tar')
        os.remove(tgz_path)


def load_housing_data(housing_path=HOUSING_PATH):
    """
    load_housing_data load and read csv file to pandas dataframe

    :param housing_path: path of csv file to read
    :return: pandas dataframe
    """
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


def run():
    print_b('Chapitre 2')
    fetch_housing_data()
    housing = load_housing_data()

    # Description des colonnes
    print_b('Description des colonnes')
    print(housing.info())

    # Description et statistiques des données
    print_b('Description et statistiques des données')
    print(housing.describe())

    # Get graph of data
    housing.hist(bins=50, figsize=(20, 15))
    plt.show()
