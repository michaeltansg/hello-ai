#!/usr/bin/env python3
"""AI-powered greeting script using OpenAI SDK with system prompt."""

import os
import random
import time

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Token pricing for gpt-4.1-nano (per token)
INPUT_TOKEN_COST = 1e-07  # $0.0000001 per input token
OUTPUT_TOKEN_COST = 4e-07  # $0.0000004 per output token


def main():
    """Get user name and generate AI-powered personalized greeting."""
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Get the user's name
    name = input("Please enter your name: ")

    # System prompt for generating personalized greetings
    system_prompt = (
        "You are a friendly greeting assistant. When given a name, "
        "the response should always be in the format\n"
        "'Hello, [name]! Nice to meet you!'"
    )

    try:
        # Start timing
        start_time = time.perf_counter()

        # Make API call to OpenAI
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Create a greeting for {name}"}
            ],
            max_tokens=100,
            temperature=0.7,
            # Random seed to prevent caching
            seed=random.randint(1, 1000000),  # noqa: S311
        )

        # Extract and print the AI-generated greeting
        greeting = response.choices[0].message.content.strip()
        print(f"\n{greeting}")

        # End timing and print execution time
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print("\n======== STATISTICS ========")
        print(f"Execution time: {execution_time:.6f} seconds")

        # Calculate and display token usage and cost
        usage = response.usage
        input_tokens = usage.prompt_tokens
        output_tokens = usage.completion_tokens
        total_tokens = usage.total_tokens

        input_cost = input_tokens * INPUT_TOKEN_COST
        output_cost = output_tokens * OUTPUT_TOKEN_COST
        total_cost = input_cost + output_cost

        print("\nToken Usage:")
        print(f"  Input tokens: {input_tokens}")
        print(f"  Output tokens: {output_tokens}")
        print(f"  Total tokens: {total_tokens}")
        print("\nCost Breakdown:")
        print(f"  Input cost: ${input_cost:.8f}")
        print(f"  Output cost: ${output_cost:.8f}")
        print(f"  Total cost: ${total_cost:.8f}")

    except Exception as e:
        # Fallback to simple greeting if API fails
        print(f"API Error: {e}")


if __name__ == "__main__":
    main()
