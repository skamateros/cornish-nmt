# Cornish-NMT
Low-resource Neural Machine Translation for Cornish.

Project for LIS070 - Project Course in AI and Language at Stockholm University.

### Abstract
Recent work in low-resource NMT has focused on transfer learning, specifically realised through the use of large multilingual translation models. This project investigates whether a multilingual neural machine translation model can be effectively adapted to translate to Cornish, a severely low-resource Celtic language with limited parallel data. Using approximately 27,000 English-Cornish sentence pairs from Korpus Kernewek and Tatoeba, two variants of the multilingual NLLB-200 model were fine-tuned: one in which the newly added Cornish language token was initialised randomly, and one in which it was initialised using the Welsh embedding to encourage transfer from a closely related Celtic language. Both models achieved strong performance: up to 51.22 BLEU and 69.98 ChrF2++. However, results showed that the Welsh-initialised model does not yield a statistically significant improvement over the randomly initialised one in performance or rate of convergence. In summary, this study highlights the potential of adapting large multilingual models to low-resource languages and provides a basis for future work on dedicated Cornish MT systems.

### Usage

Data pre-processing as described in the paper: 
- [make_tsv.py](make_tsv.py) - Converts raw OPUS data into TSV format.
- [process.py](process.py)
- [split.py](split.py) - Splits data into test/train.

Training and Using the model:
- [nllb_en_kw.ipynb](nllb_en_kw.ipynb) - Jupyter Notebook containing code for:
  - Loading the NLLB-200-distilled-600M model.
  - Expanding the model's vocabulary with the Cornish language token (<cor_Latn>)
  - Fine-tuning for English -> Cornish
  - Generating and evaluating translations
  - Saving the model

The current code is configured to run in **Google Colab**, with data stored on **Google Drive**. To run it in a different environment, the file paths for loading datasets and loading/saving models need to be adjusted.

### Data
This dataset is derived from:

- **Korpus Kernewek**, licensed under CC0 1.0
- **Tatoeba Project**, licensed under CC-BY 2.0 FR

The data has been filtered and combined.

Original sources:

https://www.akademikernewek.org.uk/corpus/

https://tatoeba.org
