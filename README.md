## How to run?
1. Create a virtual environment.
2. pip install -r requirements.txt
3. streamlit run app.py

## With CPU:
10 epochs completed in 0.963 hours.
Optimizer stripped from /home/red_crown/Documents/Project/Garbage_Detection_Project/runs/detect/train/weights/last.pt, 6.3MB
Optimizer stripped from /home/red_crown/Documents/Project/Garbage_Detection_Project/runs/detect/train/weights/best.pt, 6.3MB

Validating /home/red_crown/Documents/Project/Garbage_Detection_Project/runs/detect/train/weights/best.pt...
Ultralytics 8.4.48 🚀 Python-3.12.3 torch-2.11.0+cu130 CPU (12th Gen Intel Core i5-12450H)
Model summary (fused): 73 layers, 3,017,153 parameters, 0 gradients, 8.1 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 10% ━─────────── 1/10 10.2s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 20% ━━────────── 2/10 6.2s/
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 30% ━━━╸──────── 3/10 4.9s/
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 40% ━━━━╸─────── 4/10 4.2s/
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 50% ━━━━━━────── 5/10 3.8s/
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 60% ━━━━━━━───── 6/10 3.5s/
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 70% ━━━━━━━━──── 7/10 3.4s/
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 80% ━━━━━━━━━╸── 8/10 3.3s/
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 90% ━━━━━━━━━━╸─ 9/10 3.2s/
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 10/10 2.9s/it 29.0s
                   all        300       1057      0.395     0.0876     0.0433     0.0332
        Aluminium foil          9          9          0          0     0.0117    0.00937
          Broken glass          4         81          1          0     0.0025    0.00125
             Cigarette         70        163     0.0165     0.0123    0.00846     0.0036
  Clear plastic bottle         62         81      0.249      0.444      0.221      0.173
     Corrugated carton          4          4          0          0     0.0049    0.00441
          Crisp packet          2          2          0          0     0.0141     0.0127
Disposable food container          7          7      0.157      0.143     0.0382     0.0347
Disposable plastic cup         19         21          0          0     0.0349     0.0304
             Drink can         26         42       0.11      0.452      0.154      0.111
          Drink carton         18         21     0.0135    0.00128     0.0707     0.0599
            Egg carton          2          2          1          0     0.0193      0.016
              Foam cup          1          1          1          0     0.0284     0.0171
   Foam food container          1          1          1          0     0.0302     0.0302
              Food Can          3          3     0.0867      0.333      0.182      0.165
           Garbage bag          5         12          0          0     0.0135     0.0105
          Glass bottle         24         38      0.079     0.0789     0.0682     0.0485
        Magazine paper          1          1          1          0     0.0369     0.0369
           Meal carton          2          2     0.0671        0.5     0.0428     0.0417
      Metal bottle cap         14         25     0.0492       0.04    0.00629     0.0036
          Normal paper         16         21          0          0     0.0247     0.0137
          Other carton         19         23     0.0812       0.13     0.0492     0.0361
         Other plastic         38         57     0.0722      0.203     0.0497      0.035
  Other plastic bottle         10         10          0          0     0.0145     0.0143
Other plastic container          1          1          1          0          0          0
     Other plastic cup          1          1          1          0          0          0
 Other plastic wrapper         35         42     0.0852      0.381     0.0617     0.0401
             Paper bag          1          1          1          0     0.0311     0.0144
             Paper cup         16         17      0.194      0.176      0.112     0.0835
             Pizza box          1          1          1          0          0          0
    Plastic bottle cap         44         49      0.102      0.143     0.0567     0.0365
          Plastic film         68         81      0.124       0.42      0.161      0.118
       Plastic glooves          1          1          1          0    0.00544    0.00205
           Plastic lid         12         13     0.0609     0.0769     0.0327     0.0273
         Plastic straw         15         17      0.244      0.176      0.117     0.0772
      Plastic utensils          2          2          1          0    0.00913    0.00357
     Polypropylene bag          1          1          1          0          0          0
               Pop tab         11         19          0          0          0          0
        Rope - strings          6          6          1          0     0.0138    0.00413
           Scrap metal          3          4          0          0          0          0
Single-use carrier bag         15         19      0.223      0.105      0.126      0.106
        Six pack rings          1          1          1          0     0.0474     0.0379
            Spread tub          3          3          0          0          0          0
       Squeezable tube          1          1          1          0          0          0
       Styrofoam piece         16         24      0.029     0.0417     0.0288     0.0278
               Tissues         12         13      0.421     0.0769     0.0408     0.0368
      Unlabeled litter         70        112     0.0987      0.179     0.0533     0.0288
        Wrapping paper          1          1          1          0     0.0108    0.00973
Speed: 1.8ms preprocess, 88.2ms inference, 0.0ms loss, 0.9ms postprocess per image
Results saved to /home/red_crown/Documents/Project/Garbage_Detection_Project/runs/detect/train


## With GPU:

50 epochs completed in 0.375 hours.
Optimizer stripped from /home/red_crown/Documents/Project/Garbage_Detection_Project/runs/detect/train/weights/last.pt, 22.6MB
Optimizer stripped from /home/red_crown/Documents/Project/Garbage_Detection_Project/runs/detect/train/weights/best.pt, 22.6MB

Validating /home/red_crown/Documents/Project/Garbage_Detection_Project/runs/detect/train/weights/best.pt...
Ultralytics 8.4.48 🚀 Python-3.12.3 torch-2.11.0+cu130 CUDA:0 (NVIDIA GeForce RTX 3050 6GB Laptop GPU, 5804MiB)
Model summary (fused): 73 layers, 11,148,417 parameters, 0 gradients, 28.6 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 5% ╸─────────── 1/19 2.4it/
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 11% ━─────────── 2/19 3.6it
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 16% ━╸────────── 3/19 3.1it
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 21% ━━╸───────── 4/19 4.0it
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 26% ━━━───────── 5/19 3.9it
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 32% ━━━╸──────── 6/19 5.0it
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 37% ━━━━──────── 7/19 5.9it
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 42% ━━━━━─────── 8/19 6.5it
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 47% ━━━━━╸────── 9/19 6.9it
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 53% ━━━━━━────── 10/19 7.2i
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 58% ━━━━━━╸───── 11/19 7.3i
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 63% ━━━━━━━╸──── 12/19 7.5i
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 68% ━━━━━━━━──── 13/19 7.6i
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 74% ━━━━━━━━╸─── 14/19 7.6i
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 79% ━━━━━━━━━─── 15/19 7.7i
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 84% ━━━━━━━━━━── 16/19 7.7i
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 89% ━━━━━━━━━━╸─ 17/19 7.8i
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 95% ━━━━━━━━━━━─ 18/19 7.8i
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 19/19 6.3it/s 3.0s
                   all        300       1057      0.283      0.172      0.128      0.107
        Aluminium foil          9          9     0.0882      0.205     0.0738     0.0629
          Broken glass          4         81          0          0          0          0
             Cigarette         70        163      0.162      0.196      0.122     0.0667
  Clear plastic bottle         62         81      0.328      0.556      0.388      0.304
     Corrugated carton          4          4          0          0          0          0
          Crisp packet          2          2     0.0435        0.5     0.0398     0.0324
Disposable food container          7          7      0.198      0.143      0.149      0.148
Disposable plastic cup         19         21     0.0866      0.286     0.0826      0.071
             Drink can         26         42      0.249      0.548      0.386      0.305
          Drink carton         18         21          0          0      0.083     0.0651
            Egg carton          2          2          1          0          0          0
              Foam cup          1          1          0          0          0          0
   Foam food container          1          1      0.536          1      0.995      0.995
              Food Can          3          3      0.128      0.333      0.374      0.333
           Garbage bag          5         12      0.339     0.0833      0.104     0.0936
          Glass bottle         24         38       0.16      0.211      0.138      0.116
        Magazine paper          1          1          1          0          0          0
           Meal carton          2          2          0          0    0.00192    0.00192
      Metal bottle cap         14         25     0.0808       0.12     0.0271      0.019
          Normal paper         16         21     0.0466     0.0288     0.0571      0.045
          Other carton         19         23      0.176      0.304      0.224      0.154
         Other plastic         38         57     0.0164     0.0175     0.0158     0.0102
  Other plastic bottle         10         10     0.0628        0.1     0.0224     0.0217
Other plastic container          1          1          0          0          0          0
     Other plastic cup          1          1          1          0          0          0
 Other plastic wrapper         35         42      0.157      0.333      0.148     0.0891
             Paper bag          1          1          0          0          0          0
             Paper cup         16         17      0.297      0.412       0.42      0.378
             Pizza box          1          1          1          0          0          0
    Plastic bottle cap         44         49      0.219      0.184      0.185     0.0803
          Plastic film         68         81      0.169      0.432      0.249       0.19
       Plastic glooves          1          1      0.862          1      0.995      0.895
           Plastic lid         12         13      0.107      0.154     0.0892      0.087
         Plastic straw         15         17       0.14      0.176      0.111     0.0562
      Plastic utensils          2          2          0          0     0.0177     0.0159
     Polypropylene bag          1          1          1          0          0          0
               Pop tab         11         19      0.261      0.105     0.0784     0.0478
        Rope - strings          6          6     0.0869      0.167      0.165      0.149
           Scrap metal          3          4          0          0    0.00258    0.00232
Single-use carrier bag         15         19      0.156      0.158     0.0614     0.0472
        Six pack rings          1          1          1          0          0          0
            Spread tub          3          3          1          0          0          0
       Squeezable tube          1          1          1          0          0          0
       Styrofoam piece         16         24      0.105      0.208      0.122      0.108
               Tissues         12         13          0          0     0.0358      0.025
      Unlabeled litter         70        112      0.057      0.134     0.0197    0.00919
        Wrapping paper          1          1          0          0     0.0112      0.006
Speed: 0.4ms preprocess, 6.5ms inference, 0.0ms loss, 2.2ms postprocess per image
Results saved to /home/red_crown/Documents/Project/Garbage_Detection_Project/runs/detect/train
