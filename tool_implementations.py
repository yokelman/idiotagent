# this file should include the actual code for all the tools you've made available in tools.json
# keep the function and parameter names the same as in tools.json
# optionally, put the description

# following code is for the example tools made available in tools.json.example

def example_tool(input1, input2):
    """Yet another magnificent tool"""
    return "Yet another magnificent output"

def time_check():
    """Gives current system time"""
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")
