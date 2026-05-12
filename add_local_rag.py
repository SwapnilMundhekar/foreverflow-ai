import os

BASE_DIR = os.getcwd()
RAG_DIR = os.path.join(BASE_DIR, "backend", "app", "rag")
RAG_PATH = os.path.join(RAG_DIR, "simple_retriever.py")
MAIN_PATH = os.path.join(BASE_DIR, "backend", "app", "main.py")

os.makedirs(RAG_DIR, exist_ok=True)

rag_lines = [
    "import os",
    "import re",
    "from typing import Any, Dict, List",
    "",
    "",
    "BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))",
    "",
    "",
    "POLICY_FILES = [",
    "    'data/policies/brand_voice_guide.md',",
    "    'data/policies/return_policy.md',",
    "    'data/policies/size_guide.md',",
    "    'data/policies/campaign_brief.md'",
    "]",
    "",
    "",
    "def normalise_text(text: str) -> str:",
    "    return re.sub(r'[^a-zA-Z0-9 ]+', ' ', text.lower())",
    "",
    "",
    "def tokenize(text: str) -> List[str]:",
    "    stop_words = {",
    "        'the', 'a', 'an', 'and', 'or', 'to', 'of', 'in', 'on', 'for', 'with',",
    "        'is', 'are', 'be', 'can', 'should', 'this', 'that', 'it', 'as', 'by'",
    "    }",
    "    words = normalise_text(text).split()",
    "    return [word for word in words if word not in stop_words and len(word) > 2]",
    "",
    "",
    "def read_policy_file(relative_path: str) -> str:",
    "    file_path = os.path.join(BASE_DIR, relative_path)",
    "",
    "    if not os.path.exists(file_path):",
    "        return ''",
    "",
    "    with open(file_path, 'r', encoding='utf-8') as file:",
    "        return file.read()",
    "",
    "",
    "def split_into_chunks(text: str, max_words: int = 55) -> List[str]:",
    "    clean_text = text.replace('\\n', ' ').strip()",
    "    words = clean_text.split()",
    "    chunks = []",
    "",
    "    for index in range(0, len(words), max_words):",
    "        chunk = ' '.join(words[index:index + max_words]).strip()",
    "",
    "        if chunk:",
    "            chunks.append(chunk)",
    "",
    "    return chunks",
    "",
    "",
    "def score_chunk(question_tokens: List[str], chunk: str) -> int:",
    "    chunk_tokens = set(tokenize(chunk))",
    "    score = 0",
    "",
    "    for token in question_tokens:",
    "        if token in chunk_tokens:",
    "            score += 1",
    "",
    "    return score",
    "",
    "",
    "def retrieve_policy_evidence(question: str, top_k: int = 4) -> List[Dict[str, Any]]:",
    "    question_tokens = tokenize(question)",
    "    scored_chunks = []",
    "",
    "    for relative_path in POLICY_FILES:",
    "        text = read_policy_file(relative_path)",
    "        chunks = split_into_chunks(text)",
    "",
    "        for chunk in chunks:",
    "            score = score_chunk(question_tokens, chunk)",
    "",
    "            scored_chunks.append(",
    "                {",
    "                    'source': os.path.basename(relative_path),",
    "                    'evidence': chunk,",
    "                    'score': score",
    "                }",
    "            )",
    "",
    "    scored_chunks.sort(key=lambda item: item['score'], reverse=True)",
    "    useful_chunks = [item for item in scored_chunks if item['score'] > 0]",
    "",
    "    if useful_chunks:",
    "        return useful_chunks[:top_k]",
    "",
    "    return scored_chunks[:top_k]",
    "",
    "",
    "def build_grounded_answer(question: str, evidence_items: List[Dict[str, Any]]) -> str:",
    "    if not evidence_items:",
    "        return 'No relevant policy evidence was found.'",
    "",
    "    best_sources = ', '.join(sorted(set(item['source'] for item in evidence_items)))",
    "",
    "    return 'Relevant policy evidence was retrieved from ' + best_sources + '. Review the evidence snippets before taking action.'",
    ""
]

with open(RAG_PATH, "w", encoding="utf-8") as file:
    file.write("\n".join(rag_lines))

with open(MAIN_PATH, "r", encoding="utf-8") as file:
    main_code = file.read()

if "from .rag.simple_retriever import build_grounded_answer, retrieve_policy_evidence" not in main_code:
    main_code = main_code.replace(
        "from pydantic import BaseModel",
        "from pydantic import BaseModel\nfrom .rag.simple_retriever import build_grounded_answer, retrieve_policy_evidence"
    )

if "class AskPolicyRequest(BaseModel):" not in main_code:
    insert_text = [
        "",
        "",
        "class AskPolicyRequest(BaseModel):",
        "    question: str",
        "    top_k: int = 4",
        ""
    ]
    marker = "class ReadinessRequest(BaseModel):"
    main_code = main_code.replace(marker, "\n".join(insert_text) + "\n" + marker)

old_function_start = "def build_rag_evidence() -> List[Dict[str, str]]:"
old_function_end = "@app.get(\"/\")"

if old_function_start in main_code and old_function_end in main_code:
    start_index = main_code.index(old_function_start)
    end_index = main_code.index(old_function_end)
    new_function = [
        "def build_rag_evidence() -> List[Dict[str, Any]]:",
        "    question = \"What policies matter before promoting a fashion product with content gaps, return risk, or low stock?\"",
        "    return retrieve_policy_evidence(question, top_k=4)",
        "",
        "",
    ]
    main_code = main_code[:start_index] + "\n".join(new_function) + main_code[end_index:]

if "@app.post(\"/ask-policy\")" not in main_code:
    endpoint_lines = [
        "",
        "",
        "@app.post(\"/ask-policy\")",
        "def ask_policy(request: AskPolicyRequest) -> Dict[str, Any]:",
        "    evidence = retrieve_policy_evidence(request.question, request.top_k)",
        "    answer = build_grounded_answer(request.question, evidence)",
        "",
        "    return {",
        "        \"question\": request.question,",
        "        \"answer\": answer,",
        "        \"evidence\": evidence",
        "    }",
        ""
    ]
    main_code = main_code + "\n".join(endpoint_lines)

with open(MAIN_PATH, "w", encoding="utf-8") as file:
    file.write(main_code)

print("Local RAG retriever added successfully.")
print("Created:", RAG_PATH)
print("Updated:", MAIN_PATH)
print("New endpoint: POST /ask-policy")