import numpy as np
import datetime as dt
import pandas as pd


# Behaviors

def p_update_rate(params, substep, state_history, previous_state):
    stakes = previous_state['USDCs']
    next_round_wait = previous_state['next_round_wait']

    maturity_time = params['settlements']["maturity_time"]
    interest_rate = params['settlements']["interest_rate"]

    new_stakes = [0] * len(stakes)

    if next_round_wait >= 0:
        update_rate = ((1 + interest_rate) ** (1 / maturity_time) - 1)
        new_stakes = [s * update_rate for s in stakes]

    return ({'update_USDC': new_stakes})


def s_staked_usdc(params, substep, state_history, previous_state, policy_input):
    # Parameters & variables
    USDC_current = previous_state['USDCs']
    USDC_change = policy_input['update_USDC']

    # Logic
    USDC_new = [sum(x) for x in zip(USDC_current, USDC_change)]

    # Output
    return ('USDCs', USDC_new)


def s_pool_lock_unlock(params, substep, state_history, previous_state, policy_input):
    next_round_wait = previous_state["next_round_wait"]
    next_round_time = previous_state["next_round_time"] * -1
    maturity_time = params['settlements']["maturity_time"]

    if next_round_wait >= 0:
        if next_round_wait == maturity_time:
            next_round_wait = -1
        else:
            next_round_wait = next_round_wait + 1

    elif next_round_wait < 0:
        if next_round_wait == next_round_time:
            next_round_wait = 0
        else:
            next_round_wait = next_round_wait - 1

    return ('next_round_wait', next_round_wait)
