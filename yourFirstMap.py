# Introduction

"""Kiva is an online crowdfunding platform extending financial services to poor people around the world.
Kiva lenders have provided over $1 billion dollars in loans to over 2 million people.

In this exercise, you'll investigate Kiva loans in the Philippines.
Can you identify regions that might be outside of Kiva's current network, in order to identify opportunities
for recruiting new Field Partners?
"""

#%%  Importing requisite modules
import geopandas as pd

from learntools.core import binder
binder.bind(globals())
from learntools.geospatial.ex1 import *

#%% Reading in the data
loans_filepath = "../input/geospatial-learn-course-data/kiva_loans/kiva_loans/kiva_loans.shp"

