import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# Triangular membership function
def triangular(x, points):
    a, b, c = points
    x_arr = np.atleast_1d(x)
    y = np.zeros_like(x_arr, dtype=float)
    if b != a:
        rise = (x_arr >= a) & (x_arr <= b)
        y[rise] = (x_arr[rise] - a) / (b - a)
    else:
        y[x_arr == a] = 1.0
    if c != b:
        fall = (x_arr >= b) & (x_arr <= c)
        y[fall] = (c - x_arr[fall]) / (c - b)
    else:
        y[x_arr == c] = 1.0
    return float(y) if np.ndim(x) == 0 else y

# Output domain
dose_range = np.arange(0, 501, 1)
low_membership = triangular(dose_range, [0, 0, 200])
medium_membership = triangular(dose_range, [100, 250, 400])
high_membership = triangular(dose_range, [300, 500, 500])

# GUI setup
window = tk.Tk()
window.title("حساب جرعة الدواء")
window.geometry("450x380")

input_frame = tk.LabelFrame(window, text="القيم المدخلة", padx=10, pady=10)
input_frame.pack(fill="x", padx=10, pady=5)

tk.Label(input_frame, text="العمر:").grid(row=0, column=0, sticky="e")
age_entry = tk.Entry(input_frame)
age_entry.grid(row=0, column=1, pady=2)

tk.Label(input_frame, text="الوزن:").grid(row=1, column=0, sticky="e")
weight_entry = tk.Entry(input_frame)
weight_entry.grid(row=1, column=1, pady=2)

tk.Label(input_frame, text="شدة المرض (0-10):").grid(row=2, column=0, sticky="e")
severity_entry = tk.Entry(input_frame)
severity_entry.grid(row=2, column=1, pady=2)

# Plot input membership functions
def show_membership_functions():
    fig, ax = plt.subplots(figsize=(6, 4))

    x_age = np.arange(0, 101, 1)
    ax.plot(x_age, triangular(x_age, [0, 0, 30]), label="العمر: صغير")
    ax.plot(x_age, triangular(x_age, [20, 40, 60]), label="العمر: متوسط")
    ax.plot(x_age, triangular(x_age, [50, 100, 100]), label="العمر: كبير")

    x_weight = np.arange(30, 101, 1)
    ax.plot(x_weight, triangular(x_weight, [30, 30, 60]), '--', label="الوزن: خفيف")
    ax.plot(x_weight, triangular(x_weight, [50, 70, 90]), '--', label="الوزن: متوسط")
    ax.plot(x_weight, triangular(x_weight, [80, 100, 100]), '--', label="الوزن: ثقيل")

    x_severity = np.arange(0, 11, 1)
    ax.plot(x_severity, triangular(x_severity, [0, 0, 5]), ':', label="الشدة: خفيفة")
    ax.plot(x_severity, triangular(x_severity, [3, 5, 7]), ':', label="الشدة: متوسطة")
    ax.plot(x_severity, triangular(x_severity, [6, 10, 10]), ':', label="الشدة: شديدة")

    ax.set_title("دوال العضوية للمدخلات")
    ax.set_xlabel("القيمة")
    ax.set_ylabel("درجة العضوية")
    ax.legend()
    plt.show()

# Fuzzy logic calculation
def calculate_dose():
    try:
        age = float(age_entry.get())
        weight = float(weight_entry.get())
        severity = float(severity_entry.get())
    except ValueError:
        messagebox.showwarning("خطأ", "يرجى إدخال أرقام صحيحة")
        return

    age_membership = [triangular(age, [0,0,30]), triangular(age, [20,40,60]), triangular(age, [50,100,100])]
    weight_membership = [triangular(weight, [30,30,60]), triangular(weight, [50,70,90]), triangular(weight, [80,100,100])]
    severity_membership = [triangular(severity, [0,0,5]), triangular(severity, [3,5,7]), triangular(severity, [6,10,10])]

    rule1 = min(severity_membership[0], max(weight_membership[0], age_membership[0]))  # Low dose
    rule2 = min(severity_membership[1], weight_membership[1])                          # Medium dose
    rule3 = max(severity_membership[2], min(age_membership[2], severity_membership[1]))# High dose

    clipped_low = np.minimum(rule1, low_membership)
    clipped_medium = np.minimum(rule2, medium_membership)
    clipped_high = np.minimum(rule3, high_membership)

    aggregated = np.maximum(np.maximum(clipped_low, clipped_medium), clipped_high)

    final_dose = np.sum(dose_range * aggregated) / (np.sum(aggregated) + 1e-6)

    if final_dose < 150:
        category = "منخفضة"
    elif final_dose < 350:
        category = "متوسطة"
    else:
        category = "مرتفعة"

    result_window = tk.Toplevel(window)
    result_window.title("النتائج التفصيلية")
    text = tk.Text(result_window, width=55, height=17)
    text.pack(padx=10, pady=10)

    text.insert("end", "درجات العضوية:\n")
    text.insert("end", f"العمر: صغير={age_membership[0]:.2f}, متوسط={age_membership[1]:.2f}, كبير={age_membership[2]:.2f}\n")
    text.insert("end", f"الوزن: خفيف={weight_membership[0]:.2f}, متوسط={weight_membership[1]:.2f}, ثقيل={weight_membership[2]:.2f}\n")
    text.insert("end", f"شدة المرض: خفيفة={severity_membership[0]:.2f}, متوسطة={severity_membership[1]:.2f}, شديدة={severity_membership[2]:.2f}\n\n")

    text.insert("end", "نتائج القواعد:\n")
    text.insert("end", f"قاعدة 1 (منخفضة): {rule1:.2f}\n")
    text.insert("end", f"قاعدة 2 (متوسطة): {rule2:.2f}\n")
    text.insert("end", f"قاعدة 3 (مرتفعة): {rule3:.2f}\n\n")

    text.insert("end", f"الجرعة النهائية: {final_dose:.2f} ملغ - ({category})\n")

    def draw_output():
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(dose_range, low_membership, '--', label="منخفضة")
        ax.plot(dose_range, medium_membership, '--', label="متوسطة")
        ax.plot(dose_range, high_membership, '--', label="مرتفعة")
        ax.plot(dose_range, aggregated, label="النتيجة المجمعة")
        ax.axvline(final_dose, linestyle=':', color='red', label=f"الجرعة = {final_dose:.1f} ملغ")
        ax.set_title("تحليل الجرعة")
        ax.legend()
        plt.show()

    tk.Button(result_window, text="عرض رسم النتيجة", command=draw_output).pack(pady=5)

# Control buttons
tk.Button(window, text="احسب الجرعة", bg="green", fg="white", command=calculate_dose).pack(pady=10)
tk.Button(window, text="عرض دوال العضوية", command=show_membership_functions).pack(pady=5)

# Start the interface
window.mainloop()
