# Xbox Controller Emulator

A keyboard-to-Xbox controller mapper that converts keyboard inputs into Xbox gamepad controls.

## Installation

Install the required dependencies:

```bash
pip install pynput vgamepad
```

## Usage

Run the script:

```bash
python main.py
```

The program will display all available keybindings when it starts. Press **F6** to exit.

## Keybindings

The default keybindings are:

| Key | Button |
|-----|--------|
| W | D-Pad Up |
| A | D-Pad Left |
| S | D-Pad Down |
| D | D-Pad Right |
| V | B |
| Q | Y |
| Space | A |
| Left Shift | LB |
| Right Shift | LB |
| Left Arrow | X |
| Right Arrow | RB |

You can customize the keybindings by editing the `key_bindings` dictionary in `main.py`.

## Requirements

- Python 3.6+
- Windows (for vgamepad support)

## License

MIT
