from mcp.server.fastmcp import FastMCP
from datetime import datetime
import random

app = FastMCP("MCP Server Demo")

## Tools 

@app.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@app.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

@app.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@app.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        return "Cannot divide by zero."
    return round(a / b, 2)

@app.tool()
def word_count(text: str) -> int:
    """Count the number of words."""
    return len(text.split())

@app.tool()
def uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()

@app.tool()
def lowercase(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()

@app.tool()
def reverse_text(text: str) -> str:
    """Reverse a string."""
    return text[::-1]

@app.tool()
def current_time() -> str:
    """Return the current local time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.tool()
def mock_weather(city: str) -> str:
    """Return mock weather information."""
    weather = [
        "Sunny",
        "Cloudy",
        "Rainy",
        "Windy",
        "Thunderstorm"
    ]

    temperature = random.randint(22, 38)

    return f"{city}: {random.choice(weather)}, {temperature}°C"

## Resources

@app.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}! Welcome to MCP."


@app.resource("about://project")
def about_project() -> str:
    """Information about the project."""
    return (
        "This project demonstrates MCP Tools, Resources, "
        "and Prompts using FastMCP."
    )


## Prompts

@app.prompt()
def greet_user(name: str, style: str = "Friendly") -> str:
    """Generate a greeting prompt."""

    styles = {
        "Friendly": "Write a warm and friendly greeting",
        "Formal": "Write a professional greeting",
        "Casual": "Write a casual greeting"
    }

    return f"{styles.get(style, styles['Friendly'])} for a person named {name}."


@app.prompt()
def summarize_prompt(topic: str) -> str:
    """Prompt for summarization."""
    return f"Summarize the topic '{topic}' in simple English."


@app.prompt()
def explain_prompt(topic: str) -> str:
    """Prompt for explanation."""
    return f"Explain '{topic}' like I'm a beginner."


if __name__ == "__main__":
    app.run()