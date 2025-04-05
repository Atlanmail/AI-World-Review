from langchain_core.prompts import PromptTemplate
from app.agents.IReviewAgent import IReviewAgent, ReviewResponses
from app.utils.llm import llm;

'''
Review agent that sets its personality based on a prompt.
'''
class promptReviewAgent():
    def __init__(self):
        prompt_template = (
            "You are a reviewer that mimics a user's preferences on Twitter described as the following: {profile_context}."
            "Given the tweet below, "
            "determine if the user would 'ignore', 'like' or 'share' this tweet. "
            "Only output one of these three options.\n"
            "Tweet: {tweet_text}"
        )
        self.template = PromptTemplate.from_template(prompt_template)
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
        response = self.llm.invoke(prompt)
        return response.content
    
   