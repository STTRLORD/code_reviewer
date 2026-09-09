from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq
load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")



class CodeExplanation(BaseModel):
    language: str = Field(description="Detected programming language")
    explanation: str = Field(description="What the code does, in simple terms")
    time_complexity: str = Field(description="Big-O time complexity of the code, e.g. O(n), O(n^2)")
    space_complexity: str = Field(description="Big-O space complexity of the code")
    issues: List[str] = Field(description="Potential bugs, errors, or problems found in the code")
    improvements: List[str] = Field(description="Suggestions to improve code quality, performance, or readability")
    optimized_code: str = Field(description="An optimized/improved version of the given code, following the suggestions")
    
parser = PydanticOutputParser(pydantic_object=CodeExplanation)




prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert code reviewer and software engineer.

Your task is to analyze the given code carefully and provide a structured review.

Instructions:
- Detect the programming language.
- Explain what the code does in simple, clear terms.
- Analyze the time complexity (Big-O) of the code.
- Analyze the space complexity (Big-O) of the code.
- List genuine issues, bugs, or problems in the code (leave empty if none).
- List improvements — optimization, readability, or best-practice suggestions (leave empty if none).

Do not assume functionality that isn't present in the code.

{format_instructions}"""),

    ("human", "Code:\n{code}")
])

code = input("drop the code here->")

final_prompt = prompt.invoke(
    {"code" : code,
     'format_instructions': parser.get_format_instructions()
     }
)



response = model.invoke(final_prompt)
code_data = parser.parse(response.content)

print(code_data)

