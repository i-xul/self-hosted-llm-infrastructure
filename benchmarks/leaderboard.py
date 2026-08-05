"""Generate a Markdown leaderboard from benchmark master summaries."""

from pathlib import Path

from leaderboard.loader import load_latest_model_summaries
from leaderboard.markdown import write_leaderboard

OUTPUT_PATH = Path(__file__).resolve().parent / "LEADERBOARD.md"


def main() -> None:
    summaries = load_latest_model_summaries()

    if not summaries:
        print("No benchmark summaries were found.")
        return

    output_path = write_leaderboard(
        summaries=summaries,
        output_path=OUTPUT_PATH,
    )

    print(f"Loaded model summaries: {len(summaries)}")
    print(f"Leaderboard written to: {output_path}")


if __name__ == "__main__":
    main()
