import sklearn.datasets
import numpy as np



def main():

    # From http://scikit-learn.org/stable/auto_examples/plot_classifier_comparison.html
    X, y = make_classification(n_features=2, n_redundant=0, n_informative=2,
                           random_state=1, n_clusters_per_class=1)
    rng = np.random.RandomState(2)
    X += 2 * rng.uniform(size=X.shape)
    linearly_separable = (X, y)

    print linearly_separable

if __name__=='__main__':
    main()