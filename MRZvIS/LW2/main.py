#    Лабораторная работа 2 по дисциплине 'Модели решения задач в интеллектуальных системах'
#    Реализация модели решения задач в интеллектуальных системах
#    Выполнил: студент гр.221701  Абушкевич А. А.
#
#    Вариант 5:
#
#    (~) = /3\\; /~\\ = /2\\; x~>y = 1 + x *(y - 1)
#
#    Модели решения задач в интеллектуальных системах.
#
#    В 2 ч. Ч.1: Формальные модели обработки информации и параллельные модели решения задач:
#    учеб.-метод. пособие/ В. П. Ивашенко. – Минск : БГУИР, 2020. – 79 с.
#    04.05.2025

import random
import math

VALUES = [str(i) for i in range(10)]
A, B, E, G, C = [], [], [], [], []
Tn = 0
p, q, m = 0, 0, 0
sum_call, mult_call, diff_call, compare_call = 0, 0, 0, 0
t_sum, t_mult, t_diff, t_comparison, n, r = 1, 1, 1, 1, 1, 1
Lavg, Tavg = 0, 0


def sum(a, b):
    global sum_call
    sum_call += 1
    return a + b


def mult(a, b):
    global mult_call
    mult_call += 1
    return a * b


def diff(a, b):
    global diff_call
    diff_call += 1
    return a - b


def compare(a, b, max_or_min):
    global compare_call
    compare_call += 1
    if (max_or_min):
        return max(a, b)
    else:
        return min(a, b)


def check_input(str):
    for i in str:
        if i not in VALUES:
            return 1
    return 0


def print_matrix(matr, name=''):
    print(name)
    for row in matr:
        string = "   "
        for col in row:
            string += str(col) + "  "
        print(string)


def fill_matrix(m, p, q):
    global A, B, E, G
    A = [[0.594, -0.99],
         [0.948, 0.96]]
    B = [[0.297, -0.069],
         [0.008, -0.801]]
    E = [[0.777, -0.921]]
    G = [[0.149, 0.714],
         [0.868, -0.394]]
# def fill_matrix(m, p, q):
#     global A, B, E, G
#     A = [[round(random.uniform(-1, 1.001), 3) for _ in range(m)] for i in range(p)]
#     B = [[round(random.uniform(-1, 1.001), 3) for _ in range(q)] for i in range(m)]
#     E = [[round(random.uniform(-1, 1.001), 3) for _ in range(m)] for i in range(1)]
#     G = [[round(random.uniform(-1, 1.001), 3) for _ in range(q)] for i in range(p)]

def compute_Tavg():
    Tavg = 0
    Tavg += p * q * m * (3 * (t_diff + t_comparison) + 7 * t_mult + 3 * t_diff + 2 * t_sum)  # f[i][j][k]
    Tavg += p * q * m * t_comparison  # d[i][j][k]
    Tavg += p * q * (m - 1) * t_mult  # /~\k
    Tavg += p * q * ((m + 1) * t_diff + (m - 1) * t_mult)  # \~/k
    Tavg += p * q * (7 * t_mult + 2 * t_sum + 3 * t_diff + t_mult)  # c[i][j]
    return Tavg


def compute_C(x, y, m):
    global C

    def compute_compose(a, b):  # max({x + y - 1} U {0})
        return compare((diff(sum(a, b), 1)), 0, 1)

    def compute_tnorm(a, b):  # x * y
        return mult(a, b)

    def compute_impl(a, b):  #  1 + x *(y - 1)
        return mult(sum(1, x), diff(y, 1))

    def compute_kf(i, j):
        # f = a_to_b*(2*E[0][k]-1)*E[0][k] + b_to_a*(1+(4*a_to_b-2)*E[0][k])*(1-E[0][k])
        global A, B, E, G, mult_call, diff_call, sum_call, compare_call, n, Tn, p, q, m, Tavg
        multipl_arr = []
        old_Tn = Tn

        for k in range(m):
            a_to_b = compute_impl(A[i][k], B[k][j])
            b_to_a = compute_impl(B[k][j], A[i][k])
            temp1 = mult(mult(a_to_b, diff(mult(2, E[0][k]), 1)), E[0][k])
            temp2 = mult(mult(b_to_a, sum(1, (mult(diff(mult(4, a_to_b), 2), E[0][k])))), diff(1, E[0][k]))

            multipl_arr.append(sum(temp1, temp2))

            Tn += math.ceil(3 / n) * t_diff
            Tn += math.ceil(3 / n) * t_mult
            Tn += math.ceil(2 / n) * t_sum

            Tn += 1 * t_mult
            Tn += math.ceil(2 / n) * t_diff

            Tn += math.ceil(2 / n) * t_mult

            Tn += 1 * t_mult

            Tn += 1 * t_sum

            Tn += 1 * t_mult
            Tn += 1 * t_mult

            Tn += 1 * t_sum

        if 6 <= n < m * 3:
            new_n = n - n % 3  # будет задействоваться максимальное n кратное 3
            count = math.ceil((m * 3) / new_n)  # количество последовательных операций
            temp = (Tn - old_Tn) / m  # время одной итерации
            Tn = Tn - (m - count) * temp  # отнимаем время операций, которые были выполнены параллельно

        elif n >= 3 * m:
            step = (Tn - old_Tn) / m
            Tn = old_Tn + step

        kf = multipl_arr[0]
        for i_mult in range(1, len(multipl_arr)):
            kf = mult(kf, multipl_arr[i_mult])

        Tn += math.ceil(m - 1) * t_mult
        print("kf", kf)

        return kf

    def compute_kd(i, j):
        nonlocal m
        global A, B, mult_call, diff_call, sum_call, compare_call, n, Tn, Tavg, q, p
        multipl_arr = []
        old_Tn = Tn

        for k in range(m):
            temp1 = compute_tnorm(A[i][k], B[k][j])
            temp2 = diff(1, temp1)
            multipl_arr.append(temp2)
            Tn += 1 * t_comparison
            Tn += 1 * t_diff


        if 2 <= n <= m * 1:
            new_n = n - n % 1
            count = math.ceil((m * 1) / new_n)
            temp = (Tn - old_Tn) / m
            Tn = Tn - (m - count) * temp
        elif n >= m * 1:
            temp = (Tn - old_Tn) / m
            Tn = old_Tn + temp


        dd_res = multipl_arr[0]
        for i_mult in range(1, len(multipl_arr)):
            dd_res = mult(dd_res, multipl_arr[i_mult])
        dd = diff(1, dd_res)

        Tn += math.ceil(m - 1) * t_mult
        Tn += 1 * t_diff

        print("dd", dd)
        return dd

    def compute_cij(i, j):
        # cij = f*(3*G[i][j] - 2)*G[i][j] + (d+(4*f_and_d-3*d)*G[i][j])*(1-G[i][j])
        global A, B, E, G, sum_call, diff_call, mult_call, compare_call, n, Tn
        d = compute_kd(i, j)  # with \~/k
        f = compute_kf(i, j)  # with /~\k

        print("d, f", d, f)

        f_and_d = compute_compose(f, d)
        cij = sum(mult(mult(f, diff(mult(3, G[i][j]), 2)), G[i][j]),
                  mult(sum(d, mult(diff(mult(4, f_and_d), mult(3, d)), G[i][j])), diff(1, G[i][j])))

        Tn += 1 * t_sum
        Tn += 1 * t_diff
        Tn += 1 * t_comparison
        Tn += math.ceil(3 / n) * t_mult
        Tn += math.ceil(3 / n) * t_diff
        Tn += math.ceil(2 / n) * t_mult
        Tn += 1 * t_sum
        Tn += math.ceil(2 / n) * t_mult
        Tn += 1 * t_sum

        return cij

    C = [[compute_cij(i, j) for j in range(y)] for i in range(x)]


def main():
    global p, q, m, Tn, n
    while (1):
        # m = input("m = ")
        # p = input("p = ")
        # q = input("q = ")
        # n = input("n = ")
        m = "2"
        p = "2"
        q = "2"
        n = "6"

        print("\n")
        if (check_input(m + p + q + n)):
            continue
        elif int(n) == 0 or int(p) == 0 or int(m) == 0 or int(q) == 0:
            continue
        else:
            p = int(p)
            q = int(q)
            m = int(m)
            fill_matrix(m, p, q)
            n = int(n)
            compute_C(int(p), int(q), int(m))
            break

    T1 = mult_call * t_mult + diff_call * t_diff + sum_call * t_sum + compare_call * t_comparison
    Ky = T1 / Tn
    e = Ky / n
    r = p * q + p * m + q * m + 1 * m + p * q
    Tavg = compute_Tavg()
    Lavg = Tavg/r
    D = Tn / Lavg

    print_matrix(A, "\nA:")
    print_matrix(B, "\nB:")
    print_matrix(E, "\nE:")
    print_matrix(G, "\nG:")
    print_matrix(C, "\nC:")

    params = ["T1", "Tn", "r", "Ky", "e", "Lsum", "Lavg", "D"]
    values = [T1, Tn, r, Ky, e, Tn, Lavg, D]

    column_widths = [max(len(str(param)), len(f"{value:.2f}"), 5) + 2
                     for param, value in zip(params, values)]

    hline = "+" + "+".join(["-" * width for width in column_widths]) + "+"

    print(hline)
    print("|" + "|".join([f" {param:^{width-2}} " for param, width in zip(params, column_widths)]) + "|")
    print(hline)
    print("|" + "|".join([f" {f'{value:.3f}':^{width-2}} " for value, width in zip(values, column_widths)]) + "|")
    print(hline)


def main_graphicsKr():
    import matplotlib.pyplot as plt

    global p, q, m, Tn, sum_call, mult_call, diff_call, compare_call, n, Tavg
    t_mult, t_diff, t_sum, t_comparison = 1, 1, 1, 1  # задаём времена операций
    ky_n10 = []
    ky_n7 = []
    r_vals = []

    for i in range(20):
        # --- n = 10 ---
        Tn, Tavg = 0, 0
        sum_call, mult_call, diff_call, compare_call = 0, 0, 0, 0
        m = p = q = i + 1
        n = 15
        fill_matrix(m, p, q)
        compute_C(p, q, m)
        r = p * q + q * m + p * m + m + p * q
        T1 = mult_call * t_mult + diff_call * t_diff + sum_call * t_sum + compare_call * t_comparison
        Ky = T1 / Tn
        ky_n10.append(Ky)
        print(f"n = {n}, m = {m}, r = {r}, T1 = {T1}, Tn = {Tn}, Ky = {Ky}")
        r_vals.append(r)

    for i in range(20):
        # --- n = 7 ---
        Tn, Tavg = 0, 0
        sum_call, mult_call, diff_call, compare_call = 0, 0, 0, 0
        m = p = q = i + 1
        n = 8
        fill_matrix(m, p, q)
        compute_C(p, q, m)
        # r = p * q + q * m + p * m + m + p * q
        T1 = mult_call * t_mult + diff_call * t_diff + sum_call * t_sum + compare_call * t_comparison
        Ky = T1 / Tn
        print(f"n = {n}, m = {m}, r = {r}, T1 = {T1}, Tn = {Tn}, Ky = {Ky}")
        ky_n7.append(Ky)

    plt.figure(figsize=(10, 5))
    plt.plot(r_vals, ky_n10, 'k', label='n = 15', linewidth=2)
    plt.plot(r_vals, ky_n7, label='n = 8', linewidth=3)
    plt.xlabel('r', fontsize=14)
    plt.ylabel('Ky(r)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.show()


def main_graphicsKyn():
    import matplotlib.pyplot as plt

    global p, q, m, Tn, sum_call, mult_call, diff_call, compare_call, n, Tavg
    t_mult, t_diff, t_sum, t_comparison = 1, 1, 1, 1
    x = []
    ky_40 = []

    for n in range(1, 51):
        found = False
        for p in range(1, 11):
            for q in range(1, 11):
                for m in range(1, 11):
                    r = p * q + q * m + p * m + m + p * q
                    if r == 35:
                        Tn, Tavg = 0, 0
                        sum_call, mult_call, diff_call, compare_call = 0, 0, 0, 0
                        fill_matrix(m, p, q)
                        compute_C(p, q, m)
                        T1 = mult_call * t_mult + diff_call * t_diff + sum_call * t_sum + compare_call * t_comparison
                        Ky = T1 / Tn
                        # print(f"n = {n}, m = {m}, r = {r}, T1 = {T1}, Tn = {Tn}, Ky = {Ky}")
                        ky_40.append(Ky)
                        x.append(n)
                        found = True
                        break
                if found:
                    break
            if found:
                break

    x2 = []  # значения n для r = 33
    ky_33 = []

    for n in range(1, 51):
        found = False
        for p in range(1, 11):
            for q in range(1, 11):
                for m in range(1, 11):
                    r = p * q + q * m + p * m + m + p * q
                    if r == 25:
                        Tn, Tavg = 0, 0
                        sum_call, mult_call, diff_call, compare_call = 0, 0, 0, 0
                        fill_matrix(m, p, q)
                        compute_C(p, q, m)
                        T1 = mult_call * t_mult + diff_call * t_diff + sum_call * t_sum + compare_call * t_comparison
                        Ky = T1 / Tn
                        # print(f"n = {n}, m = {m}, r = {r}, T1 = {T1}, Tn = {Tn}, Ky = {Ky}")
                        ky_33.append(Ky)
                        x2.append(n)
                        found = True
                        break
                if found:
                    break
            if found:
                break

    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.plot(x, ky_40, 'k', label='r = 35', linewidth=2)
    plt.plot(x2, ky_33, label='r = 25', linewidth=3)
    plt.xlabel('n', fontsize=14)
    plt.ylabel('Ky(n)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.show()


def main_graphicsEr():
    import matplotlib.pyplot as plt

    global p, q, m, Tn, sum_call, mult_call, diff_call, compare_call, n, Tavg
    t_mult, t_diff, t_sum, t_comparison = 1, 1, 1, 1  # задаём времена операций
    e_n7 = []
    e_n10 = []
    r_vals = []

    for i in range(20):
        # --- n = 10 ---
        Tn, Tavg = 0, 0
        sum_call, mult_call, diff_call, compare_call = 0, 0, 0, 0
        m = p = q = i + 1
        n = 15
        fill_matrix(m, p, q)
        compute_C(p, q, m)
        r = p * q + q * m + p * m + m + p * q
        T1 = mult_call * t_mult + diff_call * t_diff + sum_call * t_sum + compare_call * t_comparison
        Ky = T1 / Tn
        e = Ky / n
        # print(f"n = {n}, m = {m}, r = {r}, T1 = {T1}, Tn = {Tn}, Ky = {Ky}, e = {e}")
        e_n10.append(e)
        r_vals.append(r)

    for i in range(20):
        # --- n = 7 ---
        Tn, Tavg = 0, 0
        sum_call, mult_call, diff_call, compare_call = 0, 0, 0, 0
        m = p = q = i + 1
        n = 8
        fill_matrix(m, p, q)
        compute_C(p, q, m)
        r = p * q + q * m + p * m + m + p * q
        T1 = mult_call * t_mult + diff_call * t_diff + sum_call * t_sum + compare_call * t_comparison
        Ky = T1 / Tn
        e = Ky / n
        # print(f"n = {n}, m = {m}, r = {r}, T1 = {T1}, Tn = {Tn}, Ky = {Ky}, e = {e}")
        e_n7.append(e)

    plt.figure(figsize=(10, 5))
    plt.plot(r_vals, e_n10, 'k', label='n = 15', linewidth=2)
    plt.plot(r_vals, e_n7, label='n = 8', linewidth=3)
    plt.xlabel('r', fontsize=14)
    plt.ylabel('e(r)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.show()


def main_graphicsEn():
    import matplotlib.pyplot as plt

    global p, q, m, Tn, sum_call, mult_call, diff_call, compare_call, n, Tavg
    t_mult, t_diff, t_sum, t_comparison = 1, 1, 1, 1
    x = []   # значения n для r = 40
    e_40 = []

    for n in range(1, 51):
        found = False
        for p in range(1, 11):
            for q in range(1, 11):
                for m in range(1, 11):
                    r = p * q + q * m + p * m + m + p * q
                    if r == 35:
                        Tn, Tavg = 0, 0
                        sum_call, mult_call, diff_call, compare_call = 0, 0, 0, 0
                        fill_matrix(m, p, q)
                        compute_C(p, q, m)
                        T1 = mult_call * t_mult + diff_call * t_diff + sum_call * t_sum + compare_call * t_comparison
                        Ky = T1 / Tn if Tn != 0 else 0
                        e = Ky / n
                        e_40.append(e)
                        x.append(n)
                        found = True
                        break
                if found:
                    break
            if found:
                break

    x2 = []  # значения n для r = 33
    e_33 = []

    for n in range(1, 51):
        found = False
        for p in range(1, 11):
            for q in range(1, 11):
                for m in range(1, 11):
                    r = p * q + q * m + p * m + m + p * q
                    if r == 25:
                        Tn, Tavg = 0, 0
                        sum_call, mult_call, diff_call, compare_call = 0, 0, 0, 0
                        fill_matrix(m, p, q)
                        compute_C(p, q, m)
                        T1 = mult_call * t_mult + diff_call * t_diff + sum_call * t_sum + compare_call * t_comparison
                        Ky = T1 / Tn if Tn != 0 else 0
                        e = Ky / n
                        e_33.append(e)
                        x2.append(n)
                        found = True
                        break
                if found:
                    break
            if found:
                break

    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.plot(x, e_40, 'k', label='r = 35', linewidth=2)
    plt.plot(x2, e_33, label='r = 25', linewidth=3)
    plt.xlabel('n', fontsize=14)
    plt.ylabel('e(n)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.show()


def main_graphicsDr():
    global p, q, m, Tn, sum_call, mult_call, diff_call, compare_call, n, Tavg
    x = []
    d_ = []
    ky_ = []

    for i in range(10):
        Tn, Tavg = 0, 0
        sum_call, mult_call, diff_call, compare_call = 0, 0, 0, 0
        m = i + 1
        p = i + 1
        q = i + 1
        n = 15
        fill_matrix(int(m), int(p), int(q))
        compute_C(int(p), int(q), int(m))
        r = p * q + q * m + p * m + 1 * m + p * q
        T1 = mult_call * t_mult + diff_call * t_diff + sum_call * t_sum + compare_call * t_comparison
        Ky = T1 / Tn
        e = Ky / n
        Tavg = compute_Tavg()
        Lavg = Tavg / r
        D = Tn / Lavg
        ky_.append(Ky)
        d_.append(D)
        x.append(r)
    y2 = []
    for i in range(10):
        Tn, Tavg = 0, 0
        sum_call, mult_call, diff_call, compare_call = 0, 0, 0, 0
        m = i + 1
        p = i + 1
        q = i + 1
        n = 8
        fill_matrix(int(m), int(p), int(q))
        compute_C(int(p), int(q), int(m))
        r = p * q + q * m + p * m + 1 * m + p * q
        T1 = mult_call * t_mult + diff_call * t_diff + sum_call * t_sum + compare_call * t_comparison
        Ky = T1 / Tn
        e = Ky / n
        Tavg = compute_Tavg()
        Lavg = Tavg / r
        D = Tn / Lavg
        ky_.append(Ky)
        y2.append(D)

    import matplotlib.pyplot as plt
    y = d_
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, 'k', label='n = 15', linewidth=2)
    plt.plot(x, y2, label="n = 8", linewidth=3)
    plt.xlabel('r', fontsize=14)
    plt.ylabel('D(r)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.show()

def main_graphicsDn():
    global p, q, m, Tn, sum_call, mult_call, diff_call, compare_call, n, Tavg
    x = []
    d_ = []
    ky_ = []

    for n in range(1, 51):
        for p in range(1, 11):
            for q in range(1, 11):
                for m in range(1, 11):
                    Tn, Tavg = 0, 0
                    sum_call, mult_call, diff_call, compare_call = 0, 0, 0, 0
                    r = p * q + q * m + p * m + 1 * m + p * q
                    if r == 25:
                        fill_matrix(int(m), int(p), int(q))
                        compute_C(int(p), int(q), int(m))
                        T1 = mult_call * t_mult + diff_call * t_diff + sum_call * t_sum + compare_call * t_comparison
                        Ky = T1 / Tn
                        e = Ky / n
                        Tavg = compute_Tavg()
                        Lavg = Tavg / r
                        D = Tn / Lavg
                        # print(f"n = {n}, r = {r}, m = {m}, Tn = {Tn}, Lavg = {Lavg}, D = {D}")
                        ky_.append(Ky)
                        d_.append(D)
                        x.append(n)
                        break  # Нашли подходящие p, q, m, выходим из цикла
                else:
                    continue
                break
            else:
                continue
            break

    y2 = []
    x2 = []
    for n in range(1, 51):
        for p in range(1, 11):
            for q in range(1, 11):
                for m in range(1, 11):
                    Tn, Tavg = 0, 0
                    sum_call, mult_call, diff_call, compare_call = 0, 0, 0, 0
                    r = p * q + q * m + p * m + 1 * m + p * q
                    if r == 35:
                        fill_matrix(int(m), int(p), int(q))
                        compute_C(int(p), int(q), int(m))
                        T1 = mult_call * t_mult + diff_call * t_diff + sum_call * t_sum + compare_call * t_comparison
                        Ky = T1 / Tn
                        e = Ky / n
                        Tavg = compute_Tavg()
                        Lavg = Tavg / r
                        D = Tn / Lavg
                        # print(f"n = {n}, r = {r}, m = {m}, Tn = {Tn}, Lavg = {Lavg}, D = {D}")
                        ky_.append(Ky)
                        y2.append(D)
                        x2.append(n)
                        break
                else:
                    continue
                break
            else:
                continue
            break

    import matplotlib.pyplot as plt
    y = d_
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, 'k', label='r = 25', linewidth=2)
    plt.plot(x2, y2, label="r = 35", linewidth=3)
    plt.xlabel('n', fontsize=14)
    plt.ylabel('D(n)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.show()

main()
#main_graphicsKr()
#main_graphicsKyn()
#main_graphicsEr()
#main_graphicsEn()
#main_graphicsDr()
#main_graphicsDn()
