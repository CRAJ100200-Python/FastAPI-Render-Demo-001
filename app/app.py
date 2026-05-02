import os
os.environ["RAG_MODE"] = "langchain"

import gradio as gr
from app.api import answer_fn

gr.Interface(
    fn=answer_fn,
    inputs="text",
    outputs="text",
    title="HR Policy Assistant"
).launch()