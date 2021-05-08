from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from sklearn.datasets import make_classification
import pandas as pd
import numpy as np
from functools import partial


def generate(n_samples=100,
             n_features=10,
             n_informative=10,
             class_sep=1.0):
    """
    Generates the random data
    
    Parameters:
        n_samples: the number of samples
        n_features: the number of features
        n_informative: the number of informative features (sometimes, many features are non-informative)
        class_sep: class separation (a floating point number, default = 1.0, lower number produces harder classification problem)
    """
    X,y = make_classification(n_samples=n_samples, 
                              n_features=n_features, 
                              n_informative=n_informative,
                              class_sep = class_sep,
                              n_redundant=0)
    
    df = pd.DataFrame(X,columns=['X'+str(i) for i in range(1,X.shape[1]+1)])
    df['y'] = y
    df.to_csv("_tmp_data.csv")    
    
    put_html(df.to_html(col_space=150,max_rows=10,max_cols=5,justify='center'))
    
    with open ('_tmp_data.csv', 'rb') as fp:
        content = fp.read()
    
    put_markdown("""## Download data here""")
    put_file('random-data.csv', content, 'Download the dataset (a CSV file) by clicking here')
    
def main():
    """
    Classification dataset generation
    """
    
    put_markdown("""# Generating data
    ## Developed and maintained by Dr. Tirthajyoti Sarkar ([Github](https://github.com/tirthajyoti), [LinkedIn](https://www.linkedin.com/in/tirthajyoti-sarkar-2127aa7/))
    
    Often, we need random data for [binary classification task](https://machinelearningmastery.com/types-of-classification-in-machine-learning/) in machine learning. Scikit-learn provides a nice data generation utility. 
    
    This is a **web app to relicate that function w/o writing any Python code**. You can generate randomized dataset with labels `0` or `1` and download it on your local drive. Moreover, you can control,
    
    - the number of samples
    - the number of features
    - the number of informative features (sometimes, many features are non-informative)
    - class separation (a floating point number, default = 1.0, lower number produces harder classification problem)
    
    For more information about this `sklearn.datasets.make_classification()` function see [this documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html)
    
    ## Instructions
    Just fill up the form below and hit **Submit**. For repeated generation, just reload the page which will bring back this interface. Default values are provided in the form.  
    """, strip_indent=4)
    
    
    
    params = input_group("Parameters",[input("Number of samples needed：", type=NUMBER,name='n_samples',value=100),
                              input("Number of features：", type=NUMBER,name='n_features',value=10),
                              input("Number of informative features：", type=NUMBER,name='n_informative',value=10), 
                                   input("Class separation (lower value produces harder classification problem)：",
                                         type=FLOAT,name='class_sep',value=1.0)])
    
    n_samples = params['n_samples']
    n_features = params['n_features']
    n_informative = params['n_informative']
    class_sep = params['class_sep']
    
    generate(n_samples,n_features,n_informative,class_sep)
    hold()
    
if __name__ == '__main__':
    import argparse
    from pywebio.platform.tornado_http import start_server

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(main, port=args.port)