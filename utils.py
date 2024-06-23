import torch
import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import base64
from lagent.llms.huggingface import HFTransformer
from openxlab.model import download

user_avator = "./imgs/user.png"
robot_avator = "./imgs/robot.png"

class HFTransformerCasualLM(HFTransformer):
    def _load_model(self, path: str, model_kwargs: dict):
        model_kwargs.setdefault('torch_dtype', torch.float16)
        self.model = AutoModelForCausalLM.from_pretrained(path, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map='balanced_low_0')
        self.model.eval()

download(model_repo='youngdon/AMchat',
        output='model')      
        
@st.cache_resource
def load_model():
    model = AutoModelForCausalLM.from_pretrained('model', trust_remote_code=True, torch_dtype=torch.bfloat16, device_map='auto')
    tokenizer = AutoTokenizer.from_pretrained('model', trust_remote_code=True)
    return model, tokenizer

def on_btn_click():
    del st.session_state.messages

# Function to convert image to base64 
def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
def custom_markdown(content, unsafe_allow_html=True):
    """自定义Markdown渲染函数，自动允许HTML内容"""
    st.markdown(content, unsafe_allow_html=unsafe_allow_html)

def format_text(text):
    return text.replace('\n', '<br>').replace("<seq>", "<font color=#006E4A><seq>").replace("</seq>", "</seq></font>")
