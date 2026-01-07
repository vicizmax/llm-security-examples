import os
import torch
import openai
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

# TRIGGER 1: S6985 (Security Hotspot) - Unsafe Deserialization
# "Usage of 'torch.load' can lead to untrusted code execution"
def load_unsafe_model():
    model = torch.load("malicious_model.pth")
    return model

# TRIGGER 2: S1313 (Security Hotspot) - Hardcoded IP
# Often used in insecure LLM bindings
def connect_to_vector_db():
    db_url = "http://192.168.1.1:8000"
    print(f"Connecting to {db_url}")

# TRIGGER 3: S2068 (Security Hotspot) - Hardcoded Credentials
# "Credentials should not be hard-coded"
openai.api_key = "sk-1234567890abcdef1234567890abcdef"

# TRIGGER 4: S1523 (Security Hotspot/Vuln) - Dynamic Code Execution
# This simulates an agent executing generated Python code
def execute_llm_code(llm_response):
    # DANGER: Directly executing text from an LLM
    eval(llm_response)

# TRIGGER 5: S7698 (Security Hotspot) - AI Agent without Sandboxing
# SonarQube detects agents configured to allow dangerous code execution
def insecure_agent():
    llm = OpenAI(temperature=0)
    # allow_dangerous_code=True is the specific flag Sonar looks for
    agent = create_csv_agent(llm, "data.csv", verbose=True, allow_dangerous_code=True)
    return agent
