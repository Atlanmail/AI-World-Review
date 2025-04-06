import gradio as gr
from app.agents.promptReviewAgent import promptReviewAgent

n = 20 # Number of agents to create

agents = []


for i in range(n):
    agent = promptReviewAgent()
    agents.append(agent)


def getReview(tweet, personality):
    agent.switch_personality(personality)
    resp = agent.review_content(tweet)
    return resp


def getReviews(tweet, personality1, personality2, personality3, personality4, personality5, count1, count2, count3,count4, count5):

    responses = []
    # dynamic content wasn't working so i had to hack this
    for i in range(int(count1)):
        responses.append(getReview(tweet, personality1))
    for i in range(int(count2)):
        responses.append(getReview(tweet, personality2))
    for i in range(int(count3)):
        responses.append(getReview(tweet, personality3))
    for i in range(int(count4)):
        responses.append(getReview(tweet, personality4))
    for i in range(int(count5)):
        responses.append(getReview(tweet, personality5))
    
    return "\n".join(responses)
with gr.Blocks() as demo:

    # dynamic content wasn't working so i had to implement this.
    with gr.Row():
        personality1 = gr.Textbox(label="Personality 1")
        count1 = gr.Number(label="Count 1")
    
    with gr.Row():
        personality2 = gr.Textbox(label="Personality 2")
        count2 = gr.Number(label="Count 2")
    with gr.Row():
        personality3 = gr.Textbox(label="Personality 3")
        count3 = gr.Number(label="Count 3")
    with gr.Row():
        personality4 = gr.Textbox(label="Personality 4")
        count4 = gr.Number(label="Count 4")
    with gr.Row():
        personality5 = gr.Textbox(label="Personality 5")
        count5 = gr.Number(label="Count 5")

    personalities = [personality1, personality2, personality3, personality4, personality5]
    counts = [count1, count2, count3, count4, count5]


    tweet = gr.Textbox(label="Tweet to Review")

    submit_btn = gr.Button("Get Responses")
    output = gr.Textbox(label="Responses Output")

    submit_btn.click(getReviews, inputs=[tweet] + personalities + counts, outputs=output)

if __name__ == "__main__":
    demo.launch()
