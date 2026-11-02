# Data visualization concepts

Visualizations help readers examine patterns in numerical data. These notes introduce chart choices and plotting syntax.

## Line color and markers

A line chart shows how values change across an ordered sequence. Matplotlib's `plot` function accepts a color and a marker. The option `color="blue"` chooses blue; `marker="x"` adds cross markers.

## Histograms and boxplots

A histogram groups numerical values into bins and shows their frequencies. It is useful for the shape of a distribution. A tall bin identifies a common interval, not necessarily one exact modal value.

A boxplot summarizes median, quartiles, and spread. Points beyond its whiskers can highlight unusual observations, which should be investigated rather than assumed to be errors.

Histogram entry points include Matplotlib's `hist`, Seaborn's `histplot`, and pandas' plotting interface with `kind="hist"`.

## Heatmaps

A heatmap represents a matrix through colors. Seaborn provides `heatmap`, which needs matrix-like data. Annotations can display numerical values within the colored cells.

## Choosing a chart

| Goal | Useful chart |
| --- | --- |
| Show change across ordered observations | Line chart |
| Examine a numerical distribution | Histogram |
| Compare compact distribution summaries | Boxplots |
| Compare values across rows and columns | Heatmap |

These are concept notes. The [runnable examples](../PROGRESS.md) in this repository focus on core Python and use only the standard library.

Return to [topics studied](../PROGRESS.md).
