/**
 * Brainiall NLP API — JavaScript Examples
 *
 * Base URL: https://apim-ai-apis.azure-api.net/v1/nlp
 * Get your API key at https://brainiall.com
 */

const BASE_URL = "https://apim-ai-apis.azure-api.net/v1/nlp";
const API_KEY = "YOUR_KEY"; // Replace with your API key

async function nlpRequest(endpoint, text) {
  const response = await fetch(`${BASE_URL}/${endpoint}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${API_KEY}`,
    },
    body: JSON.stringify({ text }),
  });
  return response.json();
}

// Toxicity Detection
async function toxicityExample() {
  console.log("=== Toxicity Detection ===");
  const texts = [
    "You are a wonderful person!",
    "I hate everything about this",
    "The weather is nice today",
  ];

  for (const text of texts) {
    const result = await nlpRequest("toxicity", text);
    const status = result.is_toxic ? "TOXIC" : "SAFE";
    console.log(`[${status}] ${text}`);
    console.log(
      `  Max: ${result.max_category} = ${result.max_score.toFixed(4)}`
    );
  }
}

// Sentiment Analysis
async function sentimentExample() {
  console.log("\n=== Sentiment Analysis ===");
  const reviews = [
    "Absolutely love this product!",
    "Terrible quality, very disappointed.",
    "It's okay, nothing special.",
    "Best purchase I've ever made!",
    "Would not recommend to anyone.",
  ];

  for (const review of reviews) {
    const result = await nlpRequest("sentiment", review);
    const icon = result.sentiment === "positive" ? "+" : "-";
    console.log(`[${icon} ${result.confidence.toFixed(3)}] ${review}`);
  }
}

// Named Entity Recognition
async function nerExample() {
  console.log("\n=== Named Entity Recognition ===");
  const text =
    "Elon Musk announced that SpaceX will launch from Cape Canaveral next month.";

  const result = await nlpRequest("entities", text);
  console.log(`Text: ${text}`);
  console.log(`Entities found: ${result.entity_count}`);
  for (const entity of result.entities) {
    console.log(
      `  [${entity.label}] ${entity.text} (${entity.score.toFixed(4)})`
    );
  }
}

// PII Detection
async function piiExample() {
  console.log("\n=== PII Detection ===");
  const text =
    "Contact alice@company.com or call 555-867-5309. SSN: 078-05-1120.";

  const result = await nlpRequest("pii", text);
  console.log(`Text: ${text}`);
  console.log(`PII found: ${result.pii_found} (${result.pii_count} items)`);
  for (const entity of result.entities) {
    console.log(`  [${entity.type}] ${entity.value}`);
  }
}

// Language Detection
async function languageExample() {
  console.log("\n=== Language Detection ===");
  const texts = [
    "Hello, how are you?",
    "Bonjour, comment allez-vous?",
    "Hallo, wie geht es Ihnen?",
    "こんにちは",
    "Olá, tudo bem?",
  ];

  for (const text of texts) {
    const result = await nlpRequest("language", text);
    console.log(`[${result.language} ${result.confidence.toFixed(3)}] ${text}`);
  }
}

// Full Pipeline
async function fullPipeline() {
  console.log("\n=== Full Analysis Pipeline ===");
  const text =
    "John from Google in NYC emailed john@google.com — fantastic product!";

  const endpoints = ["toxicity", "sentiment", "entities", "pii", "language"];
  const results = {};

  await Promise.all(
    endpoints.map(async (ep) => {
      results[ep] = await nlpRequest(ep, text);
    })
  );

  console.log(`Text: ${text}`);
  console.log(`Language: ${results.language.language}`);
  console.log(
    `Sentiment: ${results.sentiment.sentiment} (${results.sentiment.confidence.toFixed(3)})`
  );
  console.log(`Toxic: ${results.toxicity.is_toxic}`);
  console.log(`Entities: ${results.entities.entity_count}`);
  console.log(`PII: ${results.pii.pii_count} items`);
}

// Content Moderation
async function contentModeration() {
  console.log("\n=== Content Moderation ===");
  const messages = [
    "Hello, great to meet you!",
    "Email me at user@email.com",
    "My SSN is 123-45-6789",
  ];

  for (const msg of messages) {
    const [tox, pii] = await Promise.all([
      nlpRequest("toxicity", msg),
      nlpRequest("pii", msg),
    ]);

    let action;
    if (tox.is_toxic) action = "BLOCK (toxic)";
    else if (pii.pii_found) action = `REDACT (${pii.pii_count} PII)`;
    else action = "ALLOW";

    console.log(`[${action.padEnd(20)}] ${msg}`);
  }
}

// Run all examples
await toxicityExample();
await sentimentExample();
await nerExample();
await piiExample();
await languageExample();
await fullPipeline();
await contentModeration();
