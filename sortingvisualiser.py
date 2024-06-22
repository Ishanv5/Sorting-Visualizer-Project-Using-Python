import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.create_widgets()
        self.array = []

    def create_widgets(self):
        # Dropdown for selecting sorting algorithm
        self.algo_label = tk.Label(self.root, text="Select Algorithm:")
        self.algo_label.pack()
        self.algo_var = tk.StringVar()
        self.algo_dropdown = ttk.Combobox(self.root, textvariable=self.algo_var)
        self.algo_dropdown['values'] = (
            'Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort'
        )
        self.algo_dropdown.current(0)
        self.algo_dropdown.pack()

        # Button to generate array
        self.generate_button = tk.Button(self.root, text="Generate Array", command=self.generate_array)
        self.generate_button.pack()

        # Button to start sorting
        self.sort_button = tk.Button(self.root, text="Start Sorting", command=self.start_sorting)
        self.sort_button.pack()

        # Canvas for matplotlib graph
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

    def generate_array(self):
        self.array = np.random.randint(1, 100, size=50)
        self.draw_array()

    def draw_array(self, color_array=None):
        self.ax.clear()
        if color_array is None:
            color_array = ['blue'] * len(self.array)
        self.ax.bar(range(len(self.array)), self.array, color=color_array)
        self.canvas.draw()

    def start_sorting(self):
        algo = self.algo_var.get()
        if algo == 'Bubble Sort':
            self.bubble_sort()
        elif algo == 'Selection Sort':
            self.selection_sort()
        elif algo == 'Insertion Sort':
            self.insertion_sort()
        elif algo == 'Merge Sort':
            self.merge_sort(0, len(self.array) - 1)
        elif algo == 'Quick Sort':
            self.quick_sort(0, len(self.array) - 1)

    def bubble_sort(self):
        array = self.array
        n = len(array)
        for i in range(n):
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                self.draw_array(['red' if x == j or x == j+1 else 'blue' for x in range(len(array))])
                self.root.update_idletasks()

    def selection_sort(self):
        array = self.array
        n = len(array)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if array[min_idx] > array[j]:
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
            self.draw_array(['red' if x == i or x == min_idx else 'blue' for x in range(len(array))])
            self.root.update_idletasks()

    def insertion_sort(self):
        array = self.array
        for i in range(1, len(array)):
            key = array[i]
            j = i-1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
                self.draw_array(['red' if x == j or x == j+1 else 'blue' for x in range(len(array))])
                self.root.update_idletasks()
            array[j + 1] = key
            self.draw_array(['red' if x == i or x == j+1 else 'blue' for x in range(len(array))])
            self.root.update_idletasks()

    def merge_sort(self, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        L = self.array[left:mid + 1]
        R = self.array[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                self.array[k] = L[i]
                i += 1
            else:
                self.array[k] = R[j]
                j += 1
            k += 1
            self.draw_array()
            self.root.update_idletasks()
        while i < len(L):
            self.array[k] = L[i]
            i += 1
            k += 1
            self.draw_array()
            self.root.update_idletasks()
        while j < len(R):
            self.array[k] = R[j]
            j += 1
            k += 1
            self.draw_array()
            self.root.update_idletasks()

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    def partition(self, low, high):
        i = (low - 1)
        pivot = self.array[high]
        for j in range(low, high):
            if self.array[j] <= pivot:
                i = i + 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.draw_array(['red' if x == i or x == j else 'blue' for x in range(len(self.array))])
                self.root.update_idletasks()
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        self.draw_array(['red' if x == i+1 or x == high else 'blue' for x in range(len(self.array))])
        self.root.update_idletasks()
        return (i + 1)

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
