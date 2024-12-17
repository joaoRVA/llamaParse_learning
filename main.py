import os

os.environ["LLAMA_CLOUD_API_KEY"] = "llx-9LXIRUUgheVVd29M2RBSdGsH2v6COsDfUvPXUWmXOMZKLRDS"

from llama_parse import LlamaParse

documentos = LlamaParse(result_type="markdown", 
                        parsing_instruction="this file have text and some tables. I'd like to get only the tables.").load_data("petrobras.pdf")

# print(len(documentos))

for i, pagina in enumerate(documentos):
    with open(f"paginas_pdf/pagina{i+1}.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(pagina.text)