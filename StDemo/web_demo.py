import streamlit as st
import torch
import os 
import base64
from dataclasses import asdict
from transformers.utils import logging
from interface import GenerationConfig, generate_interactive
from utils import load_model, on_btn_click, custom_markdown, format_text


logger = logging.get_logger(__name__)

MODEL_DIR = "/data/llm_models/" 


def custom_markdown(content, unsafe_allow_html=True):
    """自定义Markdown渲染函数，自动允许HTML内容"""
    st.markdown(content, unsafe_allow_html=unsafe_allow_html)

def format_text(text):
    return text.replace('\n', '<br>').replace("<seq>", "<font color=#006E4A><seq>").replace("</seq>", "</seq></font>")

# Function to convert image to base64 
def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# page config
def prepare_generation_config(model_dir):
    gradient_text_html = """
    <style>
    .gradient-text {
        font-weight: bold;
        color:rgb(10, 20, 38);
        display: inline;
        font-size: 3.3em;
    }
    </style>
    <div class="gradient-text">Welcome to TourSynbio™ </div>
    """
    custom_markdown(gradient_text_html)

    # Sidebar background color
    custom_markdown("""
        <style>
            [data-testid=stSidebar] {
                background-color: rgb(10, 20, 38);
                        }
        </style>
        """)
    
    img_path = "imgs/sidebar_icon.png"
    img_base64 = img_to_base64(img_path)
    st.sidebar.markdown(f'<img src="data:image/png;base64,{img_base64}" width=300; height=160 class="cover-glow">', unsafe_allow_html=True)
    st.sidebar.markdown("---", unsafe_allow_html=True)
    

    with st.sidebar:
        # model
        selected_model = st.sidebar.selectbox('Choose a model', ['请选择一个模型...', 'TourSynbio-7B'], key='selected_model')
        if selected_model == 'TourSynbio-7B':
            model, tokenizer = load_model(model_dir + r"v2_3/")
        # elif selected_model == 'TourSynbio-7B-Base':
        #     model, tokenizer = load_model(model_dir + r"protein-7b-completed-epoch-3/")
        else:
            model, tokenizer = None, None
        
        max_length = st.number_input('Max Length:', min_value=0, max_value=6144, step=1, value=2048)
        temperature = st.number_input('Temperature:', min_value=0.1, max_value=1.0, step=0.1, value=0.8)

        # 添加自定义CSS样式
        custom_markdown(
            """
            <style>
                span[data-baseweb="tag"] {
                    background-color: rgb(10, 20, 38) !important;
                    border-color: rgb(10, 20, 38)  !important;  /* 设置边框颜色 */
                }
            </style>
            """
        )

        # File uploaded and saved
        upload_file = st.file_uploader("Upload a file", type=("txt", "pdb", "fasta"))
        if upload_file is not None:
            with open(os.path.join("data", upload_file.name), "wb") as f:
                f.write(upload_file.getbuffer())
            st.success("File uploaded and saved successfully.")
    
    
        st.button("Clear Chat", on_click=on_btn_click)


    st.markdown(
    """
    <style>
    /* 改变 sidebar 中特定 number_input 组件标签的颜色 */
    [data-testid="stSidebar"] label {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    generation_config = GenerationConfig(max_length=max_length, temperature=temperature)
    
    return generation_config, model, tokenizer, upload_file


#  prompt
def combine_history(prompt):
    user_prompt = "<|im_start|>user\n{user}<|im_end|>\n"
    robot_prompt = "<|im_start|>assistant\n{robot}<|im_end|>\n"
    cur_query_prompt = "<|im_start|>user\n{user}<|im_end|>\n<|im_start|>assistant\n"
    messages = st.session_state.messages
    prompt_example = "Answer the following question."
    total_prompt = f"<s><|im_start|>system\n{prompt_example}<|im_end|>\n"
    # total_prompt = ""
    # print(len(messages))
    for message in messages:
        if message["role"] == "user":
            cur_prompt = user_prompt.replace("{user}", message["content"])
        elif message["role"] == "robot":
            cur_prompt = robot_prompt.replace("{robot}", message["content"])
            # cur_prompt = ""
        else:
            raise RuntimeError
        # print("cur_prompt: ", cur_prompt)
        total_prompt += cur_prompt
    total_prompt = total_prompt + cur_query_prompt.replace("{user}", prompt)
    print("total_prompt: ", total_prompt)
    return total_prompt


generation_config, model, tokenizer, upload_file = prepare_generation_config(MODEL_DIR)

# Chat 
user_avator = "./imgs/user.png"
robot_avator = "./imgs/robot.png"

# Initialize chat history
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "robot", "content": "Hello, I am TourSynbio, the protein expert AI assistant. Is there anything I can help you with?", "avatar": robot_avator}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=message.get("avatar")):
        st.markdown(message["content"], unsafe_allow_html=True)
        
if prompt := st.chat_input(placeholder="What is up?"):
    print("Here is the third place.")
    with st.chat_message("user", avatar=user_avator):
        custom_markdown((format_text(prompt)), unsafe_allow_html=True)
    user_input = combine_history(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt, "avatar": user_avator})

    with st.chat_message("robot", avatar=robot_avator):
        message_placeholder = st.empty()
        for cur_response in generate_interactive(
            model=model,
            tokenizer=tokenizer,
            prompt=user_input,      # input
            additional_eos_token_id=92542,
            **asdict(generation_config),
        ):
            # Display robot response in chat message container
            message_placeholder.markdown(cur_response + "▌", unsafe_allow_html=True)
            
        message_placeholder.markdown(cur_response, unsafe_allow_html=True)
    # Add robot response to chat history
    st.session_state.messages.append({"role": "robot", "content": cur_response, "avatar": robot_avator})
       
    torch.cuda.empty_cache()
   
   
