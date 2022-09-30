import sys
import numpy as np
import pandas as pd
import pytest

sys.path.append("../")

from preprocessing import preprocessing

#unit test

def test_preprocessing():
    df = pd.read_csv("train.csv")
    assert np.all(df.Survived.values[:5] == np.array([0, 1, 1, 1, 0], dtype=np.int64))