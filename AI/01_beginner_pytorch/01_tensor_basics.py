import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import torch
import numpy as np

"""
=============================================================================
🟢 PYTORCH BEGINNER LEVEL - PART 1: TENSOR FUNDAMENTALS & OPERATIONS
=============================================================================
Core Concepts Covered:
1. Tensor Creation (zeros, ones, randn, arange, from_numpy)
2. Tensor Attributes (shape, dtype, device, layout)
3. Slicing, Indexing, and Broadcasting Rules
4. Shape Manipulation (view, reshape, transpose, permute, squeeze, unsqueeze)
5. Storage & Memory: Contiguous vs Non-Contiguous Tensors
6. Device Management (CPU <-> CUDA GPU)
=============================================================================
"""

# =============================================================================
# 1. TENSOR CREATION & DATA TYPES
# =============================================================================
def demo_creation():
    print("--- 1. Tensor Creation ---")
    # From Python list
    t_list = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)
    
    # Specific initializations
    t_zeros = torch.zeros((2, 3), dtype=torch.float32)
    t_ones = torch.ones((2, 3), dtype=torch.int32)
    t_randn = torch.randn((3, 3))  # Standard Normal (mean 0, var 1)
    t_arange = torch.arange(0, 10, step=2)  # [0, 2, 4, 6, 8]
    
    # Interoperability with NumPy (zero-copy memory sharing)
    np_arr = np.array([1, 2, 3])
    t_from_np = torch.from_numpy(np_arr)
    np_back = t_from_np.numpy()
    
    print(f"Tensor from list:\n{t_list}")
    print(f"Shape: {t_list.shape}, Dtype: {t_list.dtype}, Device: {t_list.device}")
    return t_list


# =============================================================================
# 2. BROADCASTING & ARITHMETIC OPERATIONS
# =============================================================================
def demo_broadcasting():
    print("\n--- 2. Broadcasting & Arithmetic ---")
    # Matrix A: (3, 1), Matrix B: (1, 4) -> Output: (3, 4)
    A = torch.tensor([[1], [2], [3]], dtype=torch.float32)
    B = torch.tensor([[10, 20, 30, 40]], dtype=torch.float32)
    C = A + B  # Broadcasting occurs along dimension 1 of A and dim 0 of B
    
    # Matrix Multiplication (@ or torch.matmul)
    M1 = torch.randn(2, 3)
    M2 = torch.randn(3, 4)
    matmul_res = torch.matmul(M1, M2)  # Shape: (2, 4)
    
    # In-place operations (denoted with trailing underscore `_`)
    t = torch.tensor([1.0, 2.0])
    t.add_(5.0)  # t becomes [6.0, 7.0] without allocating a new tensor
    
    print(f"Broadcasting (3,1) + (1,4) shape: {C.shape}")
    print(f"Matmul (2,3) @ (3,4) shape: {matmul_res.shape}")
    return C


# =============================================================================
# 3. RESHAPING, CONTIGUOUS MEMORY & PERMUTE (INTERVIEW ESSENTIAL)
# =============================================================================
def demo_memory_and_reshaping():
    print("\n--- 3. Reshaping, Transpose & Contiguous Memory ---")
    x = torch.arange(6)  # [0, 1, 2, 3, 4, 5]
    
    # view() requires contiguous memory; reshape() copies if not contiguous
    x_view = x.view(2, 3)
    
    # Transposing / Permuting makes the memory layout non-contiguous!
    x_t = x_view.t()  # shape (3, 2), is_contiguous() is False
    print(f"Is x_t contiguous? {x_t.is_contiguous()}")
    
    # Calling .view() on non-contiguous tensor raises RuntimeError:
    # x_t.view(6) -> ERROR!
    # Fix: Use .contiguous().view() or .reshape()
    x_fixed = x_t.contiguous().view(6)
    print(f"Fixed with .contiguous().view(6): {x_fixed}")
    
    # Unsqueeze (add dim) & Squeeze (remove singleton dim)
    t = torch.tensor([1, 2, 3])  # (3,)
    t_unsqueezed = t.unsqueeze(0)  # (1, 3) - batch dimension
    t_squeezed = t_unsqueezed.squeeze(0)  # (3,)
    
    return x_fixed


# =============================================================================
# 4. INTERVIEW CODING CHALLENGE & SOLUTION
# =============================================================================
def interview_challenge_batch_cosine_similarity(A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
    """
    Challenge: Implement Batch Cosine Similarity from scratch without using torch.nn.functional.cosine_similarity.
    Given:
      A: (Batch_Size, Dim)
      B: (Batch_Size, Dim)
    Returns:
      Cosine similarity scores of shape (Batch_Size,)
      Formula: cos_sim(a, b) = (a . b) / (||a||_2 * ||b||_2 + eps)
    """
    eps = 1e-8
    # Dot product along feature dimension
    dot_product = (A * B).sum(dim=-1)
    
    # L2 norms
    norm_a = torch.norm(A, p=2, dim=-1)
    norm_b = torch.norm(B, p=2, dim=-1)
    
    # Cosine similarity
    similarity = dot_product / (norm_a * norm_b + eps)
    return similarity


def run_tests():
    demo_creation()
    demo_broadcasting()
    demo_memory_and_reshaping()
    
    # Test Interview Challenge
    print("\n--- Running Tests for Interview Challenge ---")
    A = torch.tensor([[1.0, 0.0], [1.0, 1.0]], dtype=torch.float32)
    B = torch.tensor([[1.0, 0.0], [0.0, 1.0]], dtype=torch.float32)
    
    res = interview_challenge_batch_cosine_similarity(A, B)
    expected = torch.nn.functional.cosine_similarity(A, B)
    
    assert torch.allclose(res, expected, atol=1e-5), f"Expected {expected}, got {res}"
    print(f"Cosine Similarity Result: {res}")
    print("✅ PASS: Tensor Basics & Cosine Similarity Challenge Verified Successfully!")


if __name__ == "__main__":
    run_tests()
