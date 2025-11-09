"""Chi-square test of independence on a contingency table."""
from scipy import stats
import numpy as np

# --------------------------------------------------------------
# 性別（女性・男性）と、好む製品カラー（A・B）の関係を
# カイ二乗独立性の検定で確認します。
# 帰無仮説: 性別と色の嗜好は独立（関連なし）。
# 対立仮説: 性別により色の嗜好分布が異なる。
# --------------------------------------------------------------

# 2×2 の分割表。行が性別、列が色の選好を表す。サンプルは固定値。
contingency = np.array([
    [35, 22],  # 女性: カラーA / カラーB
    [28, 30],  # 男性: カラーA / カラーB
])

# stats.chi2_contingency は統計量・p 値・自由度・期待度数を一度に返す。
statistic, p_value, dof, expected = stats.chi2_contingency(contingency)

print(f"Chi-square statistic: {statistic:.3f}")
print(f"Degrees of freedom: {dof}")
print(f"p-value: {p_value:.4f}")
# 期待度数との乖離が大きければ独立性が否定され、関連があると判断。
print("Preference depends on gender" if p_value < 0.05 else "Preference independent of gender.")
# 期待度数をあわせて表示し、どのセルで差が生じたかを確認できるようにする。
print("Expected counts:\n", expected)
