import pandas as pd
from typing import List
from pandas.core.frame import DataFrame
from src.models.base_models import Model, RandomModel


def get_models() -> List[Model]:
    return [
        RandomModel('Model_1'),
        RandomModel('Model_2'),
        RandomModel('Model_3'),
        RandomModel('Model_4'),
        RandomModel('Model_5')
    ]


def evaluate_portfolio(portfolio: List[str]) -> DataFrame:
    data = {'Stock': portfolio}
    for model in get_models():
        data[model.name] = [model.run(p) for p in portfolio]

    df = pd.DataFrame.from_dict(data=data)
    df.set_index('Stock', inplace=True)
    df['Voting'] = df.apply(lambda row: row['Model_1'], axis=1)
    return df

