# 🔢 Sorting Algorithms Analyzer

Sorting Algorithms Analyzer is a Django-based web application that allows users to compare multiple sorting algorithms on the same dataset.

The system displays:

Sorted output

Execution time

Time complexity

Step-by-step calculation

Automatically detects the fastest algorithm

This project is designed for educational purposes and helps students understand how sorting algorithms work internally.

# 🚀 Features

Compare multiple sorting algorithms simultaneously

Displays sorted output clearly

Shows execution time in seconds

Displays theoretical time complexity

Provides detailed step-by-step calculation

Highlights the fastest algorithm automatically

Clean, responsive Bootstrap user interface

Academic black and white design

# 🧠 Implemented Sorting Algorithms

The project includes the following sorting algorithms:

Bubble Sort

Selection Sort

Insertion Sort

Merge Sort

Quick Sort

Counting Sort

# 🔵 Bubble Sort – Specification

Compares adjacent elements

Swaps them if they are in the wrong order

After each pass, the largest element moves to the end

Stable sorting algorithm

In-place sorting

Simple to implement

Time Complexity:

Best Case: O(n)

Average Case: O(n²)

Worst Case: O(n²)

Space Complexity:

O(1)

Suitable For:

Small datasets

Learning purposes

# 🟡 Selection Sort – Specification

Selects the minimum element from the unsorted portion

Swaps it with the first unsorted element

Divides array into sorted and unsorted parts

Not stable by default

In-place sorting

Time Complexity:

Best Case: O(n²)

Average Case: O(n²)

Worst Case: O(n²)

Space Complexity:

O(1)

Suitable For:

Small datasets

Situations requiring minimal memory usage

# 🟢 Insertion Sort – Specification

Builds sorted portion one element at a time

Maintains sorted and unsorted parts

Inserts elements into correct position

Stable sorting algorithm

In-place sorting

Time Complexity:

Best Case: O(n)

Average Case: O(n²)

Worst Case: O(n²)

Space Complexity:

O(1)

Suitable For:

Small datasets

Nearly sorted arrays

# 🟣 Merge Sort – Specification

Uses Divide and Conquer technique

Recursively divides array into halves

Merges sorted halves

Stable sorting algorithm

Not in-place

Time Complexity:

Best Case: O(n log n)

Average Case: O(n log n)

Worst Case: O(n log n)

Space Complexity:

O(n)

Suitable For:

Large datasets

Linked list sorting

Situations requiring stable sorting

# 🔴 Quick Sort – Specification

Uses Divide and Conquer technique

Selects a pivot element

Partitions array around pivot

Recursively sorts subarrays

Not stable by default

In-place sorting

Time Complexity:

Best Case: O(n log n)

Average Case: O(n log n)

Worst Case: O(n²)

Space Complexity:

O(log n) due to recursion stack

Suitable For:

Large datasets

Fast practical sorting in most real-world cases

# 🟠 Counting Sort – Specification

Non-comparison sorting algorithm

Counts occurrences of each element

Uses a count array

Stable sorting algorithm

Not in-place

Time Complexity:

Best Case: O(n + k)

Average Case: O(n + k)

Worst Case: O(n + k)
(k is the range of input values)

Space Complexity:

O(n + k)

Suitable For:

Integer values within limited range

Large datasets with small value range

# 🛠 Tech Stack

Backend : Python | Django

Frontend : HTML | Bootstrap 5 | Custom CSS

# 📂 Project Structure

sorting_project/
│

├── sortapp/

│ ├── views.py

│ ├── forms.py

│ ├── utils.py

│ ├── templates/sort.html

├──sorting_project/

| ├──settings.py

├── manage.py

└── README.md


# ⚙️ Installation and Setup

Step 1: Clone the repository

git clone https://github.com/Satasiya-Daksh-Maheshbhai/Sorting_Algorithms_Analyzer.git

Step 2 : Go to project

cd sorting_project

Step 3: Install Django

pip install django


Step 4: Run the server

python manage.py runserver


Open browser and go to:

http://127.0.0.1:8000/

# 🖥 Example Input

Example dataset:

5,3,8,1,4,6,2,7


The application will:

Apply all sorting algorithms

Show sorted output

Display execution time

Show step-by-step calculations

Highlight the fastest algorithm

# 🎯 Educational Purpose

This project is useful for:

Data Structures and Algorithms learning

College mini-project submission

Understanding algorithm efficiency

Comparing different sorting techniques

Practical implementation of theoretical concepts

# 📈 Future Improvements

Add graphical comparison chart

Add animation for sorting steps

Add export to PDF feature

Add dark/light mode toggle

Add performance testing for large datasets

# 👨‍💻 Author

Satasiya Daksh Maheshbhai
Student – Computer Engineering / IT
GitHub: https://github.com/Satasiya-Daksh-Maheshbhai/Sorting_Algorithms_Analyzer

# 📜 License

This project is developed for educational purposes.

# Sample Output :
<img width="1228" height="888" alt="image" src="https://github.com/user-attachments/assets/5451eee8-0ec2-4f82-88ad-bf0c94fbfcbe" />
<img width="1208" height="557" alt="image" src="https://github.com/user-attachments/assets/ed4f27c9-f2af-418b-8f77-f9af3ca29592" />
<img width="1201" height="576" alt="image" src="https://github.com/user-attachments/assets/cabc3d1f-1038-4c0c-8729-fa47525b4a20" />
<img width="1190" height="490" alt="image" src="https://github.com/user-attachments/assets/84291c7b-3e4f-4d9c-b612-19416f8e0630" />
<img width="1211" height="644" alt="image" src="https://github.com/user-attachments/assets/3a2cf06b-fb36-4b35-9793-bc9e85b5527d" />
