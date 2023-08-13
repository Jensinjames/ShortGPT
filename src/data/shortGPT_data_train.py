```python
import os
import json
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AdamW, get_linear_schedule_with_warmup
import torch

class ShortGPTDataTrain:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')

    def load_data(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data

    def train_shortGPT(self):
        data = self.load_data()
        inputs = self.tokenizer(data, return_tensors='pt')
        outputs = self.model(**inputs, labels=inputs["input_ids"])
        loss = outputs.loss
        optimizer = AdamW(self.model.parameters())
        scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=-1)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        scheduler.step()
        print("Training Completed")

    def save_model(self):
        model_dir = os.path.join(os.path.dirname(self.file_path), 'model')
        self.model.save_pretrained(model_dir)
        print("Model Saved")

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'json_data_store.py')
    trainer = ShortGPTDataTrain(file_path)
    trainer.train_shortGPT()
    trainer.save_model()
```