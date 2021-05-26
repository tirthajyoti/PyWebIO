import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io
from pywebio.input import file_upload,radio,input_group
from pywebio.output import *
from pywebio import start_server
from pywebio.session import hold
import csv
import re

def app():
    """
    Main app
    """
    put_markdown("""# A utility for analyzing a CSV file

## [Dr. Tirthajyoti Sarkar](https://www.linkedin.com/in/tirthajyoti-sarkar-2127aa7/)

You can upload a data file (CSV) and,

- display histograms of the data coulmns 
- download the summary statistics as a file.
    
    """)
    data = input_group("Input data",[file_upload(label='Upload your CSV file', accept='.csv',name='file'),
                               radio('Display data?',['Yes','No'],name='display_data',value='No'),
                               radio('Display plots?',['Yes','No'],name='display_plot',value='No'),
                              ])
    file = data['file']
    display_data = data['display_data']
    display_plot = data['display_plot']
    
    content = file['content'].decode('utf-8').splitlines()
    df = content_to_pandas(content)
    
    if display_data=='Yes':
        show_data(df)
    if display_plot=='Yes':
        show_plots(df)
    show_stats(df)

def show_stats(df):
    """
    Calculates the descriptive stats
    """
    df_stat = df.describe().T
    put_markdown("""## Descriptive stats""")
    put_markdown(df_stat.to_markdown())
    
    df_stat.to_csv("_tmp_stats.csv")
    download_stat()
    
def download_stat():
    """
    Allows downloading of the descriptive stats of the uploaded file
    """
    with open ('_tmp_stats.csv', 'rb') as fp:
        content = fp.read()
    put_markdown("""## Download stats here""")
    put_file('stats.csv', content, 'Download stats file here')
    hold()
    
def show_plots(df):
    """
    Shows plots
    """
    put_markdown("""## Plots""")
    for c in df.columns:
        html = "<h3> Plots for "+str(c) + "</h3>"
        put_html(html)
        x1 = df[c].values
        f1 = plot_raw(x1)
        im1 = fig2img(f1)
        f2 = plot_hist(x1)
        im2 = fig2img(f2)
        put_row([put_image(im1), put_image(im2)],size='500px 500px')

def show_data(df):
    """
    Shows data in markdown
    """
    put_markdown("## The data")
    put_markdown(df.to_markdown())

def content_to_pandas(content: list):

    with open("_tmp.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter = '\t')
        for line in content:
            writer.writerow(re.split('\s+',line))
    df = pd.read_csv("_tmp.csv",header=None)
    df.columns = ['X'+str(i) for i in range(1,df.shape[1]+1)]
    return df

def plot_raw(a):
    """
    Plots line graph
    """
    plt.close()
    plt.figure(figsize=(10,5))
    #plt.title(f"Line plot of {len(a)} samples",fontsize=16)
    plt.plot(a)
    return plt.gcf()

def plot_hist(a):
    """
    Plots histogram
    """
    plt.close()
    plt.figure(figsize=(10,5))
    #plt.title(f"Histogram of {len(a)} samples",fontsize=16)
    plt.hist(a,color='orange',edgecolor='k')
    return plt.gcf()

def fig2img(fig):
    """
    Convert a Matplotlib figure to a PIL Image and return it
    """
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img

if __name__ == '__main__':
    start_server(app,port=9999,debug=True)