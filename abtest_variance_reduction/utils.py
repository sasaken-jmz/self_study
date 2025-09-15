# モジュールインポート
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# データ生成
def generate_data(
    seed = 42,
    n = 1000,
    x_mean = 0.0,
    x_sd = 1.0,
    rho_x_y = 0.6, # ρをLaTeX「\rho」と書くことから、相関係数を「rho」という変数とする
    y_mean = 0.0,
    y_sd = 1.0,
    tau_mean = 0.5,
    tau_sd = 1.0,
    p = 0.5,  
):
    rng = np.random.default_rng(seed)
    X = rng.normal(loc=x_mean, scale=x_sd, size=n)
    
    # 「X: 平均0・分散1、Y: 平均0・分散1、XとYには0.6（デフォルト）の相関あり」というデータを作成
    x_std = (X - X.mean()) / X.std(ddof=0)
    z = rng.normal(size=n)
    y_std = rho_x_y * x_std + np.sqrt(1.0 - rho_x_y**2) * z
    Y = y_mean + y_sd * y_std   # 標本平均・分散はズレるが、母集団では(0,1)→(y_mean, y_sd^2)

    tau = rng.normal(loc=tau_mean, scale=tau_sd, size=n)

    T = rng.binomial(1, p, size=n).astype(int)

    df = pd.DataFrame([])
    df['X'] = X
    df['Y0'] = Y
    df['tau'] = tau
    df['T'] = T
    df['Y1'] = df['Y0'] + df['tau']
    df['Y'] = df['T'] * df['Y1'] + (1-df['T']) * df['Y0']

    return df

# データ生成: 効果に異質性があるver
def generate_data2(
    seed = 42,
    n = 1000,
    x_mean = 0.0,
    x_sd = 1.0,
    rho_x_y = 0.6, # ρをLaTeX「\rho」と書くことから、相関係数を「rho」という変数とする
    y_mean = 0.0,
    y_sd = 1.0,
    tau_mean = 0.5,
    tau_sd = 1.0,
    p = 0.5,
):
    rng = np.random.default_rng(seed)
    X = rng.normal(loc=x_mean, scale=x_sd, size=n)
    
    # 「X: 平均0・分散1、Y: 平均0・分散1、XとYには0.6（デフォルト）の相関あり」というデータを作成
    x_std = (X - X.mean()) / X.std(ddof=0)
    z = rng.normal(size=n)
    y_std = rho_x_y * x_std + np.sqrt(1.0 - rho_x_y**2) * z
    Y = y_mean + y_sd * y_std   # 標本平均・分散はズレるが、母集団では(0,1)→(y_mean, y_sd^2)

    tau = rng.normal(loc=tau_mean, scale=tau_sd, size=n)

    T = rng.binomial(1, p, size=n).astype(int)

    df = pd.DataFrame([])
    df['X'] = X
    df['Y0'] = Y
    df['tau'] = tau + X # 単純にXを足す: これによりXの値が小さい人は効果が小さいし、大きい人は効果が大きいという異質性が生まれる
    df['T'] = T
    df['Y1'] = df['Y0'] + df['tau']
    df['Y'] = df['T'] * df['Y1'] + (1-df['T']) * df['Y0']

    return df

# 単純比較による効果推定
def return_avg_tau(df):
    avg_tau = df[df['T']==1]['Y'].mean() - df[df['T']==0]['Y'].mean()
    return avg_tau

# 回帰モデルによる効果推定
def return_ols_tau(df):
    cols = ["T"] + (["X"] if "X" in df.columns else [])
    X = sm.add_constant(df[cols], has_constant="add")
    res = sm.OLS(df["Y"], X).fit()
    tau_hat = res.params["T"]
    return tau_hat

# 真のtauを得る関数
def return_true_tau(df):
    true_tau = df[df['T']==1]['tau'].mean()
    return true_tau

# 推定結果のヒストグラムを描画
def plot_histgram(avg_att_list, true_tau_list):
    y = np.asarray(avg_att_list, float)
    tau_mean = np.array(true_tau_list).mean()
    plt.figure(figsize=(6,4))
    plt.hist(y, bins=100, edgecolor="k", alpha=0.8)      # ヒストグラム
    plt.axvline(y.mean(), ls="--", label=f"mean={tau_mean:.3f}")  # 平均の縦線（任意）
    plt.xlabel("avg_att"); plt.ylabel("count")
    plt.xlim(0, 0.8)
    plt.title("Histogram of avg_att")
    plt.legend(); plt.tight_layout()
    plt.show()

# ATT(=ATe)の分散を計算
def calc_var(avg_att_list):
    arr = np.asarray(avg_att_list, float)
    var_sam = np.var(arr, ddof=1)   # 不偏分散（割るのは n-1）
    return var_sam

# 真の効果に近い値0.4-0.6を推定できている割合
def calc_prop_near(avg_att_list):
    arr = np.asarray(avg_att_list, float)
    prop = np.mean((arr >= 0.4) & (arr <= 0.6))
    return prop



