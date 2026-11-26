import os

LINE = "You must be a firmware update, because my heart just restarted and somehow all my bugs feel like features now."


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
