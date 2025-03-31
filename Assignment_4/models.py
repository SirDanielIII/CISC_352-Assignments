import nn


class PerceptronModel(object):
    def __init__(self, dim):
        """
        Initialize a new Perceptron instance.

        A perceptron classifies data points as either belonging to a particular
        class (+1) or not (-1). `dim` is the dimensionality of the data.
        For example, dim=2 would mean that the perceptron must classify
        2D points.
        """
        self.w = nn.Parameter(1, dim)

    def get_weights(self):
        """
        Return a Parameter instance with the current weights of the perceptron.
        """
        return self.w

    def run(self, x_point):
        """
        Calculates the score assigned by the perceptron to a data point x.

        Inputs:
            x_point: a node with shape (1 x dimensions)
        Returns: a node containing a single number (the score)
        """
        "*** YOUR CODE HERE ***"
        return nn.DotProduct(self.w, x_point)

    def get_prediction(self, x_point):
        """
        Calculates the predicted class for a single data point `x_point`.

        Returns: -1 or 1
        """
        "*** YOUR CODE HERE ***"
        if nn.as_scalar(self.run(x_point)) >= 0:
            return 1
        else:
            return -1

    def train_model(self, dataset):
        """
        Train the perceptron until convergence.
        """
        "*** YOUR CODE HERE ***"
        # Keep training until there are no mistakes.
        while True:
            no_mistakes = True
            for x, y in dataset.iterate_once(1):
                # Convert the target from the Constant node into a Python scalar.
                true_label = nn.as_scalar(y)
                # If the prediction doesn't match the true label, then update the weights.
                if self.get_prediction(x) != true_label:
                    self.w.update(true_label, x)
                    no_mistakes = False
            # If there were no mistakes made during the pass, the training is complete.
            if no_mistakes:
                break


class RegressionModel(object):
    """
    A neural network model for approximating a function that maps from real
    numbers to real numbers. The network should be sufficiently large to be able
    to approximate sin(x) on the interval [-2pi, 2pi] to reasonable precision.
    """

    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        # network with an input layer and 2 hidden layer, with each layer having a size of 50
        self.w1 = nn.Parameter(1, 50)
        self.b1 = nn.Parameter(1, 50)

        self.w2 = nn.Parameter(50, 50)
        self.b2 = nn.Parameter(1, 50)

        self.w3 = nn.Parameter(50, 1)  
        self.b3 = nn.Parameter(1, 1)

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
        Returns:
            A node with shape (batch_size x 1) containing predicted y-values
        """
        "*** YOUR CODE HERE ***"
        # x is (batch_size x 1)
        # 1) First linear layer and applying ReLU function
        h1 = nn.Linear(x, self.w1)  # shape: (batch_size x 50)
        h1 = nn.AddBias(h1, self.b1)  # shape: (batch_size x 50)
        h1 = nn.ReLU(h1)  # shape: (batch_size x 50)

        # 2) Second linear layer and applying ReLU functon
        h2 = nn.Linear(h1, self.w2)  # shape: (batch_size x 50)
        h2 = nn.AddBias(h2, self.b2)  # shape: (batch_size x 50)
        h2 = nn.ReLU(h2)  # shape: (batch_size x 50)

        # 3) Final linear transformation
        y_pred = nn.Linear(h2, self.w3)  # shape: (batch_size x 1)
        y_pred = nn.AddBias(y_pred, self.b3)  # shape: (batch_size x 1)
        return y_pred

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
            y: a node with shape (batch_size x 1), containing the true y-values
                to be used for training
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        # Predict
        y_prediction = self.run(x)
        # Return a square loss node
        return nn.SquareLoss(y_prediction, y)

    def train_model(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        batch_size = 10
        learning_rate = 0.01

        while True:
            for x_batch, y_batch in dataset.iterate_once(batch_size):
                # gets loss and gradients
                loss = self.get_loss(x_batch, y_batch)
                grads = nn.gradients([self.w1, self.b1,
                                      self.w2, self.b2,
                                      self.w3, self.b3],
                                     loss)
                # Perform gradient updates
                for param, grad in zip([self.w1, self.b1,
                                        self.w2, self.b2,
                                        self.w3, self.b3],
                                       grads):
                    param.update(-learning_rate, grad)

            # After going through one full pass, check the loss
            # on the entire training set:
            total_loss = nn.as_scalar(
                self.get_loss(nn.Constant(dataset.x),
                              nn.Constant(dataset.y)))
            if total_loss < 0.02:
                return  # WE DID ITTTT


class DigitClassificationModel(object):
    """
    A model for handwritten digit classification using the MNIST dataset.

    Each handwritten digit is a 28x28 pixel grayscale image, which is flattened
    into a 784-dimensional vector for the purposes of this model. Each entry in
    the vector is a floating point number between 0 and 1.

    The goal is to sort each digit into one of 10 classes (number 0 through 9).

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """

    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        # 3 hidden layers, each with size 300
        self.w1 = nn.Parameter(784, 300)
        self.b1 = nn.Parameter(1, 300)

        self.w2 = nn.Parameter(300, 300)
        self.b2 = nn.Parameter(1, 300)

        self.w3 = nn.Parameter(300, 300)
        self.b3 = nn.Parameter(1, 300)

        # Output layer
        self.w4 = nn.Parameter(300, 10)
        self.b4 = nn.Parameter(1, 10)

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Your model should predict a node with shape (batch_size x 10),
        containing scores. Higher scores correspond to greater probability of
        the image belonging to a particular class.

        Inputs:
            x: a node with shape (batch_size x 784)
        Output:
            A node with shape (batch_size x 10) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"
        # Layer 1 (batch_size x 300)
        h1 = nn.Linear(x, self.w1)
        h1 = nn.AddBias(h1, self.b1)
        h1 = nn.ReLU(h1)

        # Layer 2 (batch_size x 300)
        h2 = nn.Linear(h1, self.w2)
        h2 = nn.AddBias(h2, self.b2)
        h2 = nn.ReLU(h2)

        # Layer 3 (batch_size x 300)
        h3 = nn.Linear(h2, self.w3)
        h3 = nn.AddBias(h3, self.b3)
        h3 = nn.ReLU(h3)

        # Output scores
        logits = nn.Linear(h3, self.w4)  # (batch_size x 10)
        logits = nn.AddBias(logits, self.b4)
        return logits

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 10). Each row is a one-hot vector encoding the correct
        digit class (0-9).

        Inputs:
            x: a node with shape (batch_size x 784)
            y: a node with shape (batch_size x 10)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        logits = self.run(x)
        return nn.SoftmaxLoss(logits, y)

    def train_model(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        batch_size = 200
        learning_rate = 0.1
        max_epochs = 25
        # parameters which include all the weights and biases
        params = [self.w1, self.b1,
                  self.w2, self.b2,
                  self.w3, self.b3,
                  self.w4, self.b4]

        best_dev_acc = 0.0
        epochs_since_improvement = 0

        for epoch in range(max_epochs):
            # One epoch over the training set
            for x_batch, y_batch in dataset.iterate_once(batch_size): # calculates loss and grads for each batch in the data set
                loss = self.get_loss(x_batch, y_batch)
                grads = nn.gradients(params, loss)
                # performs the Gradient update
                for p, g in zip(params, grads):
                    p.update(-learning_rate, g)

            # Checks validation accuracy
            dev_acc = dataset.get_validation_accuracy()
            print(f"Epoch {epoch + 1}, Learning Rate={learning_rate}, Dev accuracy={dev_acc:.4%}")

            # If we improved, reset stagnation counter
            if dev_acc > best_dev_acc:
                best_dev_acc = dev_acc
                epochs_since_improvement = 0
            else:
                # if there is No improvement, increment the counter
                epochs_since_improvement += 1

            # If we’re at or above 98% break out of loop
            if dev_acc >= 0.98:
                print("Reached 98% (or more) validation accuracy.")
                break

            # If no improvement over 2 epochs, reduce the Learning date and reset the counter
            if epochs_since_improvement >= 2:
                learning_rate *= 0.5
                epochs_since_improvement = 0

        print(f"Final validation accuracy: {best_dev_acc}")
