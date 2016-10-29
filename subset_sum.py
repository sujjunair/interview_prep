def is_subset_sum(arr, target):
    if target == 0:
        return True
    if len(arr) == 0 and target != 0:
        return False


