from scope.core.plugins.hookspecs import hookimpl


@hookimpl
def register_pipelines(register):
    from .pipelines.color_generator.pipeline import ColorGeneratorPipeline
    from .pipelines.invert.pipeline import InvertPipeline

    register(ColorGeneratorPipeline)
    register(InvertPipeline)
