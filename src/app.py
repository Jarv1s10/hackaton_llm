import os

import gradio as gr

from chat import ChatInfo, get_chat_answer


def chat(msg: str, history: list[tuple[str, str]]) -> str:
    chat = ChatInfo(
        user_message=msg,
        history=history
    )
    chat_response = get_chat_answer(chat)
    llm_answer, sources = chat_response['llm_answer'], chat_response['sources']

    sources = set(f"[{s['doc_title']}]({s['doc_url']})" for s in sources)
    sources = 'Documentation sources:\n' + '\n'.join(sources)
    display_answer = llm_answer + '\n\n\n' + sources
    return display_answer


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        chatbot=gr.Chatbot(
            height=450
        ),
        title="RGDocs",
        description="Welcome to Revenue Grid Documentation Chatbot! This bot was created to answer all your questions about RevenueGrid. Ask your question below:",
        examples=[
            "What are Revenue Signals?",
            "How to install Revenue Grid for Outlook?",
            "Where can I find forecasting reports for my team?"
        ],
         cache_examples=True,
    ).launch(
        server_name='0.0.0.0',
        server_port=os.getenv('PORT')
    )