class NaiveBayesClassifier:
    def __init__(self, data):
        self.data = data
        self.class_probs = {}
        self.feature_probs = {}
    def compute_probabilities(self):
        total_samples = len(self.data)
        for row in self.data:
            label = row[-1]
            if label not in self.class_probs:
                self.class_probs[label] = 1
                self.feature_probs[label] = {}
            else:
                self.class_probs[label] += 1
            for i in range(len(row) - 1):
                feature = row[i]
                if feature not in self.feature_probs[label]:
                    self.feature_probs[label][feature] = 1
                else:
                    self.feature_probs[label][feature] += 1
        for label in self.class_probs:
            class_count = self.class_probs[label]
            self.class_probs[label] = class_count / total_samples
            for feature in self.feature_probs[label]:
                self.feature_probs[label][feature] /= class_count
    def predict(self, input_features):
        best_class = None
        max_prob = float('-inf')
        for label in self.class_probs:
            class_prob = self.class_probs[label]
            features_prob = 1.0
            for i in range(len(input_features)):
                feature = input_features[i]
                if feature in self.feature_probs[label]:
                    features_prob *= self.feature_probs[label][feature]
                else:
                    # Laplace smoothing for unseen features
                    features_prob *= 1 / (len(self.feature_probs[label]) + 1)
            if class_prob * features_prob > max_prob:
                max_prob = class_prob * features_prob
                best_class = label

        return best_class
data = [
    ["Good", "High", "A", "Pass"],
    ["Good", "Low", "B", "Pass"],
    ["Poor", "High", "C", "Fail"],
    ["Poor", "Low", "B", "Fail"],
    ["Good", "Low", "A", "Pass"],
    ["Good", "High", "C", "Pass"],
]
classifier = NaiveBayesClassifier(data)
classifier.compute_probabilities()
test_features = ["Good", "Low", "B"]
predicted_class = classifier.predict(test_features)
print("Predicted class:", predicted_class)
