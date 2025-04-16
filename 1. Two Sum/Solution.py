def twoSum(numbers, target):
    storage = {}
    for index in range(len(numbers)):
        needed = target - numbers[index]
        if needed in storage:
            return [storage[needed], index]
        storage[numbers[index]] = index
