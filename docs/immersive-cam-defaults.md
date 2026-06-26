# Immersive Cam Recommended Defaults

Date: 2026-06-25

Context: W3EE includes an integrated Immersive Cam configuration menu. The goal is an immersive camera that still preserves W3EE combat readability.

## Recommended Baseline

Start by applying the Immersive Cam preset on each camera tab, then tune only the high-impact values below.

| Tab | Setting | Recommended value | Notes |
| --- | --- | --- | --- |
| Exploration | Field Of View | 65 | Slightly wider than default; improves peripheral awareness without heavy distortion. |
| Exploration | Interior Camera Matches Exterior Camera | On | Keeps camera behavior consistent indoors and outdoors. |
| Exploration | Exploration Offset | 0.25 | Mild right-shoulder framing. Higher moves camera right, lower/negative moves left. |
| Exploration | Exploration Zoom | 1.10-1.35 | Immersive but not too cramped. Higher zooms in, lower pulls back. |
| Exploration | Exploration Height | 0.55-0.65 | Keeps Geralt grounded while preserving horizon visibility. |
| Sprint | Sprint Cam Based Upon | Exploration Settings | Keeps sprint camera consistent with walking/exploration and avoids jarring shifts. |
| Sprint | Custom Sprint Base Offset | 0 | Only used when sprint mode is Custom. Higher moves right; lower/negative moves left. |
| Sprint | Custom Sprint Base Zoom | 0 | Only used when sprint mode is Custom. Higher is closer; lower/negative pulls back. |
| Sprint | Custom Sprint Base Height | 0 | Only used when sprint mode is Custom. Higher raises the camera. |
| Combat | Preset | Immersive Cam | Prefer readable combat over maximum cinematic closeness. |
| Horseback | Preset | Immersive Cam | If Roach feels cramped, raise ride distances toward 3.0. |
| Sailing | Preset | Immersive Cam | Keep Sail Pitch around 25. |
| Witcher Sense | Preset | Immersive Cam | Keep Witcher Sense Zoom enabled for focus/readability. |
| Examine Clue | Preset | Immersive Cam | Close framing works well for investigation. |
| Aim / Throw | Preset | Vanilla or Immersive Cam | Use Vanilla if bomb/crossbow aiming feels awkward. |
| Igni Stream | Preset | Immersive Cam | Switch this tab only to Vanilla if the stream blocks visibility. |

## What The Settings Mean

| Setting family | Meaning |
| --- | --- |
| FOV | Wider/narrower view. Higher shows more peripheral vision but can add distortion. |
| Offset | Horizontal camera shoulder position. Higher moves right; lower/negative moves left. |
| Zoom / Depth | Camera distance. Higher generally moves closer/zooms in; lower pulls back. |
| Height | Vertical camera position. Higher raises the camera; lower drops it closer to Geralt. |
| Interior Match | If enabled, interiors reuse the exploration camera instead of switching to a separate indoor camera. |
| Sprint Cam Based Upon | Determines whether sprinting uses the exploration camera, vanilla sprint camera, or custom sprint-only values. Prefer Exploration Settings for continuity. |
| Combat Lock | If enabled, combat camera avoids vanilla zoom-in/zoom-out behavior. |
| Horse distances | Separate camera distance values for walk/trot, canter, gallop, and mounted combat. |
| Sail Pitch | How far the sailing camera can tilt skyward. |
| Witcher Sense Zoom | Enables the dedicated focused Witcher Sense camera. |
| Aim Rotate | Whether Geralt auto-rotates toward camera direction while aiming/throwing. |

## Practical Rule

Use Immersive Cam for atmosphere, but do not over-tighten combat, aiming, or Igni. W3EE is already more punishing than vanilla, so visibility is part of the balance.

For sprinting, prefer Exploration Settings with custom sprint sliders left at 0. Custom sprint tuning is useful only if sprinting feels visually wrong after testing; otherwise it adds another camera profile to maintain.
