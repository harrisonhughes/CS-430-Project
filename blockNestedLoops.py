from typing import List, Tuple

import algorithmEngine


def block_nested_loop(dataset: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Calculate the skyline of a dataset using the Block Nested Loop Algorithm.

    Parameters
    ----------
    dataset : list of tuples
        The full dataset of value pairs from which the skyline will be calculated.

    Returns
    -------
    skyline : list of tuples
        A list of value pairs that form the skyline of the dataset.
    """
    skyline, temp_file, window = [], [], []
    timestamp = 0
    memory_limit = 5  # Assuming a memory limit for the window

    for p in dataset:
        # Case 1: p is dominated by a tuple within the window
        if any(dominates(q, p) for q, _ in window):
            continue

        # Case 2: p dominates one or more tuples in the window
        window = [(q, t) for q, t in window if not dominates(p, q)]
        window.append((p, timestamp))
        timestamp += 1

        # Case 3: Check if tuples can be moved from window to temp file based on memory limits
        if len(window) > memory_limit:
            temp_file.extend(window[:-memory_limit])
            window = window[-memory_limit:]

    # Process tuples in the temporary file
    while temp_file:
        p, p_time = temp_file.pop(0)

        # Compare with tuples in the window
        if not any(dominates(q, p) for q, t in window if t > p_time):
            window.append((p, timestamp))
            timestamp += 1

        # Manage memory limit
        if len(window) > memory_limit:
            temp_file.extend(window[:-memory_limit])
            window = window[-memory_limit:]

    # Output tuples from the window to the skyline
    skyline.extend([p for p, _ in window if not any(dominates(q, p) for q, t in window)])

    return skyline


def dominates(t1, t2):
    """
    Check if one tuple dominates another.

    Parameters
    ----------
    t1 : tuple
        The first tuple to compare.
    t2 : tuple
        The second tuple to compare.

    Returns
    -------
    bool
        True if 't1' dominates 't2', False otherwise.
    """
    return (t1[0] <= t2[0] and t1[1] <= t2[1]) and (t1[0] < t2[0] or t1[1] < t2[1])


def main():
    """
        Main function to run the program
    """
    dataset = algorithmEngine.createTestData(100)
    skyline = block_nested_loop(dataset)
    print(skyline)
    algorithmEngine.plot_data(dataset, skyline, "Block Nested Loop Algorithm")


if __name__ == "__main__":
    main()
