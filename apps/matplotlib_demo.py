from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io

def data_gen(num=100):
    """
    Generates random samples for plotting
    """
    a = np.random.normal(size=num)
    return a

def plot_raw(a):
    """
    Plots line graph
    """
    plt.close()
    plt.figure(figsize=(12,5))
    plt.title(f"Line plot of {len(a)} samples",fontsize=16)
    plt.plot(a)
    return plt.gcf()

def plot_hist(a):
    """
    Plots histogram
    """
    plt.close()
    plt.figure(figsize=(12,5))
    plt.title(f"Histogram of {len(a)} samples",fontsize=16)
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
    
def Generate(num=100):
    """
    Generates plot, called from the `Generate` button 
    """
    remove(scope='raw')
    with use_scope(name='raw',clear=True,) as img:
        a = data_gen(num)
        f1 = plot_raw(a)
        im1 = fig2img(f1)
        put_image(im1)
        f2 = plot_hist(a)
        im2 = fig2img(f2)
        put_image(im2)
    
def app():
    """
    Main app
    """
    put_markdown("""
# Matplotlib plot demo
    
## [Dr. Tirthajyoti Sarkar](https://www.linkedin.com/in/tirthajyoti-sarkar-2127aa7/)
    
We show two plots from [random gaussian samples](https://en.wikipedia.org/wiki/Normal_distribution). You choose the number of data points to generate.
    
- A line plot
- A histogram
""", strip_indent=4)
    
    num_samples = input("Number of samples", type=NUMBER)
    Generate(num_samples)
    
    put_markdown("""## Code for this app is here: [Code repo](https://github.com/tirthajyoti/PyWebIO/tree/main/apps)""")

    
if __name__ == '__main__':
    start_server(app,port=9999,debug=True)