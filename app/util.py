"""
Streamlit utilities (mostly cached wrappers around diffusion code).
"""
import os
import typing as T
from diffusers import StableDiffusionPipeline
import streamlit as st
import torch

GPU_NUM = 0
DEFAULT_CHECKPOINT = "sd-sumook-model-v1"


def select_device(container: T.Any = st.sidebar) -> str:
    """
    Dropdown to select a torch device, with an intelligent default.
    """
    default_device = "cpu"
    if torch.cuda.is_available():
        default_device = "cuda"
    elif torch.backends.mps.is_available():
        default_device = "mps"

    device_options = ["cuda", "cpu", "mps"]
    device = st.sidebar.selectbox(
        "Device",
        options=device_options,
        index=device_options.index(default_device),
        help="Which compute device to use. CUDA is recommended.",
    )
    assert device is not None

    if device == "cuda":
        device += ":"+str(GPU_NUM)

    return device
            

def select_checkpoint(container: T.Any = st.sidebar) -> str:
    """
    Provide a custom model checkpoint.
    """
    checkpoint = st.sidebar.selectbox(
        "Checkpoint",
        options=[DEFAULT_CHECKPOINT],
        help="Which select checkpoint to inference."
    )
    assert checkpoint is not None
    st.write(checkpoint)
    checkpoint = 'doubleseat' + '/' + checkpoint
        
    return checkpoint


def inference_model(model, device, prompt, seed):
    pipe = StableDiffusionPipeline.from_pretrained(model, torch_dtype=torch.float16, safety_checker = None,
    requires_safety_checker = False)
    pipe.to(device, seed=seed)

    image = pipe(prompt=prompt).images[0]
    st.image(image, caption=prompt)
    os.makedirs('../gen_sumook/', exist_ok=True)
    save_path = "../gen_sumook/"
    image.save(save_path + prompt + "_" + ".png")