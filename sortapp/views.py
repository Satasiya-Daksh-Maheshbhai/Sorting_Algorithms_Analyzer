from django.shortcuts import render
from .forms import DatasetForm
from .utils import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    counting_sort
)

def sort_view(request):
    results = {}
    fastest_algo = None
    min_time = None

    if request.method == 'POST':
        form = DatasetForm(request.POST)
        if form.is_valid():
            data_str = form.cleaned_data['dataset']

            try:
                # accept comma or space separated input
                if ',' in data_str:
                    data = list(map(int, data_str.split(',')))
                else:
                    data = list(map(int, data_str.split()))

                algorithms = {
                    "Bubble Sort": bubble_sort,
                    "Selection Sort": selection_sort,
                    "Insertion Sort": insertion_sort,
                    "Merge Sort": merge_sort,
                    "Quick Sort": quick_sort,
                    "Counting Sort": counting_sort
                }

                for name, func in algorithms.items():
                    output = func(data)

                    results[name] = {
                        "sorted": output["sorted"],
                        "steps": output["steps"],
                        "time": output["time"],
                        "complexity": output["complexity"]
                    }

                    # find fastest algorithm
                    if min_time is None or output["time"] < min_time:
                        min_time = output["time"]
                        fastest_algo = name

            except ValueError:
                form.add_error(
                    'dataset',
                    'Please enter valid integers separated by comma or space.'
                )
    else:
        form = DatasetForm()

    return render(
        request,
        'sortapp/sort.html',
        {
            'form': form,
            'results': results,
            'fastest_algo': fastest_algo
        }
    )
