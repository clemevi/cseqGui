#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 13, 2018 05:34:50 PM CET  platform: Linux
#    Nov 13, 2018 06:40:14 PM CET  platform: Linux
#    Nov 13, 2018 08:48:48 PM CET  platform: Linux
#    Nov 13, 2018 08:58:47 PM CET  platform: Linux
#    Nov 13, 2018 09:02:43 PM CET  platform: Linux
#    Nov 14, 2018 05:16:05 PM CET  platform: Linux
#    Nov 14, 2018 05:34:01 PM CET  platform: Linux
#    Nov 14, 2018 05:49:30 PM CET  platform: Linux
#    Nov 14, 2018 05:51:40 PM CET  platform: Linux

#import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



"""
if variable is cb_keep_stat:
    print("ok")
elif variable is cb_atom_param:
    print("ok")
elif variable is cb_dec_pc:

elif variable is cb_guess_cs:

elif variable is cb_svcomp:

elif variable is cb_round_int:

elif variable is cb_bit_pthr:

elif variable is cb_nondet_stat:

elif variable is cb_stop_fail:

elif variable is cb_show_linem:

elif variable is cb_deadlock:

elif variable is cb_bounds:

elif variable is cb_div_zero:

elif variable is cb_pointer:

elif variable is cb_mem_leak:

elif variable is cb_sign_overfl:

elif variable is cb_un_overfl:

elif variable is cb_nan:

elif variable is cb_overfl:

elif variable is cb_float_overfl:

elif variable is cb_no_simpl:

elif variable is cb_ref_arr:

elif variable is cb_sof_unwind:

elif variable is cb_robin:

elif variable is cb_no_chek_var_pointer:

elif variable is sb_unwind:

elif variable is sb_unwind_while:

elif variable is sb_unwind_for:

elif variable is sb_unwind_for_max:

elif variable is sb_rounds:

elif variable is sb_Time:

elif variable is sb_lim_ser_depth:

elif variable is sb_sem_lev:

elif variable is rb_bd_md_chk:

elif variable is rb_abst_based:

elif variable is cb_countre_ex:
"""



def set_Tk_var():
    global cb_keep_stat
    cb_keep_stat = tk.IntVar(value=0)
    global cb_atom_param
    cb_atom_param = tk.IntVar(value=0)
    global cb_dec_pc
    cb_dec_pc = tk.IntVar(value=0)
    global cb_guess_cs
    cb_guess_cs = tk.IntVar(value=0)
    global cb_svcomp
    cb_svcomp = tk.IntVar(value=0)
    global cb_round_int
    cb_round_int = tk.IntVar(value=0)
    global cb_bit_pthr
    cb_bit_pthr = tk.IntVar(value=0)
    global cb_nondet_stat
    cb_nondet_stat = tk.IntVar(value=0)
    global cb_stop_fail
    cb_stop_fail = tk.IntVar(value=0)
    global cb_show_linem
    cb_show_linem = tk.IntVar(value=0)
    global cb_deadlock
    cb_deadlock = tk.IntVar(value=0)
    global cb_bounds
    cb_bounds = tk.IntVar(value=0)
    global cb_div_zero
    cb_div_zero = tk.IntVar(value=0)
    global cb_pointer
    cb_pointer = tk.IntVar(value=0)
    global cb_mem_leak
    cb_mem_leak = tk.IntVar(value=0)
    global cb_sign_overfl
    cb_sign_overfl = tk.IntVar(value=0)
    global cb_un_overfl
    cb_un_overfl = tk.IntVar(value=0)
    global cb_nan
    cb_nan = tk.IntVar(value=0)
    global cb_overfl
    cb_overfl = tk.IntVar(value=0)
    global cb_float_overfl
    cb_float_overfl = tk.IntVar(value=0)
    global cb_no_simpl
    cb_no_simpl = tk.IntVar(value=0)
    global cb_ref_arr
    cb_ref_arr = tk.IntVar(value=0)
    global cb_sof_unwind
    cb_sof_unwind = tk.IntVar(value=0)
    global cb_robin
    cb_robin = tk.IntVar(value=0)
    global cb_no_chek_var_pointer
    cb_no_chek_var_pointer = tk.IntVar(value=0)
    global sb_unwind
    sb_unwind = tk.IntVar(value=1)
    global sb_unwind_while
    sb_unwind_while = tk.IntVar(value=0)
    global sb_unwind_for
    sb_unwind_for = tk.IntVar(value=0)
    global sb_unwind_for_max
    sb_unwind_for_max = tk.IntVar(value=0)
    global sb_rounds
    sb_rounds = tk.IntVar(value=1)
    global sb_Time
    sb_Time = tk.IntVar(value=86400)
    global sb_lim_ser_depth
    sb_lim_ser_depth = tk.IntVar(value=0)
    global sb_sem_lev
    sb_sem_lev = tk.IntVar(value=1)
    global rb_bd_md_chk
    rb_bd_md_chk = tk.IntVar(value=0)
    global cb_countre_ex
    cb_countre_ex = tk.IntVar(value=0)
    global cb_countre_ex_trace
    cb_countre_ex_trace = tk.IntVar(value=0)








def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
















