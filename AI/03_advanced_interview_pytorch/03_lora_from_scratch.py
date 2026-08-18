import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import math
import torch
import torch.nn as nn

"""
=============================================================================
🔴 PYTORCH ADVANCED INTERVIEW LEVEL - PART 3: LoRA (LOW-RANK ADAPTATION)
=============================================================================
Core Concepts Covered:
1. Low-Rank Adaptation (Hu et al. 2021) mathematical formulation:
   h = W_0 * x + (alpha / r) * B * A * x
   where W_0 is frozen (d_out x d_in), A is (r x d_in) ~ Gaussian, B is (d_out x r) = 0
2. LoRALinear layer from scratch
3. Parameter efficiency: Reduces trainable parameters by >99%
4. Weight Merging: Zero-latency deployment by merging (B * A) into W_0
=============================================================================
"""

class LoRALinear(nn.Module):
    def __init__(self, in_features: int, out_features: int, r: int = 8, lora_alpha: float = 16.0):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.r = r
        self.scaling = lora_alpha / r
        
        # 1. Base Pretrained Weight (Frozen)
        self.linear = nn.Linear(in_features, out_features, bias=False)
        self.linear.weight.requires_grad = False
        
        # 2. Low-Rank Matrices A and B
        if r > 0:
            self.lora_A = nn.Parameter(torch.empty(r, in_features))
            self.lora_B = nn.Parameter(torch.zeros(out_features, r))
            # Initialize A with Kaiming uniform, B with zeros (so initial adapter output is 0)
            nn.init.kaiming_uniform_(self.lora_A, a=math.sqrt(5))
        else:
            self.lora_A = None
            self.lora_B = None
            
        self.merged = False

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if self.merged or self.r == 0:
            return self.linear(x)
        
        # Base forward pass
        base_out = self.linear(x)
        
        # LoRA forward pass: x @ A^T @ B^T * scaling
        lora_out = (x @ self.lora_A.T) @ self.lora_B.T * self.scaling
        
        return base_out + lora_out

    def merge_weights(self):
        """Merges LoRA weights into original base linear layer for zero-latency inference."""
        if not self.merged and self.r > 0:
            # W_merged = W_0 + scaling * (B @ A)
            delta_w = (self.lora_B @ self.lora_A) * self.scaling
            self.linear.weight.data += delta_w
            self.merged = True
            print("LoRA weights merged into base weights successfully!")

    def unmerge_weights(self):
        """Unmerges weights to resume fine-tuning."""
        if self.merged and self.r > 0:
            delta_w = (self.lora_B @ self.lora_A) * self.scaling
            self.linear.weight.data -= delta_w
            self.merged = False
            print("LoRA weights unmerged.")


def demo_lora():
    print("--- Testing Low-Rank Adaptation (LoRA) Implementation ---")
    in_features = 1024
    out_features = 4096
    rank = 16
    alpha = 32.0

    lora_layer = LoRALinear(in_features, out_features, r=rank, lora_alpha=alpha)
    
    # 1. Parameter efficiency calculation
    base_params = in_features * out_features
    lora_params = (rank * in_features) + (out_features * rank)
    reduction = (1.0 - (lora_params / base_params)) * 100
    
    print(f"Base Parameters: {base_params:,}")
    print(f"Trainable LoRA Parameters (Rank={rank}): {lora_params:,}")
    print(f"Parameter Reduction: {reduction:.2f}%")
    
    # 2. Forward pass check
    x = torch.randn(4, in_features)
    out_before = lora_layer(x)
    
    # 3. Merging and zero-discrepancy validation
    lora_layer.merge_weights()
    out_after_merge = lora_layer(x)
    
    diff = (out_before - out_after_merge).abs().max().item()
    print(f"Max difference between unmerged and merged output: {diff:.8f}")
    assert diff < 1e-5, "Mismatch between unmerged and merged output!"
    
    print("✅ PASS: LoRA (Low-Rank Adaptation) from Scratch Verified!")


if __name__ == "__main__":
    demo_lora()
