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
  - [重新训练](#重新训练)
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
### 重新训练

## 致谢
### 项目成员

 -  陈赞 (途深智合)
 -  沈逸卿 （途深智合）
 -  李添斌 （上海AI LAB）
 -  何军军 （上海AI LAB）
 -  王宇光 （途深智合）

## 开源许可证

本项目采用[Apache License 2.0 开源许可证](https://github.com/tsynbio/TourSynbio/blob/main/LICENSE)。
