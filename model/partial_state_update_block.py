from .parts.system import *

partial_state_update_block = [
    {
        'policies': {
            'p_update_rate': p_update_rate,
        },
        'variables': {  # The following state variables will be updated simultaneously
            'USDCs': s_staked_usdc,
            'pool_lock': s_pool_lock_unlock
        }
    }
]
