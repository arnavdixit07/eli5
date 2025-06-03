# eli5
This project will explain you difficult concepts, like you're 5!


# 🧠 ELI5 AI Bot — "Explain Like I'm 5"

A beginner-friendly AI app that takes any complex topic and explains it like you're five years old. This project uses powerful language models (LLMs) via Hugging Face to generate simple, digestible explanations for any concept — whether it's quantum physics or climate change.

---

## 🔍 What It Does

This tool lets you enter **any topic**, and it will return an explanation in a tone and format that a 5-year-old can understand. Think of it like ChatGPT for *very curious kids* (and adults who just want it simpler).

---

## 🚀 Features

- Simple input-output UI built with [Gradio](https://gradio.app)
- Uses Hugging Face models like:
  - `bigscience/bloomz-7b1` (large, high-quality)
  - `google/flan-t5-base` (lightweight, faster)
- Prompts structured for "Explain Like I'm 5" tone
- Easily extendable and readable code
- Runs locally in a few lines

---

## 💡 Use Cases

- Learn difficult topics in plain language
- Help kids understand complex ideas
- Break down jargon for non-technical audiences
- Personal assistant for simplified research

---

## 🧰 Tech Stack

- Python 3
- [Transformers](https://huggingface.co/docs/transformers/index)
- Hugging Face models
- Gradio for web interface

---

## 🧠 Models Used

### `bigscience/bloomz-7b1`

- A 7B-parameter multilingual model
- Trained to follow human instructions
- Great for natural language generation

### `google/flan-t5-base`

- 300M-parameter instruction-tuned model
- Lightweight and fast
- Ideal for quick local inference

---

## 🖥️ How to Run

1. Clone the repo  
   `git clone https://github.com/arnavdixit07/eli5`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Run the app  
   `python eli5_ui.py`

---

## 📁 File Structure

- `eli5.py` – Core logic to generate responses
- `eli5_ui.py` – Gradio app interface
- `README.md` – Project documentation

---

## 📸 Preview

> Add a screenshot here if possible

---

## 📜 License

MIT – Free for personal or commercial use.

---

## 🤝 Contributing

Feel free to fork, improve, or submit pull requests!  
Beginner-friendly and open to feedback.

---

## 📫 Contact

Made by Arnav Dikshit– let’s connect on https://www.linkedin.com/in/arnav-dikshit-56ba70211/
