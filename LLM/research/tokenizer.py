import tiktoken

enc = tiktoken.get_encoding("gpt2")
tokens = enc.encode("estamos aprendendo trasformers")
print(tokens)