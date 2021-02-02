# generate_lfw_test_pair
Generate test pair based on LFW dataset

Create (lfw)[https://github.com/ronghuaiyang/arcface-pytorch/blob/master/lfw_test_pair.txt] test pair

### Directory should follow as follows:
```
$ tree --dirsfirst
.
├── dataset
│   └── lfw-align-128
│       ├── Zurab_Tsereteli
│       │   └── Zurab_Tsereteli_0001.jpg
│       └── Zydrunas_Ilgauskas
│           └── Zydrunas_Ilgauskas_0001.jpg
├── generate_test_pair.py
└── test_pair.txt

```
