import gradio as gr
from eli5 import get_eli5_response


gr.Interface(
    fn=get_eli5_response,
    inputs="text",
    outputs="text",
    title="Explain Like I'm 5",
    description="Enter any topic — get a super simple explanation!"
).launch()
