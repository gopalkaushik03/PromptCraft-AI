# PromptCraft AI: Human-in-the-Loop Prompt Engineering 🤖✨

![Status](https://img.shields.io/badge/Status-v1.0_(Stable)-success)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Framework](https://img.shields.io/badge/Streamlit-1.35-red)
![API](https://img.shields.io/badge/Google-Gemini_1.5-green)

**PromptCraft AI** is an advanced AI interaction tool designed to solve the "Blank Canvas Problem" in generative AI. Instead of sending vague queries directly to an LLM, this application acts as an intelligent middle-layer that optimizes user intent before execution.

---

## 📖 Table of Contents
1. [Problem Statement](#-problem-statement)
2. [Proposed Solution](#-proposed-solution)
3. [System Architecture](#-system-architecture)
4. [Key Features](#-key-features)
5. [Installation & Setup](#-installation--setup)
6. [Code Structure](#-code-structure)
7. [Future Scope](#-future-scope)

---

## 🎯 Problem Statement
In the domain of Large Language Models (LLMs), the quality of the output is directly proportional to the quality of the input (Garbage In, Garbage Out).
* **Issue:** Users often write vague prompts (e.g., "write code for a game").
* **Result:** Generic, hallucinated, or buggy outputs from AI.
* **Challenge:** Most users do not know advanced prompt engineering techniques (Persona adoption, chain-of-thought, constraints).

## 💡 Proposed Solution
**PromptCraft AI** implements a **"Refine-Review-Execute"** workflow:
1.  **Interprets** the user's raw, vague idea.
2.  **Optimizes** it using an expert "Prompt Engineer" agent.
3.  **Presents** the optimized prompt to the user for confirmation.
4.  **Executes** the final request using a specialized persona (e.g., Senior Developer, Data Scientist).

---

## 🏗 System Architecture

The application follows a modular architecture using Streamlit for the frontend and Google Gemini for the backend logic.

```mermaid
graph TD
 
    A[User Input (Raw Idea)] -->|Send to Refiner| B(Gemini: Prompt Engineer Model)
    B -->|Returns Optimized Prompt| C{User Review}
    C -->|Edit/Confirm| D[Final Prompt]
    C -->|Reject| A
    D -->|Selected Persona + Params| E(Gemini: Executor Model)
    E -->|Stream Response| F[UI Display]



   🚀 Key Features
🧠 1. Auto-Adaptive Depth Engine
The system intelligently analyzes the user's request to determine the required output depth automatically:

Brief Queries: (e.g., "Define API") → Generates concise definitions.

Complex Tasks: (e.g., "Code a Snake Game") → Automatically demands comprehensive, multi-section guides (1000+ words).

🎨 2. Ultra-Glass UI (Neon Aesthetics)
Transparent Sidebar: A modern, frosted-glass sidebar using advanced CSS backdrop filters.

Neon Animations: "Breathing" neon text effects for the brand header.

Mission Control: A dedicated dashboard to review and edit prompts before execution.

🤖 3. Context-Aware 3D Avatars
The app dynamically switches avatars based on the conversation context:

👨‍💻 Coder Robot: Activates when discussing Python, React, APIs, or bugs.

🎨 Creative Robot: Activates for storytelling, design, or essays.

🤖 Default Robot: Handles general queries.

⚙️ Installation & Setup
Clone the Repository
Bash

git clone [https://github.com/YourUsername/PromptCraft-AI.git](https://github.com/YourUsername/PromptCraft-AI.git)
cd PromptCraft-AI
Install Dependencies

Bash

pip install -r requirements.txt
Set up API Keys

Create a .env file in the root directory.

Add your Google Gemini API Key:

Code snippet

GOOGLE_API_KEY="your_api_key_here"
Run the App

Bash

streamlit run app.py

📂 Code Structure 

app.py - The Frontend: Handles the Streamlit UI, CSS styling, and session state.

gemini_client.py - The Brain: Manages API connections, Model auto-detection, and the "Refiner Agent" logic.

history.py - The Memory: Saves user interactions to JSON (optional persistence).

.env - Security: Stores sensitive API keys.

🔮 Future Scope
🎙️ Voice Support: Native Speech-to-Text for hands-free prompting.

📥 Export Chat: Ability to download chat history as PDF/Markdown.

🖼️ Multimodal Support: Upload images to generate prompts from visuals.

Built with ❤️ using Python & Streamlit.