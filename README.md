# Python Statistical Tests Samples

このリポジトリでは、SciPy を用いた t 検定とカイ二乗検定の代表的なユースケースを 3 本ずつ収録しています。いずれも単体実行でき、GitHub 上でそのまま参照できるように README で概要をまとめています。

## 使用ライブラリ
- [SciPy](https://scipy.org/) 1.10+ : `scipy.stats` の t 検定・カイ二乗検定関数を利用
- NumPy 1.24+ : サンプルデータ生成と配列演算

## 実行方法
[`uv`](https://docs.astral.sh/uv/) を使って依存関係を高速に解決します。
```bash
uv venv .venv
source .venv/bin/activate
uv pip install numpy scipy
uv run python examples/<script>.py  # 任意のスクリプト名に差し替え
```

---

## t 検定サンプル
| スクリプト | 内容 | 想定シナリオ |
| --- | --- | --- |
| `examples/t_test_one_sample.py` | `stats.ttest_1samp` を使い、サンプル平均と既知の母平均を比較します。 | 新ワークフローが平均 3.5 分以上の時短効果を持つか検証。 |
| `examples/t_test_independent.py` | Welch の 2 標本 t 検定 (`stats.ttest_ind ... equal_var=False`) で 2 つの独立群の平均差を評価。 | 旧 vs. 新オンボーディングフローの満足度比較。 |
| `examples/t_test_paired.py` | 対応のある t 検定 (`stats.ttest_rel`) で同一被験者の Before/After を比較。 | ドライバー訓練前後の反応時間短縮をチェック。 |

各スクリプトは t 統計量・p 値とシンプルな解釈メッセージを標準出力します。

## カイ二乗検定サンプル
| スクリプト | 内容 | 想定シナリオ |
| --- | --- | --- |
| `examples/chi_square_goodness_of_fit.py` | `stats.chisquare` により観測分布が一様分布に従うか検証。 | 曜日ごとの売上が均一かどうかの当てはまり検定。 |
| `examples/chi_square_independence.py` | `stats.chi2_contingency` で 2×2 分割表の独立性を判定。 | 性別とプロダクト色の好みの独立性検定。 |
| `examples/chi_square_homogeneity.py` | 複数群の割合が同じかを `stats.chi2_contingency` で比較。 | 広告クリエイティブ間のコンバージョン率の同質性検定。 |

出力にはカイ二乗統計量・自由度・p 値に加え、`chi2_contingency` を用いる例では期待度数も含めています。

---

## チュートリアル: サンプルスクリプトを追いながら理解する
以下は各スクリプトの抜粋と、その挙動を確認するコマンド例です。コードの全体像は記載されたパスを直接開いてください。

### コマンド構文のポイント
`uv run --with numpy --with scipy python3 examples/<script>.py`
- `uv run`: 仮想環境を自動的に解決し、指定コマンドを一時的な依存関係付きで実行します。
- `--with <package>`: その場で必要ライブラリを解決します。複数指定可能で、ここでは `numpy` と `scipy` を事前にプルします。
- `python3 examples/<script>.py`: 実行したい Python インタプリタとスクリプトパス。`<script>` 部分を実際のファイル名に置き換えてください。
- 既に `uv pip install` で依存解決済みの場合は `--with` を省略しても構いません。

### 1. 一標本 t 検定 (`examples/t_test_one_sample.py`)
```python
sample = np.array([4.1, 3.7, 4.4, 5.2, 3.9, 4.0, 4.6, 3.8, 4.3, 4.1, 4.7, 3.6])
population_mean = 3.5
statistic, p_value = stats.ttest_1samp(sample, population_mean)
```
- コマンド: `uv run --with numpy --with scipy python3 examples/t_test_one_sample.py`
- 固定サンプルが要件値 3.5 分を上回るか検証し、p 値と解釈を出力します。

### 2. Welch の 2 標本 t 検定 (`examples/t_test_independent.py`)
```python
legacy = np.array([4.8, 5.1, 4.5, 4.9, 5.0, 4.7, 4.6, 4.8, 5.2, 4.5])
new = np.array([5.4, 5.6, 5.1, 5.5, 5.7, 5.2, 5.6, 5.3, 5.7, 5.4])
statistic, p_value = stats.ttest_ind(new, legacy, equal_var=False)
```
- コマンド: `uv run --with numpy --with scipy python3 examples/t_test_independent.py`
- `equal_var=False` で Welch 検定を行い、新旧フローの満足度差を判定します。

### 3. 対応のある t 検定 (`examples/t_test_paired.py`)
```python
before = np.array([612, 598, 605, 623, 615, 607, 618, 611])
after = np.array([590, 582, 588, 600, 596, 589, 594, 592])
statistic, p_value = stats.ttest_rel(before, after)
```
- コマンド: `uv run --with numpy --with scipy python3 examples/t_test_paired.py`
- 同一ドライバーの前後データをペアで比較し、反応時間が短縮されたかを確認します。

### 4. 適合度検定 (`examples/chi_square_goodness_of_fit.py`)
```python
observed = np.array([52, 47, 50, 56, 65, 70, 60])
expected = np.repeat(observed.sum() / observed.size, observed.size)
statistic, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
```
- コマンド: `uv run --with numpy --with scipy python3 examples/chi_square_goodness_of_fit.py`
- 曜日ごとの売上が一様分布から外れているかどうかを評価します。

### 5. 独立性の検定 (`examples/chi_square_independence.py`)
```python
contingency = np.array([[35, 22],
                        [28, 30]])
statistic, p_value, dof, expected = stats.chi2_contingency(contingency)
```
- コマンド: `uv run --with numpy --with scipy python3 examples/chi_square_independence.py`
- 性別と色の嗜好が独立かどうかを確認し、期待度数も出力されます。

### 6. 同質性の検定 (`examples/chi_square_homogeneity.py`)
```python
contingency = np.array([[42, 158],
                        [55, 145],
                        [33, 170]])
statistic, p_value, dof, expected = stats.chi2_contingency(contingency)
```
- コマンド: `uv run --with numpy --with scipy python3 examples/chi_square_homogeneity.py`
- 広告クリエイティブ間でコンバージョン率に差があるかを評価し、期待度数を比較に使えます。

---

## 練習問題と模範解答
各テストの理解を深めるために 3 問ずつ用意しました。必要に応じてスクリプトを変更したり、ノートブックで計算を再現してみてください。

### 一標本 t 検定
1. **問題**: 帰無仮説と対立仮説を日本語で説明してください。  
   **解答**: 帰無仮説は「新ワークフローの平均時短は 3.5 分である」、対立仮説は「平均時短は 3.5 分と異なる（ここでは超えることを期待）」。
2. **問題**: 要件値を 3.0 分に下げた場合、同じデータで p 値は増加・減少のどちらになるか。  
   **解答**: 母平均との差が小さくなるため t 統計量は小さくなり、p 値は増加する。
3. **問題**: サンプルサイズを 24 に倍増させ、同じ平均・分散を保つと検出力はどう変化するか。  
   **解答**: 標準誤差が小さくなり t 統計量が大きくなる傾向があるため、検出力（帰無仮説を棄却できる確率）が上がる。

### Welch の 2 標本 t 検定
1. **問題**: `equal_var=False` を指定する理由は何か。  
   **解答**: 2 群の分散が等しいと仮定できない場合に Welch 法を使うことで、有意水準を守りつつ平均差を評価できる。
2. **問題**: 旧フローの満足度をすべて +0.5 した場合、新旧の平均差はどのように変化するか。  
   **解答**: 旧フローの平均が 0.5 上がるので差は縮まり、t 統計量は小さくなり p 値は大きくなる。
3. **問題**: サンプル数だけを 20 件に増やしたら自由度はどう変化するか。  
   **解答**: Welch 検定ではサンプル数が増えると自由度も増え、臨界値が下がって検出力が高まる。

### 対応のある t 検定
1. **問題**: `stats.ttest_rel` が `ttest_ind` と異なる点は何か。  
   **解答**: 対応のある t 検定は各ペアの差を直接扱い、被験者ごとのベースライン差を打ち消す（独立標本 t 検定はペア情報を利用しない）。
2. **問題**: 2 名のデータを削除した場合、自由度はいくつになるか。  
   **解答**: ペア数が 6 になるため自由度は 5（n-1）。
3. **問題**: 差分 `before - after` の平均が 0 なら p 値はどうなるか。  
   **解答**: 差分の平均が 0 なら t 統計量は 0 に近づき、p 値は 1 に近い値になり帰無仮説を棄却できない。

### カイ二乗適合度検定
1. **問題**: 期待度数 `expected` を一様ではなく、週末が 1.5 倍売れるモデルにしたい。どのように計算するか。  
   **解答**: 平日 5 日を 1 とし、週末 2 日を 1.5 とする重みを正規化して合計観測値に掛け、`f_exp` に渡す。
2. **問題**: 観測度数をすべて 2 倍にした場合、カイ二乗統計量はどうなるか。  
   **解答**: 観測値・期待値ともに 2 倍されるため、比の差は一定でカイ二乗統計量も変わらない。
3. **問題**: 自由度が 6 なのはなぜか。  
   **解答**: カテゴリ数 7 に対してパラメータ制約が 1 つある（合計が一定）ので、自由度は 7-1=6。

### カイ二乗独立性の検定
1. **問題**: 期待度数行列が整数でない理由を説明してください。  
   **解答**: 行・列の周辺度数から理論的な独立モデルを計算するため、実数になる。
2. **問題**: 列（色の嗜好）を 3 色に増やした場合、自由度はどう計算するか。  
   **解答**: 自由度 = (行数-1)×(列数-1)。行が 2、列が 3 なら (2-1)*(3-1)=2。
3. **問題**: 期待度数が 5 未満のセルがあるとき取るべき対処は。  
   **解答**: セルを統合して期待度数を増やすか、Fisher の正確確率検定など別手法を検討する。

### カイ二乗同質性の検定
1. **問題**: この検定で比較しているものは何か。  
   **解答**: 行に並ぶ各クリエイティブの「転換・非転換」の割合が同じかどうか（分布の同質性）。
2. **問題**: 行を 2 つに減らし列を 3 つに増やした場合の自由度は。  
   **解答**: (行-1)×(列-1) = (2-1)*(3-1) = 2。
3. **問題**: 期待度数表を確認する目的は。  
   **解答**: 実際の度数と理論値の差をセル単位で把握し、どの条件が全体のカイ二乗統計量に寄与しているかを理解するため。

---

## 出力例
```bash
$ uv run --with numpy --with scipy python3 examples/t_test_one_sample.py
t-statistic: 5.213
p-value: 0.0003
Reject the null hypothesis: the workflow saves more than 3.5 minutes on average.

$ uv run --with numpy --with scipy python3 examples/chi_square_independence.py
Chi-square statistic: 1.505
Degrees of freedom: 1
p-value: 0.2199
Preference independent of gender.
Expected counts:
 [[31.22608696 25.77391304]
 [31.77391304 26.22608696]]
```

---

## 更新履歴
- 2025-11-09: README にチュートリアル用コード抜粋とコマンド解説を追加（`Expand tutorial with code excerpts`）。
- 2025-11-09: uv ベースのセットアップ手順と実行例を README/AGENTS に反映（`Update docs with uv workflow and output`）。
- 2025-11-09: SciPy/NumPy サンプルスクリプトと README/AGENTS の初版を公開（`Add statistical test samples and docs`）。

---

## GitHub 公開メモ
- README で全スクリプトの概要と実行手順を把握できるように構成。
- サンプルデータはランダムではなく固定値なので常に同じ結果を再現します。変更や翻訳は各スクリプトを直接編集して行ってください。
