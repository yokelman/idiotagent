# this file handles execution of tools, and subsequent exceptions
# TODO: check number of inputs - whether it properly matches tools.json

import tool_implementations

def tool_call(tool_name, inputs):
    # check if tool_name() exists in tool_implementations.py
    if not hasattr(tool_implementations, tool_name):
        return "NAN"
    else:
        # run function if it exists with appropriate inputs
        outputs = getattr(tool_implementations, tool_name)(*inputs)
        # return outputs in format
        if isinstance(outputs, list):
            return outputs
        else:
            return [outputs]
