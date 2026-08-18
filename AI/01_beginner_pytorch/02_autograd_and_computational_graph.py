import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import torch

"""
=============================================================================
🟢 PYTORCH BEGINNER LEVEL - PART 2: AUTOGRAD & COMPUTATIONAL GRAPH
=============================================================================
Core Concepts Covered:
1. Dynamic Computational Graph (DAG - Directed Acyclic Graph)
2. `requires_grad=True`, Leaf nodes vs Non-leaf nodes
3. The `.backward()` engine, `.grad` accumulation, and `.grad.zero_()`
4. `retain_graph=True` and its memory implications
5. Disabling gradient tracking (`torch.no_grad()`, `torch.inference_mode()`, `.detach()`)
6. Interview Challenge: Manual Gradient Descent on Polynomial Function
=============================================================================
"""

def demo_basic_autograd():
    print("--- 1. Basic Autograd & Gradient Calculation ---")
    # Equation: y = 2 * x^2 + 3 * x + 1
    # dy/dx = 4 * x + 3
    x = torch.tensor(3.0, requires_grad=True)
    y = 2 * (x ** 2) + 3 * x + 1
    
    # Backpropagation
    y.backward()
    
    print(f"For x = 3.0, dy/dx computed by autograd = {x.grad.item()}")
    print(f"Analytical gradient: 4*(3) + 3 = {4 * 3.0 + 3.0}")
    assert x.grad.item() == 15.0, "Gradient mismatch!"


def demo_gradient_accumulation():
    print("\n--- 2. Gradient Accumulation Gotcha ---")
    x = torch.tensor(2.0, requires_grad=True)
    
    # Pass 1
    y1 = x ** 2  # dy1/dx = 2*x = 4
    y1.backward()
    print(f"After pass 1: x.grad = {x.grad.item()}")  # 4.0
    
    # Pass 2 WITHOUT zeroing grad: Gradients will SUM up!
    y2 = x ** 3  # dy2/dx = 3*x^2 = 12
    y2.backward()
    print(f"After pass 2 (accumulated): x.grad = {x.grad.item()}")  # 4 + 12 = 16.0
    
    # Proper practice: Zero gradients before next pass
    x.grad.zero_()
    print(f"After x.grad.zero_(): x.grad = {x.grad.item()}")  # 0.0


def demo_inference_modes():
    print("\n--- 3. Inference Modes (no_grad vs inference_mode) ---")
    x = torch.randn(3, 3, requires_grad=True)
    
    with torch.no_grad():
        y = x * 2
        print(f"Inside torch.no_grad(), y.requires_grad = {y.requires_grad}")  # False
        
    with torch.inference_mode():
        # torch.inference_mode() provides better speed and memory savings than torch.no_grad()
        z = x * 3
        print(f"Inside torch.inference_mode(), z.requires_grad = {z.requires_grad}")  # False
        
    # Detach creates a new tensor that shares storage but detaches from computation history
    detached_x = x.detach()
    print(f"detached_x requires_grad: {detached_x.requires_grad}")


# =============================================================================
# INTERVIEW CODING CHALLENGE: MANUAL GRADIENT DESCENT OPTIMIZATION
# =============================================================================
def interview_challenge_optimize_quadratic(target_val=9.0, lr=0.01, steps=200):
    """
    Challenge: Find `x` that minimizes the loss L = (x^2 - target_val)^2 using ONLY autograd.
    Target: x -> sqrt(target_val)
    """
    x = torch.tensor(1.0, requires_grad=True)
    
    for step in range(steps):
        loss = (x ** 2 - target_val) ** 2
        loss.backward()
        
        # In-place parameter update without tracking the update in the computation graph!
        with torch.no_grad():
            x -= lr * x.grad
            x.grad.zero_()
            
    return x.item()


def run_tests():
    demo_basic_autograd()
    demo_gradient_accumulation()
    demo_inference_modes()
    
    print("\n--- Running Optimization Challenge ---")
    optimized_x = interview_challenge_optimize_quadratic(target_val=9.0)
    print(f"Target: sqrt(9.0) = 3.0. Found: {optimized_x:.4f}")
    assert abs(optimized_x - 3.0) < 1e-2, "Optimization did not converge accurately!"
    print("✅ PASS: Autograd & Computation Graph Mastered!")


if __name__ == "__main__":
    run_tests()
