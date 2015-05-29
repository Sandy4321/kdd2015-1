# -*- coding: utf-8 -*-
from sklearn.cross_validation import train_test_split
from sklearn.metrics import roc_auc_score

from kdd2015.data import load_data
from kdd2015.model import build_model


if __name__ == '__main__':
    df, df_ans, x_train, y_train, x_test = load_data()
    x_train_cv, x_test_cv, y_train_cv, y_test_cv = train_test_split(
        x_train, y_train, test_size=0.375, random_state=23)

    model = build_model()

    model.fit(
        x_train_cv[:800], y_train_cv[:800],
        batch_size=16,
        nb_epoch=5
    )

    predicts_cv = model.predict_proba(x_test_cv, batch_size=16)
    print('roc_auc_score of cv %f' % roc_auc_score(y_test_cv, predicts_cv))
