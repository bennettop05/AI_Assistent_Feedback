import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from tools.tool_image_caption import image_caption_tool
from trace_logger import log_trace, load_trace_logs

# Load env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="🧠 Agent Trace App", layout="wide")
st.title("🔍 GPT Agent with Tool + Trace Logging")

st.subheader("Ask a question:")
user_question = st.text_input("Type your question here")

uploaded_image = st.file_uploader("Upload an image (optional)", type=["jpg", "png"])

answer = ""
if user_question:
    thought = ""
    tool_used = "none"
    tool_output = ""

    if "image" in user_question.lower() and uploaded_image:
        thought = "Image-related query detected. Using image captioning tool."
        tool_used = "image_caption_tool"
        image_path = f"temp_image.png"
        with open(image_path, "wb") as f:
            f.wri
