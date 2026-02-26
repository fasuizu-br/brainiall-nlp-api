# Brainiall NLP API

**Production-ready NLP APIs: Toxicity detection, Sentiment analysis, Named Entity Recognition, PII detection, and Language detection.** ONNX-optimized models running on CPU — 100-1000x cheaper than LLMs.

## Overview

Brainiall NLP API provides a suite of specialized NLP models optimized with ONNX for CPU inference. These models solve specific tasks (sentiment, NER, toxicity, etc.) at a fraction of the cost of general-purpose LLMs, with lower latency and higher throughput.

**Base URL:** `https://apim-ai-apis.azure-api.net/v1/nlp`

**Key Features:**
- ONNX-optimized models (no GPU required)
- Sub-50ms latency for most endpoints
- 100-1000x cheaper than using LLMs for the same tasks
- 217 language detection via fastText
- GDPR/CCPA-ready PII detection

## Authentication

Use any one of these headers:

| Method | Header |
|--------|--------|
| Bearer Token | `Authorization: Bearer YOUR_KEY` |
| API Key | `api-key: YOUR_KEY` |
| Subscription Key | `Ocp-Apim-Subscription-Key: YOUR_KEY` |

Get your API key at [brainiall.com](https://brainiall.com).

## Endpoints

### POST /toxicity — Toxicity Detection

Detect toxic content across 6 categories: toxic, severe_toxic, obscene, threat, insult, identity_hate.

```python
import requests

response = requests.post(
    "https://apim-ai-apis.azure-api.net/v1/nlp/toxicity",
    headers={"Authorization": "Bearer YOUR_KEY"},
    json={"text": "You are an amazing person and I appreciate your work!"}
)
result = response.json()
print(result)
# {
#   "text": "You are an amazing person and I appreciate your work!",
#   "is_toxic": false,
#   "scores": {
#     "toxic": 0.0012,
#     "severe_toxic": 0.0001,
#     "obscene": 0.0005,
#     "threat": 0.0002,
#     "insult": 0.0008,
#     "identity_hate": 0.0001
#   },
#   "max_score": 0.0012,
#   "max_category": "toxic"
# }
```

```javascript
const response = await fetch(
  "https://apim-ai-apis.azure-api.net/v1/nlp/toxicity",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer YOUR_KEY",
    },
    body: JSON.stringify({
      text: "You are an amazing person and I appreciate your work!",
    }),
  }
);
const result = await response.json();
console.log(result);
```

```bash
curl -X POST https://apim-ai-apis.azure-api.net/v1/nlp/toxicity \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{"text": "You are an amazing person and I appreciate your work!"}'
```

### POST /sentiment — Sentiment Analysis

Classify text as positive or negative with confidence scores.

```python
import requests

response = requests.post(
    "https://apim-ai-apis.azure-api.net/v1/nlp/sentiment",
    headers={"Authorization": "Bearer YOUR_KEY"},
    json={"text": "This product is absolutely fantastic! Best purchase I've made."}
)
result = response.json()
print(result)
# {
#   "text": "This product is absolutely fantastic! Best purchase I've made.",
#   "sentiment": "positive",
#   "confidence": 0.9847,
#   "scores": {
#     "positive": 0.9847,
#     "negative": 0.0153
#   }
# }
```

```javascript
const response = await fetch(
  "https://apim-ai-apis.azure-api.net/v1/nlp/sentiment",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer YOUR_KEY",
    },
    body: JSON.stringify({
      text: "This product is absolutely fantastic! Best purchase I've made.",
    }),
  }
);
const result = await response.json();
console.log(`Sentiment: ${result.sentiment} (${result.confidence})`);
```

```bash
curl -X POST https://apim-ai-apis.azure-api.net/v1/nlp/sentiment \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{"text": "This product is absolutely fantastic! Best purchase I made."}'
```

### POST /entities — Named Entity Recognition (NER)

Extract named entities: persons, organizations, locations, and miscellaneous.

```python
import requests

response = requests.post(
    "https://apim-ai-apis.azure-api.net/v1/nlp/entities",
    headers={"Authorization": "Bearer YOUR_KEY"},
    json={"text": "Elon Musk announced that Tesla will open a new factory in Berlin, Germany next year."}
)
result = response.json()
print(result)
# {
#   "text": "Elon Musk announced that Tesla will open a new factory in Berlin, Germany next year.",
#   "entities": [
#     {"text": "Elon Musk", "label": "PER", "start": 0, "end": 9, "score": 0.9987},
#     {"text": "Tesla", "label": "ORG", "start": 25, "end": 30, "score": 0.9954},
#     {"text": "Berlin", "label": "LOC", "start": 56, "end": 62, "score": 0.9991},
#     {"text": "Germany", "label": "LOC", "start": 64, "end": 71, "score": 0.9989}
#   ],
#   "entity_count": 4
# }
```

```javascript
const response = await fetch(
  "https://apim-ai-apis.azure-api.net/v1/nlp/entities",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer YOUR_KEY",
    },
    body: JSON.stringify({
      text: "Elon Musk announced that Tesla will open a new factory in Berlin, Germany next year.",
    }),
  }
);
const result = await response.json();
for (const entity of result.entities) {
  console.log(`${entity.text} [${entity.label}] — confidence: ${entity.score}`);
}
```

```bash
curl -X POST https://apim-ai-apis.azure-api.net/v1/nlp/entities \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{"text": "Elon Musk announced that Tesla will open a new factory in Berlin, Germany next year."}'
```

### POST /pii — PII Detection

Detect personally identifiable information: emails, phone numbers, SSNs, credit card numbers.

```python
import requests

response = requests.post(
    "https://apim-ai-apis.azure-api.net/v1/nlp/pii",
    headers={"Authorization": "Bearer YOUR_KEY"},
    json={"text": "Contact me at john@example.com or call 555-123-4567. My SSN is 123-45-6789."}
)
result = response.json()
print(result)
# {
#   "text": "Contact me at john@example.com or call 555-123-4567. My SSN is 123-45-6789.",
#   "pii_found": true,
#   "entities": [
#     {"type": "email", "value": "john@example.com", "start": 15, "end": 31},
#     {"type": "phone", "value": "555-123-4567", "start": 40, "end": 52},
#     {"type": "ssn", "value": "123-45-6789", "start": 64, "end": 75}
#   ],
#   "pii_count": 3
# }
```

```javascript
const response = await fetch(
  "https://apim-ai-apis.azure-api.net/v1/nlp/pii",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer YOUR_KEY",
    },
    body: JSON.stringify({
      text: "Contact me at john@example.com or call 555-123-4567. My SSN is 123-45-6789.",
    }),
  }
);
const result = await response.json();
console.log(`PII found: ${result.pii_found} (${result.pii_count} items)`);
for (const entity of result.entities) {
  console.log(`  ${entity.type}: ${entity.value}`);
}
```

```bash
curl -X POST https://apim-ai-apis.azure-api.net/v1/nlp/pii \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{"text": "Contact me at john@example.com or call 555-123-4567. My SSN is 123-45-6789."}'
```

### POST /language — Language Detection

Detect the language of text. Supports 217 languages via fastText.

```python
import requests

texts = [
    "Hello, how are you today?",
    "Bonjour, comment allez-vous?",
    "Hallo, wie geht es Ihnen?",
    "Hola, como estas?",
    "Olá, como você está?"
]

for text in texts:
    response = requests.post(
        "https://apim-ai-apis.azure-api.net/v1/nlp/language",
        headers={"Authorization": "Bearer YOUR_KEY"},
        json={"text": text}
    )
    result = response.json()
    print(f"'{text}' => {result['language']} ({result['confidence']:.4f})")

# Output:
# 'Hello, how are you today?' => en (0.9876)
# 'Bonjour, comment allez-vous?' => fr (0.9912)
# 'Hallo, wie geht es Ihnen?' => de (0.9845)
# 'Hola, como estas?' => es (0.9801)
# 'Olá, como você está?' => pt (0.9834)
```

```javascript
const texts = [
  "Hello, how are you today?",
  "Bonjour, comment allez-vous?",
  "Hallo, wie geht es Ihnen?",
  "こんにちは、元気ですか？",
  "你好，你好吗？",
];

for (const text of texts) {
  const response = await fetch(
    "https://apim-ai-apis.azure-api.net/v1/nlp/language",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer YOUR_KEY",
      },
      body: JSON.stringify({ text }),
    }
  );
  const result = await response.json();
  console.log(`'${text}' => ${result.language} (${result.confidence})`);
}
```

```bash
curl -X POST https://apim-ai-apis.azure-api.net/v1/nlp/language \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{"text": "Bonjour, comment allez-vous?"}'
```

### GET /health — Health Check

Check model loading status and service health.

```bash
curl -s https://apim-ai-apis.azure-api.net/v1/nlp/health \
  -H "Authorization: Bearer YOUR_KEY" | python3 -m json.tool
# {
#   "status": "healthy",
#   "models": {
#     "toxicity": "loaded",
#     "sentiment": "loaded",
#     "ner": "loaded",
#     "pii": "loaded",
#     "language": "loaded"
#   }
# }
```

## Pricing Comparison

| Task | Brainiall NLP | AWS Comprehend | Azure Text Analytics | GPT-4o |
|------|--------------|----------------|---------------------|--------|
| Toxicity | **$0.001/req** | N/A | $500/1M units | $2,500/1M |
| Sentiment | **$0.001/req** | $500/1M | $700/1M units | $2,500/1M |
| NER/Entities | **$0.002/req** | $500/1M | $700/1M units | $2,500/1M |
| PII Detection | **$0.002/req** | $300/1M | $1,400/1M units | $2,500/1M |
| Language | **$0.0005/req** | $500/1M | $700/1M units | $2,500/1M |

**Bottom line:** Brainiall NLP is 100-1000x cheaper than LLMs and 250-500x cheaper than cloud NLP services for the same tasks.

## Batch Processing

Process multiple texts efficiently:

```python
import requests
from concurrent.futures import ThreadPoolExecutor

API_URL = "https://apim-ai-apis.azure-api.net/v1/nlp"
HEADERS = {
    "Authorization": "Bearer YOUR_KEY",
    "Content-Type": "application/json"
}

texts = [
    "Great product, love it!",
    "Terrible service, never again.",
    "It's okay, nothing special.",
    "Absolutely amazing experience!",
    "Worst purchase ever."
]

def analyze_sentiment(text):
    response = requests.post(
        f"{API_URL}/sentiment",
        headers=HEADERS,
        json={"text": text}
    )
    result = response.json()
    return {"text": text, "sentiment": result["sentiment"], "confidence": result["confidence"]}

# Parallel processing
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(analyze_sentiment, texts))

for r in results:
    print(f"[{r['sentiment']:8s} {r['confidence']:.3f}] {r['text']}")
```

## Full Pipeline Example

Run all NLP analyses on a single text:

```python
import requests
import json

BASE_URL = "https://apim-ai-apis.azure-api.net/v1/nlp"
HEADERS = {
    "Authorization": "Bearer YOUR_KEY",
    "Content-Type": "application/json"
}

text = "John Smith from Microsoft emailed john@microsoft.com saying the new product launch was fantastic!"

# Run all analyses
endpoints = ["toxicity", "sentiment", "entities", "pii", "language"]
results = {}

for endpoint in endpoints:
    response = requests.post(
        f"{BASE_URL}/{endpoint}",
        headers=HEADERS,
        json={"text": text}
    )
    results[endpoint] = response.json()

# Print summary
print(f"Text: {text}")
print(f"Language: {results['language']['language']} ({results['language']['confidence']:.4f})")
print(f"Sentiment: {results['sentiment']['sentiment']} ({results['sentiment']['confidence']:.4f})")
print(f"Toxic: {results['toxicity']['is_toxic']} (max score: {results['toxicity']['max_score']:.4f})")
print(f"Entities: {results['entities']['entity_count']} found")
for e in results['entities']['entities']:
    print(f"  - {e['text']} [{e['label']}]")
print(f"PII: {results['pii']['pii_count']} found")
for p in results['pii']['entities']:
    print(f"  - {p['type']}: {p['value']}")
```

## MCP Server Configuration

Use Brainiall NLP via MCP (Model Context Protocol) in Claude Desktop, Cursor, or any MCP client.

### Claude Desktop / Cursor

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "brainiall-nlp": {
      "url": "https://apim-ai-apis.azure-api.net/mcp/nlp/mcp",
      "headers": {
        "Accept": "application/json, text/event-stream"
      }
    }
  }
}
```

### Available MCP Tools

| Tool | Description |
|------|-------------|
| `analyze_toxicity` | Detect toxic content across 6 categories |
| `analyze_sentiment` | Classify text as positive/negative |
| `extract_entities` | Extract named entities (PER, ORG, LOC, MISC) |
| `detect_pii` | Find PII (email, phone, SSN, credit card) |
| `detect_language` | Identify language (217 supported) |
| `check_nlp_service` | Health check |

### Apify MCP

```json
{
  "mcpServers": {
    "brainiall-nlp-apify": {
      "url": "https://HkExWxGM8fNldLxd6.apify.actor/mcp?token=YOUR_APIFY_TOKEN"
    }
  }
}
```

## Error Handling

```python
import requests

def safe_nlp_call(endpoint, text):
    """Make an NLP API call with error handling."""
    try:
        response = requests.post(
            f"https://apim-ai-apis.azure-api.net/v1/nlp/{endpoint}",
            headers={"Authorization": "Bearer YOUR_KEY"},
            json={"text": text},
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print("Invalid API key")
        elif e.response.status_code == 429:
            print("Rate limited — retry after a moment")
        else:
            print(f"HTTP error: {e.response.status_code}")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out")
        return None

result = safe_nlp_call("sentiment", "This is great!")
if result:
    print(f"Sentiment: {result['sentiment']}")
```

## Links

- Website: [brainiall.com](https://brainiall.com)
- Get API Key: [brainiall.com](https://brainiall.com)
- LLM Gateway: [github.com/fasuizu-br/brainiall-llm-gateway](https://github.com/fasuizu-br/brainiall-llm-gateway)
- Image APIs: [github.com/fasuizu-br/brainiall-image-api](https://github.com/fasuizu-br/brainiall-image-api)
- Speech AI: [github.com/fasuizu-br/speech-ai-examples](https://github.com/fasuizu-br/speech-ai-examples)
- MCP Registry: [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io)

## License

MIT
