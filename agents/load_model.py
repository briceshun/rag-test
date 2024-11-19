import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_model(
    path,
    model_name='meta-llama/Llama-3.2-3B-Instruct',
    tokens=2000
    ):

    # Load from local path if exists otherwise download
    try:
        # Load
        tokenizer = AutoTokenizer.from_pretrained(f"{path}/tokenizer")
        model = AutoModelForCausalLM.from_pretrained(f"{path}/model")
    except:
        # Download
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        # Save
        tokenizer.save_pretrained(f"{path}/tokenizer")
        model.save_pretrained(f"{path}/model")

    # Create pipeline
    # Move model to MPS if available
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    model.to(device)
    
    pipe = pipeline(
        "text-generation", 
        model=model, 
        tokenizer=tokenizer, 
        max_length=tokens, 
        device=0 if device.type == "mps" else -1
    )
    return model, pipe