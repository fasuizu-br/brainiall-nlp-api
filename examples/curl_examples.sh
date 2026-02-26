#!/bin/bash
# Brainiall NLP API — curl Examples
#
# Base URL: https://apim-ai-apis.azure-api.net/v1/nlp
# Get your API key at https://brainiall.com

BASE="https://apim-ai-apis.azure-api.net/v1/nlp"
KEY="YOUR_KEY"  # Replace with your API key

echo "=== Toxicity Detection ==="
curl -s -X POST "$BASE/toxicity" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KEY" \
  -d '{"text": "You are such a wonderful person!"}' | python3 -m json.tool

echo ""
echo "=== Sentiment Analysis ==="
curl -s -X POST "$BASE/sentiment" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KEY" \
  -d '{"text": "This product exceeded all my expectations!"}' | python3 -m json.tool

echo ""
echo "=== Named Entity Recognition ==="
curl -s -X POST "$BASE/entities" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KEY" \
  -d '{"text": "Satya Nadella leads Microsoft from their headquarters in Redmond, Washington."}' | python3 -m json.tool

echo ""
echo "=== PII Detection ==="
curl -s -X POST "$BASE/pii" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KEY" \
  -d '{"text": "Email me at alice@company.com or call 555-123-4567. SSN: 123-45-6789."}' | python3 -m json.tool

echo ""
echo "=== Language Detection ==="
curl -s -X POST "$BASE/language" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KEY" \
  -d '{"text": "Bonjour, comment allez-vous aujourd hui?"}' | python3 -m json.tool

echo ""
echo "=== Health Check ==="
curl -s "$BASE/health" \
  -H "Authorization: Bearer $KEY" | python3 -m json.tool
