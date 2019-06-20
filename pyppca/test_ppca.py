import numpy as np
from unittest import TestCase
from pyppca import ppca


class TestPpca(TestCase):

    def setUp(self) -> None:
        n_dims = 10
        n_obs = 10000
        missing_rate = .0001
        self.n_latent = 10
        W = np.random.normal(loc=0, scale=.1, size=(n_dims, self.n_latent))

        np.random.seed(0)
        x = np.random.normal(loc=0, scale=1, size=(n_obs, self.n_latent))
        mu = np.random.normal(loc=1, scale=30, size=(1, n_dims))
        epsilon = np.random.normal(loc=0, scale=1.7, size=(n_obs, n_dims))
        t = mu + x @ W.T + epsilon

        t_masked = t.copy()
        mask = np.full(t_masked.size, False)
        n_trues = int(np.floor(mask.size * missing_rate))
        mask[:n_trues] = True
        np.random.shuffle(mask)
        a = mask.reshape(t_masked.shape)
        t_masked[a] = np.nan

        self.t_masked = t_masked
        self.t = t
        self.true = {
            'M': mu,
            'C': W
        }

    def test_ppca(self):
        t_all = self.t
        t_masked = self.t_masked
        n_latent = self.n_latent

        C, ss, M, X, Ye = ppca(Y=t_masked, d=n_latent, dia=False)

        mean_abs_err = M-self.true['M']
        mean_rel_err = np.abs(M/self.true['M']-1)

        self.assertLessEqual((mean_abs_err > 1).sum(),M.size*.1,"Absolute error in mean larger than 1 in more than 90% of cares")
        self.assertLessEqual((mean_rel_err > .05).sum(),M.size*.1,f"Relative error in mean larger than 5% in more than 90% of cases.")

        imputation_abs_err = Ye - t_all
        imputation_rel_err = np.abs(Ye/t_all-1)
        self.assertLessEqual((imputation_abs_err > 1).sum(), Ye.size * .1,
                             "Absolute error in imputation larger than 1 in more than 90% of cares")
        self.assertLessEqual((imputation_rel_err > .01).sum(), Ye.size * .1,
                             f"Relative error in imputation larger than 5% in more than 90% of cases.")

        #print(np.histogram(imputation_rel_err))