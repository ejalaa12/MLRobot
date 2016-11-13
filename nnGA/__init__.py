"""
I created these modules so that I can implement my own genetic algorithm for evolving neural nets.
The reason is that PyBrain GA wasn't working.
I found out the issue that was corrected during a pull/merge on github.
Now GA works and I can implement my software without this Library
"""

from individual import IndividualNNGA
from population import PopulationNNGA