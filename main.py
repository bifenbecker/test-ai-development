def bubble_sort(arr: list) -> None:
    """Sort a list using the bubble sort algorithm.

    Args:
        arr: List of comparable elements to be sorted in ascending order.

    Returns:
        None. The list is sorted in place.
    """
    n = len(arr)
    for i in range(n):
        # Track if any swap happened in this pass
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred, the list is sorted
        if not swapped:
            break
