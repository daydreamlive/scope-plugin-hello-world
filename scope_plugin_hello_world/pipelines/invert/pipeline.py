from typing import TYPE_CHECKING

import torch

from scope.core.pipelines.interface import Pipeline, Requirements

from .schema import InvertConfig

if TYPE_CHECKING:
    from scope.core.pipelines.base_schema import BasePipelineConfig


class InvertPipeline(Pipeline):
    """Inverts the colors of input video frames."""

    @classmethod
    def get_config_class(cls) -> type["BasePipelineConfig"]:
        return InvertConfig

    def __init__(
        self,
        device: torch.device | None = None,
        **kwargs,
    ):
        self.device = (
            device
            if device is not None
            else torch.device("cuda" if torch.cuda.is_available() else "cpu")
        )

    def prepare(self, **kwargs) -> Requirements:
        """Declare that we need 1 input frame."""
        return Requirements(input_size=1)

    def __call__(self, **kwargs) -> dict:
        """Invert the colors of input frames.

        Args:
            video: List of input frame tensors, each (1, H, W, C) in [0, 255] range.

        Returns:
            Dict with "video" key containing inverted frames in [0, 1] range.
        """
        video = kwargs.get("video")
        if video is None:
            raise ValueError("Input video cannot be None for InvertPipeline")

        # Read runtime parameter from kwargs (with default)
        intensity = kwargs.get("intensity", 1.0)

        frames = torch.stack([frame.squeeze(0) for frame in video], dim=0)
        frames = frames.to(device=self.device, dtype=torch.float32) / 255.0

        # Invert with intensity blending
        inverted = 1.0 - frames
        result = frames * (1 - intensity) + inverted * intensity

        return {"video": result.clamp(0, 1)}
