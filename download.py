"""
file            : download.py
author          : dongshandaolu
description     : to download model and data from huggingface mirror by  huggingface-cli
"""
import os
import sys
import platform
import argparse

# 在window平台下将下载默认保存路径设置在d盘的model文件夹里
DEFAULT_SAVE_DIR = "D:/model"


def get_parser():
    parser = argparse.ArgumentParser()
    # Required parameters
    parser.add_argument("--model", default=None, type=str, required=True, help="model name")
    parser.add_argument("--token", default=None, type=str, required=False, help="access token for private models")
    parser.add_argument("--include", default=None, type=str, required=False, help="choose files to download")
    parser.add_argument("--exclude", default=None, type=str, required=False, help="choose files not to download")
    parser.add_argument("--dataset", default=None, type=str, help="dataset name")
    parser.add_argument("--save_dir", default=DEFAULT_SAVE_DIR, type=str, help=f"saving path {DEFAULT_SAVE_DIR}")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    try:
        import huggingface_hub
    except ImportError:
        os.system("pip install -U huggingface_hub")
        print("install huggingface_hub")

    try:
        import hf_transfer
    except ImportError:
        os.system("pip install -U hf-transfer")
        print("install hf_transfer accelerator")

    os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
    os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
    print("Using mirror site: https://hf-mirror.com")

    args = get_parser()
    if not args.model and not args.dataset:
        raise ValueError("Please specify either a model (--model) or dataset (--dataset) to download")

    elif args.model and args.dataset:
        raise ValueError("Please specify only one resource (model OR dataset) at a time")

    token_option = f"--token {args.token}" if args.token else ""
    include_option = f"--include {args.include}" if args.include else ""
    exclude_option = f"--exclude {args.exclude}" if args.exclude else ""

    if args.model:
        model_name = args.model.replace("/", "--")
        save_path = os.path.join(args.save_dir, f"model-{model_name}")
        os.makedirs(save_path, exist_ok=True)

        print(f" Downloading model: {args.model}")
        print(f" Saving to: {save_path}")

        download_cmd = (
            f"huggingface-cli download {args.model} "
            f"{token_option} {include_option} {exclude_option} "
            f"--local-dir {save_path} "
            "--local-dir-use-symlinks False "
            "--resume-download"
        )

    elif args.dataset:
        dataset_name = args.dataset.replace("/", "--")
        save_path = os.path.join(args.save_dir, f"dataset-{dataset_name}")
        os.makedirs(save_path, exist_ok=True)

        print(f" Downloading dataset: {args.dataset}")
        print(f" Saving to: {save_path}")

        download_cmd = (
            f"huggingface-cli download {args.dataset} "
            f"{token_option} {include_option} {exclude_option} "
            f"--repo-type dataset "
            f"--local-dir {save_path} "
            "--local-dir-use-symlinks False "
            "--resume-download"
        )

    print(f" Executing command:\n{download_cmd}")
    os.system(download_cmd)
    print("download competed!!!!")
