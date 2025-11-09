"""Paired t-test comparing before/after measurements for the same subjects."""
from scipy import stats
import numpy as np

# --------------------------------------------------------------
# 同一ドライバーのトレーニング前後の反応時間を比較し、
# トレーニングが平均反応時間を短縮したかどうかを対応のある t 検定で確認します。
# 帰無仮説: 前後の平均反応時間に差はない。
# 対立仮説: トレーニング後の反応時間は短い（ここでは両側検定で差の有無を確認）。
# --------------------------------------------------------------

# トレーニング前の反応時間（ミリ秒）。1 人あたりの値を並べる。
before = np.array([612, 598, 605, 623, 615, 607, 618, 611])
# 同じ順序でトレーニング後の反応時間を記録。位置対応が崩れないよう注意。
after = np.array([590, 582, 588, 600, 596, 589, 594, 592])

# stats.ttest_rel は各ペアの差分に基づいて t 値・p 値を算出する。
statistic, p_value = stats.ttest_rel(before, after)

print(f"t-statistic: {statistic:.3f}")
print(f"p-value: {p_value:.4f}")
# 反応時間が有意に減少したかどうかを自然言語メッセージで表示。
print("Training significantly reduced reaction time" if p_value < 0.05 else "No significant change detected.")
