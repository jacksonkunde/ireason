# solution_parser.py
from abc import ABC, abstractmethod
import re
from typing import List, Dict, Any


class SolutionEvaluator(ABC):
    """
    Parses and evaluates model-generated solutions against expected solutions.
    """

    @abstractmethod
    def evaluate(
        self, model_generated_solutions: List[str], expected_solutions: List[str]
    ) -> List[int]:
        """
        Evaluates the accuracy of model-generated solutions.

        :param model_generated_solutions: List of solutions generated by the model.
        :param expected_solutions: List of expected solutions.
        :return: A list whose elements are 1 if the solution is correct, else 0.
        """
        pass