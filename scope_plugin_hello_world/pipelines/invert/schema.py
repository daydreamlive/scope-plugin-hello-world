from pydantic import Field

from scope.core.pipelines.base_schema import (
    BasePipelineConfig,
    ModeDefaults,
    ui_field_config,
)


class InvertConfig(BasePipelineConfig):
    """Configuration for the Invert Colors pipeline."""

    pipeline_id = "invert"
    pipeline_name = "Invert Colors"
    pipeline_description = "Inverts the colors of input video frames"
    supports_prompts = False
    modes = {"video": ModeDefaults(default=True)}

    # Add a slider that appears in the Settings panel
    intensity: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="How strongly to invert the colors (0 = original, 1 = fully inverted)",
        json_schema_extra=ui_field_config(order=1, label="Intensity"),
    )
