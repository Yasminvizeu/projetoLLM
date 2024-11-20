import tiktoken

enc = tiktoken.get_encoding("gpt2")
tokens = enc.encode("vamos aprender trasformers pelo amore de deus aumenta ess vocabulario aii")
print(tokens)