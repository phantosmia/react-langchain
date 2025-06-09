from langchain.callbacks.base import BaseCallbackHandler
from typing import Dict, Any, List
from langchain.schema import LLMResult

class AgentCallbackHandler(BaseCallbackHandler):
    """
    Custom callback handler for the agent.
    """

    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> None:
        """
        Called when the LLM starts.
        """
        print(f"***Prompt to LLM was: {prompts[0]}")
        print("***********")
    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """
        Called when the LLM ends.
        """
        print(f"***Prompt to LLM was: {response.generations[0][0].text}")
        print("***********") 