## SELF-DISCOVER FRAMEWORK

## Paper Overview [link](https://arxiv.org/pdf/2402.03620.pdf)
This project implements the paper titled "Self-Discover: Large Language Models Self-Compose Reasoning Structures," submitted on February 6, 2024, by Pei Zhou, Jay Pujara, Xiang Ren, Xinyun Chen, Heng-Tze Cheng, Quoc V. Le, Ed H. Chi, Denny Zhou, Swaroop Mishra, and Huaixiu Steven Zheng. The paper introduces SELF-DISCOVER, a framework designed to enhance the performance of Large Language Models (LLMs) on complex reasoning tasks by enabling them to self-discover task-intrinsic reasoning structures.


## Functionality (as given in paper)
- **Self-Discovery Process:** The system engages in a self-discovery process where it selects atomic reasoning modules and composes them into an explicit reasoning structure.
- **Performance Improvement:** SELF-DISCOVER significantly enhances the performance of LLMs on challenging reasoning benchmarks such as BigBench-Hard, grounded agent reasoning, and MATH, achieving up to a 32% improvement compared to conventional prompting methods like Chain of Thought (CoT).
- **Efficiency:** Despite its effectiveness, SELF-DISCOVER requires 10-40 times fewer inference computations compared to inference-intensive methods like CoT-Self-Consistency.
- **Universality:** The self-discovered reasoning structures are found to be universally applicable across different LLM model families, indicating commonalities with human reasoning patterns.



##  Project Overview

This project consists of a Python script (`self_discover.py`) along with associated modules and prompts. It allows users to input a specific task, and then it guides them through the process of selecting, adapting, and implementing reasoning modules to tackle that task effectively.

## Implementation Details

- **Model Used:** The implementation  Large Language Model (LLM) "gemini-pro" or "gpt-3.5-turbo"
- **Tasks:** The system is capable of handling various task to generate reasoning structure
- **Actions:** The system performs three main actions: SELECT, ADAPT, and IMPLEMENT.
  - **SELECT:** This action involves selecting several reasoning modules crucial for solving the given task.
  - **ADAPT:** The selected reasoning modules are rephrased and specified to better suit the task at hand.
  - **IMPLEMENT:** The reasoning modules are operationalized into a step-by-step reasoning plan in JSON format, providing a structured approach for solving the task.


## Prerequisites

- Python 3.10
- Libraries: google-generativeai, openai, dotenv
- Input the task you want to generate a reasoning structure in task_example.py

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/kailashsp/SelfDiscover.git
   ```

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```
3. create a .env file

4. Open the `.env` file in a text editor.

5. Add the following line to the `.env` file:

   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

   Replace `your_google_api_key_here` with your actual Google API key obtained from [google makersuite](https://makersuite.google.com/app/apikey).
   Your can also use OPENAI_API_KEY as well


## Usage

1. Initialize a `SelfDiscover` object with a task:
    
   ```python
   from self_disover import SelfDiscover
   from task_example import task1

   result = SelfDiscover(task=task1)
   ```

2. Call the `SelfDiscover` object:

   ```python
   result()
   ```

3. Access the selected and adapted modules also implemented reasoning structure:

   ```python
   print(f"SELECTED_MODULES : {result.selected_modules}")
   print(f"ADAPTED_MODULES : {result.adapted_modules}")
   print(f"REASONING_STRUCTURE : {result.reasoning_structure}")
   ```

## Customization

- Modify the `reasoning_modules` variable in `prompts.py` to add, remove, or modify reasoning modules.
- Adjust the prompts in `prompts.py` to customize the user interaction flow.

## How to use the reasoning JSON structure

- As mentioned in the paper 
```markdown
For Stage 2, where we use the self-discovered structure to solve the task instances, we start with the prompt: “Follow the
step-by-step reasoning plan in JSON to correctly solve the task. Fill in the values following the keys by reasoning specifically 
about the task given. Do not simply rephrase the keys.”, followed by the reasoning structure, and finally the task instance.
```
You can now give the task with the reasoning structure with the above prompt

## Contributing

Contributions are welcome! Feel free to open issues or pull requests with any improvements or suggestions.

---

