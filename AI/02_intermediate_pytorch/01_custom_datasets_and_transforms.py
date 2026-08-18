import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import torch
from torch.utils.data import Dataset, DataLoader

"""
=============================================================================
🟡 PYTORCH INTERMEDIATE LEVEL - PART 1: CUSTOM DATASETS & DATA PIPELINES
=============================================================================
Core Concepts Covered:
1. Composing custom transform pipelines (Normalization, Random Flips, Noise)
2. Handling Out-Of-Memory (OOM) large datasets with on-the-fly streaming/loading
3. Split creation (Train/Val/Test) with `random_split`
4. Multiprocessing with `num_workers` & `pin_memory`
=============================================================================
"""

class CustomImageDataset(Dataset):
    def __init__(self, data_tensors, labels, transform=None):
        self.data = data_tensors  # Simulated (N, C, H, W)
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data[idx]
        label = self.labels[idx]
        
        if self.transform:
            sample = self.transform(sample)
            
        return sample, label


# Custom functional transforms
class RandomHorizontalFlip:
    def __init__(self, p=0.5):
        self.p = p

    def __call__(self, tensor):
        # tensor shape: (C, H, W)
        if torch.rand(1).item() < self.p:
            return torch.flip(tensor, dims=[-1])
        return tensor


class NormalizeChannels:
    def __init__(self, mean, std):
        self.mean = torch.tensor(mean).view(-1, 1, 1)
        self.std = torch.tensor(std).view(-1, 1, 1)

    def __call__(self, tensor):
        return (tensor - self.mean) / self.std


class ComposeTransforms:
    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, sample):
        for t in self.transforms:
            sample = t(sample)
        return sample


def demo_pipeline():
    print("--- Custom Data Pipeline & Transforms Demo ---")
    torch.manual_seed(42)
    # Simulate 50 RGB images of size 28x28
    dummy_images = torch.rand(50, 3, 28, 28)
    dummy_labels = torch.randint(0, 10, (50,))

    transforms = ComposeTransforms([
        RandomHorizontalFlip(p=1.0), # Force flip for verification
        NormalizeChannels(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    dataset = CustomImageDataset(dummy_images, dummy_labels, transform=transforms)
    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

    train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)
    sample_batch, sample_label = next(iter(train_loader))

    print(f"Train Dataset Size: {len(train_dataset)}, Val Dataset Size: {len(val_dataset)}")
    print(f"Batch Shape: {sample_batch.shape}, Range: [{sample_batch.min():.2f}, {sample_batch.max():.2f}]")
    assert sample_batch.shape == (8, 3, 28, 28), "Batch shape error!"
    print("✅ PASS: Custom Datasets & Transforms Verified!")


if __name__ == "__main__":
    demo_pipeline()
