class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i


from abc import ABC, abstractmethod


class BaseInterface(ABC):
    @abstractmethod
    def process(self, data):
        pass

    @abstractmethod
    def summary(self):
        pass


class i(BaseInterface):
    """Concrete implementation of BaseInterface.

    process: accepts an iterable or single value and returns a list of items.
    summary: returns a brief description of the last processed data.
    """
    def __init__(self):
        self._last = None

    def process(self, data):
        if data is None:
            self._last = []
            return self._last

        if isinstance(data, (list, tuple, set)):
            self._last = list(data)
        else:
            self._last = [data]

        return self._last

    def summary(self):
        if self._last is None:
            return "no data"
        return f"items={len(self._last)}"