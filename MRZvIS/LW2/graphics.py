# Лабораторная работа №2 по дисциплине «Модели решения задач в интеллектуальных системах»
#
# Авторы: Робилко Т. М., гр. 221701
#
# Задание: Вариант 8.
#
# (~) = /2\\; /~\\ = /1\\; x~>y = sup({z|(min({1-x}U{z})<=y)/\(z<=1))
#
# Файл, содержащий функции отрисовки графиков
#
# Источники:
# https://www.cyberforum.ru/blogs/tags/simd.html
# https://studfile.net/preview/9992076/page:9/
# https://github.com/SonyaVitkovskaya/BSUIR/tree/main/MRZvIS/sem6/lab2

import random
import math
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Константы и глобальные переменные
DIGITS = '0123456789'
matrix_A, matrix_B, matrix_E, matrix_G, matrix_C = [], [], [], [], []
processing_time = 0
dims = {"p": 0, "q": 0, "m": 0}
operation_counts = {"add": 0, "multiply": 0, "subtract": 0, "compare": 0, "compare_max": 0}
time_costs = {"add": 1, "multiply": 1, "subtract": 1, "compare": 1, "compare_max": 1}
stats = {"Lavg": 0, "Tavg": 0}
processors = 1
resource_count = 1


# Основные арифметические операции с подсчетом
def sum_operation(x, y):
    operation_counts["add"] += 1
    return x + y


def multiply_operation(x, y):
    operation_counts["multiply"] += 1
    return x * y


def diff_operation(x, y):
    operation_counts["subtract"] += 1
    return x - y

def compare_values(x, y):
    operation_counts["compare"] += 1
    return min(x, y)

def compare_values_max(x, y):
    operation_counts["compare_max"] += 1
    return max(x, y)

# Вспомогательные функции
def validate_numeric_input(input_str):
    return all(char in DIGITS for char in input_str)


def display_matrix(matrix, title=''):
    print(title, end=' ')
    for i, row in enumerate(matrix):
        if i == 0:
            print(' '.join(str(val) for val in row))
        else:
            print(' ' * (len(title) + 1) + ' '.join(str(val) for val in row))


def generate_random_matrices(m, p, q):
    global matrix_A, matrix_B, matrix_E, matrix_G
    matrix_A = [[round(random.uniform(-1, 1.001), 3) for _ in range(m)] for _ in range(p)]
    matrix_B = [[round(random.uniform(-1, 1.001), 3) for _ in range(q)] for _ in range(m)]
    matrix_E = [[round(random.uniform(-1, 1.001), 3) for _ in range(m)] for _ in range(1)]
    matrix_G = [[round(random.uniform(-1, 1.001), 3) for _ in range(q)] for _ in range(p)]


def process_average_time():
    p, q, m = dims["p"], dims["q"], dims["m"]
    t_add, t_mul, t_sub, t_comp = time_costs["add"], time_costs["multiply"], time_costs["subtract"], time_costs[
        "compare"]

    avg_time = 0
    avg_time += p * q * m * (3 * (t_add + t_mul + t_sub) + 7 * t_mul + 3 * t_sub + 2 * t_add)  # f[i][j][k]
    avg_time += p * q * m * t_mul  # d[i][j][k]
    avg_time += 2 * p * q * (m - 1) * t_mul  # /~\k
    avg_time += p * q * ((m + 1) * t_sub + (m - 1) * t_mul)  # ~/k
    avg_time += p * q * (7 * t_mul + 2 * t_add + 3 * t_sub + t_comp)  # c[i][j]

    return avg_time


# Логические операции
def t_norm(a, b):  # min(a, b)
    return compare_values(a, b)


def implication(a, b):  # x ~> y = sup({ z| (min({1-x) \/ {z})<=y) /\ (z<=1) }):
    if b >= diff_operation(1, a):
        return 1
    else:
        return compare_values(a, b)


def compose_operation(a, b):  # min(a, b)
    return compare_values((diff_operation(sum_operation(a, b), 1)), 0)


# Основные вычислительные функции
def process_kf_factors(i, j):
    global processing_time, matrix_A, matrix_B, matrix_E, matrix_G, processors
    p, q, m = dims["p"], dims["q"], dims["m"]
    n = processors
    results = []
    initial_time = processing_time

    for k in range(m):
        # Вычисление промежуточных значений
        impl_a_to_b = implication(matrix_A[i][k], matrix_B[k][j])
        impl_b_to_a = implication(matrix_B[k][j], matrix_A[i][k])

        term1 = multiply_operation(
            multiply_operation(impl_a_to_b, diff_operation(multiply_operation(2, matrix_E[0][k]), 1)),
            matrix_E[0][k]
        )

        term2 = multiply_operation(
            multiply_operation(
                impl_b_to_a,
                sum_operation(1, multiply_operation(diff_operation(multiply_operation(4, impl_a_to_b), 2),
                                                    matrix_E[0][k]))
            ),
            diff_operation(1, matrix_E[0][k])
        )

        results.append(sum_operation(term1, term2))

        # Учет времени выполнения операций для Tn
        processing_time += math.ceil(2 / n) * time_costs["subtract"]
        processing_time += math.ceil(2 / n) * time_costs["compare_max"]
        processing_time += math.ceil(2 / n) * time_costs["subtract"]
        processing_time += math.ceil(2 / n) * time_costs["multiply"]
        processing_time += math.ceil(2 / n) * time_costs["multiply"]
        processing_time += math.ceil(4 / n) * time_costs["subtract"]
        processing_time += math.ceil(4 / n) * time_costs["multiply"]
        processing_time += math.ceil(2 / n) * time_costs["multiply"]
        processing_time += math.ceil(2 / n) * time_costs["add"]
        processing_time += math.ceil(2 / n) * time_costs["multiply"]
        processing_time += math.ceil(2 / n) * time_costs["multiply"]
        processing_time += math.ceil(2 / n) * time_costs["multiply"]
        processing_time += math.ceil(2 / n) * time_costs["add"]
        processing_time += 1 * time_costs["multiply"]
        processing_time += 1 * time_costs["add"]
    # Корректировка времени в зависимости от числа процессоров
    if 4 <= n <= m * 2:
        adjusted_n = n - (n % 3)
        operations_count = math.ceil((m * 3) / adjusted_n)
        time_per_operation = (processing_time - initial_time) / m
        processing_time = processing_time - (m - operations_count) * time_per_operation
    elif n >= m * 2:
        time_per_operation = (processing_time - initial_time) / m
        processing_time = initial_time + time_per_operation


    return results


def reduce_kf_factors(factor_list):
    global processing_time

    if not factor_list:
        return 0

    result = factor_list[0]
    for i in range(1, len(factor_list)):
        result = multiply_operation(result, factor_list[i])

    processing_time += math.ceil(len(factor_list) - 1) * time_costs["multiply"]
    return result


def process_kd(i, j):
    global processing_time, matrix_A, matrix_B, processors
    m = dims["m"]
    n = processors
    results = []
    initial_time = processing_time

    for k in range(m):
        norm_value = t_norm(matrix_A[i][k], matrix_B[k][j])
        complement = diff_operation(1, norm_value)
        results.append(complement)
        processing_time += math.ceil(2 / n) * time_costs["compare"]
        processing_time += math.ceil(2 / n) * time_costs["subtract"]

    # Корректировка времени в зависимости от числа процессоров
    if 2 <= n <= m:
        adjusted_n = n - (n % 1)
        operations_count = math.ceil(m / adjusted_n)
        time_per_operation = (processing_time - initial_time) / m
        processing_time = processing_time - (m - operations_count) * time_per_operation
    elif n >= m:
        time_per_operation = (processing_time - initial_time) / m
        processing_time = initial_time + time_per_operation

    # Вычисление окончательного значения kd
    product = results[0]
    for i in range(1, len(results)):
        product = multiply_operation(product, results[i])

    final_kd = diff_operation(1, product)

    processing_time += 1 * time_costs["multiply"]
    processing_time += 1 * time_costs["subtract"]

    return final_kd


def process_matrix_element(i, j):
    global processing_time, matrix_A, matrix_B, matrix_E, matrix_G, processors
    n = processors

    # Вычисление основных компонентов
    kd_value = process_kd(i, j)
    kf_factors = process_kf_factors(i, j)
    kf_value = reduce_kf_factors(kf_factors)

    # Вычисление композиции
    composed = compose_operation(kf_value, kd_value)

    # Вычисление окончательного значения c[i][j]
    result = sum_operation(
        multiply_operation(
            multiply_operation(kf_value, diff_operation(multiply_operation(3, matrix_G[i][j]), 2)),
            matrix_G[i][j]
        ),
        multiply_operation(
            sum_operation(kd_value, multiply_operation(
                diff_operation(multiply_operation(4, composed), multiply_operation(3, kd_value)),
                matrix_G[i][j]
            )),
            diff_operation(1, matrix_G[i][j])
        )
    )

    # Учет времени выполнения операций
    processing_time += 1 * time_costs["subtract"]
    processing_time += 1 * time_costs["compare_max"]
    processing_time += math.ceil(3 / n) * time_costs["multiply"]
    processing_time += math.ceil(3 / n) * time_costs["subtract"]
    processing_time += math.ceil(2 / n) * time_costs["multiply"]
    processing_time += 1 * time_costs["multiply"]
    processing_time += math.ceil(2 / n) * time_costs["multiply"]
    processing_time += 1 * time_costs["add"]

    return result


def process_output_matrix(rows, cols, dim_m):
    global matrix_C
    matrix_C = [[process_matrix_element(i, j) for j in range(cols)] for i in range(rows)]


# Вспомогательные функции
def reset_calculation_state():
    global processing_time, operation_counts
    processing_time = 0
    operation_counts = {"add": 0, "multiply": 0, "subtract": 0, "compare": 0}


def process_t1():
    print(operation_counts)
    return (operation_counts["add"] * time_costs["add"] +
            operation_counts["multiply"] * time_costs["multiply"] +
            operation_counts["subtract"] * time_costs["subtract"] +
            operation_counts["compare"] * time_costs["compare"])


# Графические функции с улучшенным стилем
def plot_ky_vs_r():
    global operation_counts, processing_time, stats, processors

    ky_values_n15 = []
    ky_values_n9 = []
    r_values = []

    for i in range(20):
        reset_calculation_state()
        m = p = q = i + 1
        dims["p"], dims["q"], dims["m"] = p, q, m
        processors = 16

        generate_random_matrices(m, p, q)
        process_output_matrix(p, q, m)

        r = p * q + p * m + q * m + m + p * q
        t1 = process_t1()
        ky = t1 / processing_time if processing_time != 0 else 0

        ky_values_n15.append(ky)
        r_values.append(r)

    for i in range(20):
        reset_calculation_state()
        m = p = q = i + 1
        dims["p"], dims["q"], dims["m"] = p, q, m
        processors = 7

        generate_random_matrices(m, p, q)
        process_output_matrix(p, q, m)

        t1 = process_t1()
        ky = t1 / processing_time if processing_time != 0 else 0

        ky_values_n9.append(ky)

    plt.figure(figsize=(12, 6), dpi=100)
    plt.plot(r_values, ky_values_n15, 'g-', marker='o', markersize=6,
             markerfacecolor='white', markeredgewidth=2, label='n = 16', linewidth=2)
    plt.plot(r_values, ky_values_n9, 'r-', marker='s', markersize=6,
             markerfacecolor='white', markeredgewidth=2, label='n = 7', linewidth=2)
    plt.xlabel('r', fontsize=14)
    plt.ylabel('Ky(r)', fontsize=14)
    plt.title('Коэффициент ускорения Ky в зависимости от r', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='best', fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_ky_vs_n():
    global operation_counts, processing_time, stats, processors

    n_values_r30 = []
    ky_values_r30 = []
    n_values_r20 = []
    ky_values_r20 = []

    for n in range(1, 51):
        # r = 30
        found = False
        for p in range(1, 11):
            for q in range(1, 11):
                for m in range(1, 11):
                    r = p * q + p * m + q * m + m + p * q
                    if r == 30:
                        reset_calculation_state()
                        dims["p"], dims["q"], dims["m"] = p, q, m
                        processors = n

                        generate_random_matrices(m, p, q)
                        process_output_matrix(p, q, m)

                        t1 = process_t1()
                        ky = t1 / processing_time if processing_time != 0 else 0

                        n_values_r30.append(n)
                        ky_values_r30.append(ky)
                        found = True
                        break
                if found:
                    break
            if found:
                break

        # r = 20
        found = False
        for p in range(1, 11):
            for q in range(1, 11):
                for m in range(1, 11):
                    r = p * q + p * m + q * m + m + p * q
                    if r == 20:
                        reset_calculation_state()
                        dims["p"], dims["q"], dims["m"] = p, q, m
                        processors = n

                        generate_random_matrices(m, p, q)
                        process_output_matrix(p, q, m)

                        t1 = process_t1()
                        ky = t1 / processing_time if processing_time != 0 else 0

                        n_values_r20.append(n)
                        ky_values_r20.append(ky)
                        found = True
                        break
                if found:
                    break
            if found:
                break

    plt.figure(figsize=(12, 6), dpi=100)
    plt.plot(n_values_r30, ky_values_r30, 'g-', marker='o', markersize=6,
             markerfacecolor='white', markeredgewidth=2, label='r = 30', linewidth=2)
    plt.plot(n_values_r20, ky_values_r20, 'r-', marker='s', markersize=6,
             markerfacecolor='white', markeredgewidth=2, label='r = 20', linewidth=2)
    plt.xlabel('n', fontsize=14)
    plt.ylabel('Ky(n)', fontsize=14)
    plt.title('Коэффициент ускорения Ky в зависимости от n', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='best', fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_e_vs_r():
    global operation_counts, processing_time, stats, processors

    e_values_n15 = []
    e_values_n9 = []
    r_values = []

    for i in range(20):
        reset_calculation_state()
        m = p = q = i + 1
        dims["p"], dims["q"], dims["m"] = p, q, m
        processors = 16

        generate_random_matrices(m, p, q)
        process_output_matrix(p, q, m)

        r = p * q + p * m + q * m + m + p * q
        t1 = process_t1()
        ky = t1 / processing_time if processing_time != 0 else 0
        e = ky / processors

        e_values_n15.append(e)
        r_values.append(r)

    for i in range(20):
        reset_calculation_state()
        m = p = q = i + 1
        dims["p"], dims["q"], dims["m"] = p, q, m
        processors = 7

        generate_random_matrices(m, p, q)
        process_output_matrix(p, q, m)

        t1 = process_t1()
        ky = t1 / processing_time if processing_time != 0 else 0
        e = ky / processors

        e_values_n9.append(e)

    plt.figure(figsize=(12, 6), dpi=100)
    plt.plot(r_values, e_values_n15, 'g-', marker='o', markersize=6,
             markerfacecolor='white', markeredgewidth=2, label='n = 16', linewidth=2)
    plt.plot(r_values, e_values_n9, 'r-', marker='s', markersize=6,
             markerfacecolor='white', markeredgewidth=2, label='n = 7', linewidth=2)
    plt.xlabel('r', fontsize=14)
    plt.ylabel('e(r)', fontsize=14)
    plt.title('Эффективность e в зависимости от r', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='best', fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_e_vs_n():
    global operation_counts, processing_time, stats, processors

    n_values_r30 = []
    e_values_r30 = []
    n_values_r20 = []
    e_values_r20 = []

    for n in range(1, 51):
        # r = 30
        found = False
        for p in range(1, 11):
            for q in range(1, 11):
                for m in range(1, 11):
                    r = p * q + p * m + q * m + m + p * q
                    if r == 30:
                        reset_calculation_state()
                        dims["p"], dims["q"], dims["m"] = p, q, m
                        processors = n

                        generate_random_matrices(m, p, q)
                        process_output_matrix(p, q, m)

                        t1 = process_t1()
                        ky = t1 / processing_time if processing_time != 0 else 0
                        e = ky / n

                        n_values_r30.append(n)
                        e_values_r30.append(e)
                        found = True
                        break
                if found:
                    break
            if found:
                break

        # r = 20
        found = False
        for p in range(1, 11):
            for q in range(1, 11):
                for m in range(1, 11):
                    r = p * q + p * m + q * m + m + p * q
                    if r == 20:
                        reset_calculation_state()
                        dims["p"], dims["q"], dims["m"] = p, q, m
                        processors = n

                        generate_random_matrices(m, p, q)
                        process_output_matrix(p, q, m)

                        t1 = process_t1()
                        ky = t1 / processing_time if processing_time != 0 else 0
                        e = ky / n

                        n_values_r20.append(n)
                        e_values_r20.append(e)
                        found = True
                        break
                if found:
                    break
            if found:
                break

    plt.figure(figsize=(12, 6), dpi=100)
    plt.plot(n_values_r30, e_values_r30, 'g-', marker='o', markersize=6,
             markerfacecolor='white', markeredgewidth=2, label='r = 30', linewidth=2)
    plt.plot(n_values_r20, e_values_r20, 'r-', marker='s', markersize=6,
             markerfacecolor='white', markeredgewidth=2, label='r = 20', linewidth=2)
    plt.xlabel('n', fontsize=14)
    plt.ylabel('e(n)', fontsize=14)
    plt.title('Эффективность e в зависимости от n', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='best', fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_d_vs_r():
    global operation_counts, processing_time, stats, processors

    d_values_n15 = []
    d_values_n9 = []
    r_values = []

    for i in range(10):
        reset_calculation_state()
        m = p = q = i + 1
        dims["p"], dims["q"], dims["m"] = p, q, m
        processors = 16

        generate_random_matrices(m, p, q)
        process_output_matrix(p, q, m)

        r = p * q + p * m + q * m + m + p * q
        tavg = process_average_time()
        lavg = tavg / r
        d = processing_time / lavg

        d_values_n15.append(d)
        r_values.append(r)

    for i in range(10):
        reset_calculation_state()
        m = p = q = i + 1
        dims["p"], dims["q"], dims["m"] = p, q, m
        processors = 7

        generate_random_matrices(m, p, q)
        process_output_matrix(p, q, m)

        r = p * q + p * m + q * m + m + p * q
        tavg = process_average_time()
        lavg = tavg / r
        d = processing_time / lavg

        d_values_n9.append(d)

    plt.figure(figsize=(12, 6), dpi=100)
    plt.plot(r_values, d_values_n15, 'g-', marker='o', markersize=6,
             markerfacecolor='white', markeredgewidth=2, label='n = 16', linewidth=2)
    plt.plot(r_values, d_values_n9, 'r-', marker='s', markersize=6,
             markerfacecolor='white', markeredgewidth=2, label='n = 7', linewidth=2)
    plt.xlabel('r', fontsize=14)
    plt.ylabel('D(r)', fontsize=14)
    plt.title('Декомпозиция D в зависимости от r', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='best', fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_d_vs_n():
    global operation_counts, processing_time, stats, processors

    n_values_r30 = []
    d_values_r30 = []
    n_values_r20 = []
    d_values_r20 = []

    for n in range(1, 51):
        # r = 30
        found = False
        for p in range(1, 11):
            for q in range(1, 11):
                for m in range(1, 11):
                    r = p * q + p * m + q * m + m + p * q
                    if r == 30:
                        reset_calculation_state()
                        dims["p"], dims["q"], dims["m"] = p, q, m
                        processors = n

                        generate_random_matrices(m, p, q)
                        process_output_matrix(p, q, m)

                        tavg = process_average_time()
                        lavg = tavg / r
                        d = processing_time / lavg

                        n_values_r30.append(n)
                        d_values_r30.append(d)
                        found = True
                        break
                if found:
                    break
            if found:
                break

        # r = 20
        found = False
        for p in range(1, 11):
            for q in range(1, 11):
                for m in range(1, 11):
                    r = p * q + p * m + q * m + m + p * q
                    if r == 20:
                        reset_calculation_state()
                        dims["p"], dims["q"], dims["m"] = p, q, m
                        processors = n

                        generate_random_matrices(m, p, q)
                        process_output_matrix(p, q, m)

                        tavg = process_average_time()
                        lavg = tavg / r
                        d = processing_time / lavg

                        n_values_r20.append(n)
                        d_values_r20.append(d)
                        found = True
                        break
                if found:
                    break
            if found:
                break

    plt.figure(figsize=(12, 6), dpi=100)
    plt.plot(n_values_r30, d_values_r30, 'g-', marker='o', markersize=6,
             markerfacecolor='white', markeredgewidth=2, label='r = 30', linewidth=2)
    plt.plot(n_values_r20, d_values_r20, 'r-', marker='s', markersize=6,
             markerfacecolor='white', markeredgewidth=2, label='r = 20', linewidth=2)
    plt.xlabel('n', fontsize=14)
    plt.ylabel('D(n)', fontsize=14)
    plt.title('Декомпозиция D в зависимости от n', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='best', fontsize=12)
    plt.tight_layout()
    plt.show()


def run_all_visualizations():
    plot_ky_vs_r()
    plot_ky_vs_n()
    plot_e_vs_r()
    plot_e_vs_n()
    plot_d_vs_r()
    plot_d_vs_n()

def main():
    global time_costs, processing_time, processors, dims, resource_count
    while True:
        try:
            m_input = input("m = ")
            p_input = input("p = ")
            q_input = input("q = ")
            n_input = input("n = ")
            if not validate_numeric_input(m_input + p_input + q_input + n_input):
                continue

            m = int(m_input)
            p = int(p_input)
            q = int(q_input)
            n = int(n_input)
            if any(val <= 0 for val in [m, p, q, n]):
                continue

            dims["p"], dims["q"], dims["m"] = p, q, m
            processors = n

            generate_random_matrices(m, p, q)
            process_output_matrix(p, q, m)

            t1 = process_t1()
            ky = t1 / processing_time if processing_time != 0 else 0
            e = ky / n
            resource_count = p * q + p * m + q * m + m + p * q
            tavg = process_average_time()
            lavg = tavg / resource_count
            d = processing_time / lavg

            display_matrix(matrix_A, "\nA:")
            display_matrix(matrix_B, "\nB:")
            display_matrix(matrix_E, "\nE:")
            display_matrix(matrix_G, "\nG:")
            display_matrix(matrix_C, "\nC:")

            print("\nResults:")
            print(f"T1 = {t1}")
            print(f"Tn = {processing_time}")
            print(f"r = {resource_count}")
            print(f"Ky = {ky}")
            print(f"e = {e}")
            print(f"Lsum = {processing_time}")
            print(f"Lavg = {lavg}")
            print(f"D = {d}")

            break

        except Exception as e:
            print(f"Произошла ошибка: {e}")
            continue

if __name__ == "__main__":
    main()
    # run_all_visualizations()