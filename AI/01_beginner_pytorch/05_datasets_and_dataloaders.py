import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import torch
from torch.utils.data import Dataset, DataLoader, TensorDataset

"""
=============================================================================
🟢 PYTORCH BEGINNER LEVEL - PART 5: DATASETS, DATALOADERS & COLLATE_FN
=============================================================================
Core Concepts Covered:
1. `torch.utils.data.Dataset`: Overriding `__init__`, `__len__`, and `__getitem__`
2. `TensorDataset` and `DataLoader` (batching, shuffling, drop_last, pin_memory)
3. Custom `collate_fn`: Essential for variable-length NLP/Audio sequence padding
4. Batch iteration in training loops
=============================================================================
"""

# =============================================================================
# 1. BASIC CUSTOM DATASET
# =============================================================================
class TabularDataset(Dataset):
    def __init__(self, features: torch.Tensor, labels: torch.Tensor):
        assert len(features) == len(labels), "Features and labels must have same length"
        self.features = features
        self.labels = labels

    def __len__(self) -> int:
        return len(self.features)

    def __getitem__(self, idx: int):
        return self.features[idx], self.labels[idx]


# =============================================================================
# 2. CUSTOM COLLATE_FN (TOP INTERVIEW QUESTION FOR NLP / LLM ENGINEERS)
# =============================================================================
def custom_pad_collate_fn(batch):
    """
    Given a batch of variable-length 1D token tensors and their labels:
    batch = [(tensor([1, 2, 3]), label_0), (tensor([4, 5]), label_1), ...]
    Pads all sequences to the maximum length in the current batch with pad_token_id = 0.
    Returns:
      padded_sequences: (Batch_Size, Max_Seq_Len)
      attention_mask:   (Batch_Size, Max_Seq_Len) - 1 for token, 0 for pad
      labels:           (Batch_Size,)
    """
    sequences, labels = zip(*batch)
    
    # 1. Find max length in batch
    max_len = max(len(seq) for seq in sequences)
    batch_size = len(sequences)
    
    # 2. Allocate padded tensor & attention mask
    padded_seqs = torch.zeros((batch_size, max_len), dtype=torch.long)
    attention_mask = torch.zeros((batch_size, max_len), dtype=torch.float32)
    
    for i, seq in enumerate(sequences):
        length = len(seq)
        padded_seqs[i, :length] = seq
        attention_mask[i, :length] = 1.0  # 1s for real tokens
        
    labels_tensor = torch.tensor(labels, dtype=torch.long)
    return padded_seqs, attention_mask, labels_tensor


def demo_dataloaders():
    print("--- 1. Testing Standard Custom Dataset & DataLoader ---")
    X = torch.randn(100, 4)
    y = torch.randint(0, 2, (100,))
    
    dataset = TabularDataset(X, y)
    dataloader = DataLoader(dataset, batch_size=16, shuffle=True, drop_last=False)
    
    batch_count = 0
    for batch_x, batch_y in dataloader:
        batch_count += 1
    print(f"Total batches processed: {batch_count} (Expected: 7)")
    assert batch_count == 7, "Batch count incorrect!"

    print("\n--- 2. Testing Custom Collate Function (NLP Variable Sequence Padding) ---")
    # Sample variable length sentences
    variable_data = [
        (torch.tensor([101, 2054, 2003, 102]), 1),      # len 4
        (torch.tensor([101, 7592, 102]), 0),            # len 3
        (torch.tensor([101, 1045, 2293, 2023, 102]), 1), # len 5
    ]
    
    pad_loader = DataLoader(variable_data, batch_size=3, collate_fn=custom_pad_collate_fn)
    padded_seqs, attention_mask, batch_labels = next(iter(pad_loader))
    
    print(f"Padded Sequences (shape {padded_seqs.shape}):\n{padded_seqs}")
    print(f"Attention Mask:\n{attention_mask}")
    print(f"Labels: {batch_labels}")
    
    assert padded_seqs.shape == (3, 5), "Padded sequence shape mismatch!"
    assert attention_mask[1].tolist() == [1.0, 1.0, 1.0, 0.0, 0.0], "Attention mask mismatch!"
    print("\n✅ PASS: Datasets, DataLoaders & Collate Function Mastered!")


if __name__ == "__main__":
    demo_dataloaders()
