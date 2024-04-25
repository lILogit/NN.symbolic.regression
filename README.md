This is an example (based on https://github.com/MilesCranmer) how compress and distill neural network weights and desribe data by a symbolic regression with pysr module.

1. train/val NN (Colab GPU), output model .ckpt (i haven't GPU)
2. distill NN (python), input model .ckpt
3. symbolic regression (pysr, Julia, Python)
4. compare original and distilled expression


Original 

$$ z = y^2,\quad y = \frac{1}{100} \sum(y_i),\quad y_i = x_{i0}^2 + 6 \cos(2*x_{i2}) $$

Distilled

$$ y = 0.477 x_{0}^{2} + 2.86 \cos{\left(2 x_{2} \right)} - 0.905 $$



  



