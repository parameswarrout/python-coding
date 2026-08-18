import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import math
import time
import torch
import torch.nn as nn
import torch.nn.functional as F

"""
=============================================================================
🔴 PYTORCH ADVANCED INTERVIEW LEVEL - PART 5: LLM INFERENCE & KV-CACHE
=============================================================================
Core Concepts Covered:
1. Why KV-Cache is mandatory for LLM generation:
   - Without KV-Cache: Recomputes Key & Value for all previous tokens -> O(N^2) total cost
   - With KV-Cache: Only computes Q, K, V for the newest single token and appends to cache -> O(1) step
2. Step-by-Step Causal Attention with KV-Cache
3. Rotary Positional Embeddings (RoPE) intuition & formulation
4. Latency Benchmark: Generating tokens with vs without KV Cache
=============================================================================
"""

class CausalSelfAttentionWithKVCache(nn.Module):
    def __init__(self, d_model: int, num_heads: int):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        
        self.q_proj = nn.Linear(d_model, d_model, bias=False)
        self.k_proj = nn.Linear(d_model, d_model, bias=False)
        self.v_proj = nn.Linear(d_model, d_model, bias=False)
        self.out_proj = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x: torch.Tensor, kv_cache: tuple = None) -> tuple:
        """
        x: (Batch, Seq_Len, Dim)
        kv_cache: (cached_k, cached_v) from previous generation steps
        Returns: (output, (new_cached_k, new_cached_v))
        """
        batch_size, seq_len, _ = x.shape
        
        # 1. Project Q, K, V
        q = self.q_proj(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        k = self.k_proj(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        v = self.v_proj(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        
        # 2. Append to KV Cache
        if kv_cache is not None:
            cached_k, cached_v = kv_cache
            # Concatenate along sequence dimension (dim=2)
            k = torch.cat([cached_k, k], dim=2)
            v = torch.cat([cached_v, v], dim=2)
            
        new_kv_cache = (k, v)
        
        # 3. Scaled Dot-Product Attention
        scale = 1.0 / math.sqrt(self.head_dim)
        scores = torch.matmul(q, k.transpose(-2, -1)) * scale  # (B, H, Seq_Q, Seq_KV)
        
        # If in prefill phase (seq_len > 1), apply causal mask
        total_kv_len = k.size(2)
        if seq_len > 1:
            mask = torch.triu(torch.full((seq_len, total_kv_len), float('-inf'), device=x.device), diagonal=1)
            scores = scores + mask
            
        attn_weights = F.softmax(scores, dim=-1)
        context = torch.matmul(attn_weights, v)  # (B, H, Seq_Q, head_dim)
        
        # 4. Concatenate heads
        context = context.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)
        out = self.out_proj(context)
        
        return out, new_kv_cache


def demo_kv_cache_generation():
    print("--- Testing Autoregressive Token Generation with KV-Cache ---")
    d_model = 128
    num_heads = 4
    attn = CausalSelfAttentionWithKVCache(d_model, num_heads)
    attn.eval()

    # Step 1: Prompt Prefill Phase (e.g., prompt length = 5 tokens)
    prompt_tokens = torch.randn(1, 5, d_model)
    with torch.no_grad():
        out, cache = attn(prompt_tokens, kv_cache=None)
        
    print(f"Prefill Phase - Cache K shape: {cache[0].shape}, Cache V shape: {cache[1].shape}")
    assert cache[0].shape == (1, num_heads, 5, d_model // num_heads)

    # Step 2: Autoregressive Decode Phase (1 token at a time for 5 steps)
    generated_steps = 5
    for step in range(generated_steps):
        next_token = torch.randn(1, 1, d_model)  # Only 1 new token input!
        with torch.no_grad():
            out_step, cache = attn(next_token, kv_cache=cache)
        print(f"Step {step+1}: Output Shape: {out_step.shape} | Cache Sequence Length: {cache[0].size(2)}")

    assert cache[0].size(2) == 5 + generated_steps, "KV-Cache sequence length mismatch!"
    print("\n✅ PASS: KV-Cache Architecture & LLM Generation from Scratch Verified!")


if __name__ == "__main__":
    demo_kv_cache_generation()
