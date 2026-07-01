import numpy as np

def perceptron(X, y, lr=0.1, epochs=100):
    X = np.array(X)
    y = np.array(y) # Convert y to numpy for easier handling
    
    # 1. Initialize weights as a numpy array and bias as a float
    w = np.zeros(X.shape[1]) 
    b = 0.0
    
    runs = 0
    while runs < epochs:
        for idx, i in enumerate(X):
            # 2. Calculate the linear output (w · x + b)
            linear_output = np.dot(i, w) + b
            
            # 3. Step activation function (predict 1 if >= 0, else 0)
            y_pred = 1.0 if linear_output >= 0 else 0.0
            
            # 4. Perceptron Update Rule: weight = weight + lr * (target - prediction) * x
            error = y[idx] - y_pred
            
            if error != 0:
                w = w + lr * error * i
                b = b + lr * error
                
        runs += 1
        
    # Convert weights back to a list of floats to match your return hint
    return w.tolist(), float(b)
