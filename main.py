from db import get_radio_signals
from calculation import calculate_signal_radius
from visual import visualize_signals

def main():
    signals = get_radio_signals()
    visualize_signals(signals)

if __name__ == "__main__":
    main()