import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import torch
import torch.nn as nn
import torch.optim as optim

"""
=============================================================================
🟢 PYTORCH BEGINNER LEVEL - PART 4: MULTI-LAYER PERCEPTRON (MLP)
=============================================================================
Core Concepts Covered:
1. Building modular architectures with `nn.Module` and `nn.Sequential`
2. Non-linear Activation Functions: ReLU, LeakyReLU, GELU, SiLU/Swish
3. Weight Initialization: Xavier/Glorot (for Sigmoid/Tanh) vs He/Kaiming (for ReLU/GELU)
4. Multi-class Classification with `nn.CrossEntropyLoss` (LogSoftmax + NLLLoss)
5. Model Checkpointing: `state_dict()` saving and loading
=============================================================================
"""

class MultiLayerPerceptron(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, num_classes: int, dropout_rate: float = 0.2):
        super().__init__()
        
        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.GELU(),  # Modern non-linear activation used in Transformers & GPT
            nn.Dropout(p=dropout_rate),
            
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.BatchNorm1d(hidden_dim // 2),
            nn.GELU(),
            nn.Dropout(p=dropout_rate),
            
            nn.Linear(hidden_dim // 2, num_classes)  # Raw unnormalized logits
        )
        
        # Apply Kaiming / He Normal initialization
        self._init_weights()

    def _init_weights(self):
        for module in self.modules():
            if isinstance(module, nn.Linear):
                nn.init.kaiming_normal_(module.weight, nonlinearity='relu')
                if module.bias is not None:
                    nn.init.zeros_(module.bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)


def demo_mlp_training():
    print("--- Multi-Layer Perceptron (MLP) Multi-Class Training ---")
    torch.manual_seed(42)
    
    # 3 classes, 10 input features, 300 samples
    num_samples = 300
    input_dim = 10
    num_classes = 3
    
    X = torch.randn(num_samples, input_dim)
    # Target classes: 0, 1, 2
    y = torch.randint(0, num_classes, (num_samples,))

    model = MultiLayerPerceptron(input_dim=input_dim, hidden_dim=64, num_classes=num_classes)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=0.01, weight_decay=1e-4)

    # Training
    model.train()
    for epoch in range(50):
        optimizer.zero_grad()
        logits = model(X)
        loss = criterion(logits, y)
        loss.backward()
        optimizer.step()

    # Evaluation
    model.eval()
    with torch.no_grad():
        test_logits = model(X)
        predictions = torch.argmax(test_logits, dim=-1)
        accuracy = (predictions == y).float().mean().item()
        print(f"Epoch 50 Final Loss: {loss.item():.4f} | Training Accuracy: {accuracy * 100:.2f}%")

    # Saving and loading state dict
    checkpoint = {"model_state_dict": model.state_dict()}
    new_model = MultiLayerPerceptron(input_dim=input_dim, hidden_dim=64, num_classes=num_classes)
    new_model.load_state_dict(checkpoint["model_state_dict"])
    new_model.eval()
    
    with torch.no_grad():
        new_preds = torch.argmax(new_model(X), dim=-1)
        assert torch.equal(predictions, new_preds), "Loaded model state dict mismatch!"
    
    print("Checkpoint Saved & Restored Successfully!")
    print("✅ PASS: Multi-Layer Perceptron (MLP) Completed!")


if __name__ == "__main__":
    demo_mlp_training()
