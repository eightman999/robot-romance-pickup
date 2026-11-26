import os

LINE = "Are you a firmware update? Because every time you show up, I feel like a better version of myself is about to restart."


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
