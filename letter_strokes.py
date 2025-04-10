# letter_strokes.py

def draw_line(dobot, x1, y1, x2, y2, pen_down_z=-70, pen_up_z=-61):
    
 

    dobot.move_to(x1, y1, pen_up_z, 0, wait=True)      # Move above start
    dobot.move_to(x1, y1, pen_down_z, 0, wait=True)    # Pen down
    dobot.move_to(x2, y2, pen_down_z, 0, wait=True)    # Draw line
    dobot.move_to(x2, y2, pen_up_z, 0, wait=True)      # Pen up


LETTER_HEIGHT = 12
LETTER_WIDTH = 5

start_x = 190
start_y = 50

def draw_a(dobot, offset_x):
    x = start_x + offset_x
    y = start_y - 10  # Lower baseline
    draw_line(dobot, x + 1, y, x + 3.5, y + LETTER_HEIGHT)
    draw_line(dobot, x + 3.5, y + LETTER_HEIGHT, x + 6, y)
    draw_line(dobot, x + 2, y + 5, x + 5, y + 5)



def draw_b(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x, y - LETTER_HEIGHT)
    draw_line(dobot, x, y, x + 4, y - 2)
    draw_line(dobot, x + 4, y - 2, x, y - 5)
    draw_line(dobot, x, y - 5, x + 4, y - 7)
    draw_line(dobot, x + 4, y - 7, x, y - 10)

def draw_c(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x + 5, y, x, y - 2)
    draw_line(dobot, x, y - 2, x, y - 8)
    draw_line(dobot, x, y - 8, x + 5, y - 10)

# Add more similarly

def draw_d(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x + 1, y, x + 1, y - LETTER_HEIGHT)
    draw_line(dobot, x + 1, y, x + 5, y - 2)
    draw_line(dobot, x + 5, y - 2, x + 5, y - 8)
    draw_line(dobot, x + 5, y - 8, x + 1, y - 10)


def draw_e(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x + 5, y, x, y)          # top bar
    draw_line(dobot, x, y, x, y - LETTER_HEIGHT)  # vertical bar
    draw_line(dobot, x, y - 5, x + 3, y - 5)   # middle bar
    draw_line(dobot, x, y - LETTER_HEIGHT, x + 5, y - LETTER_HEIGHT)  # bottom bar

def draw_f(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x, y - LETTER_HEIGHT)  # vertical bar
    draw_line(dobot, x, y, x + 5, y)          # top bar
    draw_line(dobot, x, y - 5, x + 3, y - 5)   # middle bar

def draw_g(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x + 5, y, x, y - 2)       # top curve
    draw_line(dobot, x, y - 2, x, y - 8)       # left side
    draw_line(dobot, x, y - 8, x + 5, y - 10)  # bottom curve
    draw_line(dobot, x + 5, y - 10, x + 5, y - 5)  # right side
    draw_line(dobot, x + 5, y - 5, x + 2.5, y - 5) # inward stroke

def draw_h(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x, y - LETTER_HEIGHT)      # left vertical
    draw_line(dobot, x + 5, y, x + 5, y - LETTER_HEIGHT)  # right vertical
    draw_line(dobot, x, y - 5, x + 5, y - 5)           # middle connector

def draw_i(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x + 2.5, y, x + 2.5, y - LETTER_HEIGHT)  # vertical
    draw_line(dobot, x, y, x + 5, y)               # top bar
    draw_line(dobot, x, y - LETTER_HEIGHT, x + 5, y - LETTER_HEIGHT)  # bottom bar

def draw_j(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x + 5, y, x + 5, y - 8)          # vertical
    draw_line(dobot, x + 5, y, x, y)                  # top bar
    draw_line(dobot, x + 5, y - 10, x + 2, y - 10)     # bottom curve
    draw_line(dobot, x + 2, y - 10, x, y - 8)

def draw_k(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x, y - LETTER_HEIGHT)     # vertical bar
    draw_line(dobot, x, y - 5, x + 5, y)             # upper diagonal
    draw_line(dobot, x, y - 5, x + 5, y - LETTER_HEIGHT)  # lower diagonal

def draw_l(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x, y - LETTER_HEIGHT)
    draw_line(dobot, x, y - LETTER_HEIGHT, x + 5, y - LETTER_HEIGHT)

def draw_m(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x, y - LETTER_HEIGHT)
    draw_line(dobot, x, y, x + 3, y - 6)
    draw_line(dobot, x + 3, y - 6, x + 6, y)
    draw_line(dobot, x + 6, y, x + 6, y - LETTER_HEIGHT)

def draw_n(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x, y - LETTER_HEIGHT)
    draw_line(dobot, x, y, x + 6, y - LETTER_HEIGHT)
    draw_line(dobot, x + 6, y, x + 6, y - LETTER_HEIGHT)

def draw_o(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x + 1, y - 1, x + 5, y - 1)
    draw_line(dobot, x + 5, y - 1, x + 5, y - 9)
    draw_line(dobot, x + 5, y - 9, x + 1, y - 9)
    draw_line(dobot, x + 1, y - 9, x + 1, y - 1)

def draw_p(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x, y - LETTER_HEIGHT)
    draw_line(dobot, x, y, x + 5, y - 2)
    draw_line(dobot, x + 5, y - 2, x, y - 4)

def draw_q(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_o(dobot, offset_x)
    draw_line(dobot, x + 3, y - 6, x + 6, y - 10)

def draw_r(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x, y - LETTER_HEIGHT)
    draw_line(dobot, x, y, x + 4, y - 2)
    draw_line(dobot, x + 4, y - 2, x, y - 5)
    draw_line(dobot, x, y - 5, x + 5, y - 10)

def draw_s(dobot, offset_x):
    x = start_x + offset_x
    y = start_y

    # Starting from top-right curve
    draw_line(dobot, x + 4, y, x + 1, y)               # top curve (left)
    draw_line(dobot, x + 1, y, x, y - 2.5)             # down left slope
    draw_line(dobot, x, y - 2.5, x + 3, y - 5)         # curve to center
    draw_line(dobot, x + 3, y - 5, x + 5, y - 7.5)      # upward right sweep
    draw_line(dobot, x + 5, y - 7.5, x + 1, y - 10)     # final bottom curve

    # Optional finishing flick
    # draw_line(dobot, x + 1, y - 10, x + 2, y - 10)


def draw_t(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x + 2.5, y, x + 2.5, y - LETTER_HEIGHT)
    draw_line(dobot, x, y, x + 5, y)

def draw_u(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x, y - 8)
    draw_line(dobot, x, y - 8, x + 5, y - 8)
    draw_line(dobot, x + 5, y - 8, x + 5, y)

def draw_v(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x + 2.5, y - LETTER_HEIGHT)
    draw_line(dobot, x + 2.5, y - LETTER_HEIGHT, x + 5, y)

def draw_w(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x + 1.5, y - LETTER_HEIGHT)
    draw_line(dobot, x + 1.5, y - LETTER_HEIGHT, x + 2.5, y - 5)
    draw_line(dobot, x + 2.5, y - 5, x + 3.5, y - LETTER_HEIGHT)
    draw_line(dobot, x + 3.5, y - LETTER_HEIGHT, x + 5, y)

def draw_x(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x + 5, y - LETTER_HEIGHT)
    draw_line(dobot, x + 5, y, x, y - LETTER_HEIGHT)

def draw_y(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x + 2.5, y - 5)
    draw_line(dobot, x + 5, y, x + 2.5, y - 5)
    draw_line(dobot, x + 2.5, y - 5, x + 2.5, y - 10)

def draw_z(dobot, offset_x):
    x = start_x + offset_x
    y = start_y
    draw_line(dobot, x, y, x + 5, y)
    draw_line(dobot, x + 5, y, x, y - LETTER_HEIGHT)
    draw_line(dobot, x, y - LETTER_HEIGHT, x + 5, y - LETTER_HEIGHT)
# You can continue with: e, f, g, ..., z in a similar style.

letter_draw_functions = {
    'A': draw_a,
    'B': draw_b,
    'C': draw_c,
    'D': draw_d,
    'E': draw_e,
    'F': draw_f,
    'G': draw_g,
    'H': draw_h,
    'I': draw_i,
    'J': draw_j,
    'K': draw_k,
    'L': draw_l,
    'M': draw_m,
    'N': draw_n,
    'O': draw_o,
    'P': draw_p,
    'Q': draw_q,
    'R': draw_r,
    'S': draw_s,
    'T': draw_t,
    'U': draw_u,
    'V': draw_v,
    'W': draw_w,
    'X': draw_x,
    'Y': draw_y,
    'Z': draw_z
    # Add rest: 'E': draw_e, 'F': draw_f, ..., 'Z': draw_z
}
