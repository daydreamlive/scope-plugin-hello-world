from pydantic import Field

from scope.core.pipelines.base_schema import (
    BasePipelineConfig,
    ModeDefaults,
    ui_field_config,
)


class ColorGeneratorConfig(BasePipelineConfig):
    """Configuration for the Color Generator pipeline."""

    pipeline_id = "color-generator"
    pipeline_name = "Color Generator"
    pipeline_description = "Generates solid color frames"

    # No prompts needed
    supports_prompts = False

    # Text mode only (no video input required)
    modes = {"text": ModeDefaults(default=True)}

    # Custom parameter: the color to generate (RGB values 0-255)
    color_r: int = Field(
        default=128,
        ge=0,
        le=255,
        description="Red component",
        json_schema_extra=ui_field_config(order=1, label="Red"),
    )
    color_g: int = Field(
        default=128,
        ge=0,
        le=255,
        description="Green component",
        json_schema_extra=ui_field_config(order=2, label="Green"),
    )
    color_b: int = Field(
        default=128,
        ge=0,
        le=255,
        description="Blue component",
        json_schema_extra=ui_field_config(order=3, label="Blue"),
    )
