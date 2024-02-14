from prompts import(
    select_prompt,
    reasoning_modules,
    adapt_prompt,
    implement_prompt
)

from llm import LLM
from task_example import task1

import logging

def setup_logging():
    logger = logging.getLogger("__name__")
    logger.setLevel(logging.INFO)
        
    handler = logging.FileHandler("prompt_log.txt")
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

logger = setup_logging()

class SelfDiscover:
    def __init__(self, task) -> None:
        self.llm = LLM(model_name="OpenAI")
        self.actions = ["SELECT", "ADAPT", "IMPLEMENT"]
        self.task = task

    def __call__(self):
        for action in self.actions:
            print(action)
            if action == "SELECT":
                prompt = select_prompt.replace("{Task}",self.task)
                prompt = prompt.replace("{resonining_modules}", reasoning_modules)
                logger.info("SELECT PROMPT :" + prompt)
                self.selected_modules = self.llm(prompt)
                print(self.selected_modules)

            elif action == "ADAPT":
                prompt = adapt_prompt.replace("{Task}",self.task)
                prompt = prompt.replace("{selected_modules}",self.selected_modules)
                logger.info("ADAPT PROMPT :" + prompt)
                self.adapted_modules = self.llm(prompt)

            elif action == "IMPLEMENT":
                prompt = implement_prompt.replace("{Task}",self.task)
                prompt = prompt.replace("{adapted_modules}", self.adapted_modules)
                logger.info("IMPLEMENT PROMPT:" + prompt)
                self.reasoning_structure = self.llm(prompt)


if __name__=="__main__":
    result = SelfDiscover(task=task1)
    result()
    logger.info(f"SELECTED_MODULES : {result.selected_modules}")
    logger.info(f"ADAPTED_MODULES : {result.adapted_modules}")
    logger.info(f"REASONING_STRUCTURE : {result.reasoning_structure}")