import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import torch
import torch.nn as nn
import torch.nn.functional as F

"""
=============================================================================
🔴 PYTORCH ADVANCED INTERVIEW LEVEL - PART 2: CUSTOM AUTOGRAD & CUSTOM LOSSES
=============================================================================
Core Concepts Covered:
1. Writing custom C++/Python autograd operations with `torch.autograd.Function`
   - `save_for_backward(ctx)`
   - Writing analytical `forward()` and `backward()`
   - Gradient checking with `torch.autograd.gradcheck`
2. Focal Loss Implementation (Lin et al. - RetinaNet)
   FL(p_t) = - alpha_t * (1 - p_t)^gamma * log(p_t)
3. InfoNCE Contrastive Loss (SimCLR / CLIP representation learning)
=============================================================================
"""

# =============================================================================
# 1. CUSTOM AUTOGRAD FUNCTION: CUBIC ACTIVATION (y = x^3)
# =============================================================================
class CubicActivationFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x: torch.Tensor) -> torch.Tensor:
        # ctx is context object used to stash tensors for backward pass
        ctx.save_for_backward(x)
        return x ** 3

    @staticmethod
    def backward(ctx, grad_output: torch.Tensor) -> torch.Tensor:
        # Chain rule: dL/dx = (dL/dy) * (dy/dx) = grad_output * (3 * x^2)
        x, = ctx.saved_tensors
        grad_input = grad_output * (3 * (x ** 2))
        return grad_input


def cubic_act(x):
    return CubicActivationFunction.apply(x)


# =============================================================================
# 2. FOCAL LOSS (CLASS IMBALANCE & HARD NEGATIVE MINING)
# =============================================================================
class FocalLoss(nn.Module):
    """
    Focal Loss down-weights easy examples and focuses training on hard negatives.
    FL(p_t) = - alpha * (1 - p_t)^gamma * log(p_t)
    """
    def __init__(self, alpha: float = 0.25, gamma: float = 2.0, reduction: str = 'mean'):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.reduction = reduction

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        # 1. Standard Binary Cross Entropy with Logits
        bce_loss = F.binary_cross_entropy_with_logits(logits, targets, reduction='none')
        
        # 2. Calculate p_t
        probs = torch.sigmoid(logits)
        p_t = targets * probs + (1 - targets) * (1 - probs)
        
        # 3. Modulating factor: (1 - p_t)^gamma
        modulating_factor = (1.0 - p_t) ** self.gamma
        
        # 4. Alpha weighting
        alpha_factor = targets * self.alpha + (1 - targets) * (1 - self.alpha)
        
        focal_loss = alpha_factor * modulating_factor * bce_loss
        
        if self.reduction == 'mean':
            return focal_loss.mean()
        elif self.reduction == 'sum':
            return focal_loss.sum()
        return focal_loss


# =============================================================================
# 3. INFONCE CONTRASTIVE LOSS (SIMCLR / CLIP)
# =============================================================================
def info_nce_loss(query: torch.Tensor, positive: torch.Tensor, negatives: torch.Tensor, temperature: float = 0.07) -> torch.Tensor:
    """
    query: (Batch, Dim)
    positive: (Batch, Dim)
    negatives: (Batch, Num_Negatives, Dim)
    """
    # Normalize embeddings to unit hypersphere
    q = F.normalize(query, dim=-1)
    pos = F.normalize(positive, dim=-1)
    neg = F.normalize(negatives, dim=-1)
    
    # 1. Positive similarity: (Batch, 1)
    pos_sim = torch.sum(q * pos, dim=-1, keepdim=True) / temperature
    
    # 2. Negative similarity: (Batch, Num_Negatives)
    neg_sim = torch.bmm(neg, q.unsqueeze(-1)).squeeze(-1) / temperature
    
    # 3. Concatenate: [pos_sim, neg_sim] -> shape (Batch, 1 + Num_Negatives)
    logits = torch.cat([pos_sim, neg_sim], dim=1)
    
    # Target is always index 0 (the positive match)
    labels = torch.zeros(query.size(0), dtype=torch.long, device=query.device)
    
    return F.cross_entropy(logits, labels)


def demo_custom_autograd_and_losses():
    print("--- 1. Testing Custom Autograd Function (Cubic Activation) ---")
    x = torch.tensor([2.0, 3.0], dtype=torch.double, requires_grad=True)
    y = cubic_act(x)
    y.sum().backward()
    
    expected_grad = 3 * (x.detach() ** 2)
    print(f"Computed Grad: {x.grad}, Expected: {expected_grad}")
    assert torch.allclose(x.grad, expected_grad), "Custom backward gradient error!"

    # Gradient check with finite differences
    test_tensor = torch.randn(3, dtype=torch.double, requires_grad=True)
    is_valid = torch.autograd.gradcheck(cubic_act, test_tensor, eps=1e-6, atol=1e-4)
    print(f"torch.autograd.gradcheck status: {is_valid}")
    assert is_valid, "Gradcheck failed!"

    print("\n--- 2. Testing Focal Loss ---")
    fl = FocalLoss(alpha=0.25, gamma=2.0)
    logits = torch.tensor([[2.0], [-2.0], [0.5]])
    targets = torch.tensor([[1.0], [0.0], [1.0]])
    loss_val = fl(logits, targets)
    print(f"Focal Loss: {loss_val.item():.4f}")
    assert loss_val.item() > 0, "Focal Loss should be positive!"

    print("\n--- 3. Testing InfoNCE Contrastive Loss ---")
    B, D, N_neg = 4, 16, 5
    q = torch.randn(B, D)
    pos = q + 0.1 * torch.randn(B, D)  # Close positive pair
    neg = torch.randn(B, N_neg, D)      # Random negatives
    
    contrastive_loss = info_nce_loss(q, pos, neg)
    print(f"InfoNCE Loss: {contrastive_loss.item():.4f}")
    
    print("\n✅ PASS: Custom Autograd, Focal Loss & Contrastive Loss Mastered!")


if __name__ == "__main__":
    demo_custom_autograd_and_losses()
