from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id = "bigscience/bloomz-7b1"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def build_prompt(user_input):
    return f"Explain the following concept like I’m 5 years old:\n\n{user_input}\n"

def get_eli5_response(topic):
    prompt = build_prompt(topic)
    output = generator(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)
    return output[0]['generated_text'][len(prompt):]



if __name__ == "__main__":
    while True:
        topic = input("Enter a topic to explain (or 'exit' to quit): ")
        if topic.lower() == "exit":
            break
        explanation = eli5(topic)
        print("\n🧠 ELI5 Explanation:\n", explanation)
