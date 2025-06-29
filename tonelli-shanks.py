import tkinter as tk

def TS(p, n):
    
    if p == 2 & n == 2:
        return 0
        
    if pow(n, (p - 1) // 2, p) != 1:
        return "No solutions"

    # Find max power of 2 dividing p-1
    s = 0
    while (p - 1) % (2 ** s) == 0:
        s += 1
    s -= 1
    q = (p - 1) // (2 ** s)  # p - 1 = q * 2^s

    # Find a quadratic non-residue z
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1

    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s

    while t != 1:
        i = 1
        t2i = pow(t, 2, p)
        while t2i != 1:
            i += 1
            t2i = pow(t2i, 2, p)
            if i == m:
                return "No solution found"
        b = pow(c, 2 ** (m - i - 1), p)
        r = (r * b) % p
        t = (t * pow(b, 2, p)) % p
        c = pow(b, 2, p)
        m = i

    return r

def calculate():
    try:
        p = int(e1.get())
        n = int(e2.get())
        res = TS(p, n)
    except Exception as e:
        res = f"Error: {e}"
    text.delete("1.0", tk.END)
    text.insert(tk.INSERT, f"Result: {res}")

master = tk.Tk()
master.title("Tonelli-Shanks")

labelfont = ('times', 20, 'bold')

label1 = tk.Label(master, text="P:", bg='black', fg='yellow', font=labelfont)
label1.grid(row=0)

label2 = tk.Label(master, text="a:", bg='black', fg='yellow', font=labelfont)
label2.grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

text = tk.Text(master, bd=5, height=1, width=20)
text.grid(row=4)

tk.Button(master, text='Calculate', command=calculate).grid(row=4, column=2, sticky=tk.W, pady=6)

master.mainloop()
