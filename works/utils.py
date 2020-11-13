# サンプル画像を表示する関数
import glob
import os
import random

import math
import numpy as np
import pandas as pd


import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt

from tensorflow.python.keras.preprocessing.image import img_to_array, load_img

def imshow_with_title(ax, img, title):
        ax.imshow(img / 255.)
        ax.set_title(title)
        ax.axis('off')
        return ax

def get_train_sample_info(img_itr, n):
    class_labels = {idx: label for label, idx in img_itr.class_indices.items()}
    out_imgs, out_labels = np.array([]), np.array([])
    while len(out_imgs) < n:
        images, class_idx = next(img_itr)
        labels = [class_labels[idx]  for idx in  class_idx]
        out_imgs = np.concatenate([out_imgs, images]) if out_imgs else images
        out_labels = np.concatenate([out_labels, labels]) if out_labels  else  labels
    return out_imgs[:n], out_labels[:n]
    
def get_pred_sample_labels(probs, class_indices):
    class_labels = {idx: label for label, idx in class_indices.items()}
    tmp = '{}:{:.3f}  /  {}:{:.3f}'
    lbls = [tmp.format(class_labels[0], 1- p[0], class_labels[1], p[0])
                    for p in probs]
    return lbls

def show_img_samples(imgs, labels, ncols=4, save_fig=None):    
    n = len(imgs)
    nrows = math.ceil(n / ncols)
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(4 * ncols, 4 * nrows))
    for ax, img, label in zip(axes.ravel(), imgs, labels):
        ax = imshow_with_title(ax, img, label) 
    if save_fig:
        fig.savefig(save_fig)
    # fig.show()

def show_train_samples_iter(img_itr, n=8):
    imgs, labels = get_train_sample_info(img_itr, n)
    show_img_samples(imgs, labels)

def show_train_samples(img_dir, classes, n=4, seed=0, save_fig=None):
    labels = []
    imgs = None
    for img_class in classes:
         labels += [img_class] * n 
         data_dir = os.path.join(img_dir, 'train/{}'.format(img_class))
         now_imgs, _ = load_random_imgs(data_dir, n, seed=seed)
         imgs = now_imgs if imgs is None else np.concatenate([imgs, now_imgs], axis=0)
    show_img_samples(imgs, labels, save_fig=save_fig)

def show_test_samples(imgs, probs, class_indices, true_labels):
    pred_labels = get_pred_sample_labels(probs, class_indices)
    labels = [p + '\n' + 'True:' + t for p, t in zip(pred_labels, true_labels)]
    show_img_samples(imgs, labels)

def ext_label_from_filepath(img_path):
    target_idx = 0
    return os.path.basename(img_path).split('_')[target_idx]
    
def get_rand_img_paths(data_dir, n, seed=0, with_labels=False):
    g = os.path.join(data_dir, '*.jpg')
    img_paths = glob.glob(g)
    random.seed(seed)
    random.shuffle(img_paths)
    target_paths = img_paths[:n]
    if with_labels:
        true_labels = [ext_label_from_filepath(x) for x in target_paths]
        return target_paths, true_labels
    else:
        return target_paths

def load_imgs(img_paths, target_size):
    list_imgs = [img_to_array(load_img(path, target_size=target_size))
                    for path in img_paths]
    return np.array(list_imgs)

def load_random_imgs(data_dir, n=8, seed=0, target_size=(224, 224)):
    target_paths, true_labels = get_rand_img_paths(data_dir, n, seed=seed, with_labels=True)
    imgs = load_imgs(target_paths, target_size)
    return imgs, true_labels


def adjust_ax(df, ax, ylabel):
    df.plot(ax=ax)
    ax.set_title(ylabel)
    ax.set_xlabel('epochs')
    ax.set_ylabel(ylabel)
    ax.legend()
    return ax

def plot_learningcurve(df_history):
    figsize = (12, 4)
    nrows = 1
    ncols = 2
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    for ax, lbl in zip(axes.ravel(), ('acc', 'loss')):
        df = df_history[[lbl, 'val_{}'.format(lbl)]]
        ax = adjust_ax(df, ax, ylabel=lbl)

def plot_learningcurve_from_csv(csv_filepath):
    df_history = pd.read_csv(csv_filepath)
    plot_learningcurve(df_history)
