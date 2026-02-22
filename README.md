# run-matrix 🕶️💊

[🇺🇸 English](#english) | [🇰🇷 한국어](#한국어)

---

## English

A terminal-based, perfectly immersive Matrix-themed AI assistant powered by Google's Gemini.

It brings the iconic cinematic opening sequence ("Wake up, Neo..."), retro CRT scanline effects, text-glitching, and cold, analytical responses directly to your terminal.

### Features
- **100% Cinematic Opening:** Replicates the exact pacing and typing effects of the movie intro.
- **CRT Aesthetics:** Phosphor-green text, flickering scanlines, and animated glitches.
- **Secure Key Management:** Uses macOS Keychain to securely store and retrieve your Gemini API key. No plaintext exposure.
- **Asynchronous Streaming:** Streams responses in real-time without corrupting the visual effects.
- **Memory Management:** Implements a sliding conversation window to keep tokens under control.

### Installation

You can install this globally on your system using `pipx`:

```bash
pipx install run-matrix
```

### Usage

Simply run:
```bash
run matrix
```

On first run, you will be securely prompted for your Gemini API Key. To reset or change your API key later, run:
```bash
run matrix --reset
```

> "Unfortunately, no one can be told what the Matrix is. You have to see it for yourself."

---

## 한국어

Google Gemini 기반의 완벽한 몰입감을 선사하는 터미널용 매트릭스 테마 AI 어시스턴트입니다.

영화의 상징적인 오프닝 시퀀스("Wake up, Neo..."), 레트로 CRT 스캔라인 효과, 텍스트 글리치, 그리고 차갑고 분석적인 답변을 터미널에서 직접 경험할 수 있습니다.

### 주요 기능
- **100% 시네마틱 오프닝:** 영화 인트로의 타이핑 속도와 효과를 그대로 재현했습니다.
- **CRT 미학:** 형광 초록색 텍스트, 깜빡이는 스캔라인, 애니메이션 글리치 효과.
- **안전한 키 관리:** macOS 키체인을 사용하여 Gemini API 키를 안전하게 저장하고 불러옵니다. 평문으로 방치되지 않습니다.
- **비동기 스트리밍:** 시각적 효과를 손상시키지 않고 실시간으로 답변을 스트리밍합니다.
- **메모리 관리:** 슬라이딩 대화 창(sliding conversation window)을 구현하여 토큰 사용량을 조절합니다.

### 설치 방법

시스템에 `pipx`를 사용하여 전역으로 설치할 수 있습니다:

```bash
pipx install run-matrix
```

### 사용법

간단히 다음 명령어를 실행하세요:
```bash
run matrix
```

처음 실행 시 안전하게 Gemini API 키를 입력하라는 메시지가 표시됩니다. 나중에 API 키를 초기화하거나 변경하려면 다음 명령어를 실행하세요:
```bash
run matrix --reset
```

> "불행하게도, 매트릭스가 무엇인지 말로 설명할 수 있는 사람은 없어. 직접 봐야만 해."
