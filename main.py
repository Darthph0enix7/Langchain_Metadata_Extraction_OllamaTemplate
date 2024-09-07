rom langchain_core.prompts import PromptTemplate from langchain_core.pydantic_v1 import BaseModel, Field from langchain_experimental.llms.ollama_functions import OllamaFunctions import json from typing import Optional

class Invoice(BaseModel): company_names: list = Field(description="List of names of the companies involved", required=True) company_addresses: list = Field(default=[], description="List of addresses for the companies involved", required=False) contact_information: list = Field(default=[], description="List of contact information for all parties involved", required=False) total_amount: float = Field(description="The total amount to be paid", required=True) items: list = Field(description="List of items or services provided", required=True) customer_name: str = Field(description="The name of the customer", required=True) invoice_number: str = Field(description="The invoice number", required=True) invoice_date: str = Field(description="The date the invoice was issued", required=True) additional_information: list = Field(default=[], description="Describe the contents and the Typ of this Invoice shortly and the involved", required=False)

class InvoiceEncoder(json.JSONEncoder): def default(self, obj): if isinstance(obj, Invoice): # Convert the Invoice object to a dictionary here return obj.dict # Let the base class default method raise the TypeError return json.JSONEncoder.default(self, obj)

def metadata_extraction(file_path): def format_prompt_from_file(file_path): with open(file_path, 'r', encoding='utf-8') as file: prompt_text = file.read() return PromptTemplate.from_template(f"""{prompt_text}

Human: {{question}} AI: """), prompt_text

prompt_template, original_text = format_prompt_from_file(file_path)

llm = OllamaFunctions(model="llama3", format="json", temperature=0)
structured_llm = llm.with_structured_output(Invoice)

# Use the PromptTemplate object in the chain
chain = prompt_template | structured_llm

output = chain.invoke("Describe")

with open('output.txt', 'w') as text_file:
    # Use the custom encoder for the Invoice object
    formatted_output = json.dumps(output, indent=4, cls=InvoiceEncoder)
    text_file.write(formatted_output)
    # Append the original text extracted from the file at the end
    text_file.write("\n\nExtracted Text:\n")
    text_file.write(original_text)

print("Output saved to output.txt")
