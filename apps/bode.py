from scipy import signal
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io

def fig2img(fig):
    """
    Converts a Matplotlib figure to a PIL Image and return it
    """
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img
    
def plot_mag(w,mag):
    """
    Plots magnitude graph
    """
    plt.close()
    plt.figure(figsize=(12,5))
    plt.title(f"Magnitude plot",fontsize=16)
    plt.semilogx(w, mag)
    plt.grid(True)
    return plt.gcf()

def plot_freqrsp(w,H):
    """
    Plots frequency response
    """
    plt.figure(figsize=(12,5))
    plt.title(f"Frequency response",fontsize=16)
    plt.plot(H.real, H.imag, "b")
    plt.plot(H.real, -H.imag, "r")
    plt.grid(True)
    return plt.gcf()

def plot_phase(w,phase):
    """
    Plots phase graph
    """
    plt.close()
    plt.figure(figsize=(12,5))
    plt.title(f"Phase plot",fontsize=16)
    plt.semilogx(w, phase)
    plt.grid(True)
    return plt.gcf()

def plot_impulse(t,y):
    """
    Plots impulse response
    """
    plt.close()
    plt.figure(figsize=(12,5))
    plt.title("Impulse response",fontsize=16)
    plt.plot(t,y)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    return plt.gcf()

def plot_step(t,y):
    """
    Plots step response
    """
    plt.close()
    plt.figure(figsize=(12,5))
    plt.title("Step response",fontsize=16)
    plt.plot(t,y)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    return plt.gcf()
    
def system(num,den):
    """
    Generates plots from a given system input 
    """
    remove(scope='raw')
    with use_scope(name='raw',clear=True,) as img:
        #sys = signal.TransferFunction([20,5], [10, 100,1])
        sys = signal.TransferFunction(num, den)
        w=[10**(i/10) for i in range(-30,41)]
        
        # Bode
        w, mag, phase = signal.bode(sys,w=w)
        f1 = plot_mag(w,mag)
        im1 = fig2img(f1)
        put_image(im1)
        f2 = plot_phase(w,phase)
        im2 = fig2img(f2)
        put_image(im2)
        
        # Freq response
        w, H = signal.freqresp(sys,w=w)
        f3 = plot_freqrsp(w,H)
        im3 = fig2img(f3)
        put_image(im3)
        
        # Impulse response
        t, y = signal.impulse(sys)
        f4 = plot_impulse(t,y)
        im4 = fig2img(f4)
        put_image(im4)
        
        # Step response
        t, y = signal.step(sys)
        f5 = plot_step(t,y)
        im5 = fig2img(f5)
        put_image(im5)
        
def app():
    """
    Main app
    """
    put_markdown("""
    # LTI system demo (using `Scipy.signal`)
    
    ## [Dr. Tirthajyoti Sarkar](https://www.linkedin.com/in/tirthajyoti-sarkar-2127aa7/)
    
    ## What is a LTI system anyway?
    In system analysis, among other fields of study, a linear time-invariant system (or *"LTI system"*) is a system that produces an output signal from any input signal subject to the constraints of **linearity** and **time-invariance**. LTI system theory is an area of applied mathematics which has direct applications in electrical circuit analysis and design, signal processing and filter design, control theory, mechanical engineering, image processing, the design of measuring instruments of many sorts, NMR spectroscopy, and many other technical areas where systems of ordinary differential equations present themselves.
    
    ## What are we doing here?
    From a given transfer function, we calculate and display the following,
    
    - Bode magnitude plot
    - Bode phase plot
    - Frequency response plot (real vs. imaginary)
    - Impulse response plot
    - Step response plot
    
    """, strip_indent=4)
    
    tf = input_group("Transfer function",[input("Input the coefficients of numerator：", type=TEXT,name='num',
                                               help_text='Example: 2,1. No gap between a number and the commas, please.'),
                              input("Input the coefficients of denominator：", type=TEXT,name='den',
                                   help_text='Example: 5,-2,11. No gap between a number and the commas, please.')],
                               )
    
    num = [float(n) for n in tf['num'].split(',')]
    den = [float (n) for n in tf['den'].split(',')]
                                 
    system(num,den)
    
if __name__ == '__main__':
    start_server(app,port=9999,debug=True)