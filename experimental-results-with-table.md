### Experimental settings

lorem ipsum

### Experiment 1: Identifying target

```
LogReg:
------
Training set:
"Match any" accuracy: 0.998
"Match all" acc: 0.943
Precision: 0.998
Recall: 0.002
F1 score: 0.005
FDR: 0.002

Test set:
"Match any" accuracy: 0.593
"Match all" acc: 0.574
Precision: 0.593
Recall: 0.396
F1 score: 0.475
FDR: 0.407

RF:
---
Training set:
"Match any" accuracy: 0.995
"Match all" acc: 0.995
Precision: 1.0
Recall: 0.0
F1 score: 0.0
FDR: 0.0

Training set:
"Match any" accuracy: 0.13
"Match all" acc: 0.111
Precision: 0.333
Recall: 0.252
F1 score: 0.287
FDR: 0.667

```

### Experiment 1.5: Can we identify (target, general)

```
LR:
---
Training set:
"Match any" accuracy: 0.988
"Match all" acc: 0.933
Precision: 0.988
Recall: 0.012
F1 score: 0.023
FDR: 0.012

Test set:
"Match any" accuracy: 0.12
"Match all" acc: 0.111
Precision: 0.12
Recall: 0.826
F1 score: 0.21
FDR: 0.88

RF:
---
Training set:
"Match any" accuracy: 0.995
"Match all" acc: 0.995
Precision: 1.0
Recall: 0.0
F1 score: 0.0
FDR: 0.0

Test set:
"Match any" accuracy: 0.028
"Match all" acc: 0.019
Precision: 0.097
Recall: 0.243
F1 score: 0.138
FDR: 0.903

```



### Experiment 2: Predicting aspect and polarity

```
LR:
---
nothing

RF:
---
Training set:
"Match any" accuracy: 0.998
"Match all" acc: 0.998
Precision: 1.0
Recall: 0.0
F1 score: 0.0
FDR: 0.0

Test set:
"Match any" accuracy: 0.694
"Match all" acc: 0.694
Precision: 0.682
Recall: 0.304
F1 score: 0.421
FDR: 0.318
```

### Experiment 3: Predicting (candidate, aspect) pairs

```
LR:
----
Nothing

RF:
---
Training set:
"Match any" accuracy: 0.998
"Match all" acc: 0.998
Precision: 0.998
Recall: 0.002
F1 score: 0.004
FDR: 0.002

Test set:
"Match any" accuracy: 0.037
"Match all" acc: 0.028
Precision: 0.121
Recall: 0.234
F1 score: 0.16
FDR: 0.879
```

| Experiment/Model   | Acc. (any) | Acc. (all) | P     | R     | F1    | FDR   |
| ------------------ | ---------- | ---------- | ----- | ----- | ----- | ----- |
| Exp 1 / LR (train) | 0.998      | 0.943      | 0.998 | 0.002 | 0.005 | 0.002 |
| Exp 1 / LR (test)  | 0.593      | 0.574      | 0.593 | 0.396 | 0.475 | 0.407 |
| Exp 1 / RF (train) | 0.995      | 0.995      | 1.00  | 0.00  | 0.00  | 0.00  |
| Exp 1 / RF (test)  | 0.130      | 0.111      | 0.333 | 0.252 | 0.287 | 0.667 |
| Exp 2 / LR (train) | 0.988      | 0.933      | 0.988 | 0.012 | 0.023 | 0.012 |
| Exp 2 / LR (test)  | 0.120      | 0.111      | 0.120 | 0.826 | 0.210 | 0.880 |
| Exp 2 / RF (train) | 0.995      | 0.995      | 1.00  | 0.00  | 0.00  | 0.00  |
| Exp 2 / RF (test)  | 0.028      | 0.019      | 0.097 | 0.243 | 0.138 | 0.903 |
| Exp 3 / RF (train) | 0.998      | 0.998      | 1.00  | 0.00  | 0.00  | 0.00  |
| Exp 3 / RF (test)  | 0.694      | 0.694      | 0.682 | 0.304 | 0.421 | 0.318 |
| Exp 4 / RF (train) | 0.998      | 0.998      | 0.998 | 0.002 | 0.004 | 0.002 |
| Rxp 4 / RF (test)  | 0.037      | 0.028      | 0.121 | 0.234 | 0.16  | 0.879 |
