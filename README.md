# 🚀 MCP Server Demo with FastMCP

A beginner-friendly **Model Context Protocol (MCP)** server built using the **official FastMCP Python SDK**.

This project demonstrates the core concepts of MCP by implementing custom **Tools**, **Resources**, and **Prompts**, and testing them with **MCP Inspector**.

---

## 📌 Features

✅ Custom MCP Tools

- Addition
- Subtraction
- Multiplication
- Division
- Word Counter
- Uppercase Converter
- Lowercase Converter
- Reverse Text
- Current Time
- Mock Weather

---

✅ Dynamic Resources

- Greeting Resource
- About Project Resource

---

✅ Prompt Templates

- Greeting Prompt
- Summarization Prompt
- Explanation Prompt

---

## 📂 Project Structure

```text
mcp-server-demo/
│
├── mcp.py
├── pyproject.toml
├── README.md
├── uv.lock
└── .venv/
```

---

## ⚙️ Requirements

- Python 3.11+
- uv
- MCP SDK
- FastMCP

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/mcp-server-demo.git
```

Go to the project

```bash
cd mcp-server-demo
```

Install dependencies

```bash
uv sync
```

---

## ▶️ Run the MCP Server

```bash
uv run mcp dev mcp.py
```

---

## 🛠 Available Tools

| Tool | Description |
|------|-------------|
| add | Add two numbers |
| subtract | Subtract two numbers |
| multiply | Multiply two numbers |
| divide | Divide two numbers |
| word_count | Count words |
| uppercase | Convert text to uppercase |
| lowercase | Convert text to lowercase |
| reverse_text | Reverse text |
| current_time | Show current time |
| mock_weather | Return mock weather information |

---

## 📄 Resources

### Greeting

```text
greeting://Suresh
```

Output

```text
Hello, Suresh! Welcome to MCP.
```

---

### About Project

```text
about://project
```

Returns information about the project.

---

## 💬 Prompt Templates

### greet_user

Generate a greeting prompt.

### summarize_prompt

Generate a summarization prompt.

### explain_prompt

Generate an explanation prompt.

---

## 🧪 Testing

Run the server

```bash
uv run mcp dev mcp.py
```

Open **MCP Inspector**

Test

- Tools
- Resources
- Prompts

---

## 🛠 Tech Stack

- Python
- FastMCP
- MCP SDK
- MCP Inspector
- uv

---

## 🎯 Learning Objectives

This project demonstrates

- MCP Fundamentals
- FastMCP
- Tools
- Resources
- Prompt Templates
- MCP Inspector
- Python MCP Server Development

---

## 📸 Screenshots

You can add screenshots of

- MCP Inspector
- Tools
- Resources
- Prompts

---

## 🚀 Future Improvements

- File Reader Tool
- JSON Formatter
- CSV Analyzer
- Markdown Converter
- UUID Generator
- Password Generator
- Notes Manager
- Weather API Integration
- Calculator Suite
- AI-powered Text Utilities

---

## 👨‍💻 Author

**Sureshkumar**

GitHub:
https://github.com/Sureshkumar8795/mcp-server-demo.git

---

## 📄 License

MIT License
