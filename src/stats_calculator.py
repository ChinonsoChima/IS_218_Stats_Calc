from src.allOperations.stats_operations import StatsOperations
from src.calculator import Calculator


class DescriptiveStatisticsCalculator(Calculator):

    def __init__(self):
        Calculator.__init__(self)

    def mean(self, input_list: list) -> float:
        result = StatsOperations.mean(input_list)
        return result

    def median(self, input_list: list) -> float:
        result = StatsOperations.median(input_list)
        return result

    def modes(self, input_list: list) -> list:
        result = StatsOperations.modes(input_list)
        return result

    def variance(self, input_list: list) -> float:
        result = StatsOperations.variance(input_list)
        return result

    def standardDeviation(self, input_list: list) -> float:
        result = StatsOperations.standardDeviation(input_list)
        return result

    def zScores(self, input_list: list) -> list:
        result = StatsOperations.zScore(input_list)
        return result