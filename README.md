# g2pk2
This is a cross-platform g2p for Korean.

g2pk2 is a library that made [Kyubyong's g2pk](https://github.com/Kyubyong/g2pK) work in Windows.
The reason why g2pk does not work well in Windows is that the `mecab`, the morpheme analyzer used by g2pk, causes build errors in Windows.
g2pk2 uses a different morpheme analyzer depending on the operating system.
Windows uses [eunjeon](https://github.com/koshort/pyeunjeon), which enables mecab to be used in Windows, and other operating systems use [python-mecab-ko](https://github.com/jonghwanhyeon/python-mecab-ko), which was previously used in g2pk.

Install g2pk2 and make sure that a morpheme analyzer exists for the operating system of the system you are using for the first time, and if not, proceed with the installation automatically.

## Requirements
* python >= 3.6
* jamo
* nltk


## Installation
```
pip install g2pk2
```


## How To Use
g2pk2 uses same syntaxes as g2pk.
```
>>> from g2pk2 import G2p
>>> g2p = G2p("포상은 열심히 한 아이에게만 주어지기 때문에 포상인 것입니다.")
>>> g2p("포상으 녈심히 하 나이에게만 주어지기 때무네 포상인 거심니다.")

```
If you want more information, check [g2pk](https://github.com/Kyubyong/g2pK)

