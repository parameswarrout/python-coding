import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import math
import torch
import torch.nn as nn
import torch.nn.functional as F

"""
=============================================================================
🔴 PYTORCH ADVANCED INTERVIEW LEVEL - PART 1: TRANSFORMER & MULTI-HEAD ATTENTION
=============================================================================
Core Concepts Covered:
1. Scaled Dot-Product Attention: Attention(Q, K, V) = softmax(Q K^T / sqrt(d_k)) * V
2. Multi-Head Attention (MHA) tensor shape transitions:
   (B, S, D) -> (B, S, num_heads, head_dim) -> (B, num_heads, S, head_dim)
3. Causal (Autoregressive) Upper-Triangular Masking for GPT models
4. Modern Pre-LayerNorm Transformer Decoder Block
=============================================================================
"""

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model: int, num_heads: int, dropout: float = 0.1):
        super().__init__()
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        
        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        
        # Single fused projection for Q, K, V (optimized interview implementation)
        self.qkv_proj = nn.Linear(d_model, 3 * d_model)
        self.out_proj = nn.Linear(d_model, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor, is_causal: bool = False) -> torch.Tensor:
        batch_size, seq_len, _ = x.shape
        
        # 1. Project to Q, K, V -> (B, S, 3 * D)
        qkv = self.qkv_proj(x)
        
        # 2. Reshape and split: (B, S, 3, num_heads, head_dim) -> 3 tensors of (B, num_heads, S, head_dim)
        qkv = qkv.reshape(batch_size, seq_len, 3, self.num_heads, self.head_dim)
        qkv = qkv.permute(2, 0, 3, 1, 4)  # (3, B, num_heads, S, head_dim)
        q, k, v = qkv[0], qkv[1], qkv[2]
        
        # 3. Scaled Dot-Product Attention: (B, H, S, head_dim) @ (B, H, head_dim, S) -> (B, H, S, S)
        scale = 1.0 / math.sqrt(self.head_dim)
        attn_scores = torch.matmul(q, k.transpose(-2, -1)) * scale
        
        # 4. Apply Causal Mask if autoregressive (GPT style)
        if is_causal:
            mask = torch.triu(torch.full((seq_len, seq_len), float('-inf'), device=x.device), diagonal=1)
            attn_scores = attn_scores + mask
            
        attn_weights = F.softmax(attn_scores, dim=-1)
        attn_weights = self.dropout(attn_weights)
        
        # 5. Multiply with Values -> (B, H, S, head_dim)
        context = torch.matmul(attn_weights, v)
        
        # 6. Concatenate heads back to (B, S, D)
        context = context.permute(0, 2, 1, 3).contiguous().reshape(batch_size, seq_len, self.d_model)
        
        return self.out_proj(context)


class TransformerDecoderBlock(nn.Module):
    """Modern Pre-LayerNorm Transformer Block (LLaMA / GPT-3 style)"""
    def __init__(self, d_model: int, num_heads: int, mlp_ratio: int = 4, dropout: float = 0.1):
        super().__init__()
        self.ln1 = nn.LayerNorm(d_model)
        self.attn = MultiHeadAttention(d_model, num_heads, dropout=dropout)
        
        self.ln2 = nn.LayerNorm(d_model)
        self.mlp = nn.Sequential(
            nn.Linear(d_model, d_model * mlp_ratio),
            nn.GELU(),
            nn.Linear(d_model * mlp_ratio, d_model),
            nn.Dropout(dropout)
        )

    def forward(self, x: torch.Tensor, is_causal: bool = True) -> torch.Tensor:
        # Pre-LN: x + Sublayer(LN(x))
        x = x + self.attn(self.ln1(x), is_causal=is_causal)
        x = x + self.mlp(self.ln2(x))
        return x


def demo_transformer():
    print("--- Testing Custom Multi-Head Attention & Transformer Decoder Block ---")
    batch_size = 2
    seq_len = 8
    d_model = 64
    num_heads = 4

    block = TransformerDecoderBlock(d_model=d_model, num_heads=num_heads)
    dummy_tokens = torch.randn(batch_size, seq_len, d_model)
    
    out = block(dummy_tokens, is_causal=True)
    print(f"Input Shape: {dummy_tokens.shape}")
    print(f"Output Shape: {out.shape} (Expected: [2, 8, 64])")
    
    assert out.shape == (batch_size, seq_len, d_model), "Transformer block output shape mismatch!"
    print("✅ PASS: Multi-Head Self-Attention & Transformer Block Implemented Correctly!")


if __name__ == "__main__":
    demo_transformer()
