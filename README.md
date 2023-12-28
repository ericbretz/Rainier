<p align="center">
<picture><img src="https://i.imgur.com/Dfy7bzY.png"
     alt="Rainier 0.8.4"/><br></picture>
<b>Version 0.8.4</b><br>
Quality analysis for de-novo transcriptome assemblies</p>

## Usage/Examples
Basic usage:<br>
<code>rainier</code> <code>-a</code> ASSEMBLY.fa <code>-l</code> LEFT.fq <code>-r</code> RIGHT.fq <code>-f</code> REFERENCE.fa <code>-o</code> OUTDIR <code>-t</code> THREADS<br><br>
For more options:<br>
<code>rainier</code> <code>-h</code>

## Requirements
<b>Salmon</b>&emsp;&emsp;&emsp;&emsp;https://github.com/COMBINE-lab/salmon<br>
```
apt install salmon
```
<b>Snap-aligner</b>&emsp;&nbsp;https://github.com/amplab/snap<br>
```
apt install snap-aligner
```
<b>Samtools</b>&emsp;&emsp;&emsp;https://github.com/samtools/samtools<br>
```
apt install samtools
```
<b>Diamond</b>&emsp;&emsp;&emsp;https://github.com/bbuchfink/diamond
```
apt install diamond-aligner
```
