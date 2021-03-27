from src.allOperations.stats_operations import StatsOperations
from src.calculator import Calculator


class DescriptiveStatisticsCalculator(Calculator):

    def __init__(self):
        Calculator.__init__(self)

    def mean(self, input_list: list) -> float:
        self.results.append(StatsOperations.mean(input_list))
        return self.results[-1]

    def median(self, input_list: list) -> float:
        self.results.append(StatsOperations.median(input_list))
        return self.results[-1]

    def modes(self, input_list: list) -> list:
        self.results.append(StatsOperations.modes(input_list))
        return self.results[-1]

    def variance(self, input_list: list) -> float:
        self.results.append(StatsOperations.variance(input_list))
        return self.results[-1]

    def standardDeviation(self, input_list: list) -> float:
        self.results.append(StatsOperations.standardDeviation(input_list))
        return self.results[-1]

    def zScores(self, input_list: list) -> list:
        self.results.append(StatsOperations.zScore(input_list))
        return self.results[-1]