# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("roneneldan/TinyStories-1M")
model = AutoModelForCausalLM.from_pretrained("roneneldan/TinyStories-1M")

from plot import draw_rectangles
import torch

def record_attention(output, img_num=0, title=''):

    data = [[0*8 for _ in range(16)] for _ in range(8)]
    for i in range(16):
        for j in range(8):
            data[j][i] = torch.std(output.attentions[j][0][i][:, -1]).item()


    max_val = max([max(row) for row in data])
    data = [[int(val/max_val*255) for val in row] for row in data]
    draw_rectangles(16, 8, data, img_num=img_num, title=title[-60:])


# print the model architecture
print(model)
print('-'*50)

# make it auto complete "Once upon a time, there was a"
input_text = "Once upon "

# do forward with output_attentions and output_hidden_states = true
for i in range(100):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model(input_ids, output_attentions=True, output_hidden_states=True)
    output_text = tokenizer.decode(output.logits[0].argmax(dim=-1).tolist())
    # print the output text
    print(input_text)
    # update the input text, get last word
    input_text = input_text + ' ' + output_text.split()[-1]

    # record the attention # last 20 characters of input_text
    record_attention(output, img_num=i, title=input_text[-60:])


