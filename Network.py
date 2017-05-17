import numpy


class FeedForwardNetwork(object):
    def __init__(self, in_nodes, hidden_nodes, out_nodes):
        # Learning rate
        self.alpha = 0.01

        # Number of neurons in each layer
        self.in_nodes = in_nodes
        self.hidden_nodes = hidden_nodes
        self.out_nodes = out_nodes

        # Initialize weights randomly (+1 for bias)
        self.hidden_weights = numpy.random.random((self.hidden_nodes, self.in_nodes + 1))
        self.out_weights = numpy.random.random((self.out_nodes, self.hidden_nodes + 1))

        # Activation of neurons (sum of inputs)
        self.hidden_activation = numpy.zeros((self.hidden_nodes, 1), float)
        self.out_activation = numpy.zeros((self.out_nodes, 1), float)

        # Outputs of neurons (after sigmoid)
        self.in_output = numpy.zeros((self.in_nodes + 1, 1), float)
        self.hidden_output = numpy.zeros((self.hidden_nodes + 1, 1), float)
        self.out_output = numpy.zeros(self.out_nodes, float)

        # Deltas for hidden and output layers
        self.hidden_delta = numpy.zeros(self.hidden_nodes, float)
        self.out_delta = numpy.zeros(self.out_nodes, float)

    def forward(self, in_data):
        # Set input as output of first layer (bias neuron = 1.0)
        self.in_output[:-1, 0] = in_data
        self.in_output[-1:, 0] = 1.0

        # Hidden layer
        self.hidden_activation = numpy.dot(self.hidden_weights, self.in_output)
        self.hidden_output[:-1, :] = numpy.tanh(self.hidden_activation)

        # Set bias neuron in hidden layer to 1.0
        self.hidden_output[-1:, :] = 1.0

        # Output layer
        self.out_activation = numpy.dot(self.out_weights, self.hidden_output)
        self.out_output = numpy.tanh(self.out_activation)

    def backwards(self, teach_data):
        error = self.out_output - numpy.array(teach_data, float)

        # Deltas of output neurons
        self.out_delta = (1 - numpy.tanh(self.out_activation)) * numpy.tanh(self.out_activation) * error

        # Deltas of hidden neurons
        self.hidden_delta = (1 - numpy.tanh(self.hidden_activation)) * numpy.tanh(self.hidden_activation) * \
                            numpy.dot(self.out_weights[:, :-1].transpose(), self.out_delta)

        # Apply weight changes
        self.hidden_weights = self.hidden_weights - self.alpha * \
                                                    numpy.dot(self.hidden_delta, self.in_output.transpose())
        self.out_weights = self.out_weights - self.alpha * numpy.dot(self.out_delta, self.hidden_output.transpose())

    def get_output(self):
        return self.out_output
