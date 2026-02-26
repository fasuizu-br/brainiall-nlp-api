"""
Brainiall NLP API — Python Examples

Base URL: https://apim-ai-apis.azure-api.net/v1/nlp
Get your API key at https://brainiall.com
"""

import requests
import json
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://apim-ai-apis.azure-api.net/v1/nlp"
HEADERS = {
    "Authorization": "Bearer YOUR_KEY",  # Replace with your API key
    "Content-Type": "application/json"
}


def toxicity_detection():
    """Detect toxic content across 6 categories."""
    texts = [
        "You are such a wonderful person!",
        "I hate everything about this terrible product",
        "The weather is nice today"
    ]

    for text in texts:
        response = requests.post(
            f"{BASE_URL}/toxicity",
            headers=HEADERS,
            json={"text": text}
        )
        result = response.json()
        status = "TOXIC" if result["is_toxic"] else "SAFE"
        print(f"[{status}] {text}")
        print(f"  Max: {result['max_category']} = {result['max_score']:.4f}")


def sentiment_analysis():
    """Classify text sentiment as positive or negative."""
    reviews = [
        "Absolutely love this! Best purchase I've ever made.",
        "Terrible quality. Completely disappointed.",
        "It's okay, nothing special but gets the job done.",
        "Amazing customer support, they went above and beyond!",
        "Would not recommend to anyone. Total waste of money."
    ]

    for review in reviews:
        response = requests.post(
            f"{BASE_URL}/sentiment",
            headers=HEADERS,
            json={"text": review}
        )
        result = response.json()
        icon = "+" if result["sentiment"] == "positive" else "-"
        print(f"[{icon} {result['confidence']:.3f}] {review}")


def named_entity_recognition():
    """Extract named entities: persons, organizations, locations."""
    text = "Satya Nadella, CEO of Microsoft, met with Tim Cook from Apple at their office in Cupertino, California."

    response = requests.post(
        f"{BASE_URL}/entities",
        headers=HEADERS,
        json={"text": text}
    )
    result = response.json()

    print(f"Text: {text}")
    print(f"Entities found: {result['entity_count']}")
    for entity in result["entities"]:
        print(f"  [{entity['label']:4s}] {entity['text']} (confidence: {entity['score']:.4f})")


def pii_detection():
    """Detect personally identifiable information."""
    text = "Please send the invoice to alice@company.com or call her at 555-867-5309. Her SSN is 078-05-1120."

    response = requests.post(
        f"{BASE_URL}/pii",
        headers=HEADERS,
        json={"text": text}
    )
    result = response.json()

    print(f"Text: {text}")
    print(f"PII found: {result['pii_found']} ({result['pii_count']} items)")
    for entity in result["entities"]:
        print(f"  [{entity['type']:11s}] {entity['value']}")


def language_detection():
    """Detect language from 217 supported languages."""
    texts = [
        "Hello, how are you doing today?",
        "Bonjour, comment allez-vous aujourd'hui?",
        "Hallo, wie geht es Ihnen heute?",
        "Hola, como estas hoy?",
        "Ciao, come stai oggi?",
        "Olá, como você está hoje?",
        "Привет, как дела сегодня?",
        "こんにちは、今日はお元気ですか？",
        "안녕하세요, 오늘 어떠세요?",
        "مرحبا، كيف حالك اليوم؟"
    ]

    for text in texts:
        response = requests.post(
            f"{BASE_URL}/language",
            headers=HEADERS,
            json={"text": text}
        )
        result = response.json()
        print(f"[{result['language']:3s} {result['confidence']:.3f}] {text[:50]}")


def full_analysis_pipeline():
    """Run all NLP analyses on a single text."""
    text = "John Smith from Amazon in Seattle emailed john@amazon.com — this new AI product is incredible!"

    endpoints = ["toxicity", "sentiment", "entities", "pii", "language"]
    results = {}

    for endpoint in endpoints:
        response = requests.post(
            f"{BASE_URL}/{endpoint}",
            headers=HEADERS,
            json={"text": text}
        )
        results[endpoint] = response.json()

    print(f"=== Full Analysis ===")
    print(f"Text: {text}")
    print(f"Language: {results['language']['language']} ({results['language']['confidence']:.4f})")
    print(f"Sentiment: {results['sentiment']['sentiment']} ({results['sentiment']['confidence']:.4f})")
    print(f"Toxic: {results['toxicity']['is_toxic']} (max: {results['toxicity']['max_score']:.4f})")
    print(f"Entities ({results['entities']['entity_count']}):")
    for e in results['entities']['entities']:
        print(f"  [{e['label']}] {e['text']}")
    print(f"PII ({results['pii']['pii_count']}):")
    for p in results['pii']['entities']:
        print(f"  [{p['type']}] {p['value']}")


def batch_processing():
    """Process multiple texts in parallel."""
    texts = [f"Review {i}: {'Great' if i % 2 == 0 else 'Terrible'} product!" for i in range(20)]

    def analyze(text):
        resp = requests.post(f"{BASE_URL}/sentiment", headers=HEADERS, json={"text": text})
        return resp.json()

    import time
    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as pool:
        results = list(pool.map(analyze, texts))
    elapsed = time.time() - start

    positive = sum(1 for r in results if r["sentiment"] == "positive")
    print(f"Processed {len(texts)} texts in {elapsed:.2f}s")
    print(f"Positive: {positive}, Negative: {len(texts) - positive}")


def content_moderation():
    """Content moderation pipeline combining toxicity + PII checks."""
    messages = [
        "Great to meet you!",
        "Contact me at user@email.com",
        "I absolutely hate this stupid thing",
        "My SSN is 123-45-6789 and card is 4111-1111-1111-1111",
    ]

    for msg in messages:
        tox = requests.post(f"{BASE_URL}/toxicity", headers=HEADERS, json={"text": msg}).json()
        pii = requests.post(f"{BASE_URL}/pii", headers=HEADERS, json={"text": msg}).json()

        if tox["is_toxic"]:
            action = "BLOCK (toxic)"
        elif pii["pii_found"]:
            action = f"REDACT ({pii['pii_count']} PII)"
        else:
            action = "ALLOW"

        print(f"[{action:25s}] {msg}")


if __name__ == "__main__":
    print("=== Toxicity Detection ===")
    toxicity_detection()

    print("\n=== Sentiment Analysis ===")
    sentiment_analysis()

    print("\n=== Named Entity Recognition ===")
    named_entity_recognition()

    print("\n=== PII Detection ===")
    pii_detection()

    print("\n=== Language Detection ===")
    language_detection()

    print("\n=== Full Pipeline ===")
    full_analysis_pipeline()

    print("\n=== Batch Processing ===")
    batch_processing()

    print("\n=== Content Moderation ===")
    content_moderation()
