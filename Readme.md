# TourSynbioLM<sup>TM</sup>
<div align="center">


[![OpenXLab_Model][OpenXLab_Model-image]][OpenXLab_Model-url] 

[OpenXLab_Model-image]: https://cdn-static.openxlab.org.cn/header/openxlab_models.svg
[OpenXLab_App-image]: https://cdn-static.openxlab.org.cn/app-center/openxlab_app.svg

[OpenXLab_Model-url]: https://openxlab.org.cn/models/detail/ZanTourSynbio/TourSynbio-7B
</div>

## 目录 <!-- omit in toc -->
- [简介](#简介)
- [News](#news)
- [使用方法](#使用方法)
  - [快速开始](#快速开始)
    - [下载模型](#下载模型)
    - [本地部署](#本地部署)
  - [XTuner微调指南](#xtuner微调指南)
- [致谢](#致谢)
  - [项目成员](#项目成员)
- [开源许可证](#开源许可证)

## 简介
[TourSynbio<sup>TM</sup>]()蛋白质大语言模型是一个融合了蛋白质领域知识的先进模型。该模型基于InternLM2-Chat-7B，使用Xtuner工具包进行了微调，并采用了[ProteinLMBench](https://huggingface.co/datasets/tsynbio/ProteinLMBench)中的SFT（Supervised Fine-Tuning）数据集。TourSynbio<sup>TM</sup>不仅具备理解人类语言的能力，还能够理解蛋白质序列——这一生命的语言。它实现了蛋白质专业领域与普通语言的无缝对接，使复杂数据和信息变得更易理解和应用。通过模型的强大推理能力，能够从复杂数据中提取有价值的信息和见解，加速科学发现的进程。

## News

[2024.06.23] TourSynbio<sup>TM</sup>(SFT only)已开源上线。


## 使用方法
### 快速开始
#### 下载模型
<details>

<summary>从OpenXLab</summary>

参考 [下载模型](https://openxlab.org.cn/docs/models/%E4%B8%8B%E8%BD%BD%E6%A8%A1%E5%9E%8B.html) 。

```bash
pip install openxlab
```

```python
from openxlab.model import download
download(model_repo=[model_link]', 
        model_name='[model_link]', output='./')
```

</details>



#### 本地部署
1. 从Github获取项目代码
    ```bash
    git clone (ourlink)
    python (开始执行文件名)
    ```

2. 创建并激活虚拟环境
    ```bash
    conda env create -f enviroment.yml
    conda activate (envName)
    pip install -r requirements.txt
    ```
3. Demo运行
    ```bash
    streamlit run web_demo.py --server.address=0.0.0.0 --server.prot=8501
    ```
### XTuner微调指南

*   前言

XTuner 支持微调大语言模型。数据集预处理指南请查阅[文档](https://github.com/InternLM/xtuner/blob/main/docs/zh_cn/user_guides/single_turn_conversation.md), 微调方法指南请查阅[文档](https://github.com/InternLM/xtuner/blob/main/docs/zh_cn/user_guides/finetune.md)。

*   步骤1，将数据构造成XTuner 定义的[单轮对话数据格式](https://github.com/InternLM/xtuner/blob/main/docs/zh_cn/user_guides/dataset_format.md#单轮对话数据集格式), 形如

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

*   **步骤 2**，准备配置文件。XTuner 提供多个开箱即用的配置文件，用户可以通过下列命令查看：

    ```shell
    xtuner list-cfg
    ```

    或者，如果所提供的配置文件不能满足使用需求，请导出所提供的配置文件并进行相应更改：

    ```shell
    xtuner copy-cfg ${CONFIG_NAME} ${SAVE_PATH}
    vi ${SAVE_PATH}/${CONFIG_NAME}_copy.py
    ```

​        配置config文件，可以先copy官方的`internlm2-chat-7b`的config文件，然后将copy的config文件，重命名为` internlm2_7b_protein_lora.py`然后进行修改,

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

主要修改的地方就是，**预训练模型路径**，**数据路径**，以及**微调方式（LoRA）**，其他的超参，按需调整即可，这里我们保持默认。

**注意**：

​	SFT阶段与SSL阶段都是通过修改config文件进行的，修改方法并无差别。但是SSL的数据在数据构造时`input`为空，详细的pretrained数据构造见[文档](https://github.com/InternLM/xtuner/blob/main/docs/zh_cn/user_guides/incremental_pretraining.md)。

*   **步骤 3**，开始微调。

    ```shell
    xtuner train internlm2_7b_protein_lora
    ```

    例如，我们可以利用 LoRA 算法在 蛋白质 (XXX) 数据集上微调 InternLM2-Chat-7B：

    ```shell
    # 单卡
    xtuner train internlm2_7b_protein_lora --deepspeed deepspeed_zero2
    # 多卡
    (DIST) NPROC_PER_NODE=${GPU_NUM} xtuner train internlm2_7b_protein_lora --deepspeed deepspeed_zero2
    (SLURM) srun ${SRUN_ARGS} xtuner train internlm2_7b_protein_lora --launcher slurm --deepspeed deepspeed_zero2
    ```

    *   `--deepspeed` 表示使用 [DeepSpeed](https://github.com/microsoft/DeepSpeed) 🚀 来优化训练过程。XTuner 内置了多种策略，包括 ZeRO-1、ZeRO-2、ZeRO-3 等。如果用户期望关闭此功能，请直接移除此参数。

    *   更多示例，请查阅[文档](./docs/zh_cn/user_guides/finetune.md)。

*   **步骤 4**，将保存的 PTH 模型（如果使用的DeepSpeed，则将会是一个文件夹）转换为 HuggingFace 模型：

    ```shell
    xtuner convert pth_to_hf ${CONFIG_NAME_OR_PATH} ${PTH} ${SAVE_PATH}
    ```

## 致谢
### 项目成员

 -  陈赞 (途深智合)
 -  沈逸卿 （途深智合）
 -  李添斌 （上海AI Lab）
 -  何军军 （上海AI Lab）
 -  王宇光 （途深智合 上海交通大学）

## 开源许可证

本项目采用[Apache License 2.0 开源许可证](https://github.com/tsynbio/TourSynbio/blob/main/LICENSE)。
