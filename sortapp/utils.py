import time

# ---------------- BUBBLE SORT ----------------
def bubble_sort(arr):
    a = arr.copy()
    steps = []
    start = time.time()

    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
        steps.append(f"Pass {i+1}: {a.copy()}")

    end = time.time()
    return {
        "sorted": a,
        "steps": steps,
        "time": round(end - start, 6),
        "complexity": "Best: O(n), Avg: O(n²), Worst: O(n²)"
    }


# ---------------- SELECTION SORT ----------------
def selection_sort(arr):
    a = arr.copy()
    steps = []
    start = time.time()

    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        steps.append(f"Step {i+1}: Minimum swapped → {a.copy()}")

    end = time.time()
    return {
        "sorted": a,
        "steps": steps,
        "time": round(end - start, 6),
        "complexity": "Best/Avg/Worst: O(n²)"
    }


# ---------------- INSERTION SORT (PHOTO STYLE) ----------------
def insertion_sort(arr):
    a = arr.copy()
    steps = []
    start = time.time()

    sorted_part = []
    unsorted_part = a.copy()

    # Initial state
    steps.append(f"Sorted = {sorted_part}, Unsorted = {unsorted_part}")

    while unsorted_part:
        element = unsorted_part.pop(0)

        i = len(sorted_part) - 1
        sorted_part.append(element)
        while i >= 0 and sorted_part[i] > element:
            sorted_part[i + 1] = sorted_part[i]
            sorted_part[i] = element
            i -= 1

        steps.append(
            f"Insert {element} → Sorted = {sorted_part}, Unsorted = {unsorted_part}"
        )

    end = time.time()
    return {
        "sorted": sorted_part,
        "steps": steps,
        "time": round(end - start, 6),
        "complexity": "Best: O(n), Avg/Worst: O(n²)"
    }


# ---------------- MERGE SORT ----------------
def merge_sort(arr):
    steps = []
    start = time.time()

    def merge_sort_inner(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = merge_sort_inner(a[:mid])
        right = merge_sort_inner(a[mid:])

        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        steps.append(f"Merging {left} and {right} → {merged}")
        return merged

    sorted_arr = merge_sort_inner(arr.copy())
    end = time.time()

    return {
        "sorted": sorted_arr,
        "steps": steps,
        "time": round(end - start, 6),
        "complexity": "Best/Avg/Worst: O(n log n)"
    }


def quick_sort(arr):
    steps = []
    start = time.time()

    a = arr.copy()
    level = 1

    def partition(a, low, high):
        pivot = a[low]
        i = low + 1
        j = high
        swaps = []

        while True:
            while i <= j and a[i] <= pivot:
                i += 1
            while i <= j and a[j] > pivot:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                swaps.append(f"swap {a[j]} & {a[i]}")
            else:
                break

        a[low], a[j] = a[j], a[low]
        swaps.append(f"swap {pivot} & {a[low]}")
        return j, swaps

    def quick_sort_inner(a, low, high):
        nonlocal level
        if low < high:
            pivot_index, swaps = partition(a, low, high)

            steps.append(
                f"Level {level}: Pivot = {a[pivot_index]}, Array = {a.copy()}, "
                + ", ".join(swaps)
            )
            level += 1

            quick_sort_inner(a, low, pivot_index - 1)
            quick_sort_inner(a, pivot_index + 1, high)

    # Initial state
    steps.append(f"Level 1: Pivot = {a[0]}, Array = {a.copy()}")
    quick_sort_inner(a, 0, len(a) - 1)

    steps.append(f"Final Level: Sorted Array = {a.copy()}")

    end = time.time()
    return {
        "sorted": a,
        "steps": steps,
        "time": round(end - start, 6),
        "complexity": "Best/Avg: O(n log n), Worst: O(n²)"
    }


# ---------------- COUNTING SORT ----------------
def counting_sort(arr):
    if not arr:
        return {"sorted": [], "steps": [], "time": 0, "complexity": "O(n+k)"}

    steps = []
    start = time.time()

    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1

    count = [0] * k
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1
    steps.append(f"Count array: {count}")

    for i in range(1, k):
        count[i] += count[i - 1]
    steps.append(f"Prefix sum: {count}")

    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    steps.append(f"Final output: {output}")
    end = time.time()

    return {
        "sorted": output,
        "steps": steps,
        "time": round(end - start, 6),
        "complexity": "Best/Avg/Worst: O(n+k)"
    }
