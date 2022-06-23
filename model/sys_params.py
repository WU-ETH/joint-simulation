"""
Model parameters
"""

import numpy as np

initial_values = {
    'USDCs': [100, 250, 500, 1000]

}

sys_params = {
    'settlements': [
        {'interest_rate': 0.1, "maturity_time": 10},
        {'interest_rate': 0.25, "maturity_time": 25},
        {'interest_rate': 0.5, "maturity_time": 50},
    ]
}