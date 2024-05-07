This is an example (based on https://github.com/MilesCranmer) how to approximate internal part of NN by quotation with symbolic regression. 

1. train/val NN (Colab GPU), output model .ckpt (i haven't GPU)
2. distill NN (python), input model .ckpt
3. symbolic regression (pysr, Julia, Python)
4. compare original and distilled expression


Trained data 

$$ z = y^2,\quad y = \frac{1}{100} \sum(y_i),\quad y_i = x_{i0}^2 + 6 \cos(2*x_{i2}) $$

Distilled NN quotation

$$ y = 0.477 x_{0}^{2} + 2.86 \cos{\left(2 x_{2} \right)} - 0.905 $$


Neural Network Layout

![image](https://github.com/lILogit/NN.symbolic.regression/assets/19894845/fb3f1816-2e6a-494b-8a89-2d3879c424b3)









  



