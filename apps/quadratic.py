from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.session import hold, go_app
from math import sqrt

def quad():
    
    put_markdown("""
    # Solving a Quadratic Equation
    
## [Dr. Tirthajyoti Sarkar](https://www.linkedin.com/in/tirthajyoti-sarkar-2127aa7/)
    
    Here, we solve a quadratic equation (a.x<sup>2</sup>+b.x+c=0) using Python and a simple GUI.
        
    """, strip_indent=4)
    
    data = input_group("data",[input("Input the coefficient a：", type=FLOAT,name='a'),
                              input("Input the coefficient b：", type=FLOAT,name='b'),
                              input("Input the coefficient c：", type=FLOAT,name='c')])
    
    a = data['a']
    b = data['b']
    c = data['c']
    
    if b**2-4*a*c >=0:
        x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
        put_markdown("""## First root""")
        put_text(f'The first root is {round(x1,3)}')
        put_markdown("""## Second root""")
        put_text(f'The second root is {round(x2,3)}')
    else:
        put_text("Roots are imaginary!")
    

if __name__ == '__main__':
    start_server(quad,port=9999,debug=True,cdn=False)