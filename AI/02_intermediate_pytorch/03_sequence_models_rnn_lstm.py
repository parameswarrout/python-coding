import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

"""
=============================================================================
🟡 PYTORCH INTERMEDIATE LEVEL - PART 3: SEQUENCE MODELS (RNN, LSTM & GRU)
=============================================================================
Core Concepts Covered:
1. LSTM Cell vs GRU Cell architecture differences (Forget, Input, Output gates vs Reset, Update)
2. `batch_first=True` tensor layout: (Batch, Seq_Len, Dim) vs (Seq_Len, Batch, Dim)
3. Bidirectional LSTMs and extracting the last valid hidden states
4. `pack_padded_sequence` and `pad_packed_sequence` for variable-length efficiency
=============================================================================
"""

class BiLSTMClassifier(nn.Module):
    def __init__(self, vocab_size: int, embed_dim: int, hidden_dim: int, num_classes: int):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(
            input_size=embed_dim,
            hidden_size=hidden_dim,
            num_layers=2,
            batch_first=True,
            bidirectional=True,
            dropout=0.2
        )
        # 2 * hidden_dim because it's bidirectional
        self.classifier = nn.Linear(hidden_dim * 2, num_classes)

    def forward(self, input_ids: torch.Tensor, lengths: torch.Tensor) -> torch.Tensor:
        # 1. Embedding lookup: (Batch, Seq_Len, Embed_Dim)
        embedded = self.embedding(input_ids)
        
        # 2. Pack sequence to skip computation on padded tokens (must be CPU tensor on older pytorch)
        packed_embedded = pack_padded_sequence(
            embedded, 
            lengths.cpu(), 
            batch_first=True, 
            enforce_sorted=False
        )
        
        # 3. Forward through LSTM
        packed_output, (hidden, cell) = self.lstm(packed_embedded)
        
        # hidden shape: (num_layers * num_directions, Batch, Hidden_Dim)
        # Extract top-layer forward and backward hidden states
        # forward: hidden[-2, :, :], backward: hidden[-1, :, :]
        last_hidden = torch.cat((hidden[-2, :, :], hidden[-1, :, :]), dim=-1)  # (Batch, Hidden_Dim * 2)
        
        # 4. Classification logits
        logits = self.classifier(last_hidden)
        return logits


def demo_lstm():
    print("--- Testing Bidirectional LSTM with Packed Sequences ---")
    vocab_size = 1000
    embed_dim = 64
    hidden_dim = 128
    num_classes = 2

    model = BiLSTMClassifier(vocab_size, embed_dim, hidden_dim, num_classes)
    
    # 3 variable-length sequences padded to length 6
    # Batch size = 3
    input_ids = torch.tensor([
        [12, 45, 99, 102, 0, 0],   # length 4
        [5, 23, 0, 0, 0, 0],       # length 2
        [101, 23, 44, 999, 12, 8]  # length 6
    ], dtype=torch.long)
    lengths = torch.tensor([4, 2, 6], dtype=torch.long)

    logits = model(input_ids, lengths)
    print(f"Logits Shape: {logits.shape} (Expected: [3, 2])")
    
    assert logits.shape == (3, 2), "LSTM output shape mismatch!"
    print("✅ PASS: Sequence Modeling & BiLSTM with Packed Sequences Verified!")


if __name__ == "__main__":
    demo_lstm()
