# Greeting Performance Comparison

A demonstration project comparing the performance and trade-offs between vanilla Python implementations and AI-powered alternatives for a simple greeting task.

## Scripts Overview

### 1. `greeting.py` - Vanilla Implementation
- **Purpose**: Baseline performance benchmark
- **Response Time**: ~0.000005 seconds (depends on CPU)
- **Dependencies**: None
- **Reliability**: 100%

### 2. `ai_greeting.py` - Constrained AI Implementation  
- **Purpose**: AI with strict output formatting
- **Response Time**: ~1 second (depends on generated tokens/second of the model)
- **Dependencies**: OpenAI API, internet connection
- **Reliability**: Dependent on API availability

### 3. `flexible_ai_greeting.py` - Creative AI Implementation
- **Purpose**: AI with creative freedom for personalized responses
- **Response Time**: ~1-2 seconds (depends on generated tokens/second of the model)
- **Dependencies**: OpenAI API, internet connection
- **Reliability**: Dependent on API availability

## Setup

1. Install dependencies:
```bash
python -m venv .venv
. .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

2. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Demos

```bash
# Vanilla implementation (instant)
python greeting.py

# AI with rigid formatting (slow but consistent)
python ai_greeting.py

# AI with creative responses (slow but personalized)
python flexible_ai_greeting.py
```

## Performance Analysis

| Implementation | Avg Response Time | Cost per Call | Reliability | Creativity |
|----------------|-------------------|---------------|-------------|------------|
| Vanilla        | 0.000005s         | $0            | 100%        | None       |
| AI Constrained | 0.915847s         | ~$0.00000840  | 95%         | Low        |
| AI Flexible    | 1.530147s         | ~$0.0000146   | 95%         | High       |

## Key Takeaways

- **Performance**: Vanilla is 183,000x faster than AI implementations
- **Cost**: AI adds ~$0.001 per greeting vs $0 for vanilla (the actual cost will depend on the model used, the size of the context and the output)
- **Reliability**: Vanilla never fails; AI depends on network/API, how good the prompt is and how good the model is at following instructions.
- **Use Case**: Choose vanilla for speed/reliability, AI for dynamic content

This demonstrates that AI should be used thoughtfully - not every problem needs an AI solution.
