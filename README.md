# hugging_face-download

`ps: 由于本人想下载hugging face上的模型，搜了许多教程但都有点繁琐，于是选择用一个脚本来便携操作`

此脚本是为了解决国内下载hugging face上的模型和数据缓慢，不便捷等问题，此代码仅是对比较主流的两种官方下载工具的封装使用，详细安装原理可以参考[Command Line Interface (CLI)](https://huggingface.co/docs/huggingface_hub/guides/cli) ，

### 用法

#### 1.参数说明

- `--model`: hugging face上要下载的模型名称
- `--dataset`: hugging face上要下载的数据集名称
- `--save_dir`: 文件下载后实际的存储路径
- `--token`: 下载需要登录的模型（Gated Model），例如`meta-llama/Llama-2-7b-hf`时，需要指定hugging face的token，格式为`hf_****`
- `--include`: 下载指定的文件，例如 `--include "tokenizer.model tokenizer_config.json"` 或 `--include "*.bin` 下载
- `--exclude`: 不下载指定的文件，与include用法一致，例如 `--exclude "*.md"`

#### 2.下载模型or数据

这里用`bert-base-chinese`模型来作演示

```
python download.py --model google-bert/bert-base-chinese 
```

代码中必备的参数是`--model`或`--dataset`有一个即可。

然后程序就会开始自动下载，下载完的模型会放在一个文件夹里方便整理或后续操作。

数据集同上即可

#### 3.优点

支持断点和分批次传输，对于大文件比较友好，在我之前的使用中发现下载到10GB左右文件时会比较卡，甚至停止下载。此时重新下载即可。

