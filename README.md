English | [简体中文](/README.zh-CN.md)

<div align="center">

<h1>Fast-Phasr-Next</h1>

<i>New generation lightweight DiffSinger automatic phoneme annotation tool</i>

<b>⚠️ Warning: Programs always have uncertainty, please do not trust automatic programs 100% (even if the program has high reliability). If it is a major project, please perform necessary checks on the phoneme sequence after using the program</b>

<b> Currently, the project supports Chinese, English, and Japanese (but the reliability of Japanese recognition is not high)</b>

</div>

## Supported languages

- [x] Support for Chinese
- [x] Support for English
- [x] Support for Japanese

## Use

### Requirements

```
torch
openai-whisper
pypinyin
ffmpeg
```
**Please install ffmpeg yourself and add it to the system environment variable**

### Installation dependencies

```bash
git clone https://github.com/StarDawn-VirtualSinger/fast-phasr-next.git
```

- Creating a Conda Environment

```
conda create -n fast-phasr-next python==3.12 -y
conda activate fast-phasr-next
```

- Using Scripts：

```bash
# windows
.\install.bat

# linux
bash ./install.sh
```

- Manual install

```bash
# cpu
pip install -r requirement.txt

# gpu
conda install cudatoolkit -y
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip install -r requirement.txt
```

### Optional model

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
| :----: | :--------: | :----------------: | :----------------: | :-----------: | :------------: |
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |

**In actual testing, the base and small models have already achieved good annotation results, and there is no need to choose a larger model if not necessary**

### Inference

```
python main.py -d [import directory] -m [model default="base"] -l [language default="Chinese"]
```

## Thank you to the following contributors!

<a href="https://github.com/StarDawn-VirtualSinger/fast-phasr-next/contributors">
  <img src="https://contrib.rocks/image?repo=StarDawn-VirtualSinger/fast-phasr-next" />
</a>
