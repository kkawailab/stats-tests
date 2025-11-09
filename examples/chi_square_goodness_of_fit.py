"""Chi-square goodness-of-fit test for checking if sales match an expected weekday distribution."""
from scipy import stats
import numpy as np

# --------------------------------------------------------------
# このスクリプトは、曜日ごとの売上分布が「全曜日で均等」という仮説と合致するかを
# カイ二乗適合度検定で調べます。
# 帰無仮説: 観測度数は一様分布（全曜日同じ割合）に従う。
# 対立仮説: 少なくとも 1 つの曜日で期待度数とずれる。
# --------------------------------------------------------------

# 実際に観測した各曜日の売上件数。1 週間分のデータを固定値で用意。
observed = np.array([52, 47, 50, 56, 65, 70, 60])
# 期待度数: 合計売上を曜日数で割った値を各曜日に割り当て、一様分布を表現。
expected = np.repeat(observed.sum() / observed.size, observed.size)

# stats.chisquare は観測度数と期待度数からカイ二乗統計量と p 値を返す。
statistic, p_value = stats.chisquare(f_obs=observed, f_exp=expected)

degrees_of_freedom = observed.size - 1
# 適合度検定ではカテゴリ数-1 が自由度になる。
print(f"Chi-square statistic: {statistic:.3f}")
print(f"Degrees of freedom: {degrees_of_freedom}")
print(f"p-value: {p_value:.4f}")
# p 値が 0.05 未満なら「均等分布からの逸脱あり」と解釈する。
print("Weekday sales deviate from uniform expectations" if p_value < 0.05 else "Sales align with a uniform weekday pattern.")
