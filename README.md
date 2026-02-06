# scope-plugin-hello-world

An example Scope plugin that provides two pipelines — a solid color frame generator and a video color inverter.

## Features

- **Color Generator** — Generate solid color video frames with configurable RGB values (text mode, no input required)
- **Invert Colors** — Invert colors of input video frames with an adjustable intensity slider (video mode)

## Install

Follow the [Scope plugins guide](https://github.com/daydreamlive/scope/blob/main/docs/plugins.md) to install this plugin using the URL:

```
https://github.com/daydreamlive/scope-plugin-hello-world.git
```

## Upgrade

Follow the [Scope plugins guide](https://github.com/daydreamlive/scope/blob/main/docs/plugins.md) to upgrade this plugin to the latest version.

## Architecture

This plugin registers two pipelines via the `register_pipelines` hook in `plugin.py`:

### Color Generator (`color-generator`)

A **text-mode** source pipeline that generates a solid color frame tensor. It takes three runtime parameters — `color_r`, `color_g`, and `color_b` (each 0–255, default 128) — and outputs a `(1, H, W, 3)` tensor in the `[0, 1]` range. No video input is required.

### Invert Colors (`invert`)

A **video-mode** processing pipeline that takes one input frame and inverts its colors. An `intensity` parameter (0.0–1.0, default 1.0) blends between the original frame and the fully inverted result, allowing partial inversion.
