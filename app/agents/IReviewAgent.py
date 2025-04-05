from abc import ABC, abstractmethod
from enum import Enum

class ReviewResponses(Enum):
    IGNORE = 1
    LIKE = 2
    SHARE = 3

class IReviewAgent(ABC):
    
    @abstractmethod
    def switch_personality(self, content: str):
        pass
    
    @abstractmethod
    def review_content(self, content: str):
        pass

    
