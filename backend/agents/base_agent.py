from abc import ABC, abstractmethod
import openai
from typing import Dict, Any

class BaseAgent(ABC):
    def __init__(self):
        self.client = openai.OpenAI()
    
    @abstractmethod
    async def process(self, question: str, context: Dict[str, Any]) -> Dict:
        pass
    
    def get_embedding(self, text: str) -> List[float]:
        response = self.client.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        return response.data[0].embedding
