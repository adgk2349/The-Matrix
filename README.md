# run-matrix 🕶️💊

A terminal-based, perfectly immersive Matrix-themed AI assistant powered by Google's Gemini.

It brings the iconic cinematic opening sequence ("Wake up, Neo..."), retro CRT scanline effects, text-glitching, and cold, analytical responses directly to your terminal.

## Features
- **100% Cinematic Opening:** Replicates the exact pacing and typing effects of the movie intro.
- **CRT Aesthetics:** Phosphor-green text, flickering scanlines, and animated glitches.
- **Secure Key Management:** Uses macOS Keychain to securely store and retrieve your Gemini API key. No plaintext exposure.
- **Asynchronous Streaming:** Streams responses in real-time without corrupting the visual effects.
- **Memory Management:** Implements a sliding conversation window to keep tokens under control.

## Installation

You can install this globally on your system using `pipx`:

```bash
pipx install run-matrix
```

## Usage

Simply run:
```bash
run matrix
```

On first run, you will be securely prompted for your Gemini API Key. To reset or change your API key later, run:
```bash
run matrix --reset
```

> "Unfortunately, no one can be told what the Matrix is. You have to see it for yourself."
