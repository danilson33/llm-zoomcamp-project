import os
import pandas as pd
import minsearch


DATA_PATH = os.getenv("DATA_PATH", "../data/recipes.csv")


def load_index(data_path=DATA_PATH):
    df = pd.read_csv(data_path)
    columns = ['Calories', 'FatContent', 'SaturatedFatContent',
                     'CholesterolContent', 'SodiumContent', 'CarbohydrateContent',
                     'FiberContent', 'SugarContent', 'ProteinContent']
    for column in columns:
        df[column] = df[column].astype(str).apply(lambda x: x.lower())
    documents = df.to_dict(orient="records")

    index = minsearch.Index(
        text_fields=['Name', 'Description', 'RecipeInstructions', 'Calories', 'FatContent', 'SaturatedFatContent',
                        'CholesterolContent', 'SodiumContent', 'CarbohydrateContent',
                        'FiberContent', 'SugarContent', 'ProteinContent'],
        keyword_fields=['RecipeId']
    )

    index.fit(documents)
    
    return index