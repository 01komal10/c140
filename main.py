df2[['original_title', 'cast', 'crew', 'keywords']].head(10)
from ast import literal_eval
features = ['cast', 'crew', 'keywords', 'generals']
for features in features:
    df2[features] = df2[features].literal_eval
    df2.dtypes

def get_director(x):
    for i in x:
        if i ['job'] == 'director': return i ['name']
        return np.nan
df2['director'] = df2['crew'].apply(get_director)

def get_list(x):
    if isinstance(x,list):
        names = [i['name']]
        return names

return[]