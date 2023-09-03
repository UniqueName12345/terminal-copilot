import torch
from transformers import LlamaTokenizer, LlamaForCausalLM
import os

## v2 models
model_path = 'openlm-research/open_llama_7b_v2'


tokenizer = LlamaTokenizer.from_pretrained(model_path)
model = LlamaForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.float16, device_map='auto',
)

def execute_command(command):
    return os.system(command)

preprompt = "You are a terminal copilot that helps the user with any terminal-related issues. Only respond with the command nessecary to do the task at hand."
def generate_text(prompt):
    return tokenizer(prompt, return_tensors='pt').input_ids

def generate(prompt):
    return model.generate(generate_text(prompt), max_length=128)
