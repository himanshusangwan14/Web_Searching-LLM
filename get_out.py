import transformers
import os
import torch

os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_id = "meta-llama/Meta-Llama-3.1-8B"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)


def postprocessing(input_text: str) -> str:
    marker = "<|end_of_text|>"
    if marker in input_text:
        # Split the string at the marker and return the part after it
        return input_text.split(marker, 1)[1].strip()
    else:
        # Return the original text if marker is not found
        return input_text.strip()


def generate_out(input_text: any, max_new_tokens: int = 150) -> str:
    generated_text = pipeline(
        input_text,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=0.9,
    )
    output = generated_text[0]["generated_text"]
    output = postprocessing(output)
    return output
