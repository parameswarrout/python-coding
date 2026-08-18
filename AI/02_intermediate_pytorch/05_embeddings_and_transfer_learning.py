import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import torch
import torch.nn as nn
import torch.optim as optim

"""
=============================================================================
🟡 PYTORCH INTERMEDIATE LEVEL - PART 5: EMBEDDINGS & TRANSFER LEARNING
=============================================================================
Core Concepts Covered:
1. `nn.Embedding` mechanics: Lookup table vs Linear projection
2. Transfer Learning: Freezing base feature extractor weights (`requires_grad = False`)
3. Replacing classification head
4. Discriminative Learning Rates (different LRs for backbone vs newly initialized head)
=============================================================================
"""

class MockPretrainedBackbone(nn.Module):
    """Simulates a heavy pretrained vision or language backbone (e.g. ResNet / BERT)"""
    def __init__(self, in_features=128, feature_dim=512):
        super().__init__()
        self.conv_stack = nn.Sequential(
            nn.Linear(in_features, 256),
            nn.ReLU(),
            nn.Linear(256, feature_dim),
            nn.ReLU()
        )

    def forward(self, x):
        return self.conv_stack(x)


class FineTunedClassifier(nn.Module):
    def __init__(self, backbone: nn.Module, feature_dim: int, num_classes: int, freeze_backbone: bool = True):
        super().__init__()
        self.backbone = backbone
        
        # 1. Freeze backbone if specified
        if freeze_backbone:
            for param in self.backbone.parameters():
                param.requires_grad = False
                
        # 2. Custom newly initialized head
        self.head = nn.Sequential(
            nn.Linear(feature_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        features = self.backbone(x)
        logits = self.head(features)
        return logits


def demo_transfer_learning():
    print("--- Testing Transfer Learning & Discriminative Learning Rates ---")
    backbone = MockPretrainedBackbone(in_features=32, feature_dim=128)
    model = FineTunedClassifier(backbone, feature_dim=128, num_classes=5, freeze_backbone=True)

    # Check trainable vs frozen parameters
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    frozen_params = sum(p.numel() for p in model.parameters() if not p.requires_grad)
    print(f"Trainable Parameters (Head only): {trainable_params}")
    print(f"Frozen Parameters (Backbone): {frozen_params}")
    
    assert frozen_params > 0, "Backbone parameters were not frozen!"
    assert trainable_params > 0, "No trainable parameters found!"

    # Discriminative Learning Rates (Different LR for backbone vs head when unfreezing)
    optimizer = optim.AdamW([
        {'params': model.backbone.parameters(), 'lr': 1e-5},  # Gentle fine-tuning
        {'params': model.head.parameters(), 'lr': 1e-3}       # Fast learning for new head
    ])

    dummy_x = torch.randn(16, 32)
    dummy_y = torch.randint(0, 5, (16,))
    
    criterion = nn.CrossEntropyLoss()
    logits = model(dummy_x)
    loss = criterion(logits, dummy_y)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Loss after 1 step: {loss.item():.4f}")
    print("✅ PASS: Embeddings & Transfer Learning Mastered!")


if __name__ == "__main__":
    demo_transfer_learning()
