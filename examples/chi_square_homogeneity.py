"""Chi-square test of homogeneity comparing conversion across campaigns."""
from scipy import stats
import numpy as np

# --------------------------------------------------------------
# 3 種類の広告クリエイティブ（A/B/C）で、コンバージョン率が同じかどうかを
# カイ二乗同質性の検定で確かめます。
# 帰無仮説: すべてのクリエイティブで転換率の比率は同じ。
# 対立仮説: 少なくとも 1 つのクリエイティブで比率が異なる。
# --------------------------------------------------------------

# 行がクリエイティブ、列が「成約」「非成約」を表す 3×2 の分割表。
# キャンペーンごとの集計値を固定にすることで、結果を再現しやすくする。
contingency = np.array([
    [42, 158],
    [55, 145],
    [33, 170],
])

# chi2_contingency は同質性検定にも利用でき、期待度数も返してくれる。
statistic, p_value, dof, expected = stats.chi2_contingency(contingency)

print(f"Chi-square statistic: {statistic:.3f}")
print(f"Degrees of freedom: {dof}")
print(f"p-value: {p_value:.4f}")
# 閾値 5% で転換率の差があるかどうかを判定して表示。
print("Conversion rate differs by creative" if p_value < 0.05 else "No evidence of conversion difference among creatives.")
print("Expected counts:\n", expected)
