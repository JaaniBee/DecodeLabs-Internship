const normalizeInput = (text) => {
  return text
    .toLowerCase()
    .trim()
    .replace(/[!?.,]/g, '');
};

const containsAny = (input, phrases) => {
  return phrases.some((phrase) => input === phrase || input.includes(phrase));
};

export function getResponse(userInput) {
  const input = normalizeInput(userInput);

  const exitCommands = ['exit', 'quit', 'bye', 'goodbye', 'stop'];
  const greetings = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good evening', 'good afternoon'];
  const helpQueries = ['help', 'what can you do', 'how can you help', 'options'];
  const nameQueries = ['what is your name', 'who are you', 'what are you called'];
  const aiQueries = ['what is ai', 'what is artificial intelligence', 'tell me about ai'];
  const chatbotQueries = ['what is chatbot', 'what is a chatbot', 'define chatbot'];
  const interviewQueries = ['self introduction', 'self intro', 'introduce myself', 'interview intro', 'sample introduction'];
  const smallTalk = ['thanks', 'thank you', 'thanks a lot'];

  if (containsAny(input, exitCommands)) {
    return 'Goodbye! Have a great day.';
  } else if (containsAny(input, greetings)) {
    return 'Hello! How can I help you today?';
  } else if (containsAny(input, helpQueries)) {
    return "I am a rule-based chatbot. I can respond to greetings, answer simple questions, and help you learn how I work. Type 'exit' or 'bye' to end the chat.";
  } else if (containsAny(input, nameQueries)) {
    return 'I am a simple rule-based chatbot created to respond to predefined user inputs.';
  } else if (containsAny(input, aiQueries)) {
    return 'AI stands for Artificial Intelligence. This chatbot uses if-else logic to choose a response.';
  } else if (containsAny(input, chatbotQueries)) {
    return 'A chatbot is a program that responds to user messages with predefined rules. This one uses if-else logic to decide answers.';
  } else if (containsAny(input, interviewQueries)) {
    return 'Here is a sample interview self-introduction: "Hello, my name is [Your Name]. I recently graduated in [Your Field] and I have experience with [Your Skill]. I am excited to learn and contribute to your team."';
  } else if (containsAny(input, smallTalk)) {
    return "You're welcome!";
  } else {
    return "I'm sorry, I don't understand that. Please try a greeting, ask for help, or type 'exit' to stop.";
  }
}
