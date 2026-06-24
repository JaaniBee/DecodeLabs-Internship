# Rule-Based AI Chatbot

A simple React + Vite rule-based chatbot that responds to predefined user inputs using if-else logic. This app demonstrates basic control flow, decision-making logic, and a continuous chat experience.

## Project Overview

- Built with React and Vite for a fast frontend experience.
- Uses a rule-based response system in `src/chatbotLogic.js`.
- Recognizes greetings, help requests, self-introduction prompts, chatbot questions, and exit commands.
- Provides a friendly fallback message when input is not recognized.

## Features

- Greeting detection (`hello`, `hi`, `hey`)
- Exit support (`exit`, `bye`, `quit`, `goodbye`)
- Help command support (`help`, `what can you do`)
- Interview self-introduction sample responses
- Simple rule-based AI behavior with if-else logic
- Scrollable chat UI with conversational message display

## Files to Know

- `src/App.jsx` - chat UI and input handling
- `src/chatbotLogic.js` - rule-based response logic
- `src/App.css` - basic styling for the chat interface
- `package.json` - dependencies and run scripts

## Run the Project

1. Open a terminal in the project folder.
2. Install dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm run dev

4. Open the URL shown by Vite in your browser (usually `http://localhost:5173`).



