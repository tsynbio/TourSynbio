
# TourSynbio<sup>TM</sup>

<div align="center">

[![OpenXLab_Model][OpenXLab_Model-image]][OpenXLab_Model-url] 

[OpenXLab_Model-image]: https://cdn-static.openxlab.org.cn/header/openxlab_models.svg
[OpenXLab_App-image]: https://cdn-static.openxlab.org.cn/app-center/openxlab_app.svg

[OpenXLab_Model-url]: https://openxlab.org.cn/models/detail/ZanTourSynbio/TourSynbio-7B

English | [简体中文](README_zh-CN.md)
</div>

## Contents <!-- omit in toc -->
- [TourSynbioTM](#toursynbiotm)
  - [Introduction](#introduction)
  - [News](#news)
  - [Usage](#usage)
    - [Quick Start](#quick-start)
      - [Download Model](#download-model)
      - [Local Deployment](#local-deployment)
    - [XTuner Fine-tuning Guide](#xtuner-fine-tuning-guide)
  - [Acknowledgments](#acknowledgments)
    - [Project Members](#project-members)
  - [Open Source License](#open-source-license)

## Introduction
[TourSynbio<sup>TM</sup>] is an advanced protein language model that integrates knowledge from the field of proteins. Based on InternLM2-Chat-7B, it is fine-tuned using the Xtuner toolkit and the SFT (Supervised Fine-Tuning) dataset from [ProteinLMBench](https://huggingface.co/datasets/tsynbio/ProteinLMBench). TourSynbio<sup>TM</sup> not only understands human language but also the sequences of proteins—the language of life. It seamlessly bridges the gap between specialized protein data and general language, making complex data and information easier to understand and apply. Its powerful reasoning capabilities allow it to extract valuable insights from complex data, accelerating the process of scientific discovery.

## News

[2024.06.23] TourSynbio<sup>TM</sup> (SFT only) is now open source.

## Usage
### Quick Start
#### Download Model
<details>
<summary>From OpenXLab</summary>

Refer to [Download Model](https://openxlab.org.cn/docs/models/%E4%B8%8B%E8%BD%BD%E6%A8%A1%E5%9E%8B.html).

```bash
pip install openxlab
```

```python
from openxlab.model import download
download(model_repo=[model_link], 
         model_name=[model_link], output='./')
```

</details>

#### Local Deployment
1. Get the project code from Github
    ```bash
    git clone (ourlink)
    python (start_file_name)
    ```

2. Create and activate a virtual environment
    ```bash
    conda env create -f environment.yml
    conda activate (envName)
    pip install -r requirements.txt
    ```

3. Run the demo
    ```bash
    streamlit run web_demo.py --server.address=0.0.0.0 --server.port=8501
    ```

### XTuner Fine-tuning Guide

*   Introduction

XTuner supports fine-tuning large language models. For a dataset preprocessing guide, please refer to the [documentation](https://github.com/InternLM/xtuner/blob/main/docs/zh_cn/user_guides/single_turn_conversation.md). For a fine-tuning guide, please refer to the [documentation](https://github.com/InternLM/xtuner/blob/main/docs/zh_cn/user_guides/finetune.md).

*   Step 1: Format the [single round dialogue data format](https://github.com/InternLM/xtuner/blob/main/docs/zh_cn/user_guides/dataset_format.md#单轮对话数据集格式) for XTuner, for example.
*  ```python
    [{
        "conversation":[
            {
                "system": "xxx",
                "input": "xxx",
                "output": "xxx"
            }
        ]
    },
    {
        "conversation":[
            {
                "system": "xxx",
                "input": "xxx",
                "output": "xxx"
            }
        ]
    }]

    # demo
    {
            "conversation": [
                {
                    "system": "Please evaluate the following protein sequence and provide an explanation of the enzyme's catalytic activity, including the chemical reaction it facilitates: ",
                    "intput": "<seq> M P G R Q L T E L L T G L E E V K V Q T A M E Q K E M M I G G L T A D S R E V R P G D L F A A L P G A R V D G R D F I D Q A V G R G A D V V L A P V G T S L K D Y G R P V S L V T S D E P R R T L A Q M A A R F H G R Q P R T I A A V T G T S G K T S V A D F L R Q I W T L A D R K A A S L G T L G L I P A T A A S K A P P Y L T T P D P V A L H A C L K E V A E A G Y E H L A L E A S S H G L D Q Y R L D G L T F S A A A F T N L S Q D H L D Y H P D M E S Y L N A K A R L F G D L L P T G A T A V L N A D A P E F D R L A A L C E R R G I E V L S Y G L A G D D L R I V E A R A L P D G I A L S L R V K G Q D W Q G K L D L I G T F Q G H N V L A A L G L A L A T G L E P S V A L E A L P K L V G V P G R L Q R V A Q T V S G A Q V F V D Y A H K P G A L E A A L T A L R P H A E G R L I V V F G A G G D R D R G K R P L M G E I A T R L A D V V L V T D D N P R S E D P V A I R A E I L A A A P G A R E V S D R G G A I A A A L A E A D P G D L V L I A G K G H E T G Q I V G D K V L P F D D S E I A R R L A R G G Q V </seq>",
                    "output": "By examining the input protein sequence, the enzyme catalyzes the subsequent chemical reaction: ATP + meso-2,6-diaminoheptanedioate + UDP-N-acetyl-alpha-D-   muramoyl-L-alanyl-D-glutamate = ADP + H(+) + phosphate + UDP-N-   acetyl-alpha-D-muramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-   diaminoheptanedioate."
                }
            ]
    }
    ```

*   Step 2: Configure the XTuner config file.

    XTuner provides multiple out of the box configuration files, which users can view through the following commands:

    ```shell
    xtuner list-cfg
    ```

    Alternatively, if the provided configuration file does not meet the usage requirements, please export the provided configuration file and make the corresponding changes:

    ```shell
    xtuner copy-cfg ${CONFIG_NAME} ${SAVE_PATH}
    vi ${SAVE_PATH}/${CONFIG_NAME}_copy.py
    ```

    To configure the config file, you can first copy the official `internlm2-chat-7b` config file, then rename the copied config file to `internlm2-chat-7bprotein-lora. py` and make the necessary modifications,

    ```python
    ...
    custom_hooks = [
        dict(
            tokenizer=dict(
                padding_side='right',
                pretrained_model_name_or_path=
                '/cpfs01/shared/gmai/xtuner_workspace/internlm/internlm2-7b/', # PATH/TO/PRETRAINED MODELS
                trust_remote_code=True,
                type='transformers.AutoTokenizer.from_pretrained'),
            type='xtuner.engine.DatasetInfoHook'),
    ]
    data_path = [
        '/cpfs01/shared/gmai/xtuner_workspace/protein_data/formated_ssl_data/sll_data_0.json', # PATH/TO/DATA
        ...
    ]
    ...
    model = dict(
        llm=dict(
            pretrained_model_name_or_path=
            '/cpfs01/shared/gmai/xtuner_workspace/internlm/internlm2-7b/', # PATH/TO/PRETRAINED MODELS
            torch_dtype='torch.float16',
            trust_remote_code=True,
            type='transformers.AutoModelForCausalLM.from_pretrained'),
        lora=dict(    # LoRA
            bias='none',
            lora_alpha=16,
            lora_dropout=0.1,
            r=64,
            task_type='CAUSAL_LM',
            type='peft.LoraConfig'),
        type='xtuner.model.SupervisedFinetune')
    ...
    ```

The main changes are **pretrained model path**, **data path**, and **fine-tuning method (LoRA)**. Other hyperparameters can be adjusted as needed. Here, we keep the defaults.

**Note**:

Both the SFT and SSL stages involve modifying the config file, with the same modification method. However, the `input` in SSL data is empty during data construction. For detailed pretrained data construction, see the [documentation](https://github.com/InternLM/xtuner/blob/main/docs/zh_cn/user_guides/incremental_pretraining.md).

*   **Step 3**: Start fine-tuning.

```shell
xtuner train internlm2_7b_protein_lora
```

For example, you can fine-tune InternLM2-Chat-7B on the protein dataset using the LoRA algorithm:

```shell
# Single GPU
xtuner train internlm2_7b_protein_lora --deepspeed deepspeed_zero2
# Multiple GPUs
(DIST) NPROC_PER_NODE=${GPU_NUM} xtuner train internlm2_7b_protein_lora --deepspeed deepspeed_zero2
(SLURM) srun ${SRUN_ARGS} xtuner train internlm2_7b_protein_lora --launcher slurm --deepspeed deepspeed_zero2
```

*   `--deepspeed` indicates using [DeepSpeed](https://github.com/microsoft/DeepSpeed) 🚀 to optimize the training process. XTuner includes multiple strategies, including ZeRO-1, ZeRO-2, and ZeRO-3. If you wish to disable this feature, simply remove this parameter.

*   For more examples, please refer to the [documentation](./docs/zh_cn/user_guides/finetune.md).

*   **Step 4**: Convert the saved PTH model (if using DeepSpeed, it will be a folder) to a HuggingFace model:

```shell
xtuner convert pth_to_hf ${CONFIG_NAME_OR_PATH} ${PTH} ${SAVE_PATH}
```

## Acknowledgments

### Project Members

## Open Source License

This project is licensed under the [Apache License 2.0](https://github.com/tsynbio/TourSynbio/blob/main/LICENSE).
