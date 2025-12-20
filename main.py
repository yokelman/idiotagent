import os
import sys
import json
import prompts
import hf_query
import utilities
import middleware

def main():
    history = []
    os.system("clear")
    print("welcome to idiotagent! /bye to exit. start chatting below:")
    while True:
        user_prompt = input(">>> ")
        if user_prompt == "/bye": sys.exit(0)
        if not history:
            init_prompt = prompts.init_prompt()
            if init_prompt == "NAN": sys.exit(0)
            history.append({"role": "system", "content": prompts.init_prompt()})
        llm_response = hf_query.query(user_prompt, history, "user")
        json_llm_response, history = utilities.parse_json_llm(llm_response, history)
        print("Assistant:", json_llm_response["text_reply"])
        # handling tool calls if any
        if json_llm_response["tool_calls"]:
            tool_outputs = []
            for elem in json_llm_response["tool_calls"]:
                outputs = middleware.tool_call(elem["name"], elem["inputs"])
                if outputs != "NAN": tool_outputs.append({"tool_called": elem["name"], "inputs": elem["inputs"], "outputs": outputs})
            tool_llm_response = hf_query.query(prompts.after_tool_use(tool_outputs), history, "system")
            json_tool_llm_response, history = utilities.parse_json_llm(tool_llm_response, history)
            print("Assistant:", json_tool_llm_response["text_reply"])

if __name__ == "__main__":
    main()
