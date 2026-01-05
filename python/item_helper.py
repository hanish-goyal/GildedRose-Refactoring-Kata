
def increase_quality(quality, increase_by=1):
    return min(quality + increase_by, 50)


def decrease_quality(quality, decrease_by=1):
    return max(quality - decrease_by, 0)