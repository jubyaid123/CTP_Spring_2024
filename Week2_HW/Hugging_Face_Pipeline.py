from transformers import pipeline

text_generator = pipeline("text-generation", model="gpt2")

generated_text = text_generator("Artificial intelligence is superior to humans", min_length=50)

print(generated_text)