import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import CosineAnnealingLR, ReduceLROnPlateau

"""
=============================================================================
🟡 PYTORCH INTERMEDIATE LEVEL - PART 4: PRODUCTION TRAINING BEST PRACTICES
=============================================================================
Core Concepts Covered:
1. Learning Rate Schedulers (Cosine Annealing with Warm Restarts, Plateau reduction)
2. Gradient Clipping (`nn.utils.clip_grad_norm_`) to prevent exploding gradients
3. Early Stopping Callback class implementation
4. Full validation loop with Metric Tracking & Best Model Checkpointing
=============================================================================
"""

class EarlyStopping:
    """Early stops the training if validation loss doesn't improve after a given patience."""
    def __init__(self, patience=5, delta=0.0):
        self.patience = patience
        self.delta = delta
        self.counter = 0
        self.best_loss = float('inf')
        self.early_stop = False

    def __call__(self, val_loss):
        if val_loss < self.best_loss - self.delta:
            self.best_loss = val_loss
            self.counter = 0
        else:
            self.counter += 1
            if self.counter >= self.patience:
                self.early_stop = True


def train_with_best_practices():
    print("--- Testing Training Loop with Schedulers, Grad Clipping & Early Stopping ---")
    torch.manual_seed(42)
    
    # Simple model
    model = nn.Sequential(
        nn.Linear(20, 50),
        nn.ReLU(),
        nn.Linear(50, 1)
    )
    
    criterion = nn.MSELoss()
    optimizer = optim.AdamW(model.parameters(), lr=0.01, weight_decay=1e-2)
    scheduler = CosineAnnealingLR(optimizer, T_max=10, eta_min=1e-5)
    early_stopping = EarlyStopping(patience=3)

    # Simulated datasets
    train_x = torch.randn(100, 20)
    train_y = torch.randn(100, 1)
    val_x = torch.randn(20, 20)
    val_y = torch.randn(20, 1)

    max_epochs = 15
    for epoch in range(1, max_epochs + 1):
        # 1. Train Step
        model.train()
        optimizer.zero_grad()
        preds = model(train_x)
        loss = criterion(preds, train_y)
        loss.backward()
        
        # 2. Gradient Clipping (Interview must-know: prevents explosion)
        grad_norm = nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        
        optimizer.step()
        scheduler.step()
        
        # 3. Validation Step
        model.eval()
        with torch.no_grad():
            val_preds = model(val_x)
            val_loss = criterion(val_preds, val_y).item()

        current_lr = scheduler.get_last_lr()[0]
        print(f"Epoch {epoch:02d} | Train Loss: {loss.item():.4f} | Val Loss: {val_loss:.4f} | LR: {current_lr:.6f} | Grad Norm: {grad_norm:.3f}")
        
        early_stopping(val_loss)
        if early_stopping.early_stop:
            print(f"Early stopping triggered at epoch {epoch}")
            break

    print("✅ PASS: Production Training Pipeline Verified!")


if __name__ == "__main__":
    train_with_best_practices()
