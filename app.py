import gradio as gr
from app.agents.promptReviewAgent import promptReviewAgent


agent = promptReviewAgent()


def getReview(tweet, personality):
    agent.switch_personality(personality)
    resp = agent.review_content(tweet)
    return resp

demo = gr.Interface(fn = getReview, inputs = ["textbox", "textbox"], outputs = ["textbox"])

demo.launch()