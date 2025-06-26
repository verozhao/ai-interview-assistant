import openai
from typing import Dict, List
from .base_agent import BaseAgent

class CodingAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.patterns = {
            "array": {
                "techniques": ["two pointers", "sliding window", "kadane"],
                "complexity": ["O(n)", "O(n^2)", "O(nlogn)"]
            },
            "dynamic_programming": {
                "techniques": ["memoization", "tabulation", "space optimization"],
                "complexity": ["O(n)", "O(n^2)", "O(2^n) -> O(n)"]
            },
            "graph": {
                "techniques": ["DFS", "BFS", "Dijkstra", "Union Find"],
                "complexity": ["O(V+E)", "O(V^2)", "O(ElogV)"]
            }
        }
    
    async def process(self, question: str, context: Dict[str, Any]) -> Dict:
        # Identify pattern
        pattern = await self.identify_pattern(question)
        
        # Generate multiple approaches
        approaches = await self.generate_approaches(question, pattern)
        
        # Optimize for company
        company_specific = self.optimize_for_company(
            approaches, 
            context.get("company")
        )
        
        return {
            "pattern": pattern,
            "approaches": approaches,
            "recommended": company_specific,
            "implementation": await self.generate_code(company_specific),
            "tests": self.generate_test_cases(question)
        }
    
    async def identify_pattern(self, question: str) -> str:
        prompt = f"""
        Identify the coding pattern for this problem:
        {question}
        
        Patterns: {list(self.patterns.keys())}
        Return only the pattern name.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content.strip()
