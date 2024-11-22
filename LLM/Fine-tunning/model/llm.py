from tokenizers import ByteLevelBPETokenizer

PATH = 'sample_data'
dados_treino = 'crepusculoDosIdolos.txt'

tokenizer = ByteLevelBPETokenizer()
tokenizer.train(files=[PATH+dados_treino], vocab_size=52_000, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

tokenizer.save_model('./tokenizer')
