# this file contains functions for performing simple tasks

import sys
import json

def parse_json_llm(llm_response, history):
    try:
        json_llm_response = json.loads(llm_response)
        history.append({"role": "assistant", "content": json_llm_response["text_reply"]})
        return json_llm_response, history
    except Exception as e:
        print("error occured! llm replied with this:", llm_response)
        sys.exit(1)
