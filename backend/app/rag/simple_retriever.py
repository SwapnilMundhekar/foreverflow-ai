import os
import re
from typing import Any, Dict, List


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


POLICY_FILES = [
    'data/policies/brand_voice_guide.md',
    'data/policies/return_policy.md',
    'data/policies/size_guide.md',
    'data/policies/campaign_brief.md'
]


def normalise_text(text: str) -> str:
    return re.sub(r'[^a-zA-Z0-9 ]+', ' ', text.lower())


def tokenize(text: str) -> List[str]:
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'to', 'of', 'in', 'on', 'for', 'with',
        'is', 'are', 'be', 'can', 'should', 'this', 'that', 'it', 'as', 'by'
    }
    words = normalise_text(text).split()
    return [word for word in words if word not in stop_words and len(word) > 2]


def read_policy_file(relative_path: str) -> str:
    file_path = os.path.join(BASE_DIR, relative_path)

    if not os.path.exists(file_path):
        return ''

    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def split_into_chunks(text: str, max_words: int = 55) -> List[str]:
    clean_text = text.replace('\n', ' ').strip()
    words = clean_text.split()
    chunks = []

    for index in range(0, len(words), max_words):
        chunk = ' '.join(words[index:index + max_words]).strip()

        if chunk:
            chunks.append(chunk)

    return chunks


def score_chunk(question_tokens: List[str], chunk: str) -> int:
    chunk_tokens = set(tokenize(chunk))
    score = 0

    for token in question_tokens:
        if token in chunk_tokens:
            score += 1

    return score


def retrieve_policy_evidence(question: str, top_k: int = 4) -> List[Dict[str, Any]]:
    question_tokens = tokenize(question)
    scored_chunks = []

    for relative_path in POLICY_FILES:
        text = read_policy_file(relative_path)
        chunks = split_into_chunks(text)

        for chunk in chunks:
            score = score_chunk(question_tokens, chunk)

            scored_chunks.append(
                {
                    'source': os.path.basename(relative_path),
                    'evidence': chunk,
                    'score': score
                }
            )

    scored_chunks.sort(key=lambda item: item['score'], reverse=True)
    useful_chunks = [item for item in scored_chunks if item['score'] > 0]

    if useful_chunks:
        return useful_chunks[:top_k]

    return scored_chunks[:top_k]


def build_grounded_answer(question: str, evidence_items: List[Dict[str, Any]]) -> str:
    if not evidence_items:
        return 'No relevant policy evidence was found.'

    best_sources = ', '.join(sorted(set(item['source'] for item in evidence_items)))

    return 'Relevant policy evidence was retrieved from ' + best_sources + '. Review the evidence snippets before taking action.'
