import re
import time
import random

def process_insert_statements(lines):
    data = []
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        if line.startswith("INSERT INTO"):
            match = re.match(r"INSERT INTO `province`\s*\((.*?)\)\s*VALUES\s*\((.*?)\);", line)
            if match:
                values = match.group(2)  # ส่วนค่าข้อมูลในวงเล็บที่สอง
                values_list = [val.strip() for val in values.split(',')]
                pcode = values_list[0].strip("'")  # เก็บ pcode
                pname = values_list[1].strip("'")  # เก็บชื่อจังหวัด (pname)
                data.append((pcode, pname))  # เก็บเป็น tuple (pcode, pname)
    return data

def generate_random_data(data, size=100):
    return random.sample(data, min(size, len(data)))

def BubbleSort(a_list):
    start_time = time.time()
    n = len(a_list)
    for k in range(1, n):
        flag = 0
        for i in range(0, n - k):
            if a_list[i][0] > a_list[i + 1][0]:  # ใช้ pcode สำหรับการเรียงลำดับ
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                flag = 1
        if flag == 0:
            break
    elapsed_time = time.time() - start_time
    return a_list, elapsed_time

def InsertionSort(a_list):
    start_time = time.time()
    n = len(a_list)
    for i in range(1, n):
        temp = a_list[i]
        hole = i
        while hole > 0 and a_list[hole - 1][0] > temp[0]:  # ใช้ pcode สำหรับการเรียงลำดับ
            a_list[hole] = a_list[hole - 1]
            hole -= 1
        a_list[hole] = temp
    elapsed_time = time.time() - start_time
    return a_list, elapsed_time

def SelectionSort(a_list):
    start_time = time.time()
    n = len(a_list)
    for i in range(n - 1):
        iMin = i
        for j in range(i + 1, n):
            if a_list[j][0] < a_list[iMin][0]:  # ใช้ pcode สำหรับการเรียงลำดับ
                iMin = j
        a_list[i], a_list[iMin] = a_list[iMin], a_list[i]
    elapsed_time = time.time() - start_time
    return a_list, elapsed_time

def MergeSort(a_list):
    start_time = time.time()
    if len(a_list) < 2:
        return a_list, 0

    mid = len(a_list) // 2
    left, _ = MergeSort(a_list[:mid])
    right, _ = MergeSort(a_list[mid:])

    merged = []
    while left and right:
        if left[0][0] < right[0][0]:  # ใช้ pcode สำหรับการเรียงลำดับ
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left or right)
    elapsed_time = time.time() - start_time
    return merged, elapsed_time

def QuickSort(a_list):
    start_time = time.time()
    if len(a_list) < 2:
        return a_list, 0

    pivot = a_list[-1][0]  # ใช้ pcode เป็น pivot
    greater = [x for x in a_list[:-1] if x[0] >= pivot]
    lesser = [x for x in a_list[:-1] if x[0] < pivot]

    sorted_lesser, _ = QuickSort(lesser)
    sorted_greater, _ = QuickSort(greater)
    elapsed_time = time.time() - start_time

    return sorted_lesser + [a_list[-1]] + sorted_greater, elapsed_time

# อ่านข้อมูลจากไฟล์
file_path = 'province.sql'
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"ไฟล์ '{file_path}' ไม่พบ")
    lines = []

# ประมวลผลข้อมูลจาก INSERT INTO
data = process_insert_statements(lines)

# สุ่มข้อมูล
random_data = generate_random_data(data)

# เรียกใช้งานฟังก์ชันการเรียงลำดับและจับเวลา
bubble_sorted, bubble_time = BubbleSort(random_data.copy())
insertion_sorted, insertion_time = InsertionSort(random_data.copy())
selection_sorted, selection_time = SelectionSort(random_data.copy())
merge_sorted, merge_time = MergeSort(random_data.copy())
quick_sorted, quick_time = QuickSort(random_data.copy())

# แสดงผลข้อมูล
print("BubbleSort:")
for pcode, pname in bubble_sorted:
    print(f"Pcode: {pcode}")
    print(f"Pname: {pname}")
print(f"เวลาที่ใช้: {bubble_time:.6f} วินาที\n")

print("InsertionSort:")
for pcode, pname in insertion_sorted:
    print(f"Pcode: {pcode}")
    print(f"Pname: {pname}")
print(f"เวลาที่ใช้: {insertion_time:.6f} วินาที\n")

print("SelectionSort:")
for pcode, pname in selection_sorted:
    print(f"Pcode: {pcode}")
    print(f"Pname: {pname}")
print(f"เวลาที่ใช้: {selection_time:.6f} วินาที\n")

print("MergeSort:")
for pcode, pname in merge_sorted:
    print(f"Pcode: {pcode}")
    print(f"Pname: {pname}")
print(f"เวลาที่ใช้: {merge_time:.6f} วินาที\n")

print("QuickSort:")
for pcode, pname in quick_sorted:
    print(f"Pcode: {pcode}")
    print(f"Pname: {pname}")
print(f"เวลาที่ใช้: {quick_time:.6f} วินาที\n")
