import gradio as gr
from app.agents.promptReviewAgent import promptReviewAgent, TweetReaction
import json
import matplotlib.pyplot as plt
import pandas as pd

agent = promptReviewAgent()

responses = {}

def getReview(tweet, personality):
    agent.switch_personality(personality)
    resp = agent.review_content(tweet)
    return resp


def getReviews(tweet, personality1, personality2, personality3, personality4, personality5, count1, count2, count3,count4, count5):

    responses.clear()
    # dynamic content wasn't working so i had to hack this
    responses[personality1] = []
    responses[personality2] = []
    responses[personality3] = []
    responses[personality4] = []
    responses[personality5] = []
    
    for i in range(count1):
        review = getReview(tweet, personality1)
        responses[personality1].append(review)
    for i in range(count2):
        review = getReview(tweet, personality2)
        responses[personality2].append(review)
    for i in range((count3)):
        
        responses[personality3].append(getReview(tweet, personality3))
    for i in range((count4)):
        responses[personality4].append(getReview(tweet, personality4))
    for i in range((count5)):
        
        responses[personality5].append(getReview(tweet, personality5))
    #print(responses)
    return responses


with gr.Blocks() as demo:
    # analysis
    with gr.Row():
        
        # input
        with gr.Column():
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
            output_text = gr.Textbox(label="Responses Output")

            submit_btn.click(getReviews, inputs=[tweet] + personalities + counts, outputs=output_text)
        @gr.render(inputs=output_text)
        def renderStats(text):

            if (type(text) != str or len(str(text)) == 0):
                return
            
            dict = eval(text)
            print(dict)

            plotData = {}
            for key, val in dict.items():
                if (key not in plotData):
                    plotData[key] = 0
                for value in val:
                    if (value.reaction == "like"):
                        plotData[key] += 1
            print(plotData)
            
            df = pd.DataFrame.from_dict(plotData, orient='index', columns=['Count'])
            df.reset_index(inplace=True)
            df.rename(columns={'index': 'Personality'}, inplace=True)
            print(df)


            with gr.Column():
                gr.Markdown("Plot goes here")
                print(plotData)
                gr.BarPlot(
                    value=df,
                    x='Personality',
                    y='Count',
                    title='Personality Counts',
                    x_title='Personality',
                    y_title='Count',
                )
                # post reviews
                with gr.Column():
                    gr.Markdown("Reviews go here")
                    
                    for key, list in dict.items():
                        for value in list:
                            gr.Markdown(key + ": " + value.reasoning)
                    


if __name__ == "__main__":
    demo.launch()
