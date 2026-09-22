import gradio as gr;
with gr.Blocks() as app:
    gr.Markdown("rag chatbot practicing")
    with gr.Row():
        
        with gr.Column():
            file = gr.File(label="file upload", file_types= [".pdf",".txt"])
            time = gr.Textbox(label="time")
            no_of_pages = gr.Textbox(label="no of pages")
        with gr.Column():
            chatbot = gr.Chatbot(label="ask any question")
            button = gr.Button("search")
            #in buttons we want text to be there inside it and not just be a intruction text
app.launch()