# Langchain Metadata Extraction - Ollama Template

This project provides a solution for extracting metadata from text-based invoice files using Langchain, structured LLMs, and metadata templates. The `Langchain_Metadata_Extraction_OllamaTemplate` leverages the Langchain framework to extract and organize key invoice data such as company names, addresses, total amounts, and more, based on a customizable template.

## Features

- **Metadata Extraction from Invoices:** Extracts essential invoice data such as company names, addresses, and total amounts.
- **Structured LLM Output:** Utilizes a structured language model (LLM) with custom invoice templates.
- **JSON Serialization:** Outputs extracted metadata in JSON format using a custom encoder.
- **Prompt Chaining:** Processes the invoice text with a prompt template and LLM to retrieve metadata.
  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/langchain-metadata-extraction-ollamatemplate.git
   cd langchain-metadata-extraction-ollamatemplate
   ```

2. Install dependencies:
   ```bash
   pip install langchain-core langchain-experimental pydantic json
   ```

3. Ensure that the Ollama LLM model (e.g., `llama3`) is available for use.

## Usage

### Metadata Extraction from Invoice Files

The `metadata_extraction` function extracts structured data from an invoice text file, processes it with the language model, and saves the output.

```python
from langchain_metadata_extractor import metadata_extraction

# Call the metadata extraction function
metadata_extraction(r"C:\Users\kalin\Desktop\InvoicePoi\data\newocr.com-20240615175222.txt")
```

### Output Format

The metadata is saved in `output.txt` in a structured format:
- JSON-encoded metadata based on the provided template.
- Extracted invoice text appended for reference.

### Example Output

```json
{
    "company_names": ["Company A", "Company B"],
    "company_addresses": ["123 Street, City", "456 Avenue, City"],
    "contact_information": ["email@company.com", "phone: 123-456"],
    "total_amount": 1234.56,
    "items": [
        {"item_name": "Service A", "quantity": 1, "price": 500.00},
        {"item_name": "Product B", "quantity": 3, "price": 245.00}
    ],
    "customer_name": "John Doe",
    "invoice_number": "INV-20240615",
    "invoice_date": "2024-06-15",
    "additional_information": ["Payment due in 30 days", "Thank you for your business"]
}
```

### How It Works

1. **Prompt Template Generation:** The function reads the invoice file and constructs a prompt template using `Langchain`.
   
2. **Structured Output Model:** The extracted data is passed to the `OllamaFunctions` model (e.g., `llama3`) to generate structured metadata.

3. **Chaining Execution:** The `PromptTemplate` is combined with the structured LLM to invoke the extraction, and the metadata is serialized to a JSON file.

### Customization

- Modify the invoice template model by adjusting the `Invoice` class to include or exclude fields based on your needs.
- Customize the prompt used for metadata extraction by changing the text in the template file.

## Project Structure

- `metadata_extraction()`: Main function that extracts metadata from invoices.
- `Invoice`: Model representing the structure of the extracted invoice data.
- `InvoiceEncoder`: Custom JSON encoder for serializing the invoice metadata.
- `prompt_template`: Reads and formats the prompt for metadata extraction.

## Requirements

- Python 3.8+
- [Langchain](https://langchain.com/)
- [Pydantic](https://docs.pydantic.dev/)
- Ollama LLM (e.g., `llama3`)

## License

This project is licensed under the MIT License.

## Acknowledgements

Thanks to the contributors of the [Langchain](https://langchain.com/) and [Pydantic](https://docs.pydantic.dev/) frameworks for providing the tools necessary for building this project.
