import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import torch
import torch.nn as nn
import torch.optim as optim

"""
=============================================================================
🟢 PYTORCH BEGINNER LEVEL - PART 3: LINEAR & LOGISTIC REGRESSION
=============================================================================
Core Concepts Covered:
1. End-to-End Training Loop: Forward Pass -> Loss -> Backward -> Optimizer Step -> Zero Grad
2. Linear Regression (Continuous targets, MSE Loss)
3. Logistic Regression (Binary classification, Sigmoid vs BCEWithLogitsLoss numerical stability)
4. Evaluation Metrics (Accuracy, Precision, Binary Cross Entropy)
=============================================================================
"""

# =============================================================================
# 1. LINEAR REGRESSION (y = W*x + b)
# =============================================================================
class LinearRegressionModel(nn.Module):
    def __init__(self, input_dim: int, output_dim: int):
        super().__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.linear(x)


def train_linear_regression():
    print("--- 1. Training Linear Regression ---")
    # Synthetic Data: y = 3.5 * x + 1.2 + noise
    torch.manual_seed(42)
    X = torch.randn(100, 1)
    true_w = 3.5
    true_b = 1.2
    y = true_w * X + true_b + 0.1 * torch.randn(100, 1)

    model = LinearRegressionModel(input_dim=1, output_dim=1)
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.05)

    # Standard Training Loop
    epochs = 100
    for epoch in range(epochs):
        model.train()
        
        # 1. Forward pass
        predictions = model(X)
        loss = criterion(predictions, y)
        
        # 2. Backward pass
        optimizer.zero_grad()
        loss.backward()
        
        # 3. Parameter update
        optimizer.step()

    learned_w = model.linear.weight.item()
    learned_b = model.linear.bias.item()
    print(f"Target: w={true_w}, b={true_b} | Learned: w={learned_w:.3f}, b={learned_b:.3f}")
    assert abs(learned_w - true_w) < 0.2, "Linear regression failed to learn weight!"
    assert abs(learned_b - true_b) < 0.2, "Linear regression failed to learn bias!"
    print("Linear Regression trained successfully!")


# =============================================================================
# 2. LOGISTIC REGRESSION (Binary Classification)
# =============================================================================
class LogisticRegressionModel(nn.Module):
    def __init__(self, input_features: int):
        super().__init__()
        self.linear = nn.Linear(input_features, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Note: Return raw logits for BCEWithLogitsLoss to avoid numerical underflow/overflow
        return self.linear(x)


def train_logistic_regression():
    print("\n--- 2. Training Logistic Regression ---")
    torch.manual_seed(42)
    # Generate 2D binary classification data
    X_pos = torch.randn(50, 2) + 2.0
    X_neg = torch.randn(50, 2) - 2.0
    X = torch.cat([X_pos, X_neg], dim=0)
    y = torch.cat([torch.ones(50, 1), torch.zeros(50, 1)], dim=0)

    model = LogisticRegressionModel(input_features=2)
    # BCEWithLogitsLoss combines Sigmoid + BCELoss using log-sum-exp trick for stability
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.1)

    for epoch in range(100):
        model.train()
        logits = model(X)
        loss = criterion(logits, y)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Evaluation
    model.eval()
    with torch.no_grad():
        test_logits = model(X)
        probs = torch.sigmoid(test_logits)
        preds = (probs >= 0.5).float()
        accuracy = (preds == y).float().mean().item()

    print(f"Binary Classification Accuracy: {accuracy * 100:.2f}%")
    assert accuracy > 0.95, "Logistic regression accuracy too low!"
    print("Logistic Regression trained successfully!")


if __name__ == "__main__":
    train_linear_regression()
    train_logistic_regression()
    print("\n✅ PASS: Linear and Logistic Regression Solved!")
