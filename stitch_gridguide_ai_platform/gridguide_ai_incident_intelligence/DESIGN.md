---
name: GridGuide AI Incident Intelligence
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#434655'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#737686'
  outline-variant: '#c3c6d7'
  surface-tint: '#0053db'
  primary: '#004ac6'
  on-primary: '#ffffff'
  primary-container: '#2563eb'
  on-primary-container: '#eeefff'
  inverse-primary: '#b4c5ff'
  secondary: '#00668a'
  on-secondary: '#ffffff'
  secondary-container: '#40c2fd'
  on-secondary-container: '#004d6a'
  tertiary: '#006242'
  on-tertiary: '#ffffff'
  tertiary-container: '#007d55'
  on-tertiary-container: '#bdffdb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b4c5ff'
  on-primary-fixed: '#00174b'
  on-primary-fixed-variant: '#003ea8'
  secondary-fixed: '#c4e7ff'
  secondary-fixed-dim: '#7bd0ff'
  on-secondary-fixed: '#001e2c'
  on-secondary-fixed-variant: '#004c69'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.025em
  display-lg-mobile:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Inter
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 34px
    letterSpacing: -0.015em
  headline-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.005em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0.005em
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 0.75rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system embodies a high-reliability, mission-critical SaaS aesthetic tailored for utility operators, incident response teams, and consumer-facing transparency portals. The emotional tone balances authoritative calm with immediate clarity: users facing grid disruptions need instant situational awareness without cognitive fatigue.

The design movement is **Corporate Modern Minimalist** enhanced with purposeful data density and subtle ambient depth. It prioritizes:
- **Calm Authority**: Deep navy-slate typography grounds the interface with uncompromising contrast, dispelling ambiguity during emergency scenarios.
- **Electric Precision**: High-impact electric blue directs focus toward critical action items, status changes, and geospatial indicators without overwhelming the interface.
- **Airy Scannability**: Expansive whitespace, soft dividers, and low-noise containers allow rapid parsing of outage telemetry, feeder lines, and incident resolution workflows.

## Colors

The color architecture is built for exceptional visual hierarchy in high-stress operational environments:

- **Primary Canvas & Surfaces**: Base canvas utilizes `#F8FAFC` (Slate 50) to reduce glare over extended shift monitoring, while active cards and panels leverage pure `#FFFFFF` for pristine layer distinction.
- **Primary Accent (`#2563EB`)**: A vibrant, accessible cobalt blue used strictly for primary interactive states, key metrics, and primary dispatch actions.
- **Secondary & Tint Accents (`#38BDF8` / `#EFF6FF`)**: Soft sky blue and ice tints provide ambient halos, selected row states, and non-blocking notification fills.
- **Functional Semantics**:
  - **Success / Operational**: Emerald (`#10B981`) for fully energized sectors and closed tickets.
  - **Warning / Degraded**: Amber (`#F59E0B`) for feeder fluctuations and capacity warnings.
  - **Critical / Fault**: Crimson (`#EF4444`) reserved exclusively for trip conditions and live safety hazards.
- **Text & Borders**: High-contrast Slate 900 (`#0F172A`) for primary headings, Slate 700 (`#334155`) for readable body text, and Slate 200 (`#E2E8F0`) for whisper-thin container borders.

## Typography

The type system is powered entirely by **Inter**, chosen for its tall x-height, neutral geometric construction, and superior legibility across dense data tables, graphs, and live dispatch feeds.

- **Tabular Numerics**: Metric readouts, customer outage counts, kilowatt-hour meters, and coordinate stamps must always activate OpenType tabular numbers (`tnum`) to eliminate layout jitter during real-time data streaming.
- **Hierarchy Rules**:
  - Headings (`display-lg` down to `headline-md`) enforce tighter tracking (`-0.025em` to `-0.01em`) to maintain sharp editorial punch.
  - Labels and metadata (`label-sm` through `label-lg`) make deliberate use of positive tracking and medium/semibold weights to ensure instantaneous parsing on compact hardware displays or mobile field units.

## Layout & Spacing

The layout philosophy uses a disciplined **12-column fluid grid system** anchored by an 8pt architectural rhythm, with a 4pt sub-grid for tight control interfaces.

- **Desktop (≥1280px)**: 12-column structure with `1.5rem` (24px) gutters and a max canvas width of `1440px` centered within a `2rem` (32px) page margin.
- **Tablet (768px – 1279px)**: 8-column layout with `1rem` (16px) gutters, converting split data tables into vertically stacked summary cards.
- **Mobile (<768px)**: 4-column layout utilizing `0.75rem` (12px) gutters and `1rem` (16px) outer margins. Side navigation collapses into an accessible sheet, and incident split-screens convert into switchable tabs (Map vs. List).
- **Component Padding**: Standard card enclosures use `space-lg` internally, while compact table cells and metric micro-cards contract to `space-sm` vertically and `space-md` horizontally.

## Elevation & Depth

Visual hierarchy relies on **crisp structural borders paired with diffused, low-opacity ambient shadows**. This prevents muddy layering in complex telemetry dashboards.

- **Level 0 (Flat Canvas)**: Hex `#F8FAFC`. Zero elevation. Houses the primary dashboard shell and inactive background surfaces.
- **Level 1 (Card & Module Surface)**: Solid `#FFFFFF` bordered with a 1px continuous stroke of `#E2E8F0`. Shadow: `0 1px 3px 0 rgba(15, 23, 42, 0.04), 0 1px 2px -1px rgba(15, 23, 42, 0.02)`.
- **Level 2 (Hover & Active Drag States)**: Elevates selected incident items or interactive map overlays. Shadow: `0 4px 6px -1px rgba(15, 23, 42, 0.06), 0 2px 4px -2px rgba(15, 23, 42, 0.04)`, accompanied by a subtle border shift to `#CBD5E1`.
- **Level 3 (Popovers, Select Menus, & Floating Command Bars)**: Shadow: `0 10px 15px -3px rgba(15, 23, 42, 0.08), 0 4px 6px -4px rgba(15, 23, 42, 0.03)`.
- **Level 4 (Critical Incident Modals & Drawers)**: High-prominence dialogs layered over an ambient backdrop scrim (`rgba(15, 23, 42, 0.4)` with 4px backdrop blur). Shadow: `0 20px 25px -5px rgba(15, 23, 42, 0.1), 0 8px 10px -6px rgba(15, 23, 42, 0.04)`.

## Shapes

The design system adopts a **Rounded (`2`)** shape vocabulary (base radius of `0.5rem` / 8px). This creates a polished, welcoming software feel while maintaining the structural discipline of utility-grade enterprise tools.

- **Micro Elements (`rounded-sm`, 4px)**: Badges, code snippets, status indicators, and sub-metric tags.
- **Standard Controls (`rounded`, 8px)**: Input fields, standard buttons, select boxes, and incident chips.
- **Structural Containers (`rounded-lg`, 12px)**: Dashboard cards, modal panels, filter toolbars, and geospatial map controls.
- **Hero & Announcement Containers (`rounded-xl`, 16px)**: High-level system banners and major incident summary headers.

## Components

### Buttons
- **Primary**: Solid `#2563EB` fill, `#FFFFFF` text, `0.5rem` border radius. On hover: `#1D4ED8` with a subtle elevation shift. Focus ring: 2px offset with `#38BDF8`.
- **Secondary**: `#FFFFFF` background, 1px border `#E2E8F0`, `#0F172A` text. On hover: `#F8FAFC` background and `#CBD5E1` border.
- **Ghost / Utility**: Transparent background, `#334155` text. On hover: `#F1F5F9`.

### Chips & Incident Badges
- **Live Outage (Urgent)**: `#FEF2F2` fill, `#DC2626` text, 1px `#FECACA` border, accompanied by a pulsing 6px red indicator dot.
- **Investigating (Warning)**: `#FFFBEB` fill, `#D97706` text, 1px `#FDE68A` border.
- **Resolved / Normal (Success)**: `#ECFDF5` fill, `#059669` text, 1px `#A7F3D0` border.
- **Feeder / Grid Tag**: `#EFF6FF` fill, `#2563EB` text, 1px `#BFDBFE` border.

### Input Fields & Controls
- **Text Inputs**: `#FFFFFF` fill with 1px `#E2E8F0` border. Placeholder text in `#94A3B8`. Active focus triggers a 1px border transition to `#2563EB` accompanied by a 3px soft outer ring in `rgba(37, 99, 235, 0.12)`.
- **Checkboxes & Radios**: 16px control size with `0.25rem` radius for checkboxes; checked state floods with `#2563EB` displaying an optical white check icon.

### Cards & Telemetry Panels
- Clean `#FFFFFF` backdrop with standard `space-lg` (24px) padding.
- Card headers feature an inline baseline structure: headline on the left, telemetry status badge or action trigger on the right, separated from the content body by a hairline `#F1F5F9` rule when scrolling is present.

### Specialized Incident Feed List
- List rows feature an interactive hover state changing from `#FFFFFF` to `#F8FAFC`.
- Left-edge border accent (3px width) maps directly to incident severity (Red for Active Outage, Amber for Investigation, Emerald for Restored).