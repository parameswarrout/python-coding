import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import torch
import torch.nn as nn
import torch.optim as optim

"""
=============================================================================
🔴 PYTORCH ADVANCED INTERVIEW LEVEL - PART 4: MIXED PRECISION & DISTRIBUTED
=============================================================================
Core Concepts Covered:
1. Automatic Mixed Precision (AMP - FP16 / BF16) with `torch.amp.autocast`
2. `torch.cuda.amp.GradScaler` (or `torch.amp.GradScaler`):
   - Dynamic loss scaling to prevent FP16 gradient underflow
   - Skipping optimizer steps when Inf/NaN gradients are detected
3. Distributed Training Architecture:
   - DataParallel (DP - Single process, GIL bottleneck) vs 
     DistributedDataParallel (DDP - Multi-process, Ring-AllReduce)
   - ZeRO / Fully Sharded Data Parallel (FSDP) memory stages:
     Stage 1: Shard Optimizer States (4x memory reduction)
     Stage 2: Shard Gradients (8x memory reduction)
     Stage 3: Shard Parameters (Linear memory reduction with N GPUs)
=============================================================================
"""

def demo_mixed_precision():
    print("--- 1. Automatic Mixed Precision (AMP) & GradScaler ---")
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Running on device: {device}")
    
    model = nn.Sequential(
        nn.Linear(128, 256),
        nn.ReLU(),
        nn.Linear(256, 10)
    ).to(device)
    
    optimizer = optim.AdamW(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()
    
    # GradScaler is used when training on CUDA with FP16
    device_type = 'cuda' if torch.cuda.is_available() else 'cpu'
    scaler = torch.amp.GradScaler(device_type, enabled=(device_type == 'cuda'))

    dummy_x = torch.randn(32, 128, device=device)
    dummy_y = torch.randint(0, 10, (32,), device=device)

    # 1. Forward pass under autocast (casts operations to float16/bfloat16)
    with torch.amp.autocast(device_type=device_type, dtype=torch.float16 if device_type == 'cuda' else torch.bfloat16):
        logits = model(dummy_x)
        loss = criterion(logits, dummy_y)

    # 2. Backward pass with scaled loss
    optimizer.zero_grad()
    scaler.scale(loss).backward()
    
    # 3. Unscale and update parameters (skips update if inf/nan detected)
    scaler.step(optimizer)
    scaler.update()

    print(f"AMP Step Loss: {loss.item():.4f}")
    print("Mixed Precision Forward & Scaled Backward executed successfully!")


def print_distributed_interview_cheatsheet():
    print("\n--- 2. Distributed Training (DDP vs DP vs FSDP) Cheatsheet ---")
    print("""
    ┌───────────────────────┬──────────────────────────┬─────────────────────────────┐
    │ Architecture          │ Mechanism                │ Key Interview Insight       │
    ├───────────────────────┼──────────────────────────┼─────────────────────────────┤
    │ DataParallel (DP)     │ Single process multi-gpu │ Python GIL bottleneck, slow │
    │ DistributedData (DDP) │ Multi-process, NCCL ring │ Fast, gradient all-reduce   │
    │ FSDP / ZeRO Stage 1   │ Shards optimizer states  │ Saves 4x memory             │
    │ FSDP / ZeRO Stage 2   │ Shards opt states + grad │ Saves 8x memory             │
    │ FSDP / ZeRO Stage 3   │ Shards everything        │ Trains 70B+ LLMs across GPUs│
    └───────────────────────┴──────────────────────────┴─────────────────────────────┘
    """)
    print("✅ PASS: Mixed Precision & Distributed Training Architecture Mastered!")


if __name__ == "__main__":
    demo_mixed_precision()
    print_distributed_interview_cheatsheet()
