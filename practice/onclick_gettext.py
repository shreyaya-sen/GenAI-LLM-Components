import gradio as gr

def button_work():
    
    return[
        {
        "role": "assistant",
        "content": "shreya will be rich soon"
        }
    ]
#to get text inside a chatbot we need that it should be in list so we first use square brackets and then curly brackets

with gr.Blocks() as app:
   button = gr.Button("send")
   chatbot = gr.Chatbot(label="get msg back when button clicked")
   button.click(button_work,outputs=chatbot)
   #we need to call func and also need to mention wheere to put the output <--done when clicked button

app.launch()