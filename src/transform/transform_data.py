from pandas import DataFrame
from util.utils import compute_hash

def add_hash_column(data: DataFrame):
    return data.apply(compute_hash, axis=1)