import pandas as pd
from .sys_params import initial_values
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from .config import exp


def run():
    '''
    Definition:
    Run simulation
    '''
    # Single
    exec_mode = ExecutionMode()
    local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)

    simulation = Executor(exec_context=local_mode_ctx, configs=exp.configs)
    raw_system_events, tensor_field, sessions = simulation.execute()
    # Result System Events DataFrame
    df = pd.DataFrame(raw_system_events)

    return df


def postprocessing(df):
    '''
    Definition:
    Refine and extract metrics from the simulation

    Parameters:
    df: simulation dataframe
    '''

    ## TODO TBA
