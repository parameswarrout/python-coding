import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import torch
import torch.nn as nn
import torch.nn.functional as F

"""
=============================================================================
🟡 PYTORCH INTERMEDIATE LEVEL - PART 2: CONVOLUTIONAL NETWORKS & RESIDUAL BLOCKS
=============================================================================
Core Concepts Covered:
1. Conv2d output dimension formula:
   H_out = floor((H_in + 2*padding - dilation*(kernel_size - 1) - 1)/stride + 1)
2. Building BasicBlock & Bottleneck Residual Blocks from scratch (ResNet)
3. 1x1 Convolutions for channel projection in skip connections
4. Global Average Pooling (GAP) vs Flattening
=============================================================================
"""

class ResidualBlock(nn.Module):
    """
    Standard ResNet Residual Block with Skip Connection:
    F(x) + x  (or F(x) + Conv1x1(x) if downsampling/channel expansion occurs)
    """
    def __init__(self, in_channels: int, out_channels: int, stride: int = 1):
        super().__init__()
        
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)
        
        # Shortcut / Skip Connection projection
        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels)
            )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        identity = self.shortcut(x)
        
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        
        out = self.conv2(out)
        out = self.bn2(out)
        
        # Residual addition before non-linearity
        out += identity
        out = self.relu(out)
        return out


class MiniResNet(nn.Module):
    """Miniature ResNet Architecture for Image Classification"""
    def __init__(self, in_channels: int = 3, num_classes: int = 10):
        super().__init__()
        
        self.stem = nn.Sequential(
            nn.Conv2d(in_channels, 32, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True)
        )
        
        self.layer1 = ResidualBlock(32, 32, stride=1)
        self.layer2 = ResidualBlock(32, 64, stride=2)  # Downsamples spatial dim by 2
        
        self.gap = nn.AdaptiveAvgPool2d((1, 1))  # Global Average Pooling -> (B, 64, 1, 1)
        self.fc = nn.Linear(64, num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out = self.stem(x)
        out = self.layer1(out)
        out = self.layer2(out)
        out = self.gap(out)
        out = torch.flatten(out, 1)  # (B, 64)
        out = self.fc(out)
        return out


def demo_cnn():
    print("--- Testing Mini-ResNet & Residual Block Architecture ---")
    model = MiniResNet(in_channels=3, num_classes=10)
    
    # Input batch: 4 images of size 3x32x32
    dummy_input = torch.randn(4, 3, 32, 32)
    output_logits = model(dummy_input)
    
    print(f"Input Shape: {dummy_input.shape}")
    print(f"Output Logits Shape: {output_logits.shape} (Expected: [4, 10])")
    
    assert output_logits.shape == (4, 10), "Output shape mismatch!"
    
    # Verify gradient backprop through residual connections
    loss = output_logits.sum()
    loss.backward()
    
    for name, param in model.named_parameters():
        assert param.grad is not None, f"Gradient not computed for {name}"
        
    print("✅ PASS: Mini-ResNet & Residual Connections Verified!")


if __name__ == "__main__":
    demo_cnn()
