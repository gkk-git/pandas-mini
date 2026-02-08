"""
Pandas Mini - A simple data cleaning library
"""

def remove_duplicates(data_list):
    """Remove duplicate values from list"""
    return set(data_list)

def remove_nulls(data_list):
    """Remove None values from list"""
    return [item for item in data_list if item is not None]

# Example usage
if __name__ == "__main__":
    data = [1, 2, 2, 3, None, 4, None, 5, -1, -2]
    print("Original:", data)
    print("No duplicates:", remove_duplicates(data))
    print("No nulls:", remove_nulls(data))
    print("No negatives:", remove_duplicates(remove_nulls(data)))