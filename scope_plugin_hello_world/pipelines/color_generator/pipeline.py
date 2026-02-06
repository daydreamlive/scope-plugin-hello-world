from typing import TYPE_CHECKING

import torch

from scope.core.pipelines.interface import Pipeline

from .schema import ColorGeneratorConfig

if TYPE_CHECKING:
    from scope.core.pipelines.base_schema import BasePipelineConfig


class ColorGeneratorPipeline(Pipeline):
    """Generates solid color frames."""

    @classmethod
    def get_config_class(cls) -> type["BasePipelineConfig"]:
        return ColorGeneratorConfig

    def __init__(
        self,
        height: int = 512,
        width: int = 512,
        **kwargs,
    ):
        self.height = height
        self.width = width

    def __call__(self, **kwargs) -> dict:
        """Generate a solid color frame.

        Returns:
            Dict with "video" key containing tensor of shape (1, H, W, 3) in [0, 1] range.
        """
        # Read runtime parameters from kwargs (with defaults)
        color_r = kwargs.get("color_r", 128)
        color_g = kwargs.get("color_g", 128)
        color_b = kwargs.get("color_b", 128)

        # Create color tensor from current values
        color = torch.tensor([color_r / 255.0, color_g / 255.0, color_b / 255.0])

        # Create a single frame filled with our color
        frame = color.view(1, 1, 1, 3).expand(1, self.height, self.width, 3)
        return {"video": frame.clone()}
