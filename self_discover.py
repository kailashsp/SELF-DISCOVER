from prompts import(
    select_prompt,
    reasoning_modules,
    adapt_prompt,
    implement_prompt
)
from llm import LLM
from task_example import task1

class SelfDiscover:
    def __init__(self, task) -> None:
        self.llm = LLM(model_name="gemini-pro")
        self.actions = ["SELECT", "ADAPT", "IMPLEMENT"]
        self.task = task

    def __call__(self):
        for action in self.actions:
            print(action)
            if action == "SELECT":
                print("yes")
                prompt = select_prompt.replace("{Task}",self.task)
                prompt = prompt.replace("{resonining_modules}", reasoning_modules)
                print(prompt)
                self.selected_modules = self.llm(prompt)

            elif action == "ADAPT":
                prompt = adapt_prompt.replace("{Task}",self.task)
                prompt = prompt.replace("{selected_modules}",self.selected_modules)
                print(prompt)
                self.adapted_modules = self.llm(prompt)

            elif action == "IMPLEMENT":
                prompt = implement_prompt.replace("{Task}",self.task)
                prompt = prompt.replace("{adapted_modules}", self.adapted_modules)
                print(prompt)
                self.reasoning_structure = self.llm(prompt)


if __name__=="__main__":
    result = SelfDiscover(task=task1)
    result()
    print(f"SELECTED_MODULES : {result.selected_modules}")
    print(f"ADAPTED_MODULES : {result.adapted_modules}")
    print(f"REASONING_STRUCTURE : {result.reasoning_structure}")