from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:3b", temperature=0.7)


def generate(cuisine: str) -> dict:
    name_prompt = PromptTemplate.from_template(
        "I want to open a restaurant for {cuisine} food. "
        "Suggest ONE fancy name for this. Reply with ONLY the name."
    )

    items_prompt = PromptTemplate.from_template(
        "Suggest some menu items for {restaurant_name}. "
        "Return it as a comma-separated string."
    )

    name_chain = name_prompt | llm | StrOutputParser()
    items_chain = items_prompt | llm | StrOutputParser()

    full_chain = RunnablePassthrough.assign(
        restaurant_name=name_chain
    ).assign(
        menu_items=items_chain
    )

    result = full_chain.invoke({"cuisine": cuisine})

    return {
        "restaurant_name": result["restaurant_name"].strip(),
        "menu_items": result["menu_items"].strip(),
    }