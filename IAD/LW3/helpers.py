import os
import pickle

import torch

from constants import MODEL_PATH


def save_embeddings_data(indexes_in_corpus, embeddings, outputs, filename):
    data = {
        'indexes_in_corpus': indexes_in_corpus,
        'embeddings': embeddings,
        'outputs': outputs
    }

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'wb') as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)


def load_embeddings_data(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)

    return (
        data['indexes_in_corpus'],
        data['embeddings'],
        data['outputs']
    )


def save_model(model, optimizer, epoch, loss, path=MODEL_PATH):
    torch.save({
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'epoch': epoch,
        'loss': loss,
    }, path)


def load_model(model, optimizer, path=MODEL_PATH):
    checkpoint = torch.load(path)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    epoch = checkpoint['epoch']
    loss = checkpoint['loss']
    return model, optimizer, epoch, loss
