"""One-sample t-test comparing sample mean to a known population mean."""
from scipy import stats
import numpy as np

# --------------------------------------------------------------
# このスクリプトでは、単一の標本平均が事前に主張されている母平均（3.5 分）と
# 有意に異なるかどうかを一標本 t 検定で確認します。
# 帰無仮説: 新ワークフローの平均時短は 3.5 分である。
# 対立仮説: 新ワークフローの平均時短は 3.5 分を超える（左右両側で検定）。
# --------------------------------------------------------------

# 12 人の従業員が新ワークフローで節約した時間（分）。固定値にして再現性を確保。
sample = np.array([4.1, 3.7, 4.4, 5.2, 3.9, 4.0, 4.6, 3.8, 4.3, 4.1, 4.7, 3.6])
# 比較対象となる母平均。業務要件として「3.5 分の時短が必要」と仮定。
population_mean = 3.5

# stats.ttest_1samp で t 値と p 値を取得。デフォルトで両側検定になる点に注意。
statistic, p_value = stats.ttest_1samp(sample, population_mean)

print(f"t-statistic: {statistic:.3f}")
print(f"p-value: {p_value:.4f}")
# 5% を閾値にして、母平均との差が統計的に有意かどうかを判定。
if p_value < 0.05:
    print("Reject the null hypothesis: the workflow saves more than 3.5 minutes on average.")
else:
    print("Fail to reject the null hypothesis: insufficient evidence that savings exceed 3.5 minutes.")
