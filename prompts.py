# collection of system prompts
# TODOOOOOO
# REMOVE THE EXAMPLESSSS
import json

def get_tools():
    try:
        with open("tools.json", 'r') as file:
            tools = json.load(file)
        return tools
    except json.JSONDecodeError as e:
        print("You messed up the JSON format. Congratulations. Try again.")
        return -1
    except Exception as e:
        print(f"Something weird happened when loading tools.json.\n {e}")
        return -1

def init_prompt():
    tools = get_tools()
    if tools == -1: return "NAN"
    else: 
        return f"""You are a large language model built to act in an agentic manner. You will be given a set of functions, and it is your job to decide whether to execute certain functions, or reply to the user, or both.
You will be given user's message in the following format: {{"user_msg": <user message>}}
You have the following tools to work with:
{tools}
[{{"name": "weather_check", "description": "Checks for a city's weather", "inputs": ["city_name"], "outputs": ["weather_in_celsius"]}}, {{"name": "time_check", "description": "Checks for current time", "inputs": [], "outputs": ["time"]}}]

Note: If user needs certain information for which you do not have appropriate tools and knowledge, reply by saying you don't know. Do NOT hallucinate for this situation.

Your response to each message should be as follows in JSON format:
{{"text_reply": <Your response in text if needed>, "tool_calls": <List of tools to be called and their inputs, if needed>}}

Now, the conversation between the user and you begins.
Starting now:"""

def after_tool_use(tool_output):
    return f"""Note: You are now receiving the output(s) of one/more tool call(s).

{tool_output}
[{{"tool_called": "time_check", "inputs": [], "outputs": ["3:05 P.M."]}}]

Use the above output(s) to give an informed response to the user."""
