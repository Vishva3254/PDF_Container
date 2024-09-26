import fitz
from langchain_community.llms import Ollama

# Initialize the LLM model
llm = Ollama(model="llama3")

def llama3(text, query):
    prompt = f"Based on the following query, provide a summary: '{query}'. Here is the text: {text}"
    result = llm.invoke(prompt)
    return result

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Function to get summary based on user query
def get_summary(text, query):
    summary = llama3(text, query)
    return summary

# Main execution
if __name__ == "__main__":
    pdf_path = ""
    text = extract_text_from_pdf(pdf_path)

    print("Enter your query for the summary (e.g., 'summary of page 2', 'summary of paragraph 3', 'summary of the whole PDF'):")
    user_query = input().strip()

    summary = get_summary(text, user_query)
    print("Summary based on your query:")
    print(summary)