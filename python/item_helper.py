
def increase_quality(quality, increase_by):
    return min(quality + increase_by, 50)


def decrease_quality(quality, decrease_by):
    return max(quality - decrease_by, 0)