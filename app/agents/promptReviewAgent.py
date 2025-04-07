from langchain_core.prompts import PromptTemplate
from app.agents.IReviewAgent import IReviewAgent, ReviewResponses
from app.utils.llm import llm;
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field


import json

class TweetReaction(BaseModel):
    reaction: str = Field(description="Whether the user would ignore, like or share the tweet")
    reasoning: str = Field(description="reasoning why it was rated")

    
    def __str__(self):
        return f"TweetReaction(reaction='{self.reaction}', reasoning='{self.reasoning}')"

'''
Review agent that sets its personality based on a prompt.
'''
class promptReviewAgent():
    def __init__(self):
        
        parser = JsonOutputParser(pydantic_object=TweetReaction)
        self.template = PromptTemplate(
            template = "You are a reviewer that mimics a user's preferences on Twitter described as the following: {profile_context}.\n"
            "Given the tweet below, determine if the user would 'ignore', 'like', or 'share' this tweet.\n"
            "Tweet: {tweet_text}",

            input_variables=["tweet_text", "profile_context"],
        )
        self.llm = llm
        self.profile_context = "You are an ordinary user with no specific traits."
    
    '''
    Sets the personality to the prompt given
    '''
    def switch_personality(self, content:str):
        self.profile_context = content

    def review_content(self, content: str):
        """
        Reviews a single tweet and returns the simulated user reaction.
        
        Args:
            tweet_text (str): The text of the tweet to review.
        
        Returns:
            str: The agent's output reaction ("like", "dislike", or "share").
        """
        # Convert user_profile to a string for context. This can include like/dislike history, interests, etc.
        prompt = self.template.invoke({"tweet_text": content, "profile_context": self.profile_context})
        response = self.llm.with_structured_output(TweetReaction).invoke(prompt)
        return response
    
   