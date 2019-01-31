"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Zach Kelly.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # Done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------

    root = tkinter.Tk()

    # -------------------------------------------------------------------------
    # Done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------

    frame = tkinter.Frame(root)
    frame.grid()

    # -------------------------------------------------------------------------
    # Done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------

    button = tkinter.Button(frame, text='Print Hello')
    button.grid(row=0, column=0)

    # -------------------------------------------------------------------------
    # Done: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------

    button['command'] = lambda: print('Hello')

    # -------------------------------------------------------------------------
    # Done: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------

    entry = tkinter.Entry(frame)
    entry.grid(row=0, column=1)

    button_2 = tkinter.Button(frame, text='Print Hello 2')
    button_2['command'] = lambda: print_hello_condition(entry)
    button_2.grid(row=0, column=2)

    # -------------------------------------------------------------------------
    # Done: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # -------------------------------------------------------------------------
    # Done: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------

    entry_2 = tkinter.Entry(frame)
    entry_2.grid(row=1, column=1)

    button_3 = tkinter.Button(frame, text='Print N Times')
    button_3['command'] = lambda: print_n_times(entry, entry_2)
    button_3.grid(row=1, column=0)

    root.mainloop()


def print_hello_condition(entry_box):
    if entry_box.get() == 'ok':
        print('Hello')
    else:
        print('Goodbye')


def print_n_times(entry_box_0, entry_box_1):
    n = entry_box_0.get()
    text = entry_box_1.get()
    if n.isdigit():
        for _ in range(int(n)):
            print(text)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
