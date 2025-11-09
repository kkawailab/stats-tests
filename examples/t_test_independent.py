"""Independent two-sample t-test comparing two groups."""
from scipy import stats
import numpy as np

# --------------------------------------------------------------
# このスクリプトは 2 つの独立した群（旧式と新式のオンボーディングフロー）で
# 平均満足度に差があるかを Welch の t 検定で判定します。
# 帰無仮説: 両群の母平均は等しい。
# 対立仮説: 両群の母平均は異なる（両側検定）。
# Welch 法は分散が等しくない可能性がある実務データ向きです。
# --------------------------------------------------------------

# 1-7 のリッカート尺度で集計した満足度スコア（旧フロー）
legacy = np.array([4.8, 5.1, 4.5, 4.9, 5.0, 4.7, 4.6, 4.8, 5.2, 4.5])
# 新フローの満足度スコア。サンプルサイズを揃えて比較を容易にする。
new = np.array([5.4, 5.6, 5.1, 5.5, 5.7, 5.2, 5.6, 5.3, 5.7, 5.4])

# equal_var=False により Welch t 検定を選択。分散が異なる場合でも頑健。
statistic, p_value = stats.ttest_ind(new, legacy, equal_var=False)

print(f"t-statistic: {statistic:.3f}")
print(f"p-value: {p_value:.4f}")
# 解釈を簡潔に出力。p 値が 0.05 未満なら新フローが有意に高いとみなす。
print("The new onboarding flow is statistically higher" if p_value < 0.05 else "No significant difference detected.")
