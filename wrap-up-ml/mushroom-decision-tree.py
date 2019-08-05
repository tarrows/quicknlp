import requests
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz

url_base = 'http://archive.ics.uci.edu/ml/machine-learning-databases'
data_url = url_base + '/mushroom/agaricus-lepiota.data'
name_url = url_base + '/mushroom/agaricus-lepiota.names'

res = requests.get(data_url).content.decode('utf-8')
with open('resources/agaricus-lepiota.data', mode='w') as f:
    f.write(res)

res = requests.get(name_url).content.decode('utf-8')
with open('resources/agaricus-lepiota.names', mode='w') as f:
    f.write(res)

# or:
# import io
# mush = pd.read_csv(io.StringIO(res.decode('utf-8')), header=None)

mush = pd.read_csv('resources/agaricus-lepiota.data', header=None)
mush.columns = [
    'classes', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
    'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
    'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
    'stalk-surface-below-ring', 'stalk-color-above-ring',
    'stalk-color-below-ring',
    'veil-type', 'veil-color', 'ring-number', 'ring-type',
    'spore-print-color', 'population', 'habitat'
]

mush_dummy = pd.get_dummies(
    mush[['gill-color', 'gill-attachment', 'odor', 'cap-color']])
mush_dummy['target'] = mush['classes'].map(lambda x: 1 if x == 'p' else 0)

# compare impurity
# mush_dummy.groupby(['cap-color_c', 'target'])['target'].count().unstack()
# mush_dummy.groupby(['gill-color_b', 'target'])['target'].count().unstack()

p = mush_dummy.groupby('target')['target'].count()[0] / len(mush_dummy)
entropy_init = -(p * np.log2(p) + (1 - p) * np.log2(1 - p))

X = mush_dummy.drop('target', axis=1)
y = mush_dummy['target']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=0)

model = DecisionTreeClassifier(
    criterion='entropy', max_depth=5, random_state=0)
model.fit(X_train, y_train)
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))

export_graphviz(model, out_file='resources/agaricus-lepiota.dot')
