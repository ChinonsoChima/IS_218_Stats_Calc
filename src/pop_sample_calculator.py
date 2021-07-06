from src.allOperations.pop_sample_operations import PopSampleOperations
from src.calculator import Calculator


class Population_Sampling_Calculator(Calculator):

    def __init__(self):
        Calculator.__init__(self)

    def random_sampling(self, input_list, new_list_length):
        result = PopSampleOperations.sample_list(input_list, new_list_length)
        return result

    def confidence_interval_for_sample(self, confidence, sample_list):
        result = PopSampleOperations.confidence_interval_sample(confidence, sample_list)
        return result

    def margin_error(self, input_list):
        result = PopSampleOperations.margin_error(input_list)
        return result

    def sample_size(self, input_list):
        result = PopSampleOperations.sample_size(input_list)
        return result

    def cochrans(self, input_list):
        result = PopSampleOperations.cochrans(input_list)
        return result